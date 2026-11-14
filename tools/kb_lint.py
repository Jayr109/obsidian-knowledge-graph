"""Structural + content lint for an Obsidian knowledge base in this workspace.

Usage:  python tools/kb_lint.py ["College CS Knowledge Base"]

Run from the workspace root (the folder containing the "College * Knowledge Base"
directories). Defaults to the CS base. Exits 1 if any check finds a defect.

Checks marked FALSE-POSITIVE HISTORY below have bitten previous audits; the
guards that prevent them must not be removed:
  - "\\|" inside a markdown table cell is CORRECT escaping, not a defect.
  - "\\|" inside $...$ math is a norm (\\|u-v\\|), also correct.
  - [[...]] inside a ``` code fence is usually list notation, not a wiki-link.
  - A page opening with an H1 followed by prose HAS a lede.
  - raw/ filenames may contain spaces and parentheses; some bases have no raw/ at all.
  - Not every base states a page count in index.md, and not every base has courses/;
    those checks skip rather than fail.
  - Root-level index.md / log.md are valid [[wiki-link]] targets in an Obsidian vault.
  - raw/ citations run to the closing backtick, NOT to a known extension: an
    extension-anchored regex truncates "... Solutions (2).pdf" at the space and
    ignores .vtt/.png/.json/.mp4 entirely. Do not reintroduce one.
  - A citation of a directory (or a glob under it) covers the files beneath it;
    pages cite a 38-file transcript folder once rather than enumerating it.

Checks 1-20 and 24 fail the run. Checks 21, 22, 26 and 27 print `info` only, because
every version of them produced mostly false positives:
  - 21 stale-claim wording: most hits are accurate headings naming a real gap
  - 22 page length: the overview and big source pages legitimately exceed any limit
  - 26 raw/ token matching trips on "Lecture25" vs "lecture-25" and on misspellings
  - 27 raw/ coverage is blocked on the citation convention: most pages that
    DO have a source never write its `raw/...` path, so ~90% of hits are
    missing citations, not missing pages. See the note at the check.
Two checks were tried and DELETED rather than kept as noise -- do not re-add them:
  - "page older than a source it cites": a source page edited later for
    cross-linking does not make the citing page stale (85/85 false positives)
  - "one-way See Also links": 408 of them with 412 pages is the normal hub->leaf
    shape, and a number nobody can act on is not information.
"""
import io
import os
import re
import sys
import glob
import fnmatch
import datetime
import collections

BS = chr(92)
ESC = BS + '|'
FENCE = chr(96) * 3
RX_LINK = re.compile(re.escape('[[') + '([^]]+)' + re.escape(']]'))
RX_FM = re.compile(r'\A---\r?\n(.*?)\r?\n---', re.S)
DIR_TYPE = {'concepts': 'concept', 'algorithms': 'algorithm',
            'data-structures': 'data-structure', 'courses': 'course',
            'people': 'person', 'sources': 'source'}

# Course-specific frontmatter invariants, as {course: ((directories,), key)}.
# CSCE 420: exam-scope separation is a standing user requirement -- every
# lecture/source page must declare which exam it belongs to, so a midterm
# question never draws on final material.
INVARIANTS = {'CSCE 420': (('sources',), 'exam')}


def strip_fences(text):
    out, inside = [], False
    for line in text.split('\n'):
        if line.lstrip().startswith(FENCE):
            inside = not inside
            continue
        if not inside:
            out.append(line)
    return out


def norm(target):
    return target.split('|')[0].split('#')[0].strip().replace(BS, '')


def cells(line):
    return line.replace(ESC, '').count('|')


# Citations are written `raw/...` in backticks throughout every base (checked:
# 100% of current occurrences). Running to the closing backtick rather than to a
# known extension is what makes spaces and parentheses safe --
# "raw/CSCE_411_HW2_Sp26_Solutions (2).pdf" is one citation, not a truncated one.
# An earlier extension-anchored regex both truncated those names AND silently
# ignored .vtt/.png/.json/.mp4, which is most of raw/ in the CS base.
RX_RAW = re.compile('`raw/([^`' + chr(10) + ']+)`')


