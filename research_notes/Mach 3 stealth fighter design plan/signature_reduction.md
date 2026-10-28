# Aircraft Signature Reduction: Principles, Public Estimates, Mach 3 Conflicts, and Tools (open sources only)

How these notes were made (please read): In this session, direct page fetching was blocked by the network for almost every host: en.wikipedia.org, globalsecurity.org, airandspaceforces.com, calhoun.nps.edu, cia.gov, gao.gov, dtic.mil, nsarchive, openems.de, mathworks.com, radartutorial.eu and github.com. The web-search quota also ran out partway through. So every "Cited Findings" item below comes from a search-engine summary of the linked page. None was checked against the full text. Treat them as "reported by", and re-verify key numbers before you use them in design decisions.

Items under "Inferences" are of two kinds. Some are **my own calculations**: standard physics (radar range equation, Stefan–Boltzmann/Planck, recovery temperature, quarter-wave absorber, radar horizon), computed in a script, with inputs and outputs shown. Others are **standard textbook background**, labelled "(textbook background, not web-verified this session)". All aircraft RCS numbers are **unofficial estimates**. Real values are classified, and they depend on frequency, aspect angle and polarization.

## 1. RCS fundamentals, the radar range equation / fourth-root law, and public RCS estimates

### Takeaway
Radar detection range scales only as σ^¼. Halving the range takes a 16× (12 dB) RCS cut, and cutting it 10× takes a 10,000× (40 dB) cut. That is why stealth fighters aim for −20 to −40 dBsm frontal RCS, against roughly +10 to +14 dBsm for F-15/Su-27-class fighters. The public figures for every aircraft are unofficial, often contradictory, and almost always frontal-sector, high-frequency (X-band) numbers.

