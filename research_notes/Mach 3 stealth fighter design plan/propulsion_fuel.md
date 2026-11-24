# Propulsion and Fuel for a Mach 3 Low-Observable Fighter

> **Read this first: research conditions and evidence labels (as of 28 Oct 2026).**
> This session's network policy blocked most primary hosts: en.wikipedia.org, ntrs.nasa.gov, apps.dtic.mil, enginehistory.org, globalsecurity.org, milavia.net, armedconflicts.com and thesr71blackbird.com all failed to resolve. The shared web-search budget also ran out partway through the work. Only github.com could be fetched in full. As a result, every finding carries one of three labels:
> - **[F]**: page fetched and read in this session.
> - **[S]**: seen only in a search-engine result summary or snippet. The URL is the result the search returned, but the page itself could not be opened, so the exact wording and attribution are probable but unconfirmed.
> - **[U]**: unverified background value from the researcher's prior knowledge. These appear **only in the Gaps sections**, each with the public source to check, and none of them is presented as a cited fact.
>
> **[Calc]** marks numbers computed in this session from standard textbook equations (ideal gas, γ = 1.4, cp = 1.004 kJ/kg·K, h_PR = 42,800 kJ/kg, ISA stratosphere T0 = 216.65 K, a0 = 295.0 m/s). The script is at `/tmp/claude-0/-home-user-ECC/2f27043a-9759-5d66-af1b-58c6cb6d5be8/scratchpad/calc.py`. The calculations are ideal (lossless) unless stated, so they show trends, not engine performance.
> No classified, leaked or export-controlled data was sought or used.

## Q1. Which engine types work across Mach 0–3+, and why do conventional turbofans fail at Mach 3?

### Takeaway
Two limits that arrive together stop a conventional turbofan at Mach 3. Ram compression heats the compressor face to about 330 °C at Mach 3.0 and 387 °C at Mach 3.2 [Calc], and the compressor-exit and turbine-inlet temperature limits then leave almost no room for compression or heat addition. A Mach 3 engine therefore has to behave like a ramjet at the top end. The J58 did this through bleed-bypass. At Mach 3+ its turbomachinery supplied only about 17% of net propulsive thrust, while the inlet supplied about 54% and the ejector about 29% [S]. Modern equivalents are TBCC and variable-cycle or adaptive engines.