def raw_citations(text):
    """Every raw/ path cited by this page, as posix-relative strings."""
    return {m.group(1).strip().rstrip('.,:;)') for m in RX_RAW.finditer(text)}


def raw_inventory(rawdir):
    """Every file actually under raw/, as posix paths relative to raw/."""
    found = set()
    for dirpath, _dirnames, filenames in os.walk(rawdir):
        rel = os.path.relpath(dirpath, rawdir).replace(BS, '/')
        for fn in filenames:
            found.add(fn if rel == '.' else rel + '/' + fn)
    return found


def load_lintignore(rawdir):
    """Globs in raw/.lintignore are exempt from the coverage check.

    One glob per line, '#' comments, matched against the posix path relative to
    raw/. For superseded duplicates, source archives, and anything else that is
    deliberately kept without a page.
    """
    path = os.path.join(rawdir, '.lintignore')
    if not os.path.isfile(path):
        return []
    out = []
    for line in io.open(path, encoding='utf-8').read().split('\n'):
        line = line.split('#')[0].strip()
        if line:
            out.append(line)
    return out


def load(base):
    files = sorted(os.path.normpath(p)
                   for p in glob.glob(os.path.join(base, 'wiki', '**', '*.md'),
                                      recursive=True))
    meta = {}
    for f in files:
        src = io.open(f, encoding='utf-8').read()
        m = RX_FM.search(src)
        fm = {}
        if m:
            for line in m.group(1).split('\n'):
                mm = re.match(r'^([a-zA-Z_]+):\s*(.*)$', line)
                if mm:
                    fm[mm.group(1)] = mm.group(2).strip()
        meta[f] = {
            'src': src,
            'body': src[m.end():] if m else src,
            'fm': fm,
            'title': fm.get('title', '').strip('"'),
            'slug': os.path.splitext(os.path.basename(f))[0],
            'dir': f.replace(BS, '/').split('/')[-2],
            'sources': [x.strip() for x in fm.get('sources', '').strip('[]').split(',') if x.strip()],
        }
    return files, meta