### Cited Findings
- **Public RCS estimates (all unofficial).** A GlobalSecurity compilation cites D. Richardson, *Stealth Warplanes* (2001). It gives: B-2 ≤ 0.1 m²; F-117A ≤ 0.025 m²; F-35 0.0015–0.005 m²; F-22 0.0001–0.0005 m². In dBsm: B-2 ≤ −10, F-117 ≤ −16, F-35 −28 to −23, F-22 −40 to −33 — [GlobalSecurity, "Stealth aircraft RCS"](https://www.globalsecurity.org/military/world/stealth-aircraft-rcs.htm)
- The same GlobalSecurity page gives conflicting B-2 numbers: a widely reported ~−40 dBsm, but also ~0.75 m², and 0.01 m² (−20 dBsm) head-on. These differ by orders of magnitude — [GlobalSecurity](https://www.globalsecurity.org/military/world/stealth-aircraft-rcs.htm)
- The page also cites a 2005 *Aviation Week* item. It ranks the F-35 slightly better than the B-2, and the B-2 "twice as good" as the F-117. That ordering contradicts the table above, which puts the F-117 well below the B-2 — [GlobalSecurity](https://www.globalsecurity.org/military/world/stealth-aircraft-rcs.htm)
- F-15 Eagle 10–25 m² (+10 to +14 dBsm); Su-27 Flanker 10–15 m² (+10 to +11.8 dBsm). The table cites enthusiast and university material — [GlobalSecurity](https://www.globalsecurity.org/military/world/stealth-aircraft-rcs.htm)
- In November 2005 the USAF reportedly said the F-22's RCS was equivalent to a "steel marble" and the F-35's to a "metal golf ball". Secondary sources convert these to ~0.0001 m² and ~0.0015 m²; that conversion is not official. Forum commentary notes the "golf ball" remark came before real-world RCS modelling of production F-35s — [StrategyPage, "F-22 Stealth Ability Revealed by USAF" (2005-11-25)](https://www.strategypage.com/htmw/htairfo/articles/20051125.aspx); [f-16.net thread "F-22 and F-35 RCS revealed by USAF"](https://www.f-16.net/f-16_forum_viewtopic-t-4408.html)
- **Su-57.** A news report says a Sukhoi patent gives a frontal RCS of 0.1–1 m² (−10 to 0 dBsm). I could not verify the patent itself. Lower-quality pages give 0.1–0.5 m², and an unsourced forum post claims −30 to −35 dBsm. Estimates span about 3 orders of magnitude — [WION, "Ghost jet effect: can enemy radar really detect the Su-57"](https://www.wionews.com/photos/ghost-jet-effect-can-enemy-radar-really-detect-the-su-57-fighter-jet-1780638318875) (the search summary did not clearly name which news page carried the patent claim)
- An open-access 2024 academic paper simulates the RCS of an F-35-like model. It is useful as a methods template: Mattei, "RCS of a F-35 Stealth Aircraft", TechDefence 2024 — [Univ. Basilicata IRIS PDF](https://iris.unibas.it/bitstream/11563/196355/1/89_Mattei_TechDefence2024_RCS_of_a_F-35_Stealth_Aircraft.pdf)
- APG-77 (F-22 radar): Wikipedia gives an operating range of 125–150 mi (201–241 km) against a 1 m² target, and flags these figures as unconfirmed — [Wikipedia, AN/APG-77](https://en.wikipedia.org/wiki/AN/APG-77)

### Inferences
- **RCS definition (textbook background, not web-verified this session; Knott/Shaeffer/Tuley, *Radar Cross Section*):** σ = lim_{R→∞} 4πR²·|E_s|²/|E_i|² [m²]. In decibels, σ_dBsm = 10·log10(σ / 1 m²). So 1 m² = 0 dBsm, 0.1 = −10, 0.01 = −20, 0.001 = −30, 0.0001 = −40, 10 m² = +10, 25 m² = +14.
- **Frequency regimes (textbook background).** These are set by ka = 2πa/λ, where a is the characteristic size of the scatterer:
  - *Rayleigh* (ka ≪ 1): σ ∝ λ⁻⁴, and shape detail barely matters.
  - *Resonance/Mie* (ka ~ 1–10): creeping waves and surface waves interfere, and σ oscillates.
  - *Optical* (ka ≫ 10): σ is dominated by local features — specular points, edges, tips, cavities.
- **Electrical size of a fighter** (my calculation, 18.9 m F-22-length airframe; 3 m fin):
  - X-band (10 GHz, λ = 3.0 cm): ~630 λ long, fin ~100 λ → deep optical region.
  - S-band (3 GHz, λ = 10 cm): ~190 λ long, fin ~30 λ.
  - L-band (1.3 GHz, λ = 23 cm): ~82 λ long, fin ~13 λ.
  - UHF (450 MHz, λ = 67 cm): ~28 λ long, fin ~4.5 λ.
  - VHF (150 MHz, λ = 2 m): ~9 λ long, fin ~1.5 λ → tails, wingtips and control-surface edges sit in the resonance region.
- **Canonical scatterers** (textbook formulas, Knott; my numbers):
  - Flat plate at normal incidence, σ = 4πA²/λ². A 1 m² plate gives 13,963 m² (+41.4 dBsm) at X-band, 1,257 m² (+31.0) at S-band and 236 m² (+23.7) at L-band. One flat panel facing the radar can therefore out-shine a whole conventional fighter by ~30 dB, so specular directions must be pointed away from threat sectors.
  - Dihedral with 0.5 m × 0.5 m faces, σ_max = 8πa²b²/λ²: 1,745 m² (+32.4 dBsm) at X-band. Wing–fuselage and fin–tailplane right angles act like this.
  - Triangular trihedral with a = 0.5 m, σ = 4πa⁴/(3λ²): 291 m² (+24.6 dBsm) at X-band.
  - (Optical formulas are not valid at VHF for these sizes.)
- **"Marble/golf ball" as metal spheres** (σ ≈ πa² in the optical limit; my calculation): a 42.7 mm golf ball gives 1.43×10⁻³ m² (−28.4 dBsm), and a 12.7 mm marble gives 1.27×10⁻⁴ m² (−39 dBsm). These match the circulated F-35 (~0.0015 m²) and F-22 (~0.0001 m²) conversions. That suggests the popular figures are just sphere-area conversions of a metaphor, not data. At X-band the golf ball has ka ≈ 4.5 and the marble ka ≈ 1.3, so they are resonance-region spheres, not purely optical.
- **Radar range equation** (textbook background, Skolnik/Knott; not web-verified this session): R_max = [P_t·G²·λ²·σ / ((4π)³·k·T_s·B·F·(S/N)_min·L)]^¼, so R_max ∝ σ^¼. Worked numbers (my calculation), with an illustrative baseline radar that detects 1 m² at 200 km (the same order as the unconfirmed APG-77 figure):

  | Target (unofficial estimate) | σ (m²) | dBsm | Detection range |
  |---|---|---|---|
  | F-15 upper bound | 25 | +14 | 447 km |
  | F-15/Su-27 typical | 10 | +10 | 356 km |
  | reference | 1 | 0 | 200 km |
  | Su-57 low-end claim / B-2 | 0.1 | −10 | 112 km |
  | F-117 | 0.025 | −16 | 80 km |
  | B-2 head-on claim / "SR-71-class" circulated figure | 0.01 | −20 | 63 km |
  | F-35 upper | 0.005 | −23 | 53 km |
  | F-35 "golf ball" | 0.0015 | −28 | 39 km |
  | F-22 upper | 0.0005 | −33 | 30 km |
  | F-22 "marble" | 0.0001 | −40 | 20 km |

  Going from 10 m² to 0.0001 m² (−50 dB) cuts detection range by a factor of only 17.8 (356 km → 20 km).
- **Rules of thumb that follow:** every −12 dB halves range; every −40 dB divides it by 10. Self-protection jamming also gets more effective as σ falls. For a self-screening jammer, J/S ∝ R²/σ, so burn-through range R_bt ∝ √σ: a 40 dB RCS cut shrinks burn-through range 100× (textbook background).

### Gaps
- **MiG-25 / MiG-31:** no public RCS estimate found. By inference from similar size and features (large rectangular inlets, twin vertical tails, external stores; ~20 m length), F-15-class values (10–25 m², +10 to +14 dBsm) are plausible. This is an inference, not a sourced figure.
- **SR-71:** a figure of ~0.01 m² (and 0.014 m²) circulates on blogs and forums. The search summary did not let me tie it to a traceable source, so treat it as folklore-level until verified (e.g., Crickmore, or CIA/Lockheed declassified histories).
- I could not fetch Knott *Radar Cross Section* (2nd ed., SciTech, 2004) or Skolnik to confirm equation forms and page numbers. The team should check them in the books.
- No public aspect-resolved (polar) RCS data exists for any operational stealth aircraft. All published figures are single numbers with unstated frequency, aspect, polarization and statistic (peak, median, average).

## 2. Shaping principles (planform alignment, faceting vs curvature, chines, canted tails, serrations, canopy, inlets, internal bays, antennas)

### Takeaway
Shaping is the primary RCS tool in the optical region. It does three things: removes specular returns from threat sectors, concentrates the remaining "spikes" into a few planform-aligned directions, and eliminates corner reflectors and cavities. The faceted F-117 was a product of 1970s computing limits (Echo 1 plus Ufimtsev's PTD). The later continuous-curvature approach (B-2, F-22) works because codes improved.

### Cited Findings
- **Ufimtsev → Echo 1 → Have Blue lineage.** Pyotr Ufimtsev, of the Moscow Institute of Radio Engineering, published "Method of Edge Waves in the Physical Theory of Diffraction". Sources give the date as 1962 or 1964. The USAF Foreign Technology Division translated it (1971 per the Pioneers of Stealth newsletter). Lockheed's Denys Overholser realised it gave a mathematical way to compute edge diffraction from flat plates — [Wikipedia, Lockheed Have Blue](https://en.wikipedia.com/wiki/Have_Blue); [Pioneers of Stealth newsletter, Apr 2024](https://pioneersofstealth.org/POSApr2024NewsFINAL.pdf)
- Lockheed's RCS-prediction program "ECHO 1" first got edge returns wrong because of diffraction. Overholser added Ufimtsev's method, and the team could then quickly rank about 20 candidate designs and settle on the faceted delta. Other accounts say faceting was chosen because the computers of the day could only handle flat surfaces — [Wikipedia, Have Blue](https://en.wikipedia.com/wiki/Have_Blue); [Pioneers of Stealth](https://pioneersofstealth.org/POSApr2024NewsFINAL.pdf)
- Have Blue was a late-1970s Lockheed Skunk Works demonstrator meant to prove that a faceted aircraft with radar-absorbing material could be nearly radar-invisible. First flight was 1 December 1977, both aircraft were lost, and the data fed the F-117 — [Wikipedia, Have Blue](https://en.wikipedia.com/wiki/Have_Blue)
- **Chines on a Mach 3 aircraft (A-12).** When the Soviet TALL KING radar appeared, the CIA directed Lockheed to rebuild the A-12 chines to change its RCS. The CIA history records the change as expensive, "undesirable", and as reducing performance — [CIA, *Archangel: CIA's Supersonic A-12 Reconnaissance Aircraft* (D. Robarge)](https://www.cia.gov/resources/csi/static/Archangel-CIAs-Supersonic-A-12-Reconnaissance-Aircraft.pdf)
- A secondary source says the A-12/SR-71 chines were added for radar reasons, then turned out to produce roughly one-fifth of total lift and to improve yaw stability. Lower-confidence source — [The Aviation Geek Club, "Why the A-12 Oxcart was the first stealth aircraft"](https://theaviationgeekclub.com/heres-why-the-lockheed-a-12-oxcart-was-the-first-stealth-aircraft/)
- **The A-12's largest radar returns** were from the vertical stabilizers and the engine inlet (the summary was cut off before the third item) — [Air & Space Forces Magazine, "The Oxcart Story" (from the declassified CIA McIninch study)](https://www.airandspaceforces.com/article/1194oxcart/)
- **Wing shaping and frequency.** Beihang University work found that shape stealth gives significant RCS reduction in the resonance and high-frequency zones, but has a weaker effect in the Rayleigh zone — [BUAA, "Multi-frequency RCS reduction characteristics of shape stealth wing"](https://research.buaa.edu.cn/en/publications/multi-frequency-rcs-reduction-characteristics-of-shape-stealth-wi/)

### Inferences
The principles below are textbook background (Knott *Radar Cross Section*, ch. on RCS reduction; not web-verified this session).
- **Planform alignment.** Make all leading/trailing edges, panel-joint edges, door and bay edges, and inlet/nozzle lips parallel to a small number of directions (typically 2–4 per side). Edge-diffraction lobes then pile into a few narrow spikes outside the frontal threat cone, rather than spraying across all aspects. The F-22 and F-35 diamond planforms and sawtooth door edges follow this rule.
- **Serrations.** Edges that cannot be aligned — door edges, access panels, the canopy frame, the inlet lip — are sawtoothed so that each tooth edge is parallel to a main planform direction. Rule of thumb: tooth size must be several wavelengths at the lowest frequency it is meant to work against.
- **Faceting vs curvature.** Flat facets send specular energy into predictable non-threat directions, but create strong edge and vertex diffraction, and they cost aerodynamic efficiency. Continuously curved surfaces (B-2, F-22 fuselage) spread specular energy and avoid facet edges. They became possible once codes (PO/PTD, later MoM/FDTD) could handle curved geometry.
- **Canted twin tails** (F-22, F-35, YF-23, also the A-12's inward-canted fins) remove the 90° fin–tailplane dihedral and move the side specular flash away from the horizontal plane. The alternative is no vertical tails at all (B-2).
- **Chines / fuselage edge shaping** replace a circular fuselage cross-section, which gives a broadside specular return across all azimuths, with a sharp edge that reflects up or down.
- **Inlets.** Line-of-sight to the compressor face must be blocked. Methods are serpentine S-ducts (F-22, F-35 with DSI), radar blockers or grids (F-117 inlet screen; mesh pitch below λ/2 at the highest threat frequency), RAM-lined ducts, and top-mounted inlets (B-2). The engine face of a fan/compressor is a large cavity-plus-rotating-blades scatterer, which also produces "jet engine modulation".
- **Exhausts.** Use 2-D or serrated nozzles with RAM-treated or shielded aft cavities, and keep the turbine face out of line of sight.
- **Canopy.** A clear canopy lets radar reach the cockpit cavity (bulkheads, helmet, seat — a strong cavity return). Thin metallic or ITO-type conductive coatings make the canopy RF-reflective while staying optically transparent. Its shape must then be treated like any other surface.
- **Internal weapons bays and conformal or embedded antennas.** External stores and pylons are corner reflectors and give large returns. Antenna apertures (radar, CNI, EW) are in-band by design, so they need frequency-selective radomes and low-RCS array design: a tilted array face, edge treatments, and "structural mode" control.
- **Gaps between panels, fasteners, steps and gaps** must be held to sub-millimetre tolerance and filled or coated. Otherwise they produce traveling-wave and edge returns. This drives LO maintenance cost (see Q8).
- **Scattering mechanisms to design against** (textbook background):
  1. Specular reflection — dominant, frontal and broadside.
  2. Edge diffraction — leading/trailing edges.
  3. Tip/vertex diffraction.
  4. Traveling and surface waves along long smooth surfaces, re-radiated at discontinuities (trailing edges, gaps). These matter at grazing incidence.
  5. Creeping waves around smooth bodies — important at lower frequencies and resonance.
  6. Cavities and ducts — inlets, exhausts, cockpit.
  7. Multi-bounce dihedral/trihedral corners.
  8. Antenna "in-band" returns.

### Gaps
- I found no web source in this session that directly documents B-2 continuous-curvature design rules, F-22 canopy metallization, or specific F-117 inlet-grid dimensions. The principle-level statements above are background from Knott/Ufimtsev and should be checked against those books. Specific aircraft implementation details (grid pitch, coating composition) are not public at an engineering level.
- No quantitative public data on RCS penalties per feature (e.g., the dB cost of an untreated canopy or an external pylon) was found.

## 3. Radar-absorbing materials and structures (RAM/RAS), the Mach 3 skin-heating conflict, A-12/SR-71 RCS reduction, and high-temperature absorbers

### Takeaway
Classical absorbers rely on quarter-wave resonance, magnetic loss (ferrites) or dielectric loss. Their thickness scales with wavelength: ~7.5 mm at X-band but ~50 cm at VHF for an air-spaced Salisbury screen, and the Rozanov-type bandwidth–thickness limit is unavoidable. At Mach 3, skin temperatures of ~290–340 °C (recovery temperature in the stratosphere), with hot spots reportedly near 1,000 °F (~540 °C), rule out most polymer-matrix RAM. They also push ferrites toward loss of magnetic performance. That is why the A-12 relied on speed and altitude plus limited high-temperature RAM, and why current research is moving toward SiC-fibre ceramic-matrix absorbers tested to ~600 °C.

### Cited Findings
- **Salisbury screen:** a resistive sheet a quarter wavelength (λ/4) in front of a conducting ground plane, separated by a dielectric spacer. It works well at only one design frequency — [Wikipedia, Salisbury screen](https://en.wikipedia.org/wiki/Salisbury_screen)
- The 20 dB (99% power absorption) bandwidth of a classic Salisbury screen is narrow, about 25% — [Defence Science Journal (DRDO), 2018](https://publications.drdo.gov.in/ojs/index.php/dsj/article/download/12025/6086/36081)
- **Jaumann absorbers** are multilayer Salisbury screens: several resistive sheets plus spacers give ultra-wideband absorption, but their large thickness limits practical use — [Defence Science Journal (DRDO)](https://publications.drdo.gov.in/ojs/index.php/dsj/article/download/12025/6086/36081)
- A six-layer Jaumann example averaged about 30 dB of RCS reduction across 7–15 GHz (cited in a US patent from Connolly et al.) — [US Patent 5,976,666](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5976666)
- **Thinner-absorber research.**
  - A capacitive-circuit absorber design reported 28% less thickness and 57% more bandwidth than a Salisbury screen — [Lund University (2008)](https://www.lunduniversity.lu.se/lup/publication/93292f5e-11ab-4ecf-8c7e-2781f0ae5299)
  - A Salisbury screen built from frequency-selective surfaces improved bandwidth and angular stability at the same thickness — [Heriot-Watt / IET MAP 2011](https://researchportal.hw.ac.uk/en/publications/design-of-a-salisbury-screen-absorber-using-frequency-selective-s/)
- RAM thickness scales with wavelength: lower frequencies need thicker RAM, and different radar bands need different RAM types — [RF Essentials, "RCS reduction" glossary](https://rfessentials.com/resources/rf-glossary/rcs-reduction/)
- **A-12/OXCART RCS reduction (declassified CIA history via Air & Space Forces).**
  - Researchers studied ferrites, high-temperature absorbing materials and high-temperature plastic structures to reduce the return.
  - Early absorbent-material work helped but did not solve the problem.
  - In late 1958 a CIA review panel judged that a much faster, higher-flying aircraft could be made nearly undetectable by radar, and the analysis found supersonic speed greatly reduced the chance of radar detection.
  — [Air & Space Forces Magazine, "The Oxcart Story"](https://www.airandspaceforces.com/article/1194oxcart/)
- Production A-12s were painted with a radar-absorbent coating of **ferrite particles in a plastic binder** — [CIA, *Archangel*](https://www.cia.gov/resources/csi/static/Archangel-CIAs-Supersonic-A-12-Reconnaissance-Aircraft.pdf)
- A secondary source describes A-12 edge structures as a composite of silicon laminate, iron ferrite and asbestos that absorbed radar. Lower confidence — [The Aviation Geek Club](https://theaviationgeekclub.com/heres-why-the-lockheed-a-12-oxcart-was-the-first-stealth-aircraft/)
- **Aft-sector plume RCS.** Kelly Johnson wrote: "To overcome the afterburner problem of a large radar cross section return from the aft quadrant, we proposed the use of [a] cesium additive to the fuel" — [The War Zone, "SR-71's predecessor created plasma stealth by burning cesium-laced fuel"](https://www.twz.com/29787/the-sr-71-blackbirds-predecessor-created-plasma-stealth-by-burning-cesium-laced-fuel.md)
- **Project KEMPSTER.** Per Wikipedia, KEMPSTER used an electron-beam generator to create an ionization cloud in front of each inlet. It was flight tested but never deployed on operational A-12s or SR-71s. The cesium fuel additive ("A-50") was a separate exhaust-ionization measure. Some web sources conflate the two — [Wikipedia, Plasma stealth](https://en.wikipedia.org/wiki/Plasma_stealth)
- **SR-71 skin temperatures at Mach 3.2** are inconsistent across popular sources. Reported values:
  - Typical skin ~400–620 °F (204–327 °C), with one source giving ~400 °C/750 °F.
  - Chines and inlets toward ~1,000 °F (538 °C).
  - Leading edges up to ~1,100 °F (593 °C), the least well supported figure.
  - A low figure of 400 °F from *National Interest*.
  None are measured IR data — [National Interest](https://nationalinterest.org/node/68752); [AIAA Aerospace Micro-Lesson #62](https://aiaa.org/detail/lesson/aerospace-micro-lesson-62); [MiGFlug, SR-71 fuel-leak/titanium article](https://migflug.com/afterburner/sr-71-blackbird/) (exact attribution of each number to each page is uncertain in the search summary)
- **High-temperature absorbers (public research, mostly Chinese university groups, X/Ku-band lab coupons).**
  - Sandwich-structured SiC-fibre/Si₃N₄ composite: broadband absorption "essentially unchanged" up to 600 °C (Composites Part B, 2025, DOI 10.1016/j.compositesb.2025.112618) — [NWPU Pure record](https://pure.nwpu.edu.cn/en/publications/sandwich-structured-sicsubfsubsisub3subnsub4sub-composite-with-di/)
  - SiCf/Si₃N₄ made by chemical vapour infiltration: still absorbs ~75% of incident energy in X and Ku band at 600 °C, about 6% below room temperature — [NWPU, "High-temperature EM wave absorption properties of SiCf/Si₃N₄"](https://pure.nwpu.edu.cn/en/publications/high-temperature-electromagnetic-wave-absorption-properties-of-si/)
  - SiCf/AlPO₄ with carbon nanotubes: 4.2 GHz bandwidth below −8 dB at 3.1 mm thickness over 25–600 °C. The paper also notes that SiC matrices from PIP/CVI processes tend to be carbon-rich and strongly reflective, while oxide matrices reflect less — [Wan et al. 2020 (PDF mirror)](https://vyunov.pp.ua/MW/LTCC/2020-Wan-Improved%20mechanical%20and%20high-temperat.pdf)
  - SiC-nanowire composite: minimum reflection loss −47.5 dB at 11.4 GHz and 2.8 GHz effective bandwidth at 600 °C — [Beihang University](https://research.buaa.edu.cn/en/publications/effect-of-sic-nanowires-on-the-high-temperature-microwave-absorpt/)
  - Structural SiC-fibre-reinforced high-temperature wave-absorbing composite (NWPU) — [NWPU](https://pure.nwpu.edu.cn/en/publications/a-high-temperature-structural-and-wave-absorbing-sic-fiber-reinfo/)
  - Reviews: [NWPU, "Research status and outlook of high temperature radar absorbing materials"](https://pure.nwpu.edu.cn/en/publications/research-status-and-outlook-of-high-temperature-radar-absorbing-m/); [J. Materials Research & Technology 2022 review on CMC high-temperature stealth (DOAJ)](https://doaj.org/article/d5cc44d9563f4cb8bf86f356ac0f3fee)

### Inferences
- **Quarter-wave spacer thickness** (my calculation; d = λ/(4√ε_r), ignoring magnetic loading):

  | Band | λ | d, air spacer | d, ε_r = 4 spacer |
  |---|---|---|---|
  | VHF 150 MHz | 2.0 m | 50 cm | 25 cm |
  | UHF 450 MHz | 67 cm | 16.7 cm | 8.3 cm |
  | L 1.3 GHz | 23 cm | 5.8 cm | 2.9 cm |
  | S 3 GHz | 10 cm | 2.5 cm | 1.25 cm |
  | C 5.5 GHz | 5.5 cm | 1.4 cm | 0.7 cm |
  | X 10 GHz | 3.0 cm | 7.5 mm | 3.7 mm |
  | Ku 15 GHz | 2.0 cm | 5.0 mm | 2.5 mm |

  Absorbers practical on a fighter skin (a few mm) work at X/Ku and partly S/C, but cannot reach VHF/UHF. This is the physical root of the counter-stealth problem in Q6.
- **Fundamental bandwidth–thickness bound** (textbook/literature background, not web-verified this session; K. N. Rozanov, IEEE Trans. Antennas Propag., 2000). For a metal-backed absorber, |∫₀^∞ ln|ρ(λ)| dλ| ≤ 2π²·Σ μ_s,i·d_i, where μ_s is static permeability. Wide band at low frequency requires thickness or high static permeability, which favours magnetic (ferrite / carbonyl-iron) RAM. Magnetic RAM is temperature-limited and heavy.
- **Absorber categories** (textbook background):
  1. *Magnetic RAM* — ferrite or carbonyl-iron particles in a polymer binder, as in the A-12's ferrite-in-plastic coating. Thin (~1–2 mm at X-band), dense and heavy. Permeability falls as temperature approaches the Curie point.
  2. *Dielectric / lossy-dielectric RAM* — carbon- or graphite-loaded foams, pyramidal and wedge absorbers. Lightweight, but thick.
  3. *Resonant absorbers* — Salisbury screen, Dallenbach layer, Jaumann multilayer, circuit-analog/FSS absorbers.
  4. *Radar-absorbing structure (RAS)* — the absorber is the load-bearing laminate or honeycomb. Example: the A-12's edge "plastic" structures per the CIA account.
- **Mach 3 temperature budget** (my calculation; recovery temperature T_r = T∞·(1 + r·(γ−1)/2·M²), r = 0.89 turbulent, T∞ = 216.65 K stratosphere):

  | Mach | T_r | T₀ (total temperature) |
  |---|---|---|
  | 0.9 | −25 °C | −21 °C |
  | 1.5 | 30 °C | 41 °C |
  | 2.0 | 98 °C | 117 °C |
  | 2.5 | 185 °C | 214 °C |
  | 3.0 | 291 °C | 333 °C |
  | 3.2 | 338 °C | 387 °C |

  Stagnation regions — leading edges, inlet lips, nose — approach T₀; the reported SR-71 hot spots are hotter still. This is consistent with the "~300 °C skin" assumption in the brief, and with the reported 400–620 °F SR-71 averages.
- **What this implies for materials** (polymer temperature limits are general materials knowledge, not web-verified this session):
  - The ~290–340 °C equilibrium skin at sustained Mach 3 exceeds common epoxy-matrix limits (~120–180 °C service) and BMI limits (~200–230 °C). It is at the edge of polyimides (~290–340 °C).
  - The F-22/F-35 polymer-based LO coating and composite approach therefore does not transfer to Mach 3 without new materials.
  - Leading edges, inlet lips and nozzle surfaces would need ceramic RAS (SiC/Si₃N₄, oxide/oxide CMC) of the type in the NWPU/BUAA work above.
- **Validation caution:** the published high-temperature CMC absorbers are X/Ku-band coupon results with reflection loss of −8 to −10 dB (85–90% absorption) at 600 °C. That is far short of the −20 dB-class treatments assumed for frontal LO. Erosion, thermal cycling and rain/particle impact at Mach 3 are not reported.
- **A-12 lesson.** RCS reduction on a Mach 3 airframe was possible but limited: a ferrite coating, plastic edges and chines, and plasma ideas for the inlet/plume. The CIA treated speed plus altitude (~80–90 kft) as the main survivability factor, and a new VHF early-warning radar (TALL KING) forced costly, performance-reducing reshaping. That is a direct historical precedent for the conflict this design study faces.

### Gaps
- No open source was found giving quantitative A-12/SR-71 RCS values by aspect, or the exact composition of their absorbers. Composition details beyond "ferrite in plastic binder" and "silicone/asbestos/ferrite edge laminate" should be treated as unknown. The project constraints also rule out pursuing them.
- The search did not return the CIA McIninch study's specific RCS goals, though the Lockheed report it cites exists in the National Security Archive. The nsarchive and cia.gov full texts could not be fetched.
- No public data on the long-duration (hundreds of hours) durability of high-temperature RAM at Mach 3 conditions was found.

## 4. Infrared signature: plume, hot parts, and aerodynamic skin heating at Mach 3 vs Mach 0.9

### Takeaway
At Mach 3 the airframe itself becomes a strong infrared source. Skin exitance rises ~12.8× in total radiated power from 30 °C to 300 °C. In-band it rises **~200× in the 3–5 µm MWIR band** and ~11× in the 8–12 µm LWIR band. For a point-source IRST, detection range scales roughly as √(in-band intensity contrast), so the MWIR skin signature alone extends detection range ~14×. No feasible low-emissivity coating closes that gap. IR is therefore the signature that most directly conflicts with Mach 3.

### Cited Findings
- **Skin heating study (2012, Trans. JSASS / KAIST).** Aircraft skin temperatures can exceed ~300 K at typical supersonic cruise, which makes skin IR suppression a key survivability technology. The study used CFD for skin temperature, a reverse Monte Carlo model for IR signature, and detection range and IR contrast as metrics. It concluded that controlling skin temperature and surface emissivity effectively reduces detectability — [KAIST repository, "Evaluating the Effectiveness of Infrared Signature Suppression of Aircraft Skin"](https://koasas.kaist.ac.kr/handle/10203/101853)
- **Main aircraft IR sources** are aerodynamically heated surfaces, hot engine components, and the exhaust plume. External surfaces radiate mainly in LWIR — [The Aeronautical Journal (Cambridge, 2025), IR signature of aero-engine exhaust plumes and aircraft surface](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D14DC72BD1247D01A1D4883B5B17B687/S0001924024001635a.pdf/infrared-signature-of-aero-engine-exhaust-plumes-potential-core-and-aircraft-surface-from-direct-bottom-view.pdf)
- **IRST detection ranges against conventional fighters** are reported (weakly sourced, blog) as ~50 km head-on and ~100 km from the rear against subsonic non-afterburning fighters, and 50–100 km head-on / 100–150+ km rear in general overviews — [MiGFlug, "How IRST lets fighters see without radar"](https://migflug.com/jetflights/?p=2243807)
- **SR-71 temperatures** for context: typical skin ~400–620 °F, hot spots near ~1,000 °F — see Q3 sources ([National Interest](https://nationalinterest.org/node/68752); [AIAA micro-lesson #62](https://aiaa.org/detail/lesson/aerospace-micro-lesson-62))

### Inferences
All numbers below are my calculations, using Stefan–Boltzmann M = εσT⁴ (σ = 5.670×10⁻⁸ W m⁻² K⁻⁴) and Planck integration.
- **Total exitance (ε = 1)**, the case the brief asked for:
  - 30 °C (303.15 K): **479 W/m²**
  - 300 °C (573.15 K): **6,119 W/m²**
  - Ratio: **12.8×**
- **In-band exitance (ε = 1), which is what IRSTs see:**

  | Skin temperature | MWIR 3–5 µm | LWIR 8–12 µm |
  |---|---|---|
  | 216.65 K stratospheric ambient | 0.10 W/m² | 18.9 W/m² |
  | 248 K (M0.9 at altitude) | 0.61 | 43.6 |
  | 303 K (30 °C) | 6.6 | 127 |
  | 371 K (M2.0) | 48 | 313 |
  | 564 K (M3.0 recovery) | 1,172 | 1,307 |
  | 573 K (300 °C) | 1,301 | 1,370 |
  | 611 K (M3.2) | 1,927 | 1,639 |

  - 300 °C vs 30 °C: **MWIR ×198, LWIR ×10.8**.
  - The Wien peak shifts from 9.6 µm at 303 K to 5.1 µm at 573 K — straight into the MWIR band where many IR seekers and IRSTs operate.
- **A more realistic like-for-like comparison** puts both aircraft at stratospheric altitude: Mach 0.9 skin ≈ −25 °C (248 K) vs Mach 3 ≈ 291 °C (564 K).
  - Exitance ratio: total ×27, MWIR ×1,900, LWIR ×30.
  - Contrast against a 216.65 K blackbody background: MWIR 0.52 → 1,172 W/m² (×~2,250); LWIR 24.7 → 1,288 W/m² (×52).
  - So the brief's "30 °C at Mach 0.9" case understates the penalty. Note, though, that a subsonic fighter's MWIR signature is dominated by plume and hot parts rather than skin, so the skin-only ratio overstates the *total*-signature ratio from some aspects.
- **Radiant intensity**, Lambertian, I = ε·M_band·A/π:
  - Head-on projected area ~10 m², 573 K, ε = 0.9: **I_MWIR ≈ 3,700 W/sr, I_LWIR ≈ 3,900 W/sr**.
  - Same area at 303 K: I_MWIR ≈ 19 W/sr, I_LWIR ≈ 365 W/sr.
  - Planform view ~80 m² (seen from below or above) at 573 K: I_MWIR ≈ 30,000 W/sr.
  - Even at ε = 0.1, a 573 K skin gives ~414 W/sr MWIR head-on — still ~20× the ε = 0.9, 303 K value.
- **IR detection-range scaling** (point-source IRST): sensor irradiance E = τ(R)·ΔI/R². Detection occurs when E ≥ NEI·SNR_req, so **R ≈ √(τ·ΔI/(NEI·SNR))**, and in clear air R ∝ √ΔI. That is a **square-root** law, versus the radar fourth-root law, so IR signature changes move detection range much more than equal-ratio RCS changes do.
  - MWIR: √198 ≈ **14× longer range** from skin heating alone (constant ε).
  - LWIR: √10.8 ≈ **3.3×**.
  - Atmospheric transmission τ(R) compresses this at long range. But a Mach 3 aircraft flies at 20–25 km in thin, dry, low-attenuation air, and is viewed against a cold sky, so the attenuation offset is smaller than at low altitude.
- **Emissivity cannot fix it.** To match the 303 K, ε = 0.9 skin in-band, a 573 K skin would need ε ≈ **0.005 in MWIR** (physically unachievable for a practical coating) and ε ≈ **0.08 in LWIR** (very aggressive). Low ε also means high reflectance, so the skin reflects sun, earthshine and sky, and lowering ε reduces radiative cooling, pushing skin temperature toward T_r.
- **Thermal-management conflict.** The SR-71 is widely reported to have used a high-emissivity black finish to shed heat. That claim was not verified in this session, but the physics holds: at 573 K and ε = 0.9 the skin radiates ~5.5 kW/m², a significant cooling mechanism. High ε cools the structure; low ε reduces IR signature. The two requirements are directly opposed.
- **Mitigation options** (textbook background, not web-verified this session):
  - Plume and hot parts: 2-D, shielded or buried nozzles that hide the turbine face and hot cavities; mixing bypass or ambient air into the plume; upper-surface exhausts (B-2, F-117 platypus); cooled nozzle liners.
  - Skin: spectrally selective low-ε coatings (low in the 3–5 and 8–12 µm atmospheric windows, high outside them for cooling); active skin cooling with fuel as heat sink (as on the SR-71, which used fuel to cool the airframe — widely reported but not verified this session); limiting Mach 3 dash duration.
- **Plume at Mach 3:** a turbojet/turbo-ramjet propulsion system sustaining Mach 3 typically runs with afterburning or ramjet combustion, producing a very hot, large plume. Kelly Johnson's "afterburner problem" quote (Q3) shows it was also a radar-signature problem for the A-12.

### Gaps
- No public measured IR signature data (W/sr by band and aspect) for the SR-71, MiG-25/31 or any Mach 3 aircraft was found.
- IRST performance numbers (NEI, aperture, false-alarm logic) for systems such as OLS-35, PIRATE or Legion Pod were not found in reliable sources. The range figures above are blog-level.
- The plume IR of a Mach 3 propulsion system — J58-type turbo-ramjet vs a modern variable-cycle engine — was not quantified in sources found.

## 5. Other signatures: acoustic / sonic boom, visual / contrails, RF emissions (LPI radar, EMCON, LPI/LPD datalinks)

### Takeaway
A Mach 3 aircraft cannot hide its sonic boom carpet along the ground track. RF emissions are often the largest detectability term for a stealth fighter, so LPI radar (wideband, low-peak-power, highly directional) and narrow-beam high-frequency datalinks (e.g., MADL) are design requirements. Sourcing for this question was the thinnest of the study.

### Cited Findings
- The **AN/APG-77** (F-22) is described as a multifunction low-probability-of-intercept radar. Its 120° azimuth/elevation field of view is the maximum practical for a flat phased array, and the antenna itself has very low RCS — [Wikipedia, AN/APG-77](https://en.wikipedia.org/wiki/AN/APG-77)
- APG-77 LPI techniques are described (in forum and secondary sources) as low-energy pulses spread over a wide frequency band (spread-spectrum), with LPI built into waveform design throughout. Whether dedicated "LPI modes" exist is disputed — [f-16.net, "APG-77 development and features"](https://www.f-16.net/forum/viewtopic.php?p=483365)
- A US patent describes **MADL** (Multifunction Advanced Data Link) as a high-frequency (~20 GHz), low-power (~5 W) link with very low probability of detection and intercept. The patent's other descriptions are unusual, so treat this as low confidence — [US Patent 7,024,309](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7024309)

### Inferences
- **Sonic boom** (my calculation, Mach angle μ = arcsin(1/M)): μ = 30° at M2.0 and **19.5° at M3.0**. A Mach 3 aircraft at 24 km lays down a continuous boom carpet tens of km wide along its ground track. It is acoustically detectable and locatable by simple ground microphone networks, and it compromises the ground-track secrecy of low-observable penetration. At high altitude the overpressure is lower, but it never goes away (textbook background).
- **Visual/contrail** (textbook background, not verified this session): contrails form when the Schmidt–Appleman criterion is met, typically at ambient temperatures below roughly −40 °C in the upper troposphere. Very dry stratospheric air above the tropopause can suppress persistent contrails, but the transit climb through the contrail layer is visible. Mach 3 skin heating does not create visible glow at ~300 °C, since visible incandescence begins near ~500 °C+; hot-spot leading edges and the afterburner plume at night are a visual concern. Visual camouflage (paint) conflicts with high-ε thermal paints and RAM top-coats.
- **RF emission control:** a stealth fighter's own radar, radar altimeter, IFF, datalinks and jammers can be detected by ESM at ranges far beyond the radar's own detection range, because the one-way propagation advantage goes R² vs R⁴. LPI methods are wideband/frequency-agile waveforms with low peak power and long integration, very low antenna sidelobes, power management (transmit only the energy needed), and passive sensing (ESM, IRST) first. LPI datalinks use high frequency (narrow beams, atmospheric absorption near the 60 GHz oxygen line for some designs) and directional antennas (textbook background).
- **Mach 3 interaction:** a Mach 3 aircraft may rely more on off-board cueing (datalinks) and passive sensors, because it covers ~53 km per minute (885 m/s). That increases dependence on LPI/LPD communications.

### Gaps
- No sources were found in this session on sonic-boom overpressure at Mach 3 and 24 km altitude (e.g., SR-71 or Concorde boom measurements, NASA studies), contrail-formation criteria, or the acoustic signature of stealth fighters.
- No reliable public detail on the waveforms of LPI radars (APG-77/81) or on MADL's operational EMCON role was found. The search budget ran out before these topics could be searched further.

## 6. Counter-stealth and limits: VHF/UHF radar (Nebo-M), multistatic/passive radar, IRST, and the wavelength dependence of shaping

### Takeaway
Shaping and thin RAM are tuned for the optical region (X/Ku/C, and partly S). At VHF (λ ≈ 1–2 m), fighter-scale features such as tails and wingtips are only ~1–5 λ, putting them in the resonance region. There, shaping has an "unsurmountable limit" and thin absorbers do nothing. VHF radars such as Nebo-M can therefore detect stealth fighters, but they lack the angular and range accuracy to guide weapons. That is why they are networked with L/S/X-band radars. A Mach 3 aircraft flying at 20–25 km is also above the radar horizon of every ground radar out to roughly 600–650 km.

### Cited Findings
- **Nebo-M** is a multiband system: the VHF-band RLM-M plus L-band and S-band radars, linked through a command post. In one deployment concept the VHF radar paints incoming stealth aircraft head-on, while the flanking L/S radars view the less-stealthy sides — [Sandboxx, "How effective is Russia's Nebo-M counter-stealth radar?"](https://www.sandboxx.us/news/how-effective-is-russias-nebo-m-counter-stealth-radar/); [Wikipedia, Nebo-M](https://en.wikipedia.org/wiki/Nebo-M)
- The low-frequency arrays (VHF Nebo-SVU and L-band Protivnik-G) can detect stealth fighters but do not provide targeting-quality data, so they are networked with an S/X-band radar (Gamma-S1) — [Sandboxx](https://www.sandboxx.us/news/how-effective-is-russias-nebo-m-counter-stealth-radar/)
- The size of fighter aircraft prevents effective shaping in the VHF band (per the same discussion) — [Sandboxx](https://www.sandboxx.us/news/how-effective-is-russias-nebo-m-counter-stealth-radar/)
- India has inducted the Nebo-UM VHF radar to detect stealth fighters such as the J-20. One report claims it can track stealth fighters at ~250 km under favourable conditions (press claim, unverified) — [The Week, 29 June 2026](https://www.theweek.in/news/defence/2026/06/29/iaf-china-pak-j-20-stealth-fighter-jets-with-nebo-um-radars.html); [IDRW](https://idrw.org/iaf-inducts-nebo-um-vhf-radar-to-strengthen-detection-of-stealth-fighters-and-ballistic-missiles/)
- An academic or student study analyses Nebo-M VHF detection performance against the F-35 (title only seen) — [Sonoma State ORSP](https://orsp.sonoma.edu/performance-analysis-nebo-m-vhf-band-radar-detection-capabilities-against-f-35-lightning-ii-using)
- **Wavelength dependence of shaping.** Beihang researchers found that shape-modification stealth "has an unsurmountable limit in Rayleigh and resonance regions". Radar stealth therefore needs to combine shaping with RAM in those regions — [BUAA, "Frequency response scattering characteristic of aircraft" (Acta Aeronautica et Astronautica Sinica 2009, 30(4):643–648)](https://hkxb.buaa.edu.cn/CN/Y2009/V30/I4/643)
- A half-wave resonance effect can still give a significant return when the radar wavelength is about twice the size of a target feature — [RF Essentials](https://rfessentials.com/resources/rf-glossary/rcs-reduction/)
- **Limits of low-frequency radar** (secondary sources): poor accuracy because of the long wavelength, crowded spectrum, and large antenna size, so they are typically too imprecise to guide a missile — [MiGFlug, "How stealth really works"](https://migflug.com/jetflights/de/?p=290580); [Aircraft Wiki (fandom), Counter-stealth radar](https://aircraft.fandom.com/wiki/Counter_Stealth_Radar)
- **Historical precedent:** the TALL KING radar prompted costly reshaping of the A-12 chines — [CIA, *Archangel*](https://www.cia.gov/resources/csi/static/Archangel-CIAs-Supersonic-A-12-Reconnaissance-Aircraft.pdf)

### Inferences
- **Electrical size at VHF** (my calculation, Q1): at 150 MHz a fighter is ~9 λ long, with fins ~1.5 λ. Edge-alignment and serration rules assume features of many wavelengths, so they lose effectiveness. A λ/4 Salisbury layer at VHF would be ~50 cm thick (Q3), which is impossible on a fighter skin. Larger flying wings (the B-2 at ~52 m span is ~26 λ at VHF) keep more shaping benefit than fighters, consistent with the claim that the B-2's size keeps shaping effective at lower bands. That claim was quoted on a fan wiki and is unverified.
- **Mach 3 vs VHF:**
  - *Doppler* (my calculation): a Mach 3 target at 885 m/s gives 885 Hz Doppler at 150 MHz and 59 kHz at X-band, vs 266 Hz / 17.7 kHz at Mach 0.9. High radial velocity makes the target easy to separate from clutter and slow birds or balloons in Doppler processing. Speed does not help against detection; it helps by shortening reaction time.
  - *Radar horizon* (my calculation, 4/3-Earth model, d ≈ 4.12(√h_t + √h_r) km with h in m, radar at 10 m): a target at 100 m altitude is visible from ~54 km, at 11 km from ~445 km, and at 24 km (~79 kft) from ~650 km. Mach 3 cruise gives up terrain masking completely and exposes the aircraft to every long-range VHF/L-band surveillance radar line-of-sight.
  - *Exposure time:* crossing an 800 km-wide detection footprint takes ~15 min at Mach 3 vs ~50 min at Mach 0.9. This was the CIA/A-12 survivability logic: get detected, but deny an intercept.
- **Multistatic/passive radar** (textbook background, not web-verified this session): stealth shaping redirects energy away from the transmitter, not away from every receiver. Bistatic receivers placed in the reflected-energy directions, and forward-scatter geometries where the target silhouette blocks a direct path (forward-scatter RCS ≈ 4πA²/λ² with A the shadow area, independent of RAM), can see returns that a monostatic radar cannot. Passive coherent location using FM, DVB-T or cellular illuminators operates at VHF/UHF, where shaping is weakest.
- **IRST** is the passive counter to RF stealth (Q4). It is the most dangerous counter for a Mach 3 design, because Mach 3 multiplies the MWIR skin signature by roughly two orders of magnitude.

### Gaps
- No quantitative public data on fighter RCS at VHF/UHF (e.g., F-35 at 150 MHz) was found. Defence-press claims of Nebo-M/UM detection ranges are unverified.
- No sources specifically on passive coherent location or multistatic detection of LO aircraft were obtained before the search budget ran out.
- Nebo-M frequency bands and parameters were not confirmed from primary or manufacturer sources.

## 7. Methods and tools a small team can use: POFACETS, open PO/MoM/FDTD codes, key textbooks, and test practice

### Takeaway
A two-person team can do credible conceptual RCS screening. Use POFACETS, a free MATLAB physical-optics facet code from NPS with a materials and coatings database, for X/S-band monostatic and bistatic trade studies on faceted CAD models. Pair it with a full-wave code such as openEMS (FDTD), or NEC-class MoM, for resonance-region (VHF/UHF) and canonical-feature checks. Validate against canonical shapes (plate, dihedral, sphere, cylinder) and, ideally, small-scale pole-model measurements.

### Cited Findings
- **POFACETS** is an NPS program that uses physical optics (PO) to predict the RCS of complex targets modelled as triangular facets. It has minimal computer-resource requirements and short run-times — [NPS Calhoun, Chatzigeorgiadis thesis record](https://calhoun.nps.edu/entities/publication/d27555d2-094e-4b7e-b150-682ce35111f1)
- **Garrido (NPS, 2000)** built the MATLAB GUI version. It lets users build facet models and compute monostatic or bistatic RCS without deep knowledge of the underlying method (advisor: David C. Jenn) — [NPS Calhoun, "Graphical user interface for a physical optics radar cross section prediction code"](https://calhoun.nps.edu/entities/publication/02a49858-3b2c-4065-a3e9-9dbb51408488); [DTIC ADA383252](https://apps.dtic.mil/sti/pdfs/ADA383252.pdf)
- **Chatzigeorgiadis (NPS, 2004/2006; the record and PDF give different dates)** extended POFACETS with:
  - a user-updatable database of materials and coatings, applied to models in one or more layers, with their effect on RCS computed;
  - ground-effect calculations;
  - symmetry planes to cut run time.
  Advisors were D. Jenn and D. C. Schleher — [NPS thesis PDF](https://calhoun.nps.edu/bitstream/handle/10945/1453/04Sep_Chatzigeorgiadis.pdf;sequence=3)
- POFACETS 4.1 (MATLAB, PO-based) remained in use in a 2017 IEEE conference paper — [IEEE Xplore 7988835](https://ieeexplore.ieee.org/document/7988835/metrics). A University of Alcalá thesis used it to design corner reflectors — [UAH e-Buah](https://ebuah.uah.es/dspace/handle/10017/26639)
- **Pole-model and range testing history.** Declassified photos show A-12 Oxcart RCS tests at Area 51 (pole-mounted full-scale or large-scale models) — [The Aviationist, 2021](https://theaviationist.com/2021/02/01/check-out-these-fascinating-declassified-photos-of-the-a-12-oxcart-rcs-tests-inside-area-51/)
- **In-service verification.** After each LO repair on the B-2, the radar cross section of the area must be checked by probe or zonal measurement — [AIN, "USAF Counts the True Cost of B-2 Stealth" (2006)](https://ainonline.com/aviation-news/defense/2006-11-30/usaf-counts-true-cost-b-2-stealth)
- **Example open methods paper:** Mattei, TechDefence 2024, F-35-like RCS simulation — [IRIS Unibas PDF](https://iris.unibas.it/bitstream/11563/196355/1/89_Mattei_TechDefence2024_RCS_of_a_F-35_Stealth_Aircraft.pdf)

### Inferences
The tool and method descriptions below are textbook or community background, not web-verified this session.
- **What PO/POFACETS captures and misses:**
  - PO integrates induced surface currents on illuminated facets. It is accurate for specular and near-specular returns in the optical region (ka ≫ 1), with simple facet-level shadowing.
  - It does **not** model, or models poorly: edge diffraction away from specular (add PTD/MEC — Ufimtsev's correction is the whole point of PTD), multiple bounces (dihedral/trihedral, inlet ducts — needs SBR ray tracing), traveling/creeping waves, cavities, and resonance-region behaviour.
  - Use it for planform and shaping trade studies at X/S-band. Do not use it to claim −30 dBsm-class absolute accuracy.
- **Recommended open toolchain for a small team:**
  1. Parametric CAD in OpenVSP (NASA open-source) or similar → triangulated STL → POFACETS (MATLAB, or Octave with adaptation) for X/S-band monostatic polar plots and bistatic maps.
  2. Full-wave validation of canonical features and low-frequency behaviour:
     - openEMS (open-source FDTD with MATLAB/Octave/Python interfaces), for small components and scaled models, including absorber stack design;
     - MEEP (MIT open-source FDTD);
     - NEC-2/4nec2 (MoM wire-grid) for crude VHF whole-aircraft resonance estimates.
     Full-wave runs on a whole fighter at X-band (~600 λ long) are out of reach without HPC; at VHF (~9 λ) they are tractable on a workstation.
  3. Absorber design: 1-D transmission-line (multilayer) models in Python/MATLAB, checked with openEMS unit-cell runs.
  4. Commercial options with academic/student licences: Altair Feko (MoM/MLFMM/PO/SBR), CST, Ansys HFSS-SBR+.
- **Validation discipline:** reproduce textbook closed forms (flat plate 4πA²/λ², sphere πa², dihedral 8πa²b²/λ², cylinder 2πaL²/λ) before trusting aircraft results. Report RCS by frequency, polarization (HH/VV), aspect sector (e.g., ±30° frontal) and statistic (median, mean, peak).
- **Measurement practice:** anechoic compact ranges for scaled models; outdoor ground-plane or pole ranges (low-RCS pylons, e.g., the A-12 pole tests) for large models; scale modelling (scale the frequency by the same factor as the size, with material properties scaled accordingly — hard for RAM). Software-only conceptual work is the realistic scope for a two-person team. Hobby-level scaled measurements need a VNA plus horn antennas and a small absorber-lined enclosure.
- **Key references:**
  - E. F. Knott, J. F. Shaeffer, M. T. Tuley, *Radar Cross Section*, 2nd ed., SciTech Publishing (2004), the standard RCS engineering text;
  - P. Ya. Ufimtsev, *Fundamentals of the Physical Theory of Diffraction*, Wiley-IEEE Press (2007; 2nd ed. 2014);
  - D. C. Jenn, *Radar and Laser Cross Section Engineering*, AIAA Education Series (Jenn was the POFACETS thesis advisor);
  - M. Skolnik, *Introduction to Radar Systems*, for the range equation.
  Edition years are from memory and need verification.

### Gaps
- I could not confirm the current POFACETS distribution point (NPS website or MathWorks File Exchange), its licence, or its latest version beyond 4.1.
- I could not verify openEMS RCS examples or licence terms (openems.de and github.com blocked; search budget exhausted).
- No public detail on US government RCS ranges (e.g., RATSCAT at Holloman/White Sands, Lockheed Helendale) was retrieved this session.

## 8. Trade-offs: stealth vs aerodynamics, stealth vs maintenance, stealth vs cost

### Takeaway
LO features cost aerodynamic performance and drive maintenance and cost. The A-12's RCS-driven chine rebuild reduced performance. LO coatings account for roughly half of the B-2's 48 maintenance man-hours per flight hour (2006), and the F-22 needed ~34 maintenance hours per flight hour vs 19 for the F-16, mostly due to RAM. The F-35 tried to engineer this down with more durable coatings and baked-in tolerances, and later F-35 coating technology was back-fitted to cut F-22 costs. A Mach 3 LO design inherits all of these and adds high-temperature materials.

### Cited Findings
- **F-22:** ~34 maintenance man-hours per flight hour vs 19 for the F-16, against a manufacturer estimate of under 10. The report attributes most of the excess to radar-absorbent material. The USAF found that applying the more durable F-35 RAM coatings to the F-22 reduces its maintenance costs — [StrategyPage, "F-35 Tech Rescues the F-22" (2011)](https://www.strategypage.com/htmw/htcbtsp/20110410.aspx)
- **GAO (2021) on the F-22:** low-observable maintenance continues to drive the not-mission-capable-maintenance (NMCM) rate. As the fleet ages, it needs more repairs for corrosion and for aging LO coatings — [GAO F-22 report (DocumentCloud copy)](https://s3.documentcloud.org/documents/21118719/gaof22.pdf)
- A 2026 secondary blog claims roughly one-third of F-22 maintenance is devoted to repairing and re-curing the stealth skin, at about 30 hours per flight hour. It also gives an implausible B-2 figure of 119 hours. Low confidence — [Aviation A2Z (2026)](https://aviationa2z.com/index.php/2026/06/26/why-f-22s-stealth-paint-costs-far-more-than-the-b-52s-exterior-coating/)
- A secondary site headlines an F-22 coating cost of $60,000 per gallon and operating costs up to $85,000 per flight hour. Low-confidence source — [Aviospace](https://aviospace.org/?p=15349)
- **B-2 (2006 Boeing briefing):** about half of the 48 maintenance man-hours per flying hour relate to LO features. After every repair, local RCS is verified by probe or zonal measurement. Spray-on coatings that cure in about 30 minutes have improved turnaround — [AIN (2006)](https://ainonline.com/aviation-news/defense/2006-11-30/usaf-counts-true-cost-b-2-stealth)
- A 2009 article cites ~25 B-2 maintenance hours per flight hour, and robotic coating application reportedly halving maintenance hours (unverified) — [StrategyPage, "F-22 Magic Backfires" (2009)](https://www.strategypage.com/htmw/htmurph/20090224.aspx)
- **F-35 sustainment (GAO 2023, via Janes):**
  - Fleet mission-capable rate ~55% in March 2023.
  - Repair backlog of 141 days, 81 days over the 60-day goal.
  - Shortfalls blamed on depot and organizational maintenance, training, and technical data.
  - This reporting is not LO-specific — [Janes](https://www.janes.com/defence-news/defence/latest/gao-says-deficient-maintenance-leaves-us-f-35s-well-below-mission-capable-rate-goal)
- The F-35 uses a Low Observable Health Assessment System (LOHAS) to record LO damage and repairs and compute maintenance requirements (forum-sourced, unverified) — [f-16.net forum](https://www.f-16.net/forum/viewtopic.php?p=487186)
- Lockheed Martin publicity (2008) presented F-35C stealth as designed for "high performance, low maintenance" on carrier decks — [Lockheed Martin press release, 2008-03-18](https://news.lockheedmartin.com/2008-03-18-F-35C-Stealth-on-the-Carrier-Deck-Means-High-Performance-Low-Maintenance)
- **Stealth vs aerodynamics on a Mach 3 aircraft (A-12):** RCS-driven reshaping of the chines was "expensive" and reduced performance — [CIA, *Archangel*](https://www.cia.gov/resources/csi/static/Archangel-CIAs-Supersonic-A-12-Reconnaissance-Aircraft.pdf)

### Inferences
- **Aerodynamics vs stealth** (textbook background):
  - Planform alignment constrains sweep angles. Leading-edge sweep at Mach 3 wants to be ~70°+ to stay behind the Mach cone (μ = 19.5°, so a leading edge needs > 70.5° sweep to be subsonic), and all other edges must then align to the same angles.
  - Internal bays add volume and cross-section, raising supersonic wave drag (area rule).
  - S-ducts cost total-pressure recovery and length. Mach 3 inlets need variable-geometry compression systems — spikes and ramps, as on the SR-71 and MiG-25 — and these are large, moving, in-line-of-sight radar scatterers that are difficult to treat.
  - Canted tails can lose control power.
  - Faceting costs lift/drag. The F-117 was subsonic, and its faceting is not compatible with Mach 3 wave-drag minimisation.
- **Maintenance vs stealth:** the US fleet trend is from fragile, labour-intensive treatments (B-2 tape and caulk; F-22 early RAM) toward durable baked-in coatings and in-situ RCS verification (F-35 LOHAS). Adding Mach 3 thermal cycling (−55 °C to ~300 °C every sortie) to LO treatments and sub-millimetre panel-gap tolerances would very likely make LO maintenance worse than on the F-22. Thermal expansion of a 20 m titanium or steel airframe at ΔT ≈ 350 K is ~6–8 cm overall (α ≈ 9×10⁻⁶ /K for Ti, 20 m × 9e-6 × 350 ≈ 6.3 cm). SR-71 panels were famously loose-fitting on the ground — widely reported, not verified this session. Expansion on this scale defeats sealed sub-millimetre LO gaps.
- **Cost vs stealth:** no quantitative public cost split (LO vs non-LO) was found. Qualitatively, LO drives acquisition cost (tolerances, materials, RCS verification ranges) and sustainment cost (coatings, hangar climate control, labour).

### Gaps
- No authoritative GAO or USAF figure for current (2024–2026) F-22 or F-35 LO-specific maintenance hours per flight hour was found. The 34 MMH/FH (F-22, 2011) and 48 MMH/FH with ~50% LO (B-2, 2006) figures are dated.
- No public, quantified acquisition-cost premium for stealth was found.

## 9. Synthesis: specific conflicts between Mach 3 flight and low observability

### Takeaway
Mach 3 and "as invisible as possible" conflict along nearly every signature axis:
- IR skin emission (MWIR ×~200–2,000);
- RAM thermal limits (~290–340 °C skin vs polymer RAM limits);
- radar horizon (~650 km exposure at 24 km altitude);
- variable-geometry inlets that are hard to shield;
- afterburning plumes (radar and IR);
- unavoidable sonic boom;
- thermal expansion vs LO tolerances.

Historically, the A-12/SR-71 resolved this by treating speed and altitude as the primary defence, with RCS reduction a secondary, partial measure. A Mach 3 LO fighter concept would need either very high-temperature RAS/CMC structures with spectrally selective, cooled skins, or a mission profile that limits Mach 3 to short dashes outside IRST engagement geometry.

### Cited Findings
- The CIA's 1958 judgment: a much faster, higher-flying aircraft could be made nearly undetectable by radar, and supersonic speed greatly reduced the chance of detection. In practice RCS work "helped but not enough", and a VHF radar (TALL KING) later forced reshaping — [Air & Space Forces, "The Oxcart Story"](https://www.airandspaceforces.com/article/1194oxcart/); [CIA, *Archangel*](https://www.cia.gov/resources/csi/static/Archangel-CIAs-Supersonic-A-12-Reconnaissance-Aircraft.pdf)
- The afterburner plume gave a large aft-quadrant radar return, which motivated the cesium fuel additive — [The War Zone](https://www.twz.com/29787/the-sr-71-blackbirds-predecessor-created-plasma-stealth-by-burning-cesium-laced-fuel.md)
- Skin temperature above ~300 K at supersonic cruise makes skin IR suppression a key survivability need; skin temperature and emissivity control are the levers — [KAIST/JSASS 2012](https://koasas.kaist.ac.kr/handle/10203/101853)
- High-temperature ceramic absorbers retain partial absorption (≈75–90%, −6 to −10 dB-class) at 600 °C in X/Ku band, in lab samples only — [NWPU](https://pure.nwpu.edu.cn/en/publications/high-temperature-electromagnetic-wave-absorption-properties-of-si/); [Wan 2020](https://vyunov.pp.ua/MW/LTCC/2020-Wan-Improved%20mechanical%20and%20high-temperat.pdf)

### Inferences
Conflict matrix (my synthesis of Q1–Q8):

| Signature | Effect of Mach 3 cruise (~24 km) | Quantified (my calcs) | Mitigation direction |
|---|---|---|---|
| Radar (X/S, monostatic) | Shaping still works; RAM must survive ~290–340 °C skin, ~540 °C hot spots; variable inlets and spikes hard to shield; afterburner plume returns | RAM: polymer limits ~120–340 °C vs T_r 291 °C (M3) | CMC/RAS edges and inlets; shielded variable inlet; plume treatment |
| Radar (VHF/UHF) | Shaping ineffective at fighter scale; detection by EW radars across ~650 km horizon | Fighter ~9 λ at 150 MHz; λ/4 absorber ~50 cm | Accept detection; deny tracking/engagement (speed, altitude, EW) |
| IR | Skin becomes an MWIR/LWIR emitter from all aspects; plume hot | MWIR ×198 (30→300 °C); range ×~14 (point-source √ law); ε needed ≈0.005 MWIR | Selective low-ε skins + fuel cooling; limit dash time; nozzle shielding |
| Acoustic | Continuous sonic boom carpet | Mach angle 19.5° | None at Mach 3; subsonic ingress |
| Visual | Contrail risk during climb; plume at night | — | Altitude selection, plume cooling |
| RF | Higher dependence on datalinks and off-board cueing | 885 m/s = 53 km/min | LPI/LPD links, EMCON, passive sensors |
| Exposure geometry | Above horizon, no terrain masking; but short exposure | 800 km crossing: 15 min (M3) vs 50 min (M0.9) | Speed as defence (A-12 logic) |

- **Design implication for the study:** treat "Mach 3" and "LO" as requirements to trade, not as both maximised. Useful parametric axes are:
  1. Fraction of the mission at Mach 3+;
  2. Frontal X-band RCS target (e.g., −20 vs −30 dBsm) and its range gain (fourth-root);
  3. MWIR skin intensity vs Mach (a square-root range penalty);
  4. Material temperature class per zone (polymer < 180 °C, BMI/polyimide < ~300 °C, Ti/CMC beyond);
  5. Inlet concept (fixed DSI is limited to roughly Mach 2-class; variable inlets are needed for Mach 3).
  The DSI Mach limit is textbook background, not verified this session.

### Gaps
- No open-source quantitative study combining RCS, IR and kinematic survivability for a Mach 3 LO fighter was found. The trade matrix above is my synthesis from physics and the cited fragments.
- Search budget exhaustion and blocked hosts prevented checking several primary sources against full text: the CIA *Archangel* and McIninch texts, GAO F-35/F-22 reports, NPS theses, and Wikipedia technical pages. Priority re-checks for the report writer or team:
  1. GlobalSecurity RCS table and original citations;
  2. CIA *Archangel* (RCS chapters);
  3. Chatzigeorgiadis thesis (POFACETS capabilities, materials database);
  4. GAO F-22 (2021) and F-35 sustainment reports;
  5. KAIST/JSASS 2012 skin IR paper.