### Cited Findings
- **J58 / SR-71 thrust split at Mach 3+ cruise:** inlet ≈ 54%, engine ≈ 17%, ejector nozzle ≈ 29%. At Mach 2.2 the inlet produced only about 13% of thrust. — [S] [Enginehistory.org, "SR-71 Propulsion System" (AEHS 2013 convention paper)](https://enginehistory.org/Convention/2013/SR-71Propul/SR-71Propul.shtml)
- An alternative rounding of the same split gives inlet 54% / engine 17.6% / ejector 28.4% at "Mach 3.0+". — [S] [The SR-71 Blackbird, "J58: the powerplant for the Blackbirds"](https://www.thesr71blackbird.com/Aircraft/Engines/j58-the-powerplant-for-the-blackbirds)
- At high Mach the J58 engine itself supplies only about 17% of propulsive thrust. Most of the rest comes from pressure forces on the inlet and ejector walls. — [S] [Enginehistory.org SR-71 thrust diagram](https://enginehistory.org/members/images/SR-71/%282%29J58Engine/sr71thrustdiagram.html)
- Popular press rounds this to about 80% of thrust coming from inlet plus ejector (54 + 29 = 83%) and describes the J58 as a hybrid turbojet–ramjet at these speeds. Treat this as secondary. — [S] [Warrior Maven, "How famous SR-71 engine hit Mach 3"](https://warriormaven.com/news/air/how-famous-sr-71-engine-hit-mach-3-and-outran-missiles)
- **R-15B-300 (MiG-25)**: a deliberately low-pressure-ratio turbojet with a 5-stage axial compressor, single-stage turbine and overall pressure ratio of 4.75:1. This is consistent with a design point near Mach 2.5–3 (see the Inferences below). — [S] [Wikipedia, Tumansky R-15](https://en.wikipedia.org/wiki/Tumansky_R-15); [S] [ArmedConflicts, Mikulin R-15B-300](https://www.armedconflicts.com/Mikulin-R-15B-300-t176038)
- **Ramjet-assist / heat-sink rationale:** at Mach 5–10, heat loads exceed what the fuel's sensible heat can absorb, which is why endothermic cracking is studied. The point applies here because the thermal problem already begins at Mach 3 (see Q4). — [S] [DTIC ADA406019 (endothermic storable fuels report)](https://apps.dtic.mil/sti/pdfs/ADA406019.pdf)

### Inferences
**1. Compressor-face (ram) temperature [Calc].** Tt2 = T0·(1 + 0.2·M0²) and θ0 = (T0/288.15)·(1 + 0.2·M0²), both in the ISA stratosphere.

| M0 | Tt2 (K) | Tt2 (°C) | θ0 | Pt0/P0 (ideal ram) |
|---|---|---|---|---|
| 0.9 | 251.7 | −21 | 0.874 | 1.69 |
| 1.5 | 314.1 | 41 | 1.090 | 3.67 |
| 2.0 | 390.0 | 117 | 1.353 | 7.82 |
| 2.5 | 487.5 | 214 | 1.692 | 17.1 |
| 2.83 | 563.7 | 290 | 1.956 | 28.4 |
| 3.0 | 606.6 | **333** | 2.105 | 36.7 |
| 3.2 | 660.3 | **387** | 2.292 | 49.4 |
| 3.5 | 747.4 | 474 | 2.594 | 76.3 |

- The brief quotes T2 ≈ 330–430 °C at Mach 3. The calculation confirms about 333 °C at Mach 3.0 and 387 °C at Mach 3.2 in standard stratosphere air. The 430 °C end of the range corresponds to roughly Mach 3.3 or a hot day. In a mixed-compression inlet the total temperature is conserved (adiabatic), so these values hold no matter how good the inlet is.

**2. The compressor runs out of temperature headroom [Calc].** The ideal π_c that keeps compressor exit Tt3 under a material limit is π_c,max = (Tt3,max/Tt2)^3.5.

| Tt3,max | SLS | M2.0 | M2.5 | M3.0 | M3.2 |
|---|---|---|---|---|---|
| 900 K | 53.8 | 18.7 | 8.6 | **4.0** | 3.0 |
| 950 K | 65.1 | 22.6 | 10.3 | **4.8** | 3.6 |
| 1000 K | 77.9 | 27.0 | 12.4 | **5.8** | 4.3 |

- If you hold π_c fixed instead, the exit temperature climbs. With π_c = 25 (F119/F135 class OPR; see Q2 Gaps), Tt3 rises from 723 K at SLS to 1,522 K at Mach 3.0, which is impossible for any compressor material. With π_c = 12 it reaches 1,234 K at Mach 3.0 [Calc]. A fixed-geometry, high-OPR turbofan must therefore cut corrected speed and airflow, so its thrust collapses. The MiG-25's OPR of 4.75 sits almost exactly at the π_c,max ≈ 4.8 that a ~950 K Tt3 limit allows at Mach 3. This is consistent with deliberate design for the top speed (inference).

**3. The turbine-inlet temperature (Tt4) limit squeezes the heat addition.** The available burner temperature ratio Tt4/Tt2 falls from 1800/288 = 6.25 at SLS to 1800/607 = 2.97 at Mach 3.0 [Calc]. Specific work, and with it specific thrust, scale with this ratio, so dry thrust lapses steeply.

**4. Ideal-cycle specific thrust and TSFC trends [Calc].** These use Mattingly's ideal turbojet and ramjet relations: Tt4 = 1,800 K, afterburner or ramburner Tt7 = 2,200 K, stratosphere, no losses. Cells show specific thrust (N per kg/s) / TSFC (per hour).

| M0 | TJ π_c=12 dry | TJ π_c=12 AB | TJ π_c=5 dry | TJ π_c=5 AB | Ideal ramjet |
|---|---|---|---|---|---|
| 0.9 | 985 / 1.08 | 1229 / 1.31 | 899 / 1.29 | 1078 / 1.50 | 519 / 3.11 |
| 2.0 | 758 / 1.10 | 1102 / 1.36 | 785 / 1.25 | 1036 / 1.45 | 811 / 1.85 |
| 2.5 | 609 / 1.10 | 1017 / 1.39 | 687 / 1.24 | 979 / 1.45 | 829 / 1.71 |
| 3.0 | 427* / 1.10 | 912* / 1.45 | 560 / 1.24 | 898 / 1.47 | 800 / 1.65 |
| 3.2 | 345* / 1.10 | 865* / 1.47 | 502 / 1.24 | 860 / 1.48 | 779 / 1.64 |
| 3.5 | 212* / 1.09 | 788* / 1.53 | 409 / 1.25 | 798 / 1.51 | 739 / 1.63 |

\* Physically unreachable: Tt3 would exceed 1,200 K (see table 2).

- Reading the table:
  - Above about Mach 2.5, the ideal ramjet's specific thrust matches or exceeds a dry turbojet's.
  - At Mach 3–3.5, the afterburning low-π_c turbojet and the ramjet converge to similar specific thrust (about 800–900 N per kg/s) and similar ideal TSFC (about 1.5–1.65 per hour).
  - This convergence is the thermodynamic case for the J58 bleed-bypass "turbo-ramjet" and for TBCC: at Mach 3+, the core adds little except as a gas generator, and the afterburner or ramburner does the work.
  - Real TSFC values are higher because of inlet recovery losses (about 0.81 at Mach 3; Q3), burner and nozzle losses, and cooling bleed.
- **Engine types, ranked by Mach 3 suitability (inference from the physics above plus the Q2 data):**
  1. *Bleed-bypass turbojet / turbo-ramjet (J58):* proven at Mach 3.2 with continuous afterburner. Heavy, with high TSFC at subsonic speeds.
  2. *Low-OPR afterburning turbojet (R-15B-300):* reaches Mach 2.83 (Mach 3.2 only with damage; see Q5). It is poor at subsonic speeds and has a short life (150 h; Q2).
  3. *Low-bypass mixed-flow turbofan (D-30F6, F119, F135, F414, AL-41F1):* excellent at Mach 0.8–2 and for supercruise near Mach 1.5–1.8. Only the D-30F6 (MiG-31) is operated near Mach 2.83, and it is time- and Tt2-limited.
  4. *Variable-cycle / adaptive three-stream (YF120, XA100/XA101, XA102/XA103):* shifts toward turbojet-like behaviour at high speed and bypass at cruise, and adds a third stream for thermal management. Public data show Mach 2-class designs; none is publicly stated as Mach 3-capable.
  5. *TBCC:* a turbine for Mach 0–2.5/3 plus a ramjet or dual-mode ramjet above that. It needs a mode-transition inlet and is heavy, but it is the only class that extends cleanly beyond Mach 3.

### Gaps
- None of the following could be opened: the J58 thrust-split source data, the original SR-71 flight-manual thrust charts, or the NASA YF-12 propulsion reports (NTRS blocked). Check NTRS for the YF-12 Propulsion Research Program, e.g. NASA TM/CP reports from Dryden and Lewis in the 1970s.
- **J58 bleed-bypass details [U], to verify against the declassified SR-71 Flight Manual and NASA YF-12 reports:** air is bled after the 4th compressor stage through six external bypass tubes into the afterburner. Bypass begins around Mach 2. At Mach 3.2 the compressor inlet temperature is about 800 °F (≈427 °C), and the afterburner is used continuously at cruise.
- I found no verified public thrust-lapse or TSFC-vs-Mach curves for any specific real engine. The Mattingly lapse models in Q6 are the standard substitute.
- No public specific-thrust or TSFC data for the TBCC demonstrators (e.g. the DARPA/AFRL Mode Transition work, the Lockheed "SR-72" concept, or Hermeus Chimera) was retrieved. **[U]** Program names are from background knowledge, and status as of 2026 is unverified.

## Q2. Engine data table (J58, R-15B-300, D-30F6, AL-41F1, AL-51F1, F119, F135, F414, YF120, XA100/101/102/103)

### Takeaway
Only the Russian engines' headline numbers could be checked this session, and only through search snippets. Treat the Russian numbers as **claims**, with conflicting weights and turbine-inlet temperatures. The US engine specifications are given as unverified reference values in Gaps, with the public source to check. The engines that have actually reached Mach 2.8+ (J58, R-15B-300, D-30F6) all trade low OPR and high weight for high-Tt2 tolerance. The modern fifth-generation engines (F119, F135, AL-41F1) trade the other way.

### Cited Findings
**Verified-by-snippet engine data.** All entries are [S], via search summaries of the listed pages. Russian values are unverified claims.

| Engine (aircraft) | Dry thrust | AB thrust | Dry weight | T/W | BPR | OPR | TIT | Other | Source |
|---|---|---|---|---|---|---|---|---|---|
| R-15B-300 (MiG-25) | ≈73.5 kN | ≈100.1 kN | 2,454 kg | 3.05 dry / 4.16 AB | 0 (turbojet) | 4.75 | 942 °C (single source; unconfirmed) | 5-stage compressor, 1-stage turbine; life 150 h | [Wikipedia R-15](https://en.wikipedia.org/wiki/Tumansky_R-15); [ArmedConflicts R-15B-300](https://www.armedconflicts.com/Mikulin-R-15B-300-t176038) |
| R-15BD-300 (later MiG-25) | ≈86 kN | ≈110 kN | (a 1,205 kg figure circulates but appears mis-attributed) | — | 0 | — | — | life ≈1,000 h | [ArmedConflicts R-15BD-300](https://origin.armedconflicts.com/topic/view/176039); [Wikipedia R-15](https://en.wikipedia.org/wiki/Tumansky_R-15) |
| D-30F6 (MiG-31) | 9,500 kgf = 93 kN | 15,500 kgf = 152 kN (Milavia: 151.9 kN) | 2,416 kg | ≈6.4 AB (calc.) | 0.57 (forum: 0.55) | 21.15 (LPC alone ≈3) | not found (1,640 K is unconfirmed) | length 7,040 mm; two-shaft AB turbofan | [Wikipedia D-30](https://en.wikipedia.org/wiki/Soloviev_D-30); [ArmedConflicts D-30F-6](https://www.armedconflicts.com/topic/view/56278); [Milavia MiG-31 specs](https://milavia.net/aircraft/mig-31/mig-31_specs.htm) |
| AL-41F1 / izd. 117 (Su-57 current) | ≈9,000 kgf ≈ 88 kN (unofficial table) | 147 kN (33,067 lbf) | 1,420 kg claimed; Air International Oct 2019 suggested ≈1,600 kg | 10.5 claimed | n/f | n/f | n/f | "most parameters classified" | [GlobalSecurity izdeliye 117](https://www.globalsecurity.org/military/world/russia/izdeliye-117.htm); [SecretProjects comparison table](https://www.secretprojects.co.uk/goto/post?id=473854); [SecretProjects post on weight](https://www.secretprojects.co.uk/goto/post?id=384590) |
| AL-51F1 / izd. 30 (Su-57 future) | ≈107.9 kN (24,300 lbf), estimate | ≈161.9 kN (36,400 lbf), estimate | n/f | n/f | n/f | n/f | n/f | first flight on Su-57: 5 Dec 2017 | [Wikipedia Saturn AL-51](https://en.wikipedia.org/wiki/Saturn_AL-51) |

**Additional findings:**
- **AL-51F1 production status conflicts.**
  - A recent summary says the engine was still **not in series production** about nine years after its 2017 first flight.
  - The same summary says a "Su-57M1" was unveiled at Dubai in Nov 2025 and first flew on 22 Dec 2025, apparently grafting AL-51F1 technology onto AL-41F1 hardware. This could not be opened or verified.
  - 2024 Rostec-linked reports promised deliveries of AL-51F1-equipped Su-57s, which did not materialise on that schedule.
  - Grokipedia claims series production was "ramping in 2025". This comes from a non-primary AI encyclopedia and should be disregarded unless confirmed.
  - Sources: [S] [Wikipedia Saturn AL-51](https://en.wikipedia.org/wiki/Saturn_AL-51); [S] [Defence Security Asia](https://defencesecurityasia.com/en/russia-su57-engine-izdelie-30/); [S] [Bulgarian Military, Feb 2024](https://bulgarianmilitary.com/2024/02/01/su-57s-new-al-51f1-engine-2024-allows-it-to-cruise-at-mach-2/); [S] [Grokipedia AL-51](https://grokipedia.com/page/Saturn_AL-51)
- The R-15 designer attribution conflicts between sources (Tumansky OKB-300 vs A.A. Mikulin). — [S] [ArmedConflicts](https://www.armedconflicts.com/Mikulin-R-15B-300-t176038) vs [Wikipedia](https://en.wikipedia.org/wiki/Tumansky_R-15)

### Inferences
- **Calculated T/W:** D-30F6 152 kN / (2,416 kg × 9.81) ≈ 6.4. R-15B-300 ≈ 4.2 (matches the source). AL-41F1 at the claimed 1,420 kg gives ≈ 10.5, but at 1,600 kg ≈ 9.4 [Calc].
- **Design pattern:** engines that sustain Mach 2.8+ have OPR ≤ ~21 (the D-30F6 with bypass) or ≤ 5 (the R-15) and T/W of 4–6.5. Fifth-generation engines reach T/W ≈ 10 with OPR ≈ 25–35 ([U], see Gaps) but are optimised for Mach 0.8–2 and supercruise. A Mach 3 stealth fighter therefore sits outside every production engine's design space.
- The D-30F6 is the most relevant "speed reference" engine: a turbofan with BPR ≈ 0.57 that powers an aircraft operated up to Mach 2.83. That shows a low-BPR turbofan can reach about Mach 2.8 if Tt2 tolerance and inlet scheduling are designed for it.

### Gaps
**Unverified US-engine reference values [U].** Hosts were blocked, so none of these could be checked. Verify each against the named public source before use.

| Engine | Dry thrust | AB thrust | Weight | BPR | OPR | Other | Verify against |
|---|---|---|---|---|---|---|---|
| P&W J58 (JT11D-20) | ≈25,000 lbf (≈111 kN) | 32,500–34,000 lbf (145–151 kN), sources differ | ≈6,000 lb (2,700 kg) | 0 (bleed-bypass turbojet) | ≈8.8 | 9-stage compressor, 2-stage turbine; TIT ≈2,000 °F (≈1,093 °C); Mach 3.2+ | P&W heritage page; SR-71 Flight Manual (declassified); NASA YF-12 reports |
| P&W F119-PW-100 (F-22) | ≈26,000 lbf (≈116 kN) | "35,000-lb class" (≈156 kN) | ≈3,900 lb (≈1,770 kg) | ≈0.3 | ≈35 | 3-stage fan, 6-stage HPC, counter-rotating single-stage HPT/LPT; 2-D ±20° pitch-vectoring nozzle | USAF F-22 fact sheet (af.mil); P&W F119 page |
| P&W F135-PW-100 (F-35A/C) | ≈28,000 lbf (≈125 kN) | ≈43,000 lbf (≈191 kN) | ≈3,750 lb (≈1,700 kg) | ≈0.57 | ≈28 | Engine Core Upgrade (ECU) chosen over AETP in the FY2024 budget (Mar 2023) | P&W F135 page; USAF FY24 budget documents |
| GE F414-GE-400 (F/A-18E/F) | ≈13,000–14,000 lbf (≈58–62 kN) | 22,000 lbf class (≈98 kN) | ≈2,445 lb (≈1,110 kg) | ≈0.25 | ≈30 | T/W ≈9 | GE Aerospace F414 page |
| GE YF120 (YF-22/YF-23 prototypes) | n/f | ≈35,000 lbf class | n/f | variable (VABI) | n/f | Variable cycle: near-turbojet at high speed, more bypass at part power. Reported higher supercruise Mach than YF119 (≈M1.58 YF-22 vs ≈M1.43; YF-23 ≈M1.6–1.7; figures conflict) | AIAA papers on VCE; Air Force Museum notes |
| GE XA100 / P&W XA101 (AETP) | n/f | ≈45,000 lbf class | n/f | adaptive three-stream | n/f | GE claims vs F135 baseline: +10% thrust, +25% fuel efficiency, +30% range, about 2× thermal-management capacity. Ground tested 2021–2023. AETP not selected for the F-35. | GE Aerospace XA100 press releases |
| GE XA102 / P&W XA103 (NGAP) | n/f | n/f | n/f | adaptive | n/f | NGAP detailed design and prototype contracts reported in early 2025; status in Oct 2026 unknown | USAF / AFLCMC releases; GE and P&W press |

**Other gaps:**
- **TSFC (dry and wet) for every engine:** no verified value found. [U] Values sometimes quoted for the D-30F6 (≈0.72 dry and ≈1.9 wet, in kg/kgf·h) are unverified.
- **Length and diameter:** found only for the D-30F6 (7.04 m).
- **Turbine inlet temperatures:** unverified for all engines. The R-15B-300 figure of 942 °C is a single source and looks low. [U] Other sources reportedly give ≈1,227 °C, which needs checking.
- **Mach envelopes:** not given by any manufacturer source found. Use the aircraft limits in Q5.
- **Gunston, *World Encyclopaedia of Aero Engines*:** could not be consulted. It is the recommended cross-check for every row above.

## Q3. How do inlet and engine match at Mach 2–3, and what are the installed thrust and drag losses?

### Takeaway
At Mach 3 the inlet is the main thrust producer (about 54% on the SR-71, per the Q1 Cited Findings), so inlet and engine must be designed as one system. Total-pressure recovery falls to about 0.81 at Mach 3 even with a good mixed-compression inlet (MIL-E-5007D standard; [Calc]). The excess airflow the engine cannot swallow must be bled or bypassed, either into an ejector or ramburner (as on the J58) or overboard at a drag cost. Low-observable serpentine ducts and fixed (caret/DSI) inlets make this harder, because fixed geometry cannot match capture area to engine demand across Mach 0–3.

### Cited Findings
- The SR-71 inlet's share of propulsive thrust rose from about 13% at Mach 2.2 to about 54% at Mach 3+, which shows how the inlet's role changes with Mach. — [S] [Enginehistory.org SR-71 Propulsion System](https://enginehistory.org/Convention/2013/SR-71Propul/SR-71Propul.shtml)
- The pyCycle example military mixed-flow turbofan models the inlet with `inlet.ram_recovery = 0.9990` at its subsonic (Mach 0.8, 35,000 ft) design point, plus duct pressure losses of about 1% (dP/P = 0.0107) per duct. That is far from Mach 3 practice and must be replaced with a Mach-dependent recovery schedule for a Mach 3 study. — [F] [pyCycle mixedflow_turbofan.py](https://github.com/OpenMDAO/pyCycle/blob/master/example_cycles/mixedflow_turbofan.py)

### Inferences
- **Inlet recovery standard [Calc]:** η_r = 1 − 0.075(M0 − 1)^1.35 for 1 < M0 < 5 (MIL-E-5007D, as reproduced in Mattingly; verify). This gives 0.925 at M2.0, 0.870 at M2.5, 0.830 at M2.83, 0.809 at M3.0 and 0.783 at M3.2. Thrust scales roughly with recovery, so a 5-point recovery loss costs about 5% or more of net thrust at Mach 3 (rule-of-thumb inference).
- **Why bypass or bleed is mandatory:**
  - A Mach 3 inlet sized for cruise captures more corrected airflow than the engine can pass at low Mach. At high Mach the engine's corrected flow falls because Tt2 rises; corrected flow is W√θ/δ.
  - The surplus must go somewhere: spill (spillage/additive drag), bleed through boundary-layer and shock-trap bleed (bleed drag), or bypass overboard or to the nozzle (bypass drag).
  - The J58 approach recovers much of that air as thrust by routing it to the ejector, which explains the large ejector share (29%).
- **Installed thrust bookkeeping (Mattingly convention):** installed thrust T = F_uninstalled·(1 − φ_inlet − φ_nozzle). Here φ_inlet covers additive (spillage), bleed and bypass drag, and φ_nozzle covers boattail and base drag. Each φ must be estimated per Mach and throttle setting. Typical numerical values were not verified (see Gaps).
- **Stealth conflict:**
  - Radar low observability wants a serpentine duct hiding the fan face and a fixed, aligned-edge inlet.
  - Mach 3 wants variable geometry (translating spike or variable ramps), large bleed and bypass systems, and short ducts to limit losses.
  - Every movable ramp or door edge and bleed slot is an RCS feature, and every bend costs pressure recovery.
  - This trade should be an explicit early study item.

### Gaps
- Numerical installed-loss data could not be verified, i.e. φ_inlet and φ_nozzle vs Mach for Mach 2–3 inlets, spillage and bleed drag fractions, and SR-71 inlet recovery at Mach 3.2. Recommended sources:
  - Mattingly, Heiser & Pratt, *Aircraft Engine Design* 2nd ed. (AIAA 2002), chapters on inlets and installation.
  - Seddon & Goldsmith, *Intake Aerodynamics*.
  - NASA YF-12 inlet reports on NTRS (blocked here).
- **SR-71 inlet details [U]:** translating axisymmetric spike (≈26 in travel), forward and aft bypass doors, shock-trap and centerbody bleed, inlet-unstart behaviour. Verify against the SR-71 Flight Manual and NASA YF-12 reports.
- No public data was found on pressure-recovery penalties of serpentine low-observable ducts at supersonic speed. [U] Typical values are a few percent.
- No public data was found on fixed DSI or caret inlets above Mach 2. [U] The F-22's limit of about Mach 2.25 with fixed caret inlets is commonly attributed partly to the inlet. Unverified.

## Q4. What fuels apply (JP-7, T-6/RT, JP-8/Jet A/Jet A-1, JP-5), what are their thermal limits, and how much heat can fuel absorb at Mach 3?

### Takeaway
At Mach 3 the airframe recovery temperature (≈290 °C) and the ram-air total temperature (≈333 °C) exceed the useful limit of conventional fuel. Ram air therefore cannot cool anything, and **fuel is the aircraft's only heat sink** [Calc]. Standard JP-8 offers only ≈270 kJ/kg of sensible sink (at the 163 °C / 325 °F limit). Raising the limit to 550 °F, as the JP-8+100 program targeted, gives about 120% more sink [S]. A JP-900-class fuel (stable at 900 °F) gives ≈1,150 kJ/kg, and endothermic cracking adds a further 500–1,150 kJ/kg [S].

### Cited Findings
- The AFRL high-heat-sink fuel program aimed to raise JP-8 thermal stability from its operating limit of **325 °F (163 °C) to 550 °F (288 °C)**, a "120 percent higher heat sink", and eventually to perfect **JP-900** for the hypersonic regime. — [S] (search summary; attribution to this exact report probable but unconfirmed) [National Academies, Review of USAF and DoD Aerospace Propulsion Needs (NAP 11780), ch. on fuels](https://www.nationalacademies.org/read/11780/chapter/8)
- The Air Force's JP-900 target was fuel **stable at 900 °F (482 °C) for two hours**. The project focus shifted in late 2005 to a coal-based drop-in replacement for JP-8. That coal-derived fuel met most JP-8 specifications and ran in a T63 engine, but its high density imposes a fuel-mass penalty relative to JP-8. — [S] (attribution among DTIC results unconfirmed) [DTIC ADA476475](https://apps.dtic.mil/sti/pdfs/ADA476475.pdf)
- Storable liquid hydrocarbons (JP-7, JP-8+100, JP-10) that undergo endothermic reactions may provide enough heat sink for hypersonic flight without cryogenic fuels. At Mach 5–10, heat loads exceed what sensible heating can absorb, and thermal cracking supplies the extra sink. — [S] [DTIC ADA406019](https://apps.dtic.mil/sti/pdfs/ADA406019.pdf)
- Typical **endothermic** heat-sink values for C8–C15 hydrocarbon fuels are **≈500–1,150 kJ/kg**, and JP-7, JP-8 and JP-900 are common test fuels. — [S] [PMC review article PMC8515821](https://pmc.ncbi.nlm.nih.gov/articles/PMC8515821/)
- A 1997 NASA / Wright Laboratory study examined heat transfer and thermal stability of **supercritical JP-7** as a coolant for Mach 8 vehicles. — [S] [NASA NTRS 19970026308](https://ntrs.nasa.gov/citations/19970026308)

### Inferences
**1. Sensible heat sink [Calc].** Q = c̄p·ΔT, with c̄p ≈ 2.2–2.6 kJ/kg·K (rising with temperature) and fuel loaded at about 40 °C.

| Fuel / limit | ΔT (K) | Sensible sink (kJ/kg) |
|---|---|---|
| JP-8 / Jet A at 163 °C (325 °F) | 123 | ≈270 |
| JP-8+100 at 288 °C (550 °F) | 248 | ≈595 (≈2.2× JP-8, consistent with the "+120%" claim above) |
| JP-7-class at ≈345 °C (assumed limit, [U]) | 305 | ≈760 |
| JP-900 goal at 482 °C (900 °F) | 442 | ≈1,150 |
| JP-900 + endothermic cracking | — | ≈1,650–2,300 |

**2. Cooling power available = fuel flow × sink [Calc].** At a Mach 3 cruise fuel flow of ≈2.9 kg/s (Q5 example: 25 t aircraft, L/D 4.5, TSFC 1.9/h):

| Fuel | Cooling power |
|---|---|
| JP-8 | ≈0.8 MW |
| JP-8+100 | ≈1.7 MW |
| JP-7-class | ≈2.2 MW |
| JP-900 | ≈3.4 MW |
| JP-900 + endothermic | up to ≈6.7 MW |

- At low throttle (descent, loiter), fuel flow and therefore cooling capacity collapse. That is the classic thermal-management trap.

**3. Airframe and fuel-tank heating [Calc].** Adiabatic wall temperature, T_aw = T0·(1 + r·0.2·M²) with r = 0.89:

| Mach | T_aw (K) | T_aw (°C) |
|---|---|---|
| 2.0 | 371 | 98 |
| 2.5 | 458 | 185 |
| 2.83 | 526 | 252 |
| 3.0 | 564 | 291 |
| 3.2 | 612 | 338 |

- At Mach 3, wing-skin tanks are therefore heated toward ≈290 °C. JP-8's whole thermal-stability margin (163 °C) is exceeded by the skin alone, before any avionics, hydraulic, oil or ECS heat is added. A Mach 3 design needs either a high-stability fuel (JP-7 or T-6 class) or insulated tanks with fuel recirculation.
- **IR-stealth consequence [Calc]:** by Wien's law (λ_peak = 2,898/T µm), skin at 564–612 K peaks at **4.7–5.1 µm**, inside the 3–5 µm mid-wave IR band used by IRST and missile seekers. An afterburner or ramburner plume near 2,000 K peaks at ≈1.45 µm. IR low observability during sustained Mach 3 flight is therefore fundamentally limited by aero-heating, not only by the exhaust. Flag this for the signature lead.
- **Coking:** above roughly 150–200 °C oxidative deposits (gums, varnish) form from dissolved oxygen. Above roughly 400–500 °C pyrolytic coking starts (general fuel-chemistry inference consistent with the JP-8 → JP-8+100 → JP-900 temperature steps above). Fuel deoxygenation and additive packages such as "+100" are the standard mitigations. Specific deposition-rate data was not retrieved.

### Gaps
**Fuel property values [U]**, to verify against the named specifications:
- **JP-7 (MIL-DTL-38219):** low-volatility, high-thermal-stability fuel; flash point ≥ 60 °C. It needs triethylborane (TEB) chemical ignition on the SR-71 because of its low volatility, and was also used as hydraulic fluid for J58 nozzle actuators. Exact thermal-stability rating unverified (≈650 °F quoted informally).
- **JP-8 (MIL-DTL-83133):** Jet A-1 plus military additives (FSII, corrosion inhibitor/lubricity improver, static dissipator); flash point ≥ 38 °C; freeze point ≤ −47 °C.
- **JP-5 (MIL-DTL-5624):** flash point ≥ 60 °C for shipboard safety; freeze point ≤ −46 °C.
- **Jet A / Jet A-1 (ASTM D1655):** freeze point −40 °C / −47 °C; JFTOT thermal-stability test at 260 °C.
- **Russian fuels:** T-6 and T-8V are high-thermal-stability, hydro-treated, heavier fuels (GOST 12308), and T-6 is associated with the MiG-25/MiG-31. RT is the standard Russian jet fuel (GOST 10227). Densities, flash points and stability temperatures unverified. Russian GOST texts were not accessed.
- **SR-71 fuel temperatures [U]:** fuel tank temperatures at Mach 3 cruise (≈300+ °F?) and fuel temperature to the burner (≈600 °F?) were not verified. Source to check: SR-71 Flight Manual, Section on the fuel system.
- **MiG-25 fuel heat-soak management:** no data found.
- **Specific heat vs temperature curves** for JP-7/JP-8 (NIST or CRC data) were not retrieved. The c̄p used above is an assumed average.
- **Fuel deoxygenation systems** and fuel-cooled cooled-cooling-air (CCA) heat exchangers: no source retrieved.

## Q5. How fuel-efficient is high-Mach flight (SR-71, MiG-25/31, Breguet at Mach 3, F-22 supercruise)?

### Takeaway
Mach 3 cruise is not thermodynamically inefficient. Overall engine efficiency η0 = V/(TSFC·h_PR) reaches about 0.38–0.49 at Mach 3 versus about 0.24 for a fighter engine at Mach 0.85 [Calc]. The range penalty comes from low L/D (≈4–6) and from the large fuel fraction spent climbing and accelerating through the transonic drag rise. The aircraft-specific cruise fuel-flow and endurance figures requested (SR-71, MiG-25, MiG-31, F-22) **could not be verified this session**.

### Cited Findings
- A related Soviet engine, the Tumansky R-25 (MiG-21bis), had an emergency rating time limit of **1 minute in training and 2 minutes in wartime**. This illustrates the Soviet practice of time-limited high-power ratings. It does not apply to the R-15B-300. — [S] [Wikipedia, Tumansky R-25](https://en.wikipedia.org/wiki/Tumansky_R-25)
- MiG-25 top speed is quoted as about Mach 3.1–3.2 at very high altitude in some secondary sources. The search found no source for the Mach 2.83 operational limit or for a time limit at that speed. — [S] [Alchetron, Tumansky R-15](https://alchetron.com/Tumansky-R-15); [S] [Wikipedia R-15](https://en.wikipedia.org/wiki/Tumansky_R-15)
- R-15B-300 engine life was only **150 h** (later R-15BD-300 ≈ 1,000 h), which shows the cost of operating a turbojet near its Tt2 limit. — [S] [ArmedConflicts R-15B-300](https://www.armedconflicts.com/Mikulin-R-15B-300-t176038); [S] [ArmedConflicts R-15BD-300](https://origin.armedconflicts.com/topic/view/176039)

### Inferences
**1. Breguet range equation:** R = (V/c)·(L/D)·ln(W_i/W_f), with V in km/h, c = TSFC in 1/h (fuel weight flow per unit thrust) and R in km. The "range factor" V·(L/D)/c is the figure of merit. All inputs below are **assumptions** chosen to illustrate trends, not measured aircraft data [Calc].

| Case (assumed inputs) | V (m/s) | Range factor (km) | Cruise range (km / nmi) |
|---|---|---|---|
| SR-71-like: M3.2, c = 1.9/h, L/D = 6, Wi/Wf = 1.6 | 944 | 10,733 | 5,045 / 2,724 |
| Same with c = 1.6/h | 944 | 12,746 | 5,991 / 3,235 |
| M3 fighter, AB-cruise turbojet c = 1.9, L/D = 4.5, Wi/Wf = 1.35 | 885 | 7,547 | 2,265 / 1,223 |
| M3 fighter, VCE/turbo-ramjet c = 1.5, L/D = 4.5, Wi/Wf = 1.35 | 885 | 9,559 | 2,869 / 1,549 |
| Supercruise M1.6, dry c = 1.1, L/D = 5.5, Wi/Wf = 1.35 | 472 | 8,497 | 2,550 / 1,377 |
| Subsonic M0.85, c = 0.85, L/D = 10, Wi/Wf = 1.35 | 251 | 10,622 | 3,188 / 1,721 |

- The SR-71-like case shows that a high-L/D (≈6) Mach 3.2 design achieves a range factor equal to a subsonic L/D = 10 aircraft. Speed compensates for TSFC.
- The fighter-like M3 case (L/D ≈ 4.5) loses about 30% of range factor. Real ranges are lower still because the climb and acceleration fuel is excluded here.

**2. Overall efficiency [Calc].** η0 = V0/(S·h_PR), with S in kg/(N·s):

| Condition | S (mg/N·s) | η0 |
|---|---|---|
| M3.2, c = 1.9/h | 53.8 | 0.41 |
| M3.0, c = 1.5/h | 42.5 | 0.49 |
| M1.6, c = 1.1/h | 31.2 | 0.35 |
| M0.85, c = 0.85/h | 24.1 | 0.24 |

**3. Fuel flow at Mach 3 [Calc].** ṁ_f = c·D = c·W/(L/D).
- A 25 t aircraft at L/D = 4.5 needs D ≈ 54.5 kN, i.e. ≈27 kN installed thrust per engine for a twin.
- That is **≈10,600 kg/h (≈176 kg/min)** at c = 1.9/h and ≈8,300 kg/h at c = 1.5/h.
- With, say, 6,000 kg of fuel reserved for the Mach 3 segment, that gives about **34–43 minutes** at Mach 3. This is a sizing heuristic for constraint and mission analysis.
- At 30 t: ≈12,700 kg/h.

**4. Supercruise:** the attraction is dry-power TSFC (≈1.0–1.2/h assumed) at M1.5–1.8 with no afterburner plume, which also suits IR stealth. A Mach 3 requirement probably forces afterburner or ramburner operation at top speed, and therefore a large IR plume. This is a key requirement-trade to surface early.

### Gaps
None of the following could be verified (hosts blocked, search budget exhausted).

**Aircraft-specific values [U]**, to check against the sources named:
- **SR-71:** internal fuel ≈80,000 lb (≈36,300 kg, ≈12,200 US gal JP-7); unrefueled range ≈2,900–3,200 nmi; cruise fuel flow and installed TSFC at Mach 3.2. Check the declassified SR-71 Flight Manual (performance section) and the NASA SR-71/YF-12 reports.
- **MiG-25:** operational limit Mach 2.83 (≈3,000 km/h). The 1970s Mach 3.2 dashes reportedly caused engine overspeed and over-temperature damage. Any minute-limit at max speed is unverified. Check Russian-language MiG-25 flight-manual excerpts and Gordon, *MiG-25 Foxbat / MiG-31 Foxhound* (Aerofax).
- **MiG-31:** max speed Mach 2.83 (3,000 km/h) at altitude; supersonic cruise ≈M2.35; internal fuel ≈16,000+ kg; combat radius ≈720 km at M2.35. Check UAC/RAC MiG official pages, Milavia and Gordon.
- **F-22:** supercruise ≈M1.5–1.8; internal fuel ≈18,000 lb; USAF fact sheet ferry range ">1,850 miles with 2 external tanks". Check the USAF F-22 fact sheet. No public F119 supercruise TSFC exists.
- **Measured TSFC:** none verified for any engine at Mach 2–3. The c values in the Breguet table are assumptions bracketing the ideal-cycle results in Q1 with realistic losses.

## Q6. Which cycle analysis methods and tools suit a two-person team, and which thrust-lapse models apply?

### Takeaway
Use **Mattingly's parametric (on-design) then performance (off-design) method** for hand checks, early trade studies and thrust-lapse estimates. Use **NASA pyCycle (OpenMDAO, open source)** as the main modelling tool. pyCycle was designed to mirror NASA NPSS, ships with an afterburning turbojet and a military mixed-flow afterburning turbofan as examples, and supports gradient-based optimisation [F]. NPSS (licensed, US-controlled) and GasTurb (commercial) are optional upgrades. T-MATS (Apache 2.0, MATLAB/Simulink) covers transient and controls work [F].

### Cited Findings
- **pyCycle basics:** a thermodynamic cycle modelling library built on OpenMDAO, "designed primarily to model jet engine performance" and "heavily inspired by NASA's NPSS software".
  - Recent releases require OpenMDAO ≥ 3.7.0 (pyCycle 4.0.0) or ≥ 3.10.0 (4.1.x and 4.2.0). The latest release, 4.2, is a PyPI packaging update with "no significant code changes".
  - The documentation is self-described as "nearly non-existent".
  - The repo has 402 commits, 199 stars and 100 forks.
  - Source: [F] [GitHub OpenMDAO/pyCycle](https://github.com/OpenMDAO/pyCycle)
- **pyCycle thermodynamics:**
  - Two packages: **CEA** (chemical-equilibrium solver, the original) and **TABULAR** (faster, precomputed).
  - The default tabular data covers only Jet-A without water injection, so a JP-7 or T-6 study needs CEA or regenerated tables.
  - Cite it as: E. S. Hendricks and J. S. Gray, "pyCycle: a tool for efficient optimization of gas turbine engine cycles," *Aerospace*, 2019.
  - Source: [F] [GitHub OpenMDAO/pyCycle README](https://github.com/OpenMDAO/pyCycle)
- **pyCycle example models:**
  - Included: `afterburning_turbojet.py`, `mixedflow_turbofan.py`, `high_bypass_turbofan.py`, `simple_turbojet.py`, `wet_simple_turbojet.py`, `multi_spool_turboshaft.py`, `single_spool_turboshaft.py`, `electric_propulsor.py`, `wet_propulsor.py` and `tab_thermo_data_generator.py`.
  - There is also an `N+3ref` folder (NASA N+3 reference engine).
  - Source: [F] [pyCycle example_cycles](https://github.com/OpenMDAO/pyCycle/tree/master/example_cycles)
- **pyCycle `mixedflow_turbofan.py` (template for a fighter engine).** Source: [F] [mixedflow_turbofan.py](https://github.com/OpenMDAO/pyCycle/blob/master/example_cycles/mixedflow_turbofan.py)
  - Design point: 35,000 ft / M0.8, Fn = 5,500 lbf; BPR = 1.05 (balanced by mixer extraction ratio).
  - Components: fan PR 3.3 (η 0.8948), LPC PR 1.935 (η 0.9243), HPC PR 4.9 (η 0.8707), so OPR ≈ 31.3. HPT η 0.8888, LPT η 0.8996.
  - Temperatures: burner exit T4 = 3,200 °R (1,778 K) at design and 3,100 °R off-design; afterburner target 3,400 °R (1,889 K).
  - Exhaust: convergent-divergent mixed nozzle, Cfg = 0.9933.
  - Cooling bleeds 5.07% and 6.72% of flow; 250 hp shaft offtake.
  - Element chain: inlet → fan → splitter → (core: LPC → HPC → bleed → burner → HPT → LPT | bypass duct) → mixer → afterburner → CD nozzle.
- **pyCycle `afterburning_turbojet.py`.** Source: [F] [afterburning_turbojet.py](https://github.com/OpenMDAO/pyCycle/blob/master/example_cycles/afterburning_turbojet.py)
  - Design point: SLS, Fn = 11,800 lbf, compressor PR 13.5 (η 0.83), turbine η 0.86, T4 = 2,370 °R (1,317 K); CD nozzle with Cv = 0.99; afterburner dP/P = 0.06.
  - Off-design points run to **M1.6 at 35,000 and 50,000 ft and M1.8 at 70,000 ft**. It is a ready-made start for building an M2–3 lapse deck by adding points.
- **NASA T-MATS:** a Simulink toolbox for steady-state and transient thermodynamic and turbomachinery simulation with controls. It is "released under the Apache V2.0 license agreement" and requires MATLAB/Simulink. — [F] [GitHub nasa/T-MATS](https://github.com/nasa/T-MATS)
- MIT OCW 16.50 (Introduction to Propulsion Systems, 2012) lecture notes on turbofan cycle design are a free public alternative text based on Kerrebrock. — [S] [MIT OCW 16.50 Lecture 21](https://mitocw.ups.edu.ec/courses/aeronautics-and-astronautics/16-50-introduction-to-propulsion-systems-spring-2012/lecture-notes/MIT16_50S12_lec21.pdf)

### Inferences
**Recommended workflow for two people:**
1. **Constraint analysis** (thrust-to-weight vs wing loading), using Mattingly thrust-lapse α(θ0, δ0, TR) as a first approximation (formulas in Gaps; verify first).
2. **Parametric cycle analysis** by hand or in a spreadsheet: ideal and then real turbojet or mixed-flow turbofan relations, per Mattingly *Elements of Propulsion*. The [Calc] tables in Q1 were produced this way.
3. **pyCycle model of the chosen cycle.**
   - Start from `mixedflow_turbofan.py`.
   - Lower the OPR, raise the T4 and afterburner temperatures, add off-design points at M2.0–3.2 between 50,000 and 80,000 ft, and replace `ram_recovery` with the MIL-E-5007D schedule.
   - Add a bypass-bleed path from a mid-compressor stage to the afterburner to approximate a J58-style cycle. This needs a bleed port plus a mixer element; feasibility in pyCycle is inferred, not verified.
4. **Mission and Breguet analysis** using the pyCycle deck.
5. **Optimisation** using OpenMDAO drivers.

**Key parametric relations** (standard Mattingly *Elements of Propulsion* notation):
- τ_r = 1 + (γ−1)/2·M0² and π_r = τ_r^(γ/(γ−1))
- τ_λ = Tt4/T0 and τ_c = π_c^((γ−1)/γ)
- τ_t = 1 − (τ_r/τ_λ)(τ_c − 1)
- **Dry turbojet:** V9/a0 = √{[2/(γ−1)]·[τ_λ/(τ_rτ_c)]·(τ_rτ_cτ_t − 1)}, and F/ṁ0 = a0(V9/a0 − M0)
- **Afterburning turbojet:** V9/a0 = √{[2/(γ−1)]·τ_λAB·[1 − 1/(τ_rτ_cτ_t)]}
- **Fuel-air ratio:** f = c_pT0(τ_λ − τ_rτ_c)/h_PR dry, or f = c_pT0(τ_λAB − τ_r)/h_PR with afterburner
- **TSFC:** S = f/(F/ṁ0)
- **Overall efficiency:** η0 = V0/(S·h_PR)
- **Optimum compressor pressure ratio** for maximum dry specific thrust (ideal turbojet): τ_c,opt = √τ_λ/τ_r. At M3 with Tt4 = 1,800 K: τ_λ = 8.31, τ_r = 2.8, so τ_c,opt = 1.03 and π_c,opt ≈ 1.1 [Calc]. **The ideal turbojet wants almost no compressor at Mach 3**, which is the analytical reason the ramjet takes over.

**Tool choice:**

| Tool | Cost / access | Use |
|---|---|---|
| Spreadsheet / Python of Mattingly equations | free | concept trades |
| pyCycle + OpenMDAO | free, open source | main design and off-design deck plus optimisation |
| NASA CEA | free; also embedded in pyCycle | combustion thermo for non-Jet-A fuels |
| T-MATS | free (Apache 2.0) but needs MATLAB | transients and controls |
| GasTurb | commercial ([U]) | fast, validated GUI; cross-check |
| NPSS | licensed; US-person/export-control issues likely ([U]) | industry-standard but probably out of reach |

### Gaps
**Mattingly thrust-lapse equations [U]**, recalled from *Aircraft Engine Design* 2nd ed. (AIAA 2002), eq. 2.54. **Verify exact coefficients in the book before use:**
- Definitions:
  - θ0 = (T/T_std)(1 + 0.2M0²) and δ0 = (P/P_std)(1 + 0.2M0²)^3.5
  - TR = throttle ratio = Tt4,max / Tt4,SLS, numerically equal to the θ0 at which the engine reaches its Tt4 limit
- **Low-bypass mixed-flow turbofan, max (afterburner):**
  - α = δ0 for θ0 ≤ TR
  - α = δ0·[1 − 3.5(θ0 − TR)/θ0] for θ0 > TR
- **Low-bypass mixed-flow turbofan, military (dry):**
  - α = 0.6δ0 for θ0 ≤ TR
  - α = 0.6δ0·[1 − 3.8(θ0 − TR)/θ0] for θ0 > TR
- **Turbojet, max:** α = δ0·[1 − 0.3(θ0 − 1) − 0.1√M0] for θ0 ≤ TR, with an additional −1.5(θ0 − TR)/θ0 term above TR.
- **Implication (contingent on these coefficients):** the max-power low-bypass model reaches α = 0 at θ0 = 1.4·TR. For a typical TR ≈ 1.0–1.1 that is θ0 ≈ 1.4–1.54, i.e. about M2.1–2.3 in the stratosphere (θ0 table in Q1). A Mach 3 engine (θ0 = 2.1) therefore needs TR near 1.5–2.1, meaning it runs well below its Tt4 limit at take-off. That implies a heavier engine for its take-off thrust, which is the classic "high throttle ratio" trade. These models were fitted to conventional engines and are **not validated for Mach 3**, so use pyCycle off-design for the real lapse.

**Mattingly TSFC models [U]**, same book, eq. ≈3.55c–d. Here θ = T/T_std (static), units per hour, and the forms are to be verified:
- Low-bypass mixed-flow: c = (0.9 + 0.30M0)√θ (military) and (1.6 + 0.27M0)√θ (max)
- Turbojet: c = (1.1 + 0.30M0)√θ (military) and (1.5 + 0.23M0)√θ (max)

**Other unverified items:**
- **Mattingly software [U]:**
  - AEDsys (with *Aircraft Engine Design*, 2nd ed.) includes ONX (on-design parametric) and OFFX (off-design performance) plus constraint, mission, atmosphere and component-design modules.
  - The *Elements of Propulsion* software (1st ed. 2006; 2nd ed. 2016 with K. Boyer) includes PARA/PERF-type parametric and performance programs.
  - Not verified (publisher pages not accessed).
- **NPSS licensing [U]:** managed via the NPSS Consortium / Southwest Research Institute, with commercial and academic licences, and likely export-controlled (EAR/ITAR). Not verified.
- **GasTurb [U]:** commercial, from GasTurb GmbH (J. Kurzke); covers turbojet, turbofan, mixed-flow and afterburning cycles; licence prices not verified.
- **Other tools [U]:** GSP (NLR), PROOSIS (commercial) and TURBOMATCH (Cranfield) exist. Not verified.
- **pyCycle licence:** the repository LICENSE file is linked but its type was not displayed. [U] Apache 2.0 is believed; check `LICENSE.txt`.

## Q7. Practical reality: which existing engine classes could notionally power the study, and what export and availability limits apply?

### Takeaway
A two-person team cannot develop or obtain a Mach 3 fighter engine. For a paper study, the defensible approach is a **"rubber" (scalable) parametric engine** built in pyCycle and anchored to public data. Two anchors are most relevant: a **D-30F6-class low-BPR turbofan** (a speed-reference engine operated to Mach 2.83) and a **J58-style bleed-bypass turbo-ramjet** (Mach 3.2 heritage), with **F119/F135-class technology levels** (OPR, T4, T/W ≈ 10) as the US technology reference. Real US hot-section and design data are export-controlled, and Russian engines are commercially and legally unavailable to Western users. All engine-availability statements below are thought experiments only.

### Cited Findings
- Fifth-generation Russian engine data is largely classified. For the AL-41F1, "most parameters still classified". — [S] [GlobalSecurity izdeliye 117](https://www.globalsecurity.org/military/world/russia/izdeliye-117.htm)
- The AL-51F1 has flown since 2017 but its series-production status is disputed (see Q2), so it is not a usable "available" reference. — [S] [Wikipedia Saturn AL-51](https://en.wikipedia.org/wiki/Saturn_AL-51)
- Open-source modelling tools with no purchase cost exist and are adequate for study-level cycle decks: pyCycle (OpenMDAO) and T-MATS (Apache 2.0). — [F] [pyCycle](https://github.com/OpenMDAO/pyCycle); [F] [T-MATS](https://github.com/nasa/T-MATS)

### Inferences
**Notional propulsion options for the design study (thought experiment).** Specs for the US anchors are unverified ([U], Q2 Gaps).

| Option | Anchor data | Mach 3 viability | Stealth fit | Notes |
|---|---|---|---|---|
| A. Scaled low-BPR mixed turbofan with high TR (≈1.5–2) | D-30F6 (BPR 0.57, OPR 21) for speed; F135 (BPR ≈0.57, OPR ≈28) for technology | marginal; time- and Tt2-limited near M2.8 | good subsonic/supercruise IR; afterburner needed at top speed | lowest risk to model; probably caps near M2.8 |
| B. J58-style bleed-bypass turbo-ramjet | J58 (54/17/29 thrust split) | proven M3.2 | poor: continuous afterburner/ejector at cruise; large IR plume | heavy; poor subsonic TSFC |
| C. Adaptive three-stream VCE with third-stream heat sink | XA100/XA101 public claims | not public; Mach 2-class designs | best: third stream cools exhaust and airframe heat loads | data mostly unavailable; model generically |
| D. TBCC (turbofan + ramjet in over/under or wraparound arrangement) | no public engine data retrieved | yes (M3+) | duct complexity hurts RCS | heaviest; mode transition at M2–2.5 |

**Recommendation for modelling:** build both A and B in pyCycle. The difference between them (thrust lapse, TSFC, weight) then quantifies the Mach 3 penalty for the requirement-setting phase.

**Export and availability:**
- US gas-turbine engine technical data, especially hot-section technology, is controlled under ITAR (USML Category XIX, gas turbine engines) and the EAR (Commerce Control List category 9). This is why the team should rely only on published, public-release data.
- Russian UEC/Saturn/Aviadvigatel products are unavailable to Western users because of sanctions on Russia's defence sector.
- The specific category numbers and sanctions designations are [U]; see Gaps.

### Gaps
- **Export-control specifics [U]:** USML Category XIX covers military gas turbine engines and associated technical data, and ECCN 9E003 covers hot-section technology. The specific USML paragraph numbers were not verified because ecfr.gov was not accessed. A legal or compliance review is advised if the team ever moves beyond public data.
- **Russia sanctions [U]:** the US/EU/UK designation status of UEC (United Engine Corporation, part of Rostec) and its subsidiaries as of Oct 2026 was not verified.
- **Commercial or available Mach 2+ engines:** none were identified that a civilian team could legally obtain. [U] Surplus J85, F100 or F110-class engines are used by some companies (e.g. Hermeus uses a GE J85-based approach and later an F100 for its Quarterhorse program), but status and details were not verified.
- **NGAP engine status (XA102/XA103) for the F-47/NGAD as of Oct 2026:** not verified (search budget exhausted).