def main(base):
    out = io.open(1, 'w', encoding='utf-8', closefd=False)
    files, M = load(base)
    index = os.path.join(base, 'index.md')
    logmd = os.path.join(base, 'log.md')
    titles = {M[f]['title']: f for f in files}
    # Root-level vault notes are legitimate link targets even though they live outside wiki/.
    for extra in ('index', 'log', 'CLAUDE'):
        if os.path.exists(os.path.join(base, extra + '.md')):
            titles.setdefault(extra, os.path.join(base, extra + '.md'))
    lower = {t.lower() for t in titles}
    src_slugs = {M[f]['slug'] for f in files if M[f]['dir'] == 'sources'}
    idx_text = '\n'.join(strip_fences(io.open(index, encoding='utf-8').read()))
    idx_links = [norm(x) for x in RX_LINK.findall(idx_text)]
    fails = 0

    def report(label, bad, show=6):
        nonlocal fails
        if bad:
            fails += 1
            out.write('FAIL %-52s %d\n' % (label, len(bad)))
            for b in list(bad)[:show]:
                out.write('       %s\n' % (b,))
        else:
            out.write('ok   %s\n' % label)

    out.write('%s — %d pages\n\n' % (base, len(files)))

    dup = collections.Counter(M[f]['title'] for f in files)
    report('1  duplicate titles', [k for k, v in dup.items() if v > 1])
    report('2  missing title', [f for f in files if not M[f]['title']])

    broken = []
    for f in files + [index]:
        text = '\n'.join(strip_fences(io.open(f, encoding='utf-8').read()))
        for raw in RX_LINK.findall(text):
            t = norm(raw)
            if t and t not in titles and t.lower() not in lower:
                broken.append('%s -> [[%s]]' % (os.path.basename(f), t))
    report('3  broken wiki-links (fences excluded)', broken)

    inbound = collections.Counter()
    for f in files:
        for t in {norm(x) for x in RX_LINK.findall(M[f]['src'])}:
            if t != M[f]['title']:
                inbound[t] += 1
    for t in set(idx_links):
        inbound[t] += 1
    report('4  orphans', [M[f]['title'] for f in files if inbound[M[f]['title']] == 0])

    req = ['title', 'type', 'tags', 'updated']
    report('5  frontmatter gaps',
           ['%s missing %s' % (f, [k for k in req if k not in M[f]['fm']])
            for f in files if [k for k in req if k not in M[f]['fm']]])
    report('6  type vs directory',
           ['%s type=%r want %r' % (f, M[f]['fm'].get('type'), DIR_TYPE[M[f]['dir']])
            for f in files if M[f]['dir'] in DIR_TYPE
            and M[f]['fm'].get('type') != DIR_TYPE[M[f]['dir']]])
    report('7  sources: pointing at missing slug',
           ['%s -> %s' % (M[f]['title'], sl) for f in files
            for sl in M[f]['sources'] if sl not in src_slugs])

    idx_lower = {i.lower() for i in idx_links}
    report('8  pages missing from index.md',
           [M[f]['title'] for f in files
            if M[f]['title'] not in idx_links and M[f]['title'].lower() not in idx_lower])
    report('9  index entries with no page',
           sorted({l for l in idx_links if l not in titles and l.lower() not in lower}))
    cnt = collections.Counter(idx_links)
    report('10 duplicate index entries', ['%s x%d' % (k, v) for k, v in cnt.items() if v > 1])

    m = re.search(r'\*\*Current count:\*\* (\d+) pages', idx_text)
    if m is None:
        # Not every base states a page count in index.md; absence is a convention, not a defect.
        out.write('skip 11 stated page count (no count line in index.md)'+chr(10))
    else:
        report('11 stated page count == actual',
               [] if int(m.group(1)) == len(files) else
               ['stated %s, actual %d' % (m.group(1), len(files))])

    course_files = glob.glob(os.path.join(base, 'wiki', 'courses', '*.md'))
    if not course_files:
        out.write('skip 12 source pages linked from a course page (base has no courses/)'+chr(10))
    else:
        course_links = set()
        for f in course_files:
            course_links |= {norm(x) for x in RX_LINK.findall(io.open(f, encoding='utf-8').read())}
        report('12 source pages not linked from a course page',
               [M[f]['title'] for f in files
                if M[f]['dir'] == 'sources' and M[f]['title'] not in course_links])

    report('13 missing "## See Also"',
           [f for f in files if '## See Also' not in M[f]['src']])

    bad_rows = []
    for f in files + [index, logmd]:
        L = strip_fences(io.open(f, encoding='utf-8').read())
        i = 0
        while i < len(L) - 1:
            if L[i].startswith('|') and re.match(r'^\|[\s:-]+\|', L[i + 1]):
                want = cells(L[i])
                j = i + 2
                while j < len(L) and L[j].startswith('|'):
                    if cells(L[j]) != want:
                        bad_rows.append('%s:%d %s' % (os.path.basename(f), j + 1, L[j][:60]))
                    j += 1
                i = j
            else:
                i += 1
    report('14 malformed table rows', bad_rows)

    concepts = {M[f]['title'] for f in files if M[f]['dir'] in ('concepts', 'data-structures')}
    report('15 algorithm pages with no concept link',
           [M[f]['title'] for f in files if M[f]['dir'] == 'algorithms'
            and not any(norm(x) in concepts for x in RX_LINK.findall(M[f]['src']))])

    today = datetime.date.today()
    bad_dates = []
    for f in files:
        u = M[f]['fm'].get('updated', '')
        try:
            if datetime.date.fromisoformat(u) > today:
                bad_dates.append('%s %s FUTURE' % (f, u))
        except Exception:
            bad_dates.append('%s %r INVALID' % (f, u))
    report('16 updated: dates valid, not future', bad_dates)

    slug2f = {M[f]['slug']: f for f in files if M[f]['dir'] == 'sources'}
    missing_back = []
    for f in files:
        if M[f]['dir'] not in ('concepts', 'algorithms', 'data-structures'):
            continue
        for sl in M[f]['sources']:
            sf = slug2f.get(sl)
            if not sf:
                continue
            if M[f]['title'] not in {norm(x) for x in RX_LINK.findall(M[sf]['src'])}:
                missing_back.append('%s <- %s' % (M[f]['title'], sl))
    report('17 source page does not link a page citing it', missing_back)

    no_lede = []
    for f in files:
        b = M[f]['body'].lstrip()
        if b.startswith('# '):
            b = b.split('\n', 1)[1].lstrip() if '\n' in b else ''
        if b.startswith('#'):
            no_lede.append(f)
    report('18 pages with no lede', no_lede)

    rawdir = os.path.join(base, 'raw')
    raws = None   # stays None when the base has no raw/ directory (checks 26/27 read it)
    inventory = None
    if not os.path.isdir(rawdir):
        out.write('skip 19 raw/ path existence (base has no raw/ directory)'+chr(10))
    else:
        raws = set(os.listdir(rawdir))
        inventory = raw_inventory(rawdir)
        # A citation resolves if it names a file, a directory, or a glob that
        # matches something. Globs are how pages cite a whole transcript folder.
        dirs = {os.path.relpath(os.path.join(dp, d), rawdir).replace(BS, '/')
                for dp, dn, _ in os.walk(rawdir) for d in dn}
        missing_raw = []
        for f in files:
            for c in raw_citations(M[f]['src']):
                c = c.rstrip('/')
                if c in inventory or c in dirs:
                    continue
                if any(ch in c for ch in '*?[') and \
                        any(fnmatch.fnmatch(p, c) for p in inventory):
                    continue
                missing_raw.append('%s -> %s' % (os.path.basename(f), c))
        report('19 raw/ paths cited that do not exist', missing_raw)

    drift = []
    for cf in glob.glob(os.path.join(base, 'wiki', 'courses', '*.md')):
        cf = os.path.normpath(cf)
        course = M[cf]['fm'].get('course', '').strip() or M[cf]['title']
        tagged = {M[f]['slug'] for f in files
                  if M[f]['dir'] == 'sources' and M[f]['fm'].get('course', '').strip() == course}
        listed = set(M[cf]['sources'])
        if tagged - listed:
            drift.append('%s: tagged but not in frontmatter %s' % (M[cf]['title'], sorted(tagged - listed)))
    report('20 course frontmatter vs source pages tagged to it', drift)


    # ---- 21 stale-claim phrases ----------------------------------------
    # Wording that asserts incompleteness. These go stale silently: a page
    # that says "not yet ingested" stays wrong long after the source arrives.
    # Reported for review, not auto-failed, since some are legitimate headings.
    stale_rx = re.compile(
        r'(not yet (been )?ingested|not yet in the (KB|knowledge base)'
        r'|no .{0,30}(page|pages) (yet|exist)|to be (added|ingested)|coming soon)',
        re.I)
    stale = []
    for f in files + [index]:
        for i, ln in enumerate(io.open(f, encoding='utf-8').read().split('\n'), 1):
            if stale_rx.search(ln):
                stale.append('%s:%d %s' % (os.path.basename(f), i, ln.strip()[:90]))
    out.write('info 21 stale-claim phrases to review: %d'%len(stale)+chr(10))
    for x in stale[:10]:
        out.write('       %s'%x+chr(10))

    # ---- 22 page size against the ~700-word guideline ------------------
    # Reported as a count, never a failure: the overview and large source
    # pages legitimately exceed it, and splitting a coherent reference hurts.
    def words(f):
        return len(re.findall(r'\w+', '\n'.join(strip_fences(M[f]['body']))))
    big = sorted(((words(f), M[f]['title']) for f in files
                  if M[f]['dir'] in ('concepts', 'algorithms', 'data-structures')),
                 reverse=True)
    over = [x for x in big if x[0] > 1200]
    out.write('info 22 concept/algorithm pages over 1200 words: %d (largest: %s)\n'
              % (len(over), ', '.join('%s %d' % (t, w) for w, t in over[:3]) or 'none'))

    # ---- 24 course-specific frontmatter invariants ---------------------
    # Declared per course in INVARIANTS below. CSCE 420 requires exam-scope
    # separation on every lecture/source page (a standing user requirement).
    inv = []
    for course, (want_dirs, key) in INVARIANTS.items():
        pages = [f for f in files
                 if M[f]['fm'].get('course', '').strip() == course
                 and M[f]['dir'] in want_dirs]
        missing = [M[f]['title'] for f in pages if key not in M[f]['fm']]
        if missing:
            inv.append('%s: %d of %d %s pages missing %r: %s'
                       % (course, len(missing), len(pages), '/'.join(want_dirs),
                          key, missing[:4]))
    report('24 course frontmatter invariants', inv)

    # ---- 26 raw/ files with no plausible source page -------------------
    # Token-overlap match, so a miss means "look at this", not "defect".
    if raws is not None:
        src_slug_set = {M[f]['slug'] for f in files if M[f]['dir'] == 'sources'}
        src_tokens = {sl: set(re.split(r'[^a-z0-9]+', sl.lower())) for sl in src_slug_set}
        unmatched = []
        for r in sorted(raws):
            if r == 'assets' or not os.path.isfile(os.path.join(rawdir, r)):
                continue
            rt = set(t for t in re.split(r'[^a-z0-9]+', os.path.splitext(r)[0].lower())
                     if len(t) > 2)
            if not any(rt & st for st in src_tokens.values()):
                unmatched.append(r)
        out.write('info 26 raw files with no token overlap with any source slug: %d %s\n'
                  % (len(unmatched), unmatched[:4]))

    # ---- 27 archived raw/ files that no page cites -----------------------
    # The inverse of check 19. 19 asks "does every citation resolve?"; 27 asks
    # "did every archived file produce a page?" -- the direction that let three
    # CSCE 420 lecture transcripts sit in raw/ for weeks with no page while
    # every other check passed, because all of them verify pages, never sources.
    #
    # INFO ONLY, and the reason matters. The `raw/...` citation convention is
    # only partly adopted: when this check was written, 4 of 38 CSCE 420 lecture
    # pages cited their transcript and the eight slide-deck pages cited nothing,
    # so a strict version reported 96 "uncited" files of which ~90% had a
    # perfectly good page that simply never wrote the path down. That is the
    # noise this file has twice deleted checks for. Promote 27 to report() only
    # once source pages reliably cite their raw file; until then the list is a
    # backfill worklist, not a defect count.
    #
    # Granularity: a citation of a directory, or a glob under it, covers every
    # file beneath it -- pages cite a 38-file transcript folder once rather than
    # enumerating it.
    if inventory is not None:
        cited = set()
        for f in files:
            cited |= raw_citations(M[f]['src'])
        covered = set()
        for c in cited:
            c = c.rstrip('/')
            if c in inventory:
                covered.add(c)
                continue
            pref = c + '/'
            covered |= {p for p in inventory
                        if p.startswith(pref)
                        or (any(ch in c for ch in '*?[') and fnmatch.fnmatch(p, c))}
        ignored = load_lintignore(rawdir)
        uncited = sorted(p for p in inventory - covered
                         if os.path.basename(p) != '.gitkeep'
                         and not any(fnmatch.fnmatch(p, g) for g in ignored))
        bydir = collections.Counter(
            p.split('/')[0] if '/' in p else '(top level)' for p in uncited)
        out.write('info 27 archived raw/ files no page cites: %d of %d%s\n'
                  % (len(uncited), len(inventory),
                     (' -- ' + ', '.join('%s %d' % (d, n)
                                         for d, n in bydir.most_common(4)))
                     if uncited else ''))
        for p in uncited[:8]:
            out.write('       %s\n' % p)

    out.write('\n%s\n' % ('ALL CHECKS PASS' if not fails else '%d CHECK(S) FAILED' % fails))
    return 1 if fails else 0


if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'College CS Knowledge Base'
    sys.exit(main(target))
