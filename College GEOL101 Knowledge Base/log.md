# Operation Log — GEOL 101 Knowledge Base

Entries prepended (newest first).

---

## [2026-09-01] lint | Cross-base deep check — 1 self-link fixed

A workspace-wide deep check (run from the CS base, covering all six knowledge bases and 463 pages) found one defect here:

- `wiki/concepts/earthquake-hazards.md` contained **`See [[Earthquake Hazards]] — tsunamis are covered extensively here`** — the page wiki-linking to itself while the sentence says "here". A self-link is inert in Obsidian and reads as a broken cross-reference. Rewritten as plain text: *"Tsunamis are covered extensively on this page and in [[Earthquakes]]."*

Also confirmed earlier today: `wiki/sources/module-6-sedimentary-rocks.md` was missing the required `sources:` frontmatter field; `sources: []` was added.

This base is otherwise clean — 75 pages, all frontmatter valid, no broken links, no duplicate titles. Note it carries no `**Current count:**` line in `index.md`, so automated count verification is skipped for this base.

---

## [2026-07-20] INGEST | Labs 5 & 6 — Topographic Maps and Geologic Dating
- **Source**: `Geol lab 5&6 Empty.pdf` (10 pages; system reported 518 — pypdf/pymupdf both count 10). **Image-only scan, no text layer.** pdftoppm unavailable, so pages were rendered to PNG with pymupdf and read as images. Figures were further analyzed by pixel transects (contour counting, scale-bar measurement) where visual reading was ambiguous.
- **Pages created**: wiki/sources/lab-05-topographic-maps.md, wiki/sources/lab-06-relative-and-numerical-dating.md, wiki/concepts/topographic-maps.md, wiki/concepts/latitude-and-longitude.md
- **Gap closed**: the knowledge base previously had **zero coverage of topographic maps** — contours, contour interval, gradient, relief, lat/long. This was the single largest hole in the wiki relative to the course. Lab 6 material already mapped onto the existing [[Geologic Time]] page and needed no new concept pages.
- **Contents**: Lab 5 = activity sheets 9.1 (lat-long, quadrangles, Google Earth), 9.3 (contour construction at 100 ft and 10 ft intervals; labeling pre-drawn contours with depression hachures), 9.5 (relief and gradient on a Merced River/Yosemite quad). Lab 6 = activity sheets 8.1 (contacts, superposition/cross-cutting/inclusions, angular unconformity at Sedona), 8.2 (four geologic cross-sections to sequence), 8.4 (half-life and parent-daughter isotope calculations).
- **Quantitative results derived**: Fig. A9.5.1 contour interval **40 ft** (index contours 200 ft apart, 4 intermediate rings counted); A→B ≈ **2400 ft** (2.41 × bar scale), gradient **0.17 ft/ft**; X→Y ≈ **500 ft**, gradient **0.48 ft/ft**; B = 6560–6600 ft, X = 6440–6480 ft, Y = 6200–6240 ft. Fig. A9.3.3 shoreline-inland sequence **0 through 70 ft**.
- **Cross-section sequences resolved**: XS1 `E,P,G,L,C,H,O,M,D,J,A,S,N,K,B,R,F`; XS2 (Grand Canyon) `K,J,S,M,E,L,D,C,B,A,F,R,I,H,G`; XS3 `F,P,G,C,B,R,H,A,M,O,E,X,D,K,Z,J,N`.
- **Open items**: (1) **Cross Section 4 not resolved** — ~27 letters, multiple dikes/faults/a gneiss dome; truncation relationships not verifiable at scan resolution. Only anchors established: V oldest, N (house) youngest. Needs the printed sheet. (2) Activity 9.3 part D references **Figs. 9.1B–C**, textbook figures absent from this PDF. (3) Elevation of point A on Fig. A9.5.1 is the softest number (~6160–6200 ft) — orange township grid lines and the river label interfered with automated contour counting. (4) Activities 9.2, 9.4, 8.3 are not in this scan.

