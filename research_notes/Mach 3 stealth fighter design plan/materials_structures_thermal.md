# Materials, Structures and Thermal Management for a Mach 3 Low-Observable Single-Seat Fighter

Research note on how this was gathered (read this first): this session could not open any full documents. The fetch tool and direct HTTPS were blocked for ntrs.nasa.gov, nasa.gov, en.wikipedia.org, apps.dtic.mil and thesr71blackbird.com, and the shared web-search budget ran out partway through. So every cited finding below comes from search-engine result summaries and snippets, not from reading the primary documents in full. Where a summary did not clearly say which URL a number came from, the attribution is marked "(attribution approximate)". The primary documents worth pulling directly are named in each Gaps list. All tables of computed numbers (marked "computed") are my own arithmetic from the cited equations and the standard ISA atmosphere. They are not taken from any source.

## 1. Aerodynamic heating at Mach 2–3.5: equations, stagnation and recovery temperatures, measured skin temperatures, heat soak

### Takeaway
Skin temperature on a Mach 3 cruiser is set by the adiabatic-wall (recovery) temperature, T_aw = T∞[1 + r(γ−1)/2·M²] with r ≈ Pr^(1/3) ≈ 0.896 for a turbulent boundary layer. At 18–24 km this gives about 290–300 °C (≈560–580 °F) at Mach 3 and about 340–350 °C (≈650–670 °F) at Mach 3.2. That matches the SR-71's reported average skin temperatures of 462–622 °F. Stagnation points such as noses and leading edges run hotter, and areas around the engines reach about 1,050 °F (565 °C) from engine heat, not from aerodynamic heating.

