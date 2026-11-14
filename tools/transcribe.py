# -*- coding: utf-8 -*-
"""
Video -> timestamped transcript (+ slide frames) for knowledge-base ingest.

    python tools/transcribe.py <video-or-URL> [--out DIR] [--no-frames] [--lang en]

Produces, in --out (default: a scratch folder next to the video):
    <name>.transcript.md   timestamped segments, large-v3 int8, beam 5, VAD on
    <name>.words.json      word-level timestamps (for aligning speech to slides)
    <name>_frames/         one PNG per detected scene change (slide transitions)

Quality choices (deliberate — user asked for best, not fastest):
    model=large-v3, beam_size=5, best_of=5, vad_filter=True, word_timestamps=True,
    condition_on_previous_text=True. On this 16-core CPU expect ~0.5-1.5x realtime.
"""
import argparse, io, json, os, re, subprocess, sys, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")

def run(cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)

def hms(s):
    h, r = divmod(int(s), 3600); m, s2 = divmod(r, 60)
    return "%02d:%02d:%02d" % (h, m, s2)

def fetch_if_url(src, out):
    if not re.match(r"^https?://", src):
        return src, None
    print("downloading via yt-dlp ...", flush=True)
    tmpl = os.path.join(out, "%(title)s.%(ext)s")
    # also grab any existing caption track - free ground truth if present
    run(["yt-dlp", "-q", "--no-playlist", "-f", "bv*[height<=1080]+ba/b",
         "--write-auto-subs", "--write-subs", "--sub-langs", "en", "--sub-format", "vtt",
         "-o", tmpl, src])
    vids = [f for f in os.listdir(out) if f.lower().endswith((".mp4", ".mkv", ".webm"))]
    vids.sort(key=lambda f: os.path.getmtime(os.path.join(out, f)), reverse=True)
    subs = [f for f in os.listdir(out) if f.lower().endswith(".vtt")]
    return os.path.join(out, vids[0]), (os.path.join(out, subs[0]) if subs else None)

def extract_audio(video, wav):
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", video,
         "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", wav])

def extract_frames(video, frame_dir, thresh=0.30):
    """One frame per scene change - catches slide transitions in lecture video."""
    os.makedirs(frame_dir, exist_ok=True)
    # showinfo on stderr gives pts_time per selected frame -> map filenames to timestamps
    r = subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "info", "-i", video,
         "-vf", "select='gt(scene,%.2f)',showinfo" % thresh, "-fps_mode", "vfr",
         os.path.join(frame_dir, "frame_%04d.png")],
        capture_output=True, text=True)
    times = [float(t) for t in re.findall(r"pts_time:([0-9.]+)", r.stderr)]
    idx = {}
    for i, t in enumerate(times, 1):
        idx["frame_%04d.png" % i] = t
    with io.open(os.path.join(frame_dir, "index.json"), "w", encoding="utf-8") as f:
        json.dump(idx, f, indent=1)
    return idx

def transcribe(wav, lang):
    from faster_whisper import WhisperModel
    print("loading large-v3 (int8, 16 threads) ...", flush=True)
    m = WhisperModel("large-v3", device="cpu", compute_type="int8", cpu_threads=16)
    t0 = time.time()
    segs, info = m.transcribe(
        wav, language=lang, beam_size=5, best_of=5, vad_filter=True,
        vad_parameters=dict(min_silence_duration_ms=500),
        word_timestamps=True, condition_on_previous_text=True)
    out, words = [], []
    dur = info.duration
    for s in segs:
        out.append((s.start, s.end, s.text.strip()))
        for w in (s.words or []):
            words.append({"t0": round(w.start, 2), "t1": round(w.end, 2), "w": w.word})
        pct = min(100, int(100 * s.end / dur)) if dur else 0
        print("\r  %3d%%  %s  %s" % (pct, hms(s.end), out[-1][2][:60].ljust(60)), end="", flush=True)
    print("\n  done in %.0fs  (audio %.0fs, %.2fx realtime)" % (time.time() - t0, dur, dur / max(1, time.time() - t0)))
    return out, words, info

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("--out"); ap.add_argument("--lang", default="en")
    ap.add_argument("--no-frames", action="store_true")
    ap.add_argument("--scene", type=float, default=0.30, help="scene-change threshold 0-1 (lower = more frames)")
    a = ap.parse_args()

    out = a.out or os.path.join(os.path.dirname(os.path.abspath(a.src)) if not a.src.startswith("http") else os.getcwd(), "_transcribe_out")
    os.makedirs(out, exist_ok=True)
    video, captions = fetch_if_url(a.src, out)
    name = os.path.splitext(os.path.basename(video))[0]
    wav = os.path.join(out, name + ".16k.wav")

    print("audio ...", flush=True); extract_audio(video, wav)
    frames = {}
    if not a.no_frames:
        print("frames ...", flush=True); frames = extract_frames(video, os.path.join(out, name + "_frames"), a.scene)
        print("  %d scene-change frames" % len(frames))

    segs, words, info = transcribe(wav, a.lang)

    md = os.path.join(out, name + ".transcript.md")
    with io.open(md, "w", encoding="utf-8", newline="") as f:
        f.write("# Transcript — %s\n\n" % name)
        f.write("- source: `%s`\n- duration: %s\n- model: faster-whisper large-v3 (int8), beam 5, VAD\n"
                "- language: %s (p=%.2f)\n- segments: %d\n" % (video, hms(info.duration), info.language, info.language_probability, len(segs)))
        if captions: f.write("- platform captions also saved: `%s`\n" % os.path.basename(captions))
        if frames:   f.write("- slide frames: `%s_frames/` (%d, timestamps in index.json)\n" % (name, len(frames)))
        f.write("\n---\n\n")
        # interleave frame markers so the transcript shows where slides changed
        ft = sorted(frames.items(), key=lambda kv: kv[1]); fi = 0
        for s0, s1, txt in segs:
            while fi < len(ft) and ft[fi][1] <= s0:
                f.write("\n> 🖼 **slide change** @ %s — `%s`\n\n" % (hms(ft[fi][1]), ft[fi][0])); fi += 1
            f.write("**[%s → %s]** %s\n\n" % (hms(s0), hms(s1), txt))
    with io.open(os.path.join(out, name + ".words.json"), "w", encoding="utf-8") as f:
        json.dump(words, f)
    os.remove(wav)
    print("\nwrote:\n  %s\n  %s" % (md, os.path.join(out, name + ".words.json")))
    if frames: print("  %s" % os.path.join(out, name + "_frames"))

if __name__ == "__main__":
    main()