## [2026-07-20] QUERY | Lab 5 & 6 worksheet walkthrough
- **Trigger**: human supplied the scanned lab PDF and worked through it activity by activity across the session (9.1 → 9.3 → 9.5 → 8.1/8.2/8.4), supplying personal inputs where the worksheet required them.
- **Personal context supplied**: home place = **Woodcreek Junior High School, 1801 Woodcreek Bend Lane, Katy, TX 77494**; country = USA; using the **browser version of Google Earth** (not Pro), so Activity 9.1 part C.4 (historical imagery) is N/A.
- **Deliverables**: full answers for 9.1, 9.3 (with drawn contour diagrams for Figs. A9.3.1 and A9.3.2 and a labeling scheme for A9.3.3), 9.5 (including a sketched gentle switchback route from A to B, ~5600 ft at 0.071 ft/ft), and 8.1/8.2/8.4.
- **Note**: items requiring the student's own ruler measurement or pencil work were flagged as such rather than answered — Activity 9.1 parts A/B1–3/C, and the hand-contouring in 9.3 A–C.

## [2026-06-23] QUERY | Module 13 quiz review — mesa/butte/pinnacle distinction
- **Trigger**: human shared a graded Module 13 quiz (7.83/10). Image-label question (Monument Valley) was missed because the mesa/butte/pinnacle distinction was assigned by proportion.
- **Confirmed from image**: A = mesa (wider than tall), B = pinnacle (slender spire), C = butte (taller than wide). Correct ordering by erosion stage: mesa → butte → pinnacle.
- **Fix**: sharpened the Colorado Plateau bullet in wiki/concepts/deserts.md to define each by proportion (mesa wider-than-tall, butte taller-than-wide, pinnacle = spire).
- **Open item**: Q4 iceberg "% exposed" — answered 10 (standard ~10% exposed / 90% submerged), marked incorrect; lecture's exact figure unknown (slide was image-only). Pending the key's expected value before recording in wiki/concepts/glaciers.md.

## [2026-06-23] INGEST | Module 14: Climate Change
- **Source**: GEOL101_Module14_ClimateChange.pdf (182 pages; pypdf count — system reported 207)
- **Pages created**: wiki/sources/module-14-climate-change.md, wiki/concepts/atmosphere.md, wiki/concepts/climate-change.md, wiki/concepts/global-warming-impacts.md, wiki/concepts/historical-climate-change.md
- **Extraction note**: extracted text with pypdf to a temp file (per established workflow), then ingested.
- **Notes**: Slides cover (1) Climate vs. weather; the climate system (atmosphere/hydrosphere/geosphere/biosphere/cryosphere) and two-way climate–geology links. (2) Atmosphere — composition (N₂/O₂/Ar + variable CO₂/water vapor/methane/ozone, aerosols), four-layer structure (troposphere/stratosphere/mesosphere/thermosphere), solar radiation paths (50% surface, 20% atmosphere, 30% albedo), greenhouse effect (shortwave in, longwave trapped). (3) Detecting climate change — ice cores (Vostok), seafloor sediments, corals (¹⁸O/¹⁶O paleothermometer), tree rings, fossil pollen. (4) Natural causes — plate tectonics, Milankovitch orbital variations, volcanic aerosols/SO₂ cooling (Tambora 1815, El Chichón 1982 −0.5°C), solar variability/sunspots (11-yr, too short). (5) Human causes — CO₂ (fossil fuels/deforestation, Keeling curve, 416 ppm July 2022), methane (20× effective), nitrous oxide (150 yr), black-carbon aerosols; IPCC consensus (CO₂↔temp linked, CO₂↑, temp↑ "unequivocal," humans "very likely" >90%). (6) Feedbacks (positive ice-albedo/permafrost; negative cloud cover) and GCM limitations. (7) Historical — Medieval Warm Period (900–1300 CE, Norse Greenland, Maya) and Little Ice Age (1300–1850 CE: glacier advance, Black Death, French Revolution food riots, Thirty Years War, potato, Irish Potato Famine; causes — Maunder Minimum, volcanism, ocean circulation). (8) Consequences — sea-level rise (thermal expansion + land-ice melt, 25 cm since 1870, ~52–98 cm by 2100), Arctic sea-ice loss/permafrost thaw, Larsen B/C ice-shelf collapse, ocean acidification (~30% since 1850s), longer growing seasons/declining yields, desertification, stronger hurricanes/floods/droughts (Lake Mead lows), billion-dollar disasters, sixth mass extinction (five prior: end-Ordovician/Devonian/Permian-95%/Triassic/Cretaceous-dinosaurs) and pollinator/insect decline (CCD).