### Cited Findings
**Equations**
- Recovery temperature: T_r = T∞ + r·(γ−1)/2·M∞²·T∞, i.e. T_r/T∞ = 1 + r(γ−1)M²/2. For a turbulent boundary layer the recovery factor is r = Pr^(1/3). With Pr = 0.72, r = 0.896. The turbulent relation has been confirmed experimentally for air around Pr ≈ 0.7 — [pygasflow docs: temperatures](https://pygasflow.readthedocs.io/en/latest/modules/atd/temperatures.html); [NASA NTRS 19930086815](https://ntrs.nasa.gov/api/citations/19930086815/downloads/19930086815.pdf); [mrforum open-access chapter](https://mrforum.com/wp-content/uploads/open_access/9781644903193/4.pdf) (attribution approximate across these three)
- In Crocco-type analysis the wall temperature equals the adiabatic-wall temperature T_aw, with the recovery factor applied at Pr = 0.72 — [Chemical Engineering: temperature effects in high-velocity gas flow](https://www.chemengonline.com/temperature-effects-high-velocity-gas-flow/) (attribution approximate)

**SR-71 / YF-12 measured and design temperatures**
- NASA Dryden SR-71 fact sheet: surface temperatures reach up to 800 °F during sustained Mach 3 flight — [NASA FS-030 SR-71](https://www.nasa.gov/centers/dryden/pdf/495839main_FS-030_SR-71.pdf)
- Kelly Johnson's development paper gave design temperatures of 1,050 °F at the nacelle, 585 °F at the nose and 470 °F at the tail — [Code One: SR-71 Blackbird, A Fast History](https://www.codeonemagazine.com/article.html?item_id=153)
- NASA historian Peter Merlin (AIAA 2009, "Design and Development of the Blackbird: Challenges and Lessons Learned"), as relayed by a secondary source: average surface temperatures at speed were 462–622 °F (≈240–330 °C), and some parts near the engines reached 1,050 °F. This ruled out aluminium as the main structural material — [Merlin, NASA NTRS 20090007797](https://ntrs.nasa.gov/api/citations/20090007797/downloads/20090007797.pdf); relayed by [allbase.co.uk](https://allbase.co.uk/blog/sr71-blackbird-materials)
- A zone breakdown from a 1979 declassified article, reposted on a gallery page, gives about 800 °F for the leading edges and inside the inlet, about 500 °F for mid-wing, and 450–500 °F for wing and fuselage. This is a secondhand source — [Renderosity gallery comment](https://api.renderosity.com/gallery/items/1726646/sr-71-blackbird)
- Other secondary figures: skin about 400 °C (750 °F) at Mach 3.2 with the wing leading edges among the hottest surfaces ([migflug](https://migflug.com/jetflights/fr/sr-71-blackbird-titanium-fuel-leak-design-jp-7/)), and titanium skin about 620 °F at Mach 3.2 ([19FortyFive, Oct 2026](https://www.19fortyfive.com/2026/10/lockheed-sr-71-blackbird-came-back-from-every-mission-3-to-4-inches-longer-than-it-took-off-at-mach-3-2-the-titanium-skin-ran-around-620-degrees-fahrenheit-so-lockheed-built-the-panels-loose-on-purp/))
- Windshield: a secondary article citing Merlin gives about 420 °F for the outer surface of the cockpit glass ([19FortyFive, Oct 2026](https://www.19fortyfive.com/2026/10/lockheed-sr-71-blackbird-came-back-from-every-mission-3-to-4-inches-longer-than-it-took-off-at-mach-3-2-the-titanium-skin-ran-around-620-degrees-fahrenheit-so-lockheed-built-the-panels-loose-on-purp/), attribution approximate). A wiki derived from Wikipedia says the windscreen exterior reached 600 °F ([NASA Fandom wiki](https://nasa.fandom.com/wiki/Lockheed_SR-71_Blackbird)). An account of the inner windshield gives up to 120 °C even with the cooling system running at full capacity ([airforces.fr](https://airforces.fr/tag/cooling/)). These figures conflict.
- One aggregator page claims about 1,100 °F skin temperatures. It looks like scraped or AI-written content and should not be used — [aptraining.csc.com](https://aptraining.csc.com/sr-71-max-temps)
- The YF-12 could hold high-speed cruise long enough for structural temperatures to stabilize, which the X-15 could not. NASA heated the YF-12 airframe in the Flight Research Center High Temperature Loads Laboratory in 1972–73 to match flight temperatures. A fan-history site reports that flight and lab temperatures differed by up to about 20 °F, because radiant lab heating differs from aerodynamic heating and because fuel acts as a heat sink in flight. With dry tanks in the ground tests, tank skins ran hotter than in flight — [thesr71blackbird.com: thermal loads research](https://www.thesr71blackbird.com/History/CIA/thermal-loads-research)
- The NASA YF-12 program covered flight loads and structural heating, in-flight heat transfer, skin-friction cooling, and a "coldwall" heat-transfer experiment — [NASA Fact Sheet FS-047](https://www.nasa.gov/wp-content/uploads/2021/09/fs-047-dfrc-04-20-20.pdf); [GlobalSecurity F-12 NASA](https://www.globalsecurity.org/military/systems/aircraft/f-12-nasa.htm)
- Jenkins & Quinn (1996), NASA Dryden history of the YF-12A Thermal Loads and Structures Program: laboratory structural heating with infrared systems was largely developed during this program, which produced cross-correlated flight, lab and computational data. This is the key primary source for YF-12 skin-temperature data — [NASA NTRS 19960027893](https://ntrs.nasa.gov/api/citations/19960027893/downloads/19960027893.pdf)
- The YF-12 airframe, mainly titanium alloy, withstood skin temperatures above 500 °F during sustained high-speed flight — [Vintage Aviation News](https://vintageaviationnews.com/warbird-articles/flight-test-files/yf-12.html)

**MiG-25 and XB-70**
- The MiG-25's steel structure tolerated skin temperatures of about 300 °C at Mach 2.8. This comes from a single secondary source — [migflug MiG-25](https://migflug.com/aircraft/mig-25-foxbat/)
- XB-70: a pre-flight press projection said parts of the structure would reach about 650 °F at Mach 3, above the softening point of aluminium and magnesium. The rear fuselage, heated by the engines from inside and by airflow from outside, was expected to reach 1,000 °F and was made of high-strength tool steel — [TIME, "The Supersonic Cobra"](https://content.time.com/time/subscriber/article/0,33009,871114-1,00.html)

### Inferences
- **Computed table** (ISA, γ = 1.4, calorically perfect gas; turbulent r = 0.896, laminar r ≈ 0.85 taken as Pr^(1/2), a textbook value not verified in this session; stagnation r = 1):

| Altitude (T∞) | Mach | T0 stagnation | T_aw laminar (r=0.85) | T_aw turbulent (r=0.896) |
|---|---|---|---|---|
| 11–20 km (216.65 K) | 2.0 | 117 °C / 242 °F | 91 °C / 195 °F | 99 °C / 210 °F |
| 11–20 km | 2.5 | 214 °C / 418 °F | 173 °C / 344 °F | 186 °C / 367 °F |
| 11–20 km | 2.8 | 283 °C / 542 °F | 232 °C / 449 °F | 248 °C / 478 °F |
| 11–20 km | 3.0 | 333 °C / 632 °F | 275 °C / 526 °F | 293 °C / 559 °F |
| 11–20 km | 3.2 | 387 °C / 729 °F | 320 °C / 608 °F | 341 °C / 646 °F |
| 11–20 km | 3.5 | 474 °C / 886 °F | 394 °C / 741 °F | 419 °C / 786 °F |
| 24 km (220.65 K) | 3.0 | 345 °C / 652 °F | 285 °C / 544 °F | 303 °C / 578 °F |
| 24 km | 3.2 | 399 °C / 751 °F | 331 °C / 628 °F | 352 °C / 666 °F |
| 24 km | 3.5 | 488 °C / 911 °F | 406 °C / 764 °F | 432 °C / 809 °F |
| 27 km (223.65 K) | 3.2 | 409 °C / 767 °F | 339 °C / 643 °F | 361 °C / 682 °F |
| Sea level (288 K), reference only | 3.0 | 534 °C / 993 °F | 455 °C / 852 °F | 480 °C / 896 °F |

- The computed turbulent T_aw at Mach 3.2 and 24 km (≈666 °F) falls within Merlin's 462–622 °F average-skin range or just above it. Real skins run below T_aw because they radiate heat away, and the SR-71's high-emissivity black paint helps.
- An 800 °F stagnation or leading-edge value exceeds T0 on a standard day at Mach 3.2 and 24 km (751 °F). On a hot day of ISA+15 K, T0 at Mach 3.2 is about 706 K (811 °F) (computed). So the NASA "up to 800 °F" figure is consistent with hot-day stagnation regions. The 1,050 °F nacelle figure must come mostly from engine and exhaust heat.
- Rule of thumb for a design study: below the tropopause, temperatures above isothermal-stratosphere values make heating worse. Mach 3 at low altitude (T_aw ≈ 480 °C at sea level) is structurally prohibitive, so the flight envelope must restrict Mach at low altitude.
- **Heat-soak method.** Thin skins reach near-equilibrium within minutes. Thick structure, fuel and internal bays lag, which is why the YF-12's long cruise was useful. For design, model the transient as a lumped-capacitance or finite-element conduction problem. The surface boundary condition is h·(T_aw − T_w) = ε·σ·T_w⁴ + conduction into the structure. This is a standard heat balance, not verified against a source in this session.
- **IR implication.** By Wien's law, λ_peak ≈ 2,898 µm·K / T. Skin at 550–650 K peaks at about 4.5–5.3 µm, in the mid-wave infrared 3–5 µm band used by IR search-and-track sensors. Aerodynamic heating therefore makes the whole airframe an IR source at Mach 3, independent of engine plume. This is a standard physics constant and was not verified against a source in this session.

### Gaps
- Could not open Jenkins & Quinn (NTRS 19960027893), Merlin (NTRS 20090007797) or the NASA fact sheet. These hold the authoritative YF-12 thermocouple maps and should be pulled directly.
- No primary measured SR-71 exhaust-area or ejector temperatures were found beyond the 1,050 °F nacelle design figure.
- No measured MiG-25 skin temperatures from a primary or CIA/FTD source were found. The ~300 °C figure is a single secondary claim. MiG-25 time limits at Mach 2.8+ (heat-soak and engine limits) were not found.
- XB-70 measured flight temperatures (NASA XB-70 research flights 1967–69) were not found. Only the pre-flight 650 °F and 1,000 °F projections are available. SAE 620374, "The B-70's New Structural Design Concepts for Mach 3 Temperatures", was identified but not read.
- No source was found quantifying how much the SR-71 black paint lowered skin temperature. Figures sometimes quoted are unverified.

## 2. Candidate materials: temperature limits and property data

### Takeaway
Aluminium alloys are limited to about 120–175 °C. 2618-T61, the Concorde-type alloy, keeps about 80 % of its room-temperature properties at 400 °F after short exposure but creeps and overages, which rules out conventional aluminium for Mach 3 skins. Titanium alloys cover roughly 300–400 °C: Ti-6Al-4V is rated "high strength to 600 °F" and for service to 750 °F. Inconel 718 is usable to 650 °C and René 41 to 650–980 °C, at roughly twice titanium's density. Polyimide composites such as PMR-15 top out at about 260–288 °C, and BMI and epoxy are lower still. Carbon-carbon and CMCs are needed only for leading edges, exhaust areas and hot spots.

### Cited Findings
**Aluminium**
- 2618-T61 keeps its static and fatigue properties well at elevated temperature and resists creep well. At 400 °F (204 °C) it retains about 80 % of its room-temperature properties after short exposure — [DTIC AD0801499, "Mechanical Properties of 2618 Aluminum Alloy"](https://apps.dtic.mil/sti/html/tr/AD0801499/index.html)
- EN AW-2618A (T61) was creep-tested at 160–230 °C under 40–290 MPa for up to 4,700 h. Strength declines in service because the S-phase precipitates overage — [BAM, Rockenhäuser et al.](https://opus4.kobv.de/opus4-bam/solrsearch/index/search/searchtype/authorsearch/author/Christian+Rockenh%C3%A4user)
- NASA describes 2618 as likely "creep brittle", with time-dependent crack growth at 175 °C showing mixed transgranular and intergranular fracture — [NASA NTRS 19900013338](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19900013338.pdf)
- Supplier statement (not peer-reviewed): 7075 is stronger at room temperature but loses strength at elevated temperature, while 2618A stays more stable and has higher creep and fatigue strength than 2014 and 2024 — [Referans Metal 2618A T851 datasheet](https://www.referansmetal.com/alasimli-aluminyum/product/21/levha-plaka/air-9048-640-alcu2mg1-5ni-2618a-t851?lang=en)
- A 1963 SAE survey of aluminium for supersonic aircraft includes 2024-T81 data after exposures of up to 70,000 h — [SAE 630407](https://saemobilus.sae.org/papers/survey-candidate-aluminum-materials-supersonic-aircraft-applications-630407)

**Titanium**
- Ti-6Al-4V: "High strength to 600 °F", typically used annealed, with service temperatures through 750 °F (400 °C) — [Rolled Alloys 6Al-4V datasheet](https://www.rolledalloys.com/wp-content/uploads/6AL4V_Data-sheet.pdf)
- Yield of HIP-treated EBM Ti-6Al-4V at 350 °C is about 65 % of room-temperature yield. This is additively manufactured material, so treat it only as an indicator — [PMC9146263](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9146263/)
- Yield of direct-laser-deposited Ti-6Al-4V falls by about 40 % at 500 °C — [Materials 14(21):6432 / PMC8585263](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8585263/)
- Ti-13V-11Cr-3Al (B120VCA) is a beta alloy, nominally 13 % V, 11 % Cr, 3 % Al, specified under MIL-T-9046 and AMS 4917 — [eFunda](https://www.efunda.com/glossary/materials/alloys/materials--alloys--titanium_alloy--wrought--ti-13v-11cr-3al.cfm). Minimum tensile strength is 861 MPa for the MIL and SAE forms — [Total Materia](https://www.totalmateria.com/en-us/material/3255813). A powder supplier lists a density of about 4.58 g/cm³ and UTS of about 950 MPa — [Stanford Advanced Materials](https://powder.samaterials.com/titanium-alloy-13-11-3-spherical-powder-ti-13v-11cr-3al.html)
- In 1962 Lockheed-Georgia measured design data for heat-treated B120VCA sheet against other titanium alloys — [IIT Contrails, "Determination of Design Data for Heat Treated Titanium Alloy Sheet", Vol. 3](https://contrails.library.iit.edu/item/159100)

**Nickel superalloys**
- Inconel 718: density 8.19 g/cm³. High tensile, yield and creep-rupture properties up to 1,200 °F (650 °C), with an operating range of −200 to 650 °C. Another source gives about 650 °C long-term and 800 °C short-term — [Xometry Inconel 718 datasheet](https://xometry.pro/wp-content/uploads/2023/08/Inconel-718-1.pdf); [Continental Steel Inconel 718 sheet](https://titanium-stainless-steel.continentalsteel.com/compare/inconel/inconel-718-sheet); [KX Alloy](https://en.kx-alloy.com/products_page.html?id=50)
- René 41: density 8.25 g/cm³ (0.298 lb/in³). Solution-treated and aged sheet has a minimum yield of 130 ksi (896 MPa) and minimum UTS of 170 ksi (1,172 MPa). Strength and oxidation resistance are rated for 1,200–1,800 °F (649–982 °C) — [Aircraft Materials R41 datasheet](https://aircraftmaterials.com/data/nickel/r41.html); [Upmet René 41](https://www.upmet.com/products/nickel/rene-41)

**Polymer-matrix composites**
- PMR-15 is the state-of-the-art polyimide for composites used at 260–288 °C — [NASA NTRS 20050187016](https://ntrs.nasa.gov/citations/20050187016)
- PMR-15 Tg is about 635 °F (≈335 °C). The transition is broad, so use temperature is capped below Tg — [US Patent 4,992,528](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/4992528). A PMR-15/T650-35 composite has Tg 348 °C, against 414 °C for NASA's DMBZ-15 — [NASA NTRS 20050187016 PDF](https://ntrs.nasa.gov/api/citations/20050187016/downloads/20050187016.pdf)
- AFR-PE-4 is an MDA-free 6F-dianhydride polyimide with 4-PEPA end caps, developed in the mid-1990s. It reaches a higher service temperature than PMR-type resins and is USAF-qualified. No numeric limit was given — [CompositesWorld, "Resins for the Hot Zone, Part I: Polyimides"](https://compositesworld.com/articles/resins-for-the-hot-zone-part-i-polyimides)

### Inferences
- **Material-to-zone screening for Mach 3 cruise**, using the computed T_aw from Q1 of about 290–350 °C on acreage and about 390–490 °C at stagnation:
  - Aluminium: internal and cool structure only. Even at Mach 2.5 (T_aw ≈ 186 °C) 2618 is at its limit.
  - Ti-6Al-4V: acreage skins and primary structure at Mach 3 (≤ 400 °C).
  - Beta titanium (B120VCA type): high-strength heat-treated skins and spars, as on the SR-71.
  - Inconel 718 / René 41: nacelle and exhaust structure (≥ 500 °C).
  - PMR-15 / AFR-PE-4 polyimide: limited to ≤ 260–288 °C. At Mach 3 acreage temperatures (~290–300 °C) that leaves no margin, so polyimides are realistic only at Mach ≤ ~2.8 or on shaded or cooled surfaces.
  - BMI and epoxy are unusable on external Mach 3 skin. (BMI and epoxy service limits were not sourced in this session; see Gaps.)
- Specific strength favours titanium at 300–400 °C. Nickel alloys are about 1.8× denser than titanium (8.2 vs ~4.4–4.6 g/cm³), so use them only where titanium's ~400–540 °C ceiling is exceeded.

### Gaps
- MMPDS elevated-temperature curves (F_tu, F_ty and E as % of room temperature vs exposure time) for 2024-T81, 7075-T6, 2618-T61, Ti-6Al-4V and Ti-13V-11Cr-3Al were not retrieved. MMPDS (formerly MIL-HDBK-5) is the source to use. These reference values were recalled from memory, not verified in this session, and must be checked against MMPDS:
  - 7075-T6: ρ ≈ 2.81 g/cm³, F_tu ≈ 570 MPa
  - 2024-T3: ρ ≈ 2.78 g/cm³, F_tu ≈ 480 MPa
  - Ti-6Al-4V annealed: ρ ≈ 4.43 g/cm³, F_tu ≈ 900–950 MPa, E ≈ 110–114 GPa, α ≈ 9 × 10⁻⁶ /K
  - Ti-13V-11Cr-3Al: the MIL-HDBK-5 density may be nearer 4.8 g/cm³ than the supplier's 4.58, which needs checking.
- No sourced data was found for:
  - MiG-25 steels VNS-2 and VNS-5, or maraging steels generally (density, strength, temperature limit).
  - BMI and epoxy service limits. Typical industry figures of about 120–180 °C for epoxy and about 200–230 °C for BMI were not verified.
  - Carbon-carbon or CMC (C/SiC, SiC/SiC, oxide/oxide) properties and temperature limits.
  - Relative cost per kg and manufacturability ratings for any of these materials.
  - The AFR-PE-4 Tg and service temperature.
  - Titanium machining-rate or cost penalties versus aluminium.

## 3. How real Mach 3 (and 5th-generation) aircraft were built

### Takeaway
The SR-71 and A-12 used about 85–93 % titanium, by structural weight according to Merlin. Their skins were corrugated or beaded to absorb thermal expansion. The aircraft grew about 3–4 inches in length at cruise and leaked fuel on the ground. Production ran into chlorine and cadmium embrittlement of titanium. The MiG-25 chose welded nickel steel (~80 % steel, 11 % aluminium, 8–9 % titanium) because Soviet industry could not reliably weld thin titanium. The XB-70 used brazed PH15-7Mo stainless honeycomb. Modern stealth fighters use about 39–42 % titanium plus about 24–35 % composites (F-22 and F-35); the Su-57 uses about 25 % composites by weight.

### Cited Findings
**SR-71 / A-12**
- Titanium share: Merlin gives 93 % of structural weight, while 85 % is widely quoted — [Merlin, NTRS 20090007797](https://ntrs.nasa.gov/api/citations/20090007797/downloads/20090007797.pdf) via [allbase.co.uk](https://allbase.co.uk/blog/sr71-blackbird-materials). Another source gives an 85–90 % titanium airframe and says much of the titanium was bought from the USSR through shell companies — [19FortyFive, Oct 2026](https://www.19fortyfive.com/2026/10/america-did-not-have-enough-high-grade-titanium-to-build-the-usaf-sr-71-blackbird-so-the-cia-bought-it-from-the-soviet-union-through-shell-companies-in-neutral-countries-the-airframe-was-85-to-90-pe/)
- The external surfaces of the upper and lower wing panels were beaded and corrugated so skin and structure could expand under heat. Corrugation lets panels grow chordwise without buckling — [Merlin, NTRS 20090007797](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20090007797.pdf)
- The aircraft came back from each mission 3–4 inches longer. Panels were deliberately fitted loose, and the tanks leaked on the ramp until heat closed the joints — [19FortyFive, Oct 2026](https://www.19fortyfive.com/2026/10/lockheed-sr-71-blackbird-came-back-from-every-mission-3-to-4-inches-longer-than-it-took-off-at-mach-3-2-the-titanium-skin-ran-around-620-degrees-fahrenheit-so-lockheed-built-the-panels-loose-on-purp/). The fuel system was not sealed because no sealant could survive the temperature cycles. The aircraft leaked on the ground and stopped once it reached temperature — [migflug](https://migflug.com/afterburner/sr-71-blackbird-titanium-fuel-leak-design-jp-7/)
- Titanium spot-welded parts made in summer failed while winter-built parts held. The cause was chlorine added to Burbank tap water in warm months, and Lockheed switched to distilled water — [SlashGear](https://www.slashgear.com/2203752/why-sr-71-blackbird-summer-titanium-corrode-fail/); [BoltFlight](https://boltflight.com/how-burbank-tap-water-caused-sr-71-titanium-panels-to-crack/)
- Cadmium from cadmium-plated tools contaminated titanium bolts and fittings and caused failures. The tools were replaced with titanium tools — [National Security Journal](https://nationalsecurityjournal.org/inside-the-sr-71-blackbird-corrosion-cadmium-and-high-speed-flight/)
- The titanium alloy in a 1962 Lockheed design-data study was B120VCA (Ti-13V-11Cr-3Al) — [IIT Contrails](https://contrails.library.iit.edu/item/159100). The search did not directly confirm that this was the SR-71 alloy; see Gaps.

**MiG-25**
- The airframe is about 80 % steel, 11 % aluminium and 8 % titanium by one count. The steel was tempered, and new welding techniques had to be developed to avoid cracking — [Aerospaceweb](https://aerospaceweb.org/question/performance/q0239.shtml). Another source gives 9 % titanium and calls the steel nickel steel — [migflug](https://migflug.com/afterburner/?p=23239121)
- Assembly relied mostly on automatic and semi-automatic contact and arc welding, plus extensive manual arc and spot welding. The wings were largely welded steel with titanium sheet. The source is OCR-garbled — [Scribd MiG-25 document](https://www.scribd.com/doc/244886200/MiG-25)
- Mikoyan reportedly preferred titanium. A Soviet design account says cracking in thin-walled welded titanium could not be solved, so heavier nickel steel was used — [migflug](https://migflug.com/afterburner/it/why-aircraft-are-riveted-not-welded-damage-tolerance/)
- Teardown after Belenko's defection (6 Sept 1976, Hakodate) showed mainly steel construction, not the titanium Western intelligence had assumed — [migflug MiG-25](https://migflug.com/aircraft/mig-25-foxbat/); [National Security Journal](https://nationalsecurityjournal.org/u-s-intelligence-thought-russias-mig-25-foxbat-was-made-of-titanium-it-was-actually-cheap-stainless-steel/)

**XB-70**
- The wing cover panels were PH15-7Mo face sheets brazed to a 1-inch-deep PH15-7Mo honeycomb core. The intermediate fuselage was also PH15-7Mo brazed honeycomb — [DTIC AD1168612](https://apps.dtic.mil/sti/trecms/pdf/AD1168612.pdf)
- Titanium was about 9 % of the structure, used in the hottest areas — [sr-71.org XB-70](https://sr-71.org/aircraft/xb-70.php) (attribution approximate). The rear fuselage was tool steel ([TIME](https://content.time.com/time/subscriber/article/0,33009,871114-1,00.html)). The fuel tanks were nitrogen-blanketed so the fuel could not ignite as the skin heated — [FIU course page](https://web.eng.fiu.edu/allstar/wings7.htm)

**5th-generation fighters**
- F-22 by weight: about 39 % titanium, 16 % aluminium, 6 % steel, 24 % thermoset composites, 1 % thermoplastic composites and 14 % other materials — [NASA NTRS 20040086015](https://ntrs.nasa.gov/api/citations/20040086015/downloads/20040086015.pdf). GlobalSecurity gives 42 % titanium of structural weight, split as 36 % Ti-6-4 and 3 % Ti-62222 in its chart — [GlobalSecurity F-22 materials](https://www.globalsecurity.org/military/systems/aircraft/f-22-mp.htm). Purdue gives 27 % composites — [Purdue MSE](https://engineering.purdue.edu/MSE/aboutus/gotmaterials/Planes/reynolds.html)
- F-35: about 35 % composites by structural weight — [CompositesWorld CAMX 2021](https://www.compositesworld.com/articles/download-todays-news-from-camx-2021-wednesday-oct-20). Airframer quotes about 42 % on an unclear basis — [Airframer](https://www.airframer.com/news/release/lockheed-martin-extends-cytec-contract)
- Su-57: about 25 % composites by weight of the empty aircraft, according to a Sukhoi developer — [GlobalSecurity PAK FA design](https://www.globalsecurity.org/military/world/russia/pak-fa-design.htm). Rosoboronexport at LIMA 2025 also gave about 25 % — [EDR Magazine](https://www.edrmagazine.eu/lima-2025-rosoboronexport-provides-new-details-on-the-sukhoi-su-57-russias-new-fifth-generation-stealth-fighter). Another source gives 22–26 % by weight and about 70 % of outer surface — [aircraftpilots.com](https://www.aircraftpilots.com/aircraft/military/sukhoi-su-57-r1341/)

### Inferences
- **Thermal growth check (computed).** Take length 32.7 m, α_Ti ≈ 9 × 10⁻⁶ /K (from memory; check in MMPDS) and ΔT ≈ 250–350 K. Then ΔL = L·α·ΔT ≈ 74–103 mm (2.9–4.1 in). This matches the reported 3–4 inch growth, so simple α·ΔT·L estimates are adequate for sizing expansion joints, sliding fuel-tank interfaces and hinge-line gaps.
- There is a lesson for a stealth design. SR-71-style loose panels and corrugated skins conflict with low-observable requirements for tight, gap-free, edge-aligned surfaces. A Mach 3 LO fighter needs expansion accommodation hidden under the outer mold line, for example floating skins on slotted attachments or compliant edge treatments.
- The MiG-25 steel approach paid a weight penalty. Its total airframe composition was steel-dominated, while the SR-71 was titanium-dominated. For a fighter that needs high g and agility, the MiG-25 route is unattractive except for local hot structure.
- Composite fractions of 24–35 % on the F-22 and F-35 rest on epoxy and BMI resins, the F-22 "thermoset" share. These cannot be carried over to Mach 3 external skins. See Q2.

### Gaps
- B120VCA (Ti-13V-11Cr-3Al) as the main SR-71 alloy was not directly confirmed in the retrieved snippets, though it is widely reported. Confirm from Merlin (2009) or Johnson's 1981 paper. Also unconfirmed: SR-71 Ti-6Al-4V or other alloy use, SR-71 empty weight and structural weight fraction, and the A-12 / SR-71 machining figures, such as how many tools were consumed or the scrap rate.
- MiG-25 primary sources were not retrieved: the CIA/FTD assessments and Belyakov & Marmain's "MiG: Fifty Years of Secret Aircraft Design". Also missing are the exact VNS steel grades used and their distribution in the airframe.
- No primary source was found for the XB-70 honeycomb delamination or brazing-quality problems.

## 4. Structural design criteria: load factors, factor of safety, fatigue/damage tolerance, flutter, thermal stress

### Takeaway
US military aircraft use an ultimate factor of 1.5 on design limit load under JSSG-2006, with ≥ 1.875 allowed in lieu of static test. Damage tolerance is assessed from specified initial flaw sizes (originally MIL-A-83444, now JSSG-2006), with fail-safe residual strength equal to design limit load. The SR-71 was limited to about 3.5 g. Fighter +9/−3 g criteria, MiG-25 g limits and MIL-STD-1530D details could not be verified in this session. At Mach 3, dynamic pressure and heating both drive aeroelastic design.

### Cited Findings
- JSSG-2006: "the Factor of Uncertainty (FS) shall be 1.5 unless otherwise approved by the Airworthiness Certifying Official". A factor of 1.875 or greater can be used case by case in lieu of static test verification (JSSG-2006 para A.4.10.5.2) — [Dayton Aerospace USAF/USN flight-release document](https://daytonaero.com/_files/ugd/742fa6_dd8ead2d2ac74a18bf4f4f6a1f15f0e9.pdf)
- Initial crack sizes for damage-tolerance design were first specified in MIL-A-83444 and later in JSSG-2006. A later revision set fail-safe residual strength equal to design limit load (DLL) — [Dayton Aerospace USAF Structures Bulletin](https://daytonaero.com/_files/ugd/742fa6_83b0f14de785494bbfa3f4c755e7d44d.pdf) (attribution approximate between the two Dayton PDFs)
- JSSG-2006 §3.10.5: "All structure shall be design[ed] to nominal dimensional values or 110 percent of minimum values, whichever is less" — [Eng-Tips forum quoting JSSG-2006](https://eng-tips.com/viewthread.cfm?qid=512773)
- The 1.5 ultimate factor exists in part to cover inadvertent in-service loads greater than design limit — [NASA NTRS 20140011147](https://ntrs.nasa.gov/api/citations/20140011147/downloads/20140011147.pdf)
- The SR-71 "could not exceed 3.5 G" — [airforces.fr](https://airforces.fr/tag/heat/). The declassified flight manual's Section V, "Operating Limitations", contains the load-factor limit tables — [sr-71.org Flight Manual Sec. V](https://sr-71.org/blackbird/manual/5)
- Civil comparison: ultimate load = limit load × 1.5 — [SKYbrary, Ultimate Load](https://skybrary.aero/articles/ultimate-load); [14 CFR 25.305](https://www.govinfo.gov/content/pkg/CFR-2010-title14-vol1/pdf/CFR-2010-title14-vol1-sec25-305.pdf)

### Inferences
- **Computed dynamic pressure** q = ½·γ·p·M² (ISA):

| Altitude | Mach 2.0 | Mach 3.0 | Mach 3.2 |
|---|---|---|---|
| 11 km | 63 kPa (1,323 psf) | 143 kPa (2,978 psf) | 162 kPa (3,388 psf) |
| 15 km | 34 kPa (704 psf) | 76 kPa (1,585 psf) | 86 kPa (1,803 psf) |
| 18 km | 21 kPa (439 psf) | 47 kPa (987 psf) | 54 kPa (1,124 psf) |
| 20 km | 15 kPa (320 psf) | 35 kPa (720 psf) | 39 kPa (820 psf) |
| 24 km | 8 kPa (171 psf) | 18.5 kPa (386 psf) | 21 kPa (439 psf) |

  Mach 3 below about 15 km gives q well above typical fighter design limits of roughly 1,800–2,100 psf, a range recalled from memory and not verified. Mach 3 should therefore be restricted to high altitude (≥ 18–20 km), which also lowers the airframe flutter, divergence and load requirements.
- **Thermal stress (standard elasticity relation, not verified against a source in this session).** For fully restrained material, σ = E·α·ΔT uniaxially and σ = E·α·ΔT/(1−ν) for a plate restrained in both directions. For titanium (E ≈ 110 GPa, α ≈ 9 × 10⁻⁶ /K, ν ≈ 0.34, values from memory): ΔT = 100 K gives ≈ 99 MPa uniaxial and ≈ 150 MPa biaxial, and ΔT = 200 K gives ≈ 300 MPa biaxial. The skin-to-spar temperature differences during acceleration transients are therefore a primary load case. Thermal stress adds to the 1.5 × limit mechanical loads, and E and yield both fall with temperature.
- **Aerothermoelasticity.** Heating lowers E, which lowers natural frequencies and flutter speed. In-plane thermal compression lowers panel stiffness further and can buckle panels. Flutter clearance must therefore be done at the hot condition, using the stiffness distribution from the transient temperature field, not at room temperature. This is the reasoning behind the YF-12 thermal loads program (Q1).
- Under JSSG-2006, the damage-tolerance analysis must use crack-growth data (da/dN) at temperature. Hold-time and creep–fatigue interaction, which matters for 2618 aluminium (creep-brittle at 175 °C, Q2) and for titanium at 300+ °C, are outside conventional room-temperature databases.

### Gaps
- Not verified in this session:
  - Fighter symmetric limit load factors of +9.0/−3.0 g (F-16, F-22, F-35A), and the MIL-A-8861 / JSSG-2006 maneuver-envelope definitions.
  - MiG-25 g limits, especially the subsonic and supersonic limits, figures often quoted around +4.5–5 g supersonic.
  - SR-71 flight-manual numbers for KEAS and dynamic-pressure limits.
  - The MIL-STD-1530D ASIP tasks: the five tasks, durability test to 2 lifetimes, initial flaw sizes such as 0.05 in corner cracks at holes, and inspection intervals of half the crack-growth life.
  - JSSG-2006 service-life and usage-spectrum requirements.
- No source was found on flutter criteria (for example, a 15 % margin on equivalent airspeed per MIL-A-8870) or on hot-structure aeroelastic test data.

## 5. Weight-estimation methods and structural/empty weight fractions

### Takeaway
For first-pass sizing, use Raymer's historical trend for jet fighters, W_e/W_0 = 2.34·W_0^(−0.13) with W_0 in lb (2.11 when W_0 is in kgf). Close the sizing with W_0 = (W_crew + W_payload)/(1 − W_f/W_0 − W_e/W_0). Then move to Raymer's approximate group weights, such as W_wing ≈ 9.0 lb/ft² × S_exposed for fighters, and finally to his statistical group equations, applying fudge factors for titanium and hot structure. The detailed Raymer, Nicolai and Roskam Class II equations themselves could not be retrieved in this session.

### Cited Findings
- Historical empty-weight trend W_e/W_0 = A·W_0^C. Jet fighter: A = 2.34 (W_0 in lb) or 2.11 (W_0 in kgf), C = −0.13. Jet trainer: 1.59, −0.10. Jet transport: 1.02, −0.06 — [Scribd copy of Raymer-based Chapter 3](https://www.scribd.com/document/264516694/Chapter-3); [MathWorks File Exchange: Fuel fraction sizing](https://la.mathworks.com/matlabcentral/fileexchange/38973-fuel-fraction-sizing) (secondary sources; verify against Raymer). Sizing closure is W_0 = (W_crew + W_payload)/[1 − W_f/W_0 − W_e/W_0], solved by iteration. One variant uses a factor K = 1.00 for non-composite aircraft and 0.95 for composite aircraft — same sources.
- Raymer's "Approximate Group Weights" method uses simple linear regressions on historical data. For a fighter, W_wing = 9.0 × S_exposed planform (lb per ft²). Raymer notes that the constants in his statistical equations need revision over time, handled by applying a "fudge factor" to each equation's result — [Raymer, Aircraft Design website: Weights Methods Sources](https://aircraftdesign.com/weights-methods-sources-for-aircraft-design-a-conceptual-approach/)
- Raymer's horizontal-tail equation uses the same (N_z·W_dg) load-factor × design-gross-weight grouping as his wing equation — [ABCM COBEM 1999 empennage-weight paper](https://abcm.org.br/anais/cobem/1999/english/..\pdf\AACAHJ.pdf)
- Torenbeek's 1971 semi-empirical wing group-weight formula has a 9.64 % standard deviation against 46 aircraft — [Aircraft Engineering, Emerald](https://emeraldinsight.com/insight/content/doi/10.1108/eb034787/full/html)
- SAWE Paper 62, "Weight Trends on High Speed Aircraft", is a historical weight-trend source for high-speed aircraft — [SAWE Paper 0062](https://www.sawe.org/product/paper-0062/)
- Open-source tools: AeroSandbox implements Raymer's general-aviation weight equations in Python ([AeroSandbox docs](https://aerosandbox.readthedocs.io/en/master/autoapi/aerosandbox/library/weights/raymer_general_aviation_weights/index.html)), and HyperStruct offers a structural-sizing framework ([HyperStruct docs](https://hyperstruct.readthedocs.io/en/latest/introduction.html))

### Inferences
- Worked check (computed): for W_0 = 40,000 lb, W_e/W_0 = 2.34 × 40,000^(−0.13) ≈ 0.594. For 60,000 lb it is ≈ 0.563. The trend is fitted to aluminium and composite fighters, so a Mach 3 titanium and steel airframe should get a positive correction, applied as a material fudge factor in Raymer's sense.
- Recommended workflow for a two-person team:
  1. Class I: the W_e/W_0 trend, adjusted by +5–15 % for hot structure. This range is my judgement, not a sourced value.
  2. Class II: Raymer's or Roskam's fighter group equations (wing, fuselage, tails, gear, nacelle/inlet), with per-group material factors.
  3. Class III: FEM-based sizing (HyperStruct, or a Nastran-format model in MYSTRAN or CalculiX) for wing and fuselage primary structure at hot-condition allowables.

### Gaps
- Not retrieved in this session:
  - Raymer's full fighter or attack group-weight equations, such as the wing equation W_wing = 0.0103·K_dw·K_vs·(W_dg·N_z)^0.5·S_w^0.622·A^0.785·(t/c)^−0.4·(1+λ)^0.05·(cos Λ)^−1·S_csw^0.04. That form is recalled from memory, and the exponents must be verified against Raymer Ch. 15.
  - Nicolai & Carichner's fighter weight equations and Roskam Class II (Part V) equations.
  - Typical structural weight fractions, roughly 30 % of TOGW for fighters (unverified).
  - Actual empty-weight fractions for the SR-71, MiG-25 and XB-70. No sourced empty or gross weights were obtained for these aircraft.

## 6. Thermal management systems

### Takeaway
Fuel is the main heat sink. JP-8 is limited to about 163 °C bulk at the nozzle inlet and 205 °C wetted wall, and JP-8+100 to about 218 °C bulk and 260 °C wetted wall. The SR-71's JP-7 reached the fuel nozzles at about 316 °C after absorbing heat from the cockpit, avionics and hydraulics. The F-35 shows the risk of under-sizing cooling: its PTMS supplies about 30–32 kW, draws more engine bleed than planned (adding about $38 B in life-cycle cost per GAO 2023), and upgrades now target 40 kW (Honeywell P40, 2026) and 62–80 kW (EPACS / ECU). A Mach 3 fighter's ram air arrives at about 300+ °C, so it cannot be used directly as a coolant.

### Cited Findings
- JP-7 absorbed heat from the cockpit, avionics and hydraulics before it was burned, and reached the engine fuel nozzles at about 316 °C (600 °F) — [Merlin, NTRS 20090007797](https://ntrs.nasa.gov/api/citations/20090007797/downloads/20090007797.pdf) via [allbase.co.uk](https://allbase.co.uk/blog/sr71-blackbird-materials). The fuel had to serve as a heat sink in the aircraft's severe thermal environment — [Wikipedia: JP-7](https://en.wikipedia.org/wiki/JP-7)
- A fan site says JP-7 was also used as the engine hydraulic fluid and as a coolant — [airforces.fr](https://airforces.fr/tag/jp7/) (attribution approximate)
- SR-71 crew comfort: even with the cooling system running at full capacity, the inner windshield could reach 120 °C — [airforces.fr](https://airforces.fr/tag/cooling/). The full-pressure suit had a network of tubes in its bladder layer that carried cooling air, especially to the extremities. Portable cooling units were used between the van and the aircraft — [Gizmodo on the SR-71 flight suit](https://gizmodo.com/the-most-badass-plane-ever-had-an-equally-awesome-fligh-5994110) (attribution approximate)
- The windscreen was quartz, fused ultrasonically to a titanium frame. This claim carries a "citation needed" tag at its origin — [NASA Fandom wiki](https://nasa.fandom.com/wiki/Lockheed_SR-71_Blackbird)
- JP-4 and JP-8 limits in current US fighters: about 163 °C bulk fuel at the main-burner nozzle inlet and 205 °C wetted wall inside the nozzle passages, both set to minimise thermal deposits. JP-8+100 aims for about 50 % more heat sink, with a bulk limit of 218 °C (425 °F) and a wetted-wall limit of 260 °C (500 °F). Sources disagree on the thermal-stability gain, giving +38 °C or +56 °C — [SAE 932084, "High Heat Sink Fuels for Improved Aircraft Thermal Management"](https://saemobilus.sae.org/content/932084); [DTIC ADA396761](https://apps.dtic.mil/sti/pdfs/ADA396761.pdf); [SAE 2002-01-1651, JP-8+100 lab testing](https://saemobilus.sae.org/content/2002-01-1651) (attribution approximate among these)
- F-35 PTMS: provides main-engine start, auxiliary and emergency power, plus about 30 kW of aircraft cooling — [Defense Daily](https://defensedaily.com/replacing-f-35-ptms-may-cost-3-billion-honeywell-estimates/air-force). Honeywell puts it at about 32 kW — [Aviation Today](https://www.aviationtoday.com/2023/08/15/replacing-f-35-ptms-may-cost-3-billion-honeywell-estimates/)
- GAO (2023): the PTMS needs more engine bleed air than originally anticipated, which shortens engine life. GAO estimated that this adds about $38 B to life-cycle cost, mostly through reduced engine life — [Defense News, 1 Jun 2023](https://www.defensenews.com/air/2023/06/01/auditors-future-f-35-cooling-needs-unknown-as-dod-eyes-engine-upgrade/); [AviationPros](https://www.aviationpros.com/aircraft/defense/news/53062066/overworked-f35-jet-engines-could-cost-the-pentagon-38b-in-upkeep-gao-finds)
- Upgrades:
  - Honeywell P40 raises PTMS capacity from about 32 to 40 kW (+25 %) through software and liquid-loop changes — [The Defense Post, 24 Sep 2026](https://thedefensepost.com/2026/09/24/honeywell-f35-cooling-boost/); [Australian Defence Magazine](https://www.australiandefence.com.au/news/news/honeywell-improves-on-f-35-cooling-technology)
  - Collins EPACS has demonstrated 80 kW and uses less bleed air — [Airforce Technology](https://www.airforce-technology.com/newsletters/collins-epacs-testing-f-35/); [Breaking Defense, Feb 2024](https://breakingdefense.com/2024/02/as-the-heat-rises-with-f-35-upgrades-inside-collinss-bet-on-a-new-cooling-system)
  - Pratt & Whitney says the F135 ECU paired with an upgraded PTMS can deliver 80 kW or more — [Airforce Technology: RTX cooling system](https://www.airforce-technology.com/newsletters/rtx-unveils-cooling-system-paving-the-way-for-future-f-35-upgrades)
  - The JPO's desired state is 62–80 kW for post-Block 4 upgrades — [Frontier India](https://frontierindia.com/f-35-cooling-woes-upgrades-needed-to-enable-future-capabilities/)
  - Honeywell estimated a full PTMS replacement at about $3 B — [Aviation Today](https://www.aviationtoday.com/2023/08/15/replacing-f-35-ptms-may-cost-3-billion-honeywell-estimates/)
- XB-70 fuel tanks were nitrogen-blanketed to prevent fuel ignition as skin temperatures rose — [FIU](https://web.eng.fiu.edu/allstar/wings7.htm)

### Inferences
- **Ram air at Mach 3 is a heat source.** Ram air stagnates at T0 ≈ 333–399 °C (computed, Q1), so every cooling load (cockpit, avionics, radar, IR sensors, hydraulics, generator) must be rejected to fuel. Air must be cooled by an air cycle machine or vapour cycle, or rejected to fuel, before use. The PTMS has to be sized for the end of a Mach 3 dash, when fuel remaining is lowest and fuel temperature highest. That is the opposite of the F-35's subsonic sizing case, and its result was the 30–32 kW shortfall.
- **Fuel heat-sink budget (method).** Q_sink = ṁ_fuel·c_p,fuel·(T_limit − T_fuel,in). Using c_p ≈ 2.0 kJ/(kg·K) (a typical kerosene value, from memory, unverified) and a 163 °C limit with fuel starting at 60 °C, each kg/s of burned fuel absorbs about 200 kW. Total capacity is therefore tied to throttle setting, and recirculation to tank adds a tank-temperature constraint. Moving to a JP-8+100-type fuel with a 218 °C limit adds about 50 % heat sink, consistent with the SAE claim.
- The SR-71 needed a special fuel (JP-7) and nitrogen tank inerting. A modern Mach 3 design study must treat the fuel specification as a design variable: JP-8+100, JPTS or a JP-7-class fuel. That choice has logistics cost.
- A canopy of polycarbonate or acrylic cannot take 300+ °C outer-surface temperatures. A Mach 3 design needs a glass or quartz outer ply with an inner pressure ply and cooling or insulation between them, following the SR-71 pattern. It also needs a stealth-compatible conductive coating rated to temperature (see Q7).

### Gaps
- Not found:
  - The SR-71 ECS architecture, cooling capacity and cockpit air temperatures, and primary sources for the quartz windshield (material grade and thickness).
  - JP-7 and JPTS thermal-stability (coking) limits from a primary source.
  - Avionics heat-load numbers for 5th-generation fighters beyond the F-35 PTMS capacity.
  - The fuel c_p and heat-sink kJ/kg values; the figure used above was not sourced.
  - Heat-exchanger and air-cycle-machine weight per kW data, which would be needed for weight estimation.

## 7. Materials vs stealth at Mach 3: RAM temperature limits, SR-71/A-12 ferrite paint and composite edges

### Takeaway
Conventional polymer-bound RAM is the weak link. Leading-edge hot spots on supersonic aircraft already exceed 250 °C, and at Mach 3 acreage reaches about 300 °C. Ferrite absorbers stop working above their Curie temperature. High-Curie-point spinel ferrites (> 700 °F) have historically had adhesion and thermal-shock problems. The A-12 and SR-71 used an "iron ball" ferrite paint plus radar-absorbing composite fillets of iron ferrite and silicon laminate with asbestos. Research ceramics claim absorption at > 1,000–1,800 °C but are not flight-proven.

### Cited Findings
- The A-12 top coat was "iron ball paint", with small iron balls mixed into the paint. It reportedly cost $400 per quart in the 1960s and was also used on the SR-71 — [The War Zone (TWZ), electron guns article](https://www.twz.com/32722/cias-predecessor-to-the-sr-71-blackbird-tested-electron-guns-to-hide-from-radars)
- The A-12's fillets were replaced with radar-absorbing composites made from iron ferrite and silicon laminate combined with asbestos — [Wikipedia: Lockheed A-12](https://en.wikipedia.org/wiki/Lockheed_A-12)
- The A-12 burned cesium-laced fuel to create "plasma stealth", reducing the exhaust plume's radar return. The CIA also tested electron guns to cut radar returns — [TWZ: plasma stealth](https://twz.com/29787/the-sr-71-blackbirds-predecessor-created-plasma-stealth-by-burning-cesium-laced-fuel); [TWZ: electron guns](https://www.twz.com/32722/cias-predecessor-to-the-sr-71-blackbird-tested-electron-guns-to-hide-from-radars)
- A 1968 Skunk Works internal history of the A-12 program has been declassified and is in the CIA reading room, along with a CIA diagram of the A-12's anti-radar features — [TWZ](https://www.twz.com/32722/cias-predecessor-to-the-sr-71-blackbird-tested-electron-guns-to-hide-from-radars)
- A US patent describes spinel ferrites with Curie temperatures above 700 °F as a route to high-temperature radar-absorbing coatings. It notes that such coatings had poor adhesion and stability under thermal shock and vibration — [US Patent 6,909,395 "Radar absorbing coatings"](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6909395)
- Above its Curie temperature a ferrite loses its magnetic absorbing properties. Shown for accelerator ferrite absorbers — [KEK / IPAC2013 THPFI047](https://epaper.kek.jp/IPAC2013/papers/thpfi047.pdf)
- Stealth aircraft generally rely on radar-absorbent polymer skins, which are fragile and degrade under salt, moisture and abrasion. Leading-edge hot spots on supersonic aircraft can exceed 250 °C — [ASM International](https://www.asminternational.org/?p=70892); [ASM International](https://www.asminternational.org/tss/wp-json/wp/v2/posts/5122) (attribution approximate between the two)
- NC State reports a ceramic that absorbs ≥ 90 % of incident radar energy and works up to 1,800 °C, from lab tests reported via trade press — [ASM International](https://www.asminternational.org/?p=70892). An NSF I-Corps project describes a Ka-band ceramic nanocomposite surviving > 1,000 °C and says current RAM is heavy and has limited temperature survivability — [NSF I-Corps project](https://msesiom.demo.elsevierpure.com/es/projects/i-corps-radar-absorbing-materials-for-high-temperature-harsh-envi)
- Radar-transparent ceramics rated to 1,500 °C exist for radomes and fairings. These transmit rather than absorb — [KDPU Ukraine](https://kdpu-nt.gov.ua/en/node/64708)
- A commercial anechoic-chamber ferrite tile, PPG C-RAM FT-10, has a Curie point of only 203 °F (95 °C). It shows that off-the-shelf ferrites are not flight-temperature materials — [PPG Aerospace](https://www.ppg.com/en-US/aerospace/product/c-ram-ft-a-thin-ceramic-ferrite-tile-for-low-frequency-applications/PLP0000016017)

### Inferences
- Using the computed Mach 3 T_aw (Q1): RAM on acreage must survive about 300 °C continuous at Mach 3 (about 350 °C at Mach 3.2), and leading edges and inlet lips must survive about 330–400 °C. Polymer binders at the level of polyimides (≤ 260–288 °C, Q2) are marginal. Silicone binders (the A-12 "silicon laminate") or ceramic and glass binders, and ferrites with Curie temperatures well above about 400 °C, are the published direction.
- **Edge treatments.** The A-12 approach of absorbing composite fillets and chines, rather than metal edges, is the public precedent. A modern equivalent would be CMC or high-temperature polyimide-matrix absorbing edge structure, designed for thermal expansion mismatch against a titanium substructure (α of titanium differs from ceramics and composites).
- **IR stealth conflicts with Mach 3.** The skin at about 550–650 K radiates in the 3–5 µm band (Wien's law, Q1). Low-emissivity IR coatings reduce emission but also reduce the radiative cooling that holds skin temperature below T_aw. Lower ε means a hotter skin, which further stresses RAM and resin limits. This trade must be modelled explicitly with the heat balance in Q1.
- RAM and coating weight should be carried as a separate group-weight item in Q5. No sourced areal-density value was found.

### Gaps
- Not found, per the unclassified scope:
  - Quantitative temperature ratings for any fielded aircraft RAM.
  - The composition or RCS performance of the SR-71's paint beyond the "iron ball" description.
  - Ferrite Curie temperatures of specific absorber chemistries.
  - The emissivity of SR-71 paint.
- The CIA reading-room A-12 documents (1968 Skunk Works history) were identified but not read, and are the best public primary source.
- No public data was found on IR-signature levels from aerodynamic heating, or on low-ε coating temperature limits.

## 8. Tools: FEA, thermal analysis, and MMPDS as the property standard

### Takeaway
A free toolchain can cover the study. Use pyNastran to build and post-process Nastran-format (BDF/OP2) models, MYSTRAN for linear static, modal and buckling solutions in Nastran format, and CalculiX (Abaqus-like input) or Code_Aster (EDF, GPL) for coupled thermal–structural and nonlinear thermal analysis. For design allowables use MMPDS (formerly MIL-HDBK-5), the public material-property standard, which is purchased, not free.

### Cited Findings
- MYSTRAN is a Fortran solver for linear structural problems. Its input closely follows NASTRAN, so many NASTRAN models run with little or no change. A forum post notes that it lacks some element types CalculiX has, such as BUSH. FreeCAD's FEM workbench can drive MYSTRAN through pyNastran — [FreeCAD wiki: FEM Solver Mystran](https://wiki.freecad.org/FEM_SolverMystran/ru); [Mecway forum](https://mail.mecway.com/forum/discussion/1188/mystran-nastran-support). A third-party listing gives its licence as MIT, which is unconfirmed — [AlternativeTo](https://alternativeto.net/software/mystran)
- pyNastran is a Python API for reading and writing NASTRAN BDF, F06 and OP2 files. It supports about 200 of the roughly 700 BDF cards, and a Nastran-to-Code_Aster converter is under development — [pyNastran docs: Project Overview](https://pynastran-git.readthedocs.io/en/v0.7/manual/introduction.html)
- CalculiX is suited to structural and thermal analysis, uses Abaqus-like input, and has implicit and explicit solvers — [FEAssistant: Top free FEA options](https://feassistant.com/top-free-options-for-finite-element-analysis-fea/)
- Code_Aster, developed by EDF under the GPL, supports linear and nonlinear thermal analysis including phase change, and mechanical and multiphysics analysis — [EDF Code_Aster brochure](https://www.edf.fr/sites/default/files/Lot%203/CHERCHEURS/Code_Aster/code_aster_brochure_presentation.pdf)
- MMPDS succeeds MIL-HDBK-5 as the source of temperature-dependent design allowables. The relevant tables are in its titanium chapter, for example the Ti-6Al-4V elevated-temperature factors. This comes from a search-engine summary, not a primary MMPDS page — see [PMC9146263](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9146263/) for context on elevated-temperature Ti-6Al-4V data (attribution approximate)
- Historical public design-data reports, such as the Lockheed 1962 B120VCA sheet study, are freely available through the IIT Contrails archive and complement MMPDS for older alloys — [IIT Contrails](https://contrails.library.iit.edu/item/159100)

### Inferences
- Suggested workflow:
  1. Run a transient thermal analysis in CalculiX or Code_Aster with the convective-radiative boundary condition from Q1, h·(T_aw − T_w) = ε·σ·T_w⁴ + conduction. Run it over a mission profile: climb, Mach 3 cruise soak, then deceleration (the worst ΔT, with skin cooling faster than the spars).
  2. Map the temperatures onto a Nastran-format structural model with pyNastran.
  3. Run linear static, buckling and modal analysis in MYSTRAN, or nonlinear and thermal-stress analysis in CalculiX or Code_Aster, using temperature-dependent E, α and allowables from MMPDS.
  4. Check margins at 1.5 × limit plus thermal stress.
- The YF-12 program (Q1) is the best public validation dataset for a thermal–structural workflow: flight data, IR lamp-heated ground tests and NASTRAN predictions on the same airframe. Reproducing a YF-12 wing-panel case would be a useful verification exercise.

### Gaps
- No source confirmed MMPDS's current edition (MMPDS-19 or later, as of 2026), its price or its access terms.
- No aerospace-specific verification benchmarks were found comparing MYSTRAN, CalculiX and Code_Aster for thermal stress.
- Open-source aeroelastic and flutter tools were not researched: for example Nastran SOL 145 equivalents, which MYSTRAN does not offer as far as known (unverified), or the doublet-lattice / piston-theory codes needed for supersonic panel flutter.