## [2026-06-23] INGEST | Module 13: Glaciers and Deserts
- **Source**: GEOL101_Module13_GlaciersAndDeserts.pdf (137 pages; pypdf count — system reported 117)
- **Pages created**: wiki/sources/module-13-glaciers-and-deserts.md, wiki/concepts/glaciers.md, wiki/concepts/glacial-landforms.md, wiki/concepts/ice-ages.md, wiki/concepts/deserts.md, wiki/concepts/wind-erosion-and-deposition.md
- **Extraction note**: large PDF; extracted text with pypdf to a temp file (per established workflow), then ingested.
- **Notes**: Slides cover (1) Glaciers — valley/alpine glaciers, ice sheets (Greenland/Antarctica), ice shelves/caps/outlet/piedmont; firn formation; plastic flow + basal slip; zone of fracture/crevasses; accumulation vs. wastage, ablation (melting/calving), glacial budget (advance/retreat), most glaciers retreating. (2) Glacial erosion (plucking, abrasion → rock flour/striations) and landforms — U-shaped trough, hanging valleys, cirque/tarn/paternoster, arête/col/horn, roches moutonnées, fjords; deposits — drift, till (erratics) vs. stratified drift, moraines (lateral/medial/end/ground), drumlins, outwash plains/valley trains, kettles, kames, eskers. (3) Ice ages — ~2.6 My, ~20 cycles (~100 ka), Last Glacial Maximum ~18 ka; sea-level drop ~100 m, isostatic rebound, Great Lakes/Finger Lakes, proglacial lakes (Agassiz/Missoula), pluvial lakes (Bonneville); tillite; causes (plate tectonics, Milankovitch eccentricity/obliquity/precession, albedo). (4) Deserts — dry = precip < evaporation, ~30% of land, desert/steppe; four causes (subsiding air/horse latitudes, cold currents, continental interiors, rain shadow); desert varnish/petroglyphs; ephemeral streams (wash/arroyo/wadi), flash floods, exotic rivers (Colorado/Nile); Basin and Range (alluvial fan→bajada→playa, inselbergs), Colorado Plateau (mesas/buttes/pinnacles). (5) Wind — bed load (saltation) vs. suspended (silt); deflation/blowouts/Dust Bowl, ventifacts/yardangs, desert pavement; dunes (slip face 34°, cross-bedding; barchan/transverse/barchanoid/longitudinal/parabolic/star), loess.

## [2026-06-23] INGEST | Module 12: Mass Movement and Coastal Processes
- **Source**: GEOL101_Module12_MassMovementAndCoastalProcesses.pdf (441 pages; pypdf count — system reported 507)
- **Pages created**: wiki/sources/module-12-mass-movement-and-coastal-processes.md, wiki/concepts/mass-movement.md, wiki/concepts/slope-stability.md, wiki/concepts/coastal-processes.md, wiki/concepts/coastal-hazards-and-protection.md, wiki/concepts/hurricanes.md
- **Extraction note**: very large PDF (mostly photo slides); extracted text with pypdf to a temp file, then ingested.
- **Notes**: Slides cover (1) Mass movement — downslope motion under gravity; classification by material (rock/soil) × motion (fall/slide/flow) with rate increasing; rock fall, translational slide, rotational slide/slump (head scarp/toe), creep (soil/rock), earthflow, mudflow (>50% water)/lahar, debris flow, debris avalanche; subsidence, snow avalanches, underwater landslides→tsunamis; Vaiont Dam 1963, Nevados Huascarán 1970, Oso WA 2014. (2) Slope stability — driving vs. resisting forces, angle of repose (~35° dry sand), cohesion vs. pore pressure, zones of weakness; triggers (volcanic, earthquake, precipitation, land use/oversteepening/toe-cut/vegetation removal); warning signs and prevention (retaining walls, gabions, drainage, regrading, rock bolts, debris barriers). (3) Coastal processes — coast/shore/beach; waves (height/wavelength/period, velocity=λ/T, wave base ½λ, energy∝height²), breakers/surf; refraction concentrates energy on headlands; longshore current/beach drift, rip currents (~100 deaths/yr). (4) Coastal landforms — wave-cut cliff/platform, marine terrace, sea cave→arch→stack; spit, baymouth bar, tombolo, barrier islands; emergent (CA) vs. submergent (Atlantic, estuaries) coasts. (5) Coastal hazards/protection — erosion (~3.3 ft/yr Atlantic/Gulf), tidal/king-tide flooding, sediment starvation; hard structures (seawall/groin/jetty/breakwater) disrupt longshore transport; beach nourishment, setback (E-60), Cape Hatteras Lighthouse relocation 1999. (6) Hurricanes — form over ≥27 °C water, 5–20° lat; depression→tropical storm (≥39 mph)→hurricane (≥74 mph); eye/eye wall, CCW (N Hem); Saffir-Simpson 1–5; storm surge (worst right of eye), wind, inland flooding; Galveston 1900 (deadliest US, 8–12k dead), Katrina 2005 (levee failures, $108B), Harvey 2017 (Houston rainfall).

## [2026-06-23] QUERY | Module 10 groundwater quiz review + soda-straw gap fix
- **Trigger**: human answered a 15-question groundwater quiz using the wiki, then pasted the graded results (13.5/15).
- **Gap found**: graded key showed the correct label for the ceiling dripstone tip in the speleothem diagram (Q7) is **"soda straw"** — a term the wiki did not have. Added a **Soda straw** row to the speleothems table in wiki/concepts/karst-topography.md (thin hollow calcite tube = earliest stage of a stalactite) and a parenthetical mention in wiki/sources/module-10-groundwater.md Section 6.
- **Open items (not yet resolved in wiki)**:
  - **Q4** (landfill leachate → which wells): wiki-reasoned answer was {A, C}; key marked it incorrect. Likely intended answer involves the confined-aquifer well too (figure shows flow through both layers) — pending confirmation of the actual answer before recording a principle note.
  - **Q15** (unsaturated vs saturated zone flow direction): "straight down" / "horizontal" scored 0.5; saturated-zone phrasing likely wanted "parallel to the water table / along the hydraulic gradient." Not a wiki gap — direction contrast is already implied in the flow sections.

## [2026-06-22] LINT | Resolve dangling cross-references (Modules 2–5)
- **Trigger**: connectivity audit after Modules 10–11 ingest (script cross-checked every wiki-link against every page title).
- **Finding**: Module 10/11 pages were clean (0 broken links). But 12 pre-existing dangling links from Modules 2–5 pointed to concept pages that had been referenced but never created.
- **Resolution**: created the 12 missing concept pages, synthesized from content already in the parent module/concept pages:
  - **Module 2**: wiki/concepts/continental-drift.md, seafloor-spreading.md, divergent-boundaries.md, convergent-boundaries.md, transform-boundaries.md
  - **Module 3**: wiki/concepts/nonsilicate-minerals.md, mineral-physical-properties.md
  - **Module 4**: wiki/concepts/bowens-reaction-series.md, igneous-rock-textures.md, intrusive-igneous-structures.md
  - **Module 5**: wiki/concepts/pyroclastic-materials.md, lava-flows.md
- **Also**: added all 12 to index.md (under existing concept categories) and to overview.md page list. Re-ran lint → 0 broken links and 0 orphans across the wiki (CLAUDE.md schema-template examples excluded).

## [2026-06-22] INGEST | Module 11: Rivers and Streams
- **Source**: GEOL101_Module11_RiversAndStreams.pdf (227 pages; pypdf count — system reported 214)
- **Pages created**: wiki/sources/module-11-rivers-and-streams.md, wiki/concepts/streams-and-rivers.md, wiki/concepts/stream-erosion-and-deposition.md, wiki/concepts/floods-and-flood-control.md, wiki/concepts/wetlands.md
- **Pages also created (shared with Module 10)**: wiki/concepts/water-pollution-and-contamination.md
- **Extraction note**: PDF Read tool unavailable (`pdftoppm`/poppler not installed); extracted text with pypdf to a temp file, then ingested.
- **Notes**: PDF covers eight lecture sections. (1) Hydrologic stream flow: stream/river/drainage-basin/divide/network definitions, slope, base level; snowmelt/groundwater sources; ephemeral streams; Pakistan 2010 floods case history; floods = most common/costly disaster. (2) River systems: three zones (production/transport/deposition); drainage patterns (dendritic/radial/rectangular/trellis); laminar vs turbulent flow; velocity controls (gradient, wetted perimeter, channel size/roughness). (3) Discharge: Q = A × v (m³/s); longitudinal profile concave — downstream discharge/size/velocity increase, slope decreases. (4) Erosion & transport: abrasion (potholes), hydraulic action, corrosion; dissolved/suspended/bed load; saltation; capacity vs competence; alluvium and sorting. (5) Meandering streams: cut bank/point bar, oxbow lakes, incised meanders (San Juan); floodplains; natural levees, back swamps, yazoo tributaries. (6) Channel types: braided, bedrock (steps/pools); V-shaped valleys, slot canyons; valley deepening/widening; deltas (foreset/bottomset beds, distributaries, Mississippi bird-foot delta), alluvial fans. (7) Floods: stage, lag time, hydrograph; regional/flash/storm-surge types; 100-year flood (1% annual probability); human causes; case studies (Big Thompson 1976 — 144 deaths; Death Valley 2015; Zion 2015); flood control (dams, channelization, levees, floodwalls, relocation, NFIP); dam failures (Johnstown 1889 — 2,209 deaths; Teton 1976; St. Francis 1928). (8) Surface-water issues: land-use change, wetlands (criteria, coastal/freshwater, functions, Great Black Swamp, Everglades/CERP), HABs (Lake Erie/Toledo 2014), Cuyahoga River fire 1969 → Clean Water Act 1970, federal water laws.

## [2026-06-22] INGEST | Module 10: Groundwater
- **Source**: GEOL101_Module10_Groundwater.pdf (170 pages; pypdf count — system reported 161)
- **Pages created**: wiki/sources/module-10-groundwater.md, wiki/concepts/groundwater.md, wiki/concepts/karst-topography.md, wiki/concepts/groundwater-resources-and-hazards.md
- **Pages also created (shared with Module 11)**: wiki/concepts/water-pollution-and-contamination.md
- **Extraction note**: PDF Read tool unavailable (`pdftoppm`/poppler not installed); extracted text with pypdf to a temp file, then ingested.
- **Notes**: PDF covers ten lecture sections. (1) Importance of groundwater: <1% of Earth's water usable, >96% of unfrozen freshwater is groundwater, ~25% of U.S. freshwater use; runoff vs infiltration "battle." (2) Porosity (storage, % pore space) vs permeability (transmission, pore connectivity). (3) Water table & subsurface zones: vadose/unsaturated zone, capillary fringe, zone of saturation (phreatic), gaining/losing streams. (4) Aquifers (sand/gravel — 80% of US) vs aquitards (clay/shale); confined/unconfined; Darcy's law (hydraulic gradient × conductivity × area); flow ~1 ft/day, 10,000× slower than surface water. (5) Wells: drawdown, cone of depression, perched water table; artesian systems (confined inclined aquifer + aquitards; flowing vs nonflowing; potentiometric surface). (6) Springs, hot springs (>95% heated by cooling igneous rock), geysers (Old Faithful); deposits — siliceous sinter/geyserite, travertine. (7) Resources: Ogallala/High Plains Aquifer (174,000 mi², fossil water 10–15 ka, mining water, 50–150 ft decline); agriculture ~69% of US groundwater use; Keystone XL concern. (8) Caverns & karst: carbonic-acid dissolution of limestone, speleothems (stalactites/stalagmites/columns/flowstone), sinkholes, cenotes, tower karst. (9) Challenges: overdraft, subsidence (San Joaquin Valley), saltwater intrusion (freshwater lens). (10) Quality & contamination: point/non-point sources, surface vs groundwater pollution, VOCs (TCE/PCE), Woburn MA (*A Civil Action*) Superfund case, cleanup steps and treatment methods (pump-and-treat, vapor extraction, bioremediation, permeable treatment bed).

## [2026-06-13] INGEST | Module 9: Earthquakes
- **Source**: GEOL101_Module9_Earthquakes.pdf (170 pages)
- **Pages created**: wiki/sources/module-9-earthquakes.md, wiki/concepts/earthquakes.md, wiki/concepts/seismic-waves.md, wiki/concepts/earthquake-hazards.md
- **Notes**: PDF covers eight lecture sections. (1) Historical earthquakes and global frequency statistics. (2) Key vocabulary: fault, focus, epicenter, fault scarp, fault trace, foreshocks/aftershocks. (3) Elastic rebound theory (developed from 1906 San Francisco earthquake): stress accumulation, rupture, elastic snap-back. (4) Seismic waves: P-waves (fastest, all media, compressional), S-waves (slower, solids only, shear), surface waves (slowest, most destructive). (5) Seismographs and triangulation to locate epicenters using P–S time interval. (6) Magnitude: Modified Mercalli intensity, Richter scale (1935, logarithmic — 1 unit = 10× amplitude, 32× energy), moment magnitude Mw (now standard — slip × area × rigidity). (7) Earthquakes and plate tectonics: convergent (deepest, highest Mw; thrust faults), divergent (shallow, low Mw; normal faults), transform (shallow; strike-slip), intraplate (New Madrid 1811–1812, 3 quakes up to 7.7 Mw). (8) Hazards: ground shaking + amplification (soft sediment 4–5×), resonance (building period matching), liquefaction (water-saturated loose sediment behaves as fluid; sand blows), landslides, fires. Tsunamis: causes (seafloor displacement, submarine landslides, volcanic caldera collapse), properties (800–1000 kph, 100–500 km wavelength, wall of water), case studies (Banda Aceh 2004 — 9.1 Mw, 227,898 killed; Tohoku 2011 — 9.0 Mw, 20,896 killed, Fukushima meltdown). Risk zones: San Andreas (62% probability >6.7 Mw by 2032), Cascadia Subduction Zone (10% chance >9.0 in 50 yr, five cities, 11M people at risk). Mitigation: land use, building codes, base isolation, resonance avoidance, early warning systems, tsunami buoys, education.

## [2026-06-13] INGEST | Module 8: Geologic Time
- **Source**: GEOL101_Module8_GeologicTime.pdf (68 pages)
- **Pages created**: wiki/sources/module-8-geologic-time.md, wiki/concepts/geologic-time.md
- **Notes**: PDF covers six lecture sections. (1) Origin of Earth via nebular theory: solar nebula collapse → proto-Sun + planetary accretion; chemical differentiation produced core/mantle/crust; volcanic outgassing formed primitive atmosphere. (2) Geologic time scale overview. (3) Relative dating: five principles — Superposition (Steno 1669), Original Horizontality, Lateral Continuity, Cross-Cutting Relationships, Inclusions. (4) Unconformities: angular unconformity, disconformity, nonconformity; all three appear in Grand Canyon. (5) Fossils: permineralization, molds/casts, carbonization/impressions, amber, trace fossils; conditions (rapid burial + hard parts); Principle of Faunal Succession; index fossils; fossil assemblages; environmental indicators. (6) Radiometric dating: alpha/beta/electron-capture decay; half-life concept and decay chart; five common isotope pairs (U-238/Pb-206 4.5 Ga, U-235/Pb-207 704 Ma, Th-232/Pb-208 14.1 Ga, Rb-87/Sr-87 47 Ga, K-40/Ar-40 1.3 Ga); zircon geochronology; C-14 for organics <70 ka; alternative methods (dendrochronology, varves, ice cores). Age of Earth: 4.56 Ga (meteorites and moon rocks); oldest Earth rocks 4.013 Ga; oldest mineral zircon 4.4 Ga.

## [2026-06-08] INGEST | Module 7: Metamorphism and Deformation
- **Source**: GEOL101_Module7_MetamorphismAndDeformation.pdf (156 pages)
- **Pages created**: wiki/sources/module-7-metamorphism-and-deformation.md, wiki/concepts/metamorphic-rocks.md, wiki/concepts/rock-deformation.md, wiki/concepts/mountain-building.md
- **Pages updated**: wiki/concepts/rock-cycle.md (added sources, See Also links)
- **Notes**: PDF covers three major lecture sections. (1) Metamorphic rocks: protoliths, metamorphic grade, recrystallization (pressure solution + plastic deformation), neocrystallization (polymorphs), agents of metamorphism (heat/pressure/differential stress/fluids), foliated textures (slaty cleavage → schistosity → gneissic banding), non-foliated textures, full rock classification table (slate, phyllite, schist, gneiss, marble, quartzite, hornfels), and metamorphic environments (contact, hydrothermal, burial, subduction zone, regional, fault zone, impact). (2) Stress/strain and rock deformation: stress types, strain types (elastic/brittle/ductile), four controlling factors, fault anatomy and types (normal/reverse/thrust/strike-slip/oblique-slip), horst-graben systems, slickensides, joints, fold anatomy and types (anticline/syncline/symmetrical/asymmetrical/overturned/plunging/dome/basin/monocline). (3) Mountain building: orogenesis, subduction zones (volcanic island arc, Andean-type with batholiths/accretionary wedge/forearc basin/back-arc spreading, example: Andes + California), collisional belts (Alpine-type: Himalayas, Appalachians — three orogenies, Cordilleran terrane accretion), fault-block mountains (Tetons, Basin and Range Province with two formation hypotheses).

## [2026-06-06] INGEST | Module 6: Sedimentary Rocks
- **Source**: GEOL101_Module6_SedimentaryRocks.pdf (137 pages)
- **Pages created**: wiki/sources/module-6-sedimentary-rocks.md
- **Concepts created**: Weathering and Soil, Sedimentary Rocks
- **Notes**: PDF contains three lecture sections. (1) Mechanical weathering: frost wedging, salt crystal growth, sheeting/unloading, hydration, biological activity. (2) Chemical weathering: dissolution, oxidation, hydrolysis; soil horizons (O, A, E, B, C), five formation controls, soil erosion/conservation (Dust Bowl case study). (3) Sedimentary rocks: clastic (shale, mudstone, siltstone, sandstone, conglomerate, breccia), organic (coal stages, coquina, oil shale), chemical (limestone varieties, dolostone, chert, evaporites), sedimentary structures (bedding, cross-bedding, graded beds, ripple marks, mud cracks, fossils), depositional environments (continental, marine, transitional, sedimentary facies).

## [2026-05-31] INGEST | Module 5: Volcanoes
- **Source**: GEOL101_Module5_Volcanoes_ACC.pdf (142 pages)
- **Pages created**: wiki/sources/module-5-volcanoes.md
- **Concepts updated/created**: Volcanoes, Volcanic Hazards
- **Notes**: Covers eruption types, volcano landforms, lava types, pyroclastic materials, anatomy, tectonic settings, volcanic hazards (with Mt. St. Helens 1980 and Pompeii 79 CE case studies), and volcanic monitoring.

## [2026-05-31] INGEST | Module 4: Igneous Rocks
- **Source**: GEOL101_Module4_IgneousRocks_ACC.pdf (83 pages)
- **Pages created**: wiki/sources/module-4-igneous-rocks.md
- **Concepts updated/created**: Igneous Rocks, Magma
- **Notes**: Covers magma properties, felsic/intermediate/mafic/ultramafic compositions, all texture types, named rocks (granite through tuff), three magma origin mechanisms, Bowen's Reaction Series, magmatic differentiation, partial melting, and all intrusive pluton types.

## [2026-05-31] INGEST | Module 3: Minerals
- **Source**: GEOL101_Module3_Minerals-1_ACC.pdf (84 pages)
- **Pages created**: wiki/sources/module-3-minerals.md
- **Concepts updated/created**: Minerals, Silicate Minerals
- **Notes**: Covers atomic structure, all bonding types, all physical properties, Mohs hardness, mineral groups (silicate and nonsilicate), five silicate structures, common light and dark silicates, mineral formation and destruction.

## [2026-05-31] INGEST | Module 2: Plate Tectonics
- **Source**: GEOL101_Module2_PlateTectonics_ACC.pdf (86 pages)
- **Pages created**: wiki/sources/module-2-plate-tectonics.md
- **Concepts updated/created**: Plate Tectonics, Paleomagnetism, Hot Spots and Mantle Plumes
- **Notes**: Covers Wegener/continental drift, Hess/seafloor spreading, all three boundary types, magnetic reversals and marine anomalies, hot spots (Hawaii, Yellowstone), slab-pull and ridge-push forces, mantle convection. Paleomagnetism slides credited to Michelle Chrpa.

## [2026-05-31] INGEST | Module 1: The Science of Geology
- **Source**: GEOL101_Module1_Geology_ACC (1).pdf (58 pages)
- **Pages created**: wiki/sources/module-1-science-of-geology.md
- **Concepts updated/created**: Earth's Internal Structure, Rock Cycle
- **Notes**: Covers geology definition, human population growth (exponential), uniformitarianism, scientific method, nebular theory/origin of Earth, Earth's layered structure (compositional and physical), rock cycle, ocean floor and continental surface features.

## [2026-05-31] INIT | Knowledge Base Created
- Created CLAUDE.md, index.md, log.md, wiki/overview.md
- Created wiki/courses/geol101.md
- Created wiki/people/brandi-lenz.md
- Total pages at initialization: 18 (5 sources + 9 concepts + 1 overview + 1 course + 1 person + index + log + CLAUDE.md)
