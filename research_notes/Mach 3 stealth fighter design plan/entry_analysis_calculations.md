# Entry analysis: first-pass quantitative sizing of a single-seat, low-observable, Mach 3 fighter

> **Research-conditions note for the report writer.** This session could verify only a few items online. WebFetch failed for every host tried (nbviewer.org, apps.dtic.mil, kcl.digimat.in; DNS "ENOTFOUND", meaning the hosts are outside the session's allowed network), and the shared web-search budget (200 per turn) ran out after 5 searches. Reference-aircraft data and several physical facts are therefore re-cited from **sibling research notes in this folder**, which recorded their source URLs (`russian_korean_programs.md`, `us_programs_lockheed_martin.md`, `propulsion_fuel.md`, `materials_structures_thermal.md`, `aerodynamics_configuration.md`, `signature_reduction.md`).
>
> Textbook coefficients that could not be re-checked online are labelled **[T]** (published method, recalled, not re-verified this session; check against the book). Values computed in this study are labelled **[Calc]**. Full copies of Raymer and Mattingly also turned up in search results on non-publisher hosts. They were **deliberately not used**, because they appear to be unauthorised copies.
>
> **All numbers in this file are reproducible.** Run `python3 "calc/run_all.py"` (numpy required; matplotlib optional) from this folder, or from anywhere using the absolute path. It regenerates every table in `calc/out/`. Every input lives in `calc/assumptions.py`, with its source and a confidence code, and the generated register is in `calc/out/assumptions_register.md`.

## Q1. Which published methods and coefficients apply, and how are they implemented?

### Takeaway
A standard chain covers all three parts. The atmosphere comes from USSA-1976. Sizing uses Raymer's statistical empty-weight fits and mission-segment fractions with the Breguet range/endurance equations. Constraints use Mattingly's master equation, with his installed thrust-lapse and TSFC fits. Only some parts are verified online. Raymer's simple jet-fighter fit (A = 2.34 lb / 2.11 kg, C = −0.13) and the Table 3.2 segment fractions (0.970 / 0.985 / 0.995) are verified. The detailed Raymer fit, the Mattingly lapse/TSFC coefficients and Raymer's supersonic-acceleration fit are recalled textbook values [T]. The biggest methodological finding is about Mattingly's lapse fits: they are not valid at Mach 3 for a conventional fighter turbofan, because they predict zero thrust above about Mach 2.2 when the throttle ratio (TR) is 1.07. A Mach 3 study therefore needs a high-TR turbojet/turbo-ramjet model now and a cycle deck later.

### Cited Findings
- Raymer's simple empty-weight fit for a **jet fighter** is We/W0 = A·W0^C with **A = 2.34, C = −0.13 (W0 in lb)**. One source writes it as We/W0 = 2.34·W0^−0.13, attributed to a historical-data fit. — [USPTO 6981671 (patent citing Raymer)](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6981671)
- A course lecture gives the metric form with coefficient **2.11** and exponent **−0.13**. It notes that the exponent is unchanged whether W0 is in lb or kg, while the constant changes. It puts a fighter's empty-weight fraction at about 0.55. — [Pant, NPTEL "Introduction to Aircraft Design", lecture 48](http://elearn.psgcas.ac.in/nptel/courses/video/101101083/lec48.pdf)
- Raymer's fit carries a wing-sweep constant **Kvs**, which distinguishes fixed from variable-sweep wings. Raymer suggests about a 5% reduction for composite construction (secondary statement in a search summary). — [Linköping FLEX thesis](https://liu.diva-portal.org/smash/get/diva2:1241559/FULLTEXT01.pdf)
- Raymer's historical mission-segment fractions are **warm-up & takeoff 0.970, climb 0.985, landing 0.995**. — [SJSU YA-94 thesis](https://www.sjsu.edu/ae/docs/project-thesis/Alex.Nuyn-Su22.pdf); [ERAU IJAAA paper](https://commons.erau.edu/cgi/viewcontent.cgi?article=1289&context=ijaaa)
- Mattingly, Heiser & Pratt, *Aircraft Engine Design*, 2nd ed. (AIAA 2002) is the source of the installed thrust-lapse treatment. It specifically emphasises the **"theta break / throttle ratio"** concept. — [Google Books record](https://books.google.com/books/about/Aircraft_Engine_Design.html?id=2Wy5rpdm3DMC); [Lavoisier catalogue](https://www.lavoisier.fr/livre/autre/aircraft-engine-design-2nd-ed-2002-cd-rom/mattingly/descriptif_1819445)
- Mattingly's constraint analysis uses the drag polar **C_D = K1·C_L² + K2·C_L + C_D0** (Section 2.3.1, as implemented in an open code). — [DEA code documentation](https://deepwiki.com/kongshan12/DEA/3.1-lift-drag-polar-calculation)
- In constraint analysis, the thrust-lapse parameter α can be below 1 at altitude or above 1 with afterburner. — [Pant, NPTEL lecture 65 (constraint analysis of military aircraft)](http://kcl.digimat.in/nptel/courses/video/101101083/lec65.pdf). In the "rubberised engine" form, thrust ratio represents lapse with speed and altitude as well as throttling. — [McDonald, Cal Poly, "Mission Performance as Point Performance"](https://digitalcommons.calpoly.edu/cgi/viewcontent.cgi?article=1094&context=aero_fac)
- The turbulent recovery factor is r = Pr^(1/3) ≈ 0.896 (Pr = 0.72), and the brief's value is 0.89. — [pygasflow documentation](https://pygasflow.readthedocs.io/en/latest/modules/atd/temperatures.html) (via sibling note `materials_structures_thermal.md`)
- (L/D)max: **Concorde 7.4; A-12/SR-71 family 6.6**. — [W.H. Mason, Virginia Tech, supersonic aerodynamics presentation](https://archive.aoe.vt.edu/mason/Mason_f/SupersonicPres.pdf) (via sibling note `aerodynamics_configuration.md`)
- D-30F6 (MiG-31) TSFC: **0.716 dry / 1.863 afterburning** lb/(lbf·h). — [Wikipedia, Thrust-specific fuel consumption table](https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption); 0.72 kg/(kgf·h) dry — [19FortyFive](https://www.19fortyfive.com/2025/06/mig-31-foxhound-origins-history-and-technical-data-report/) (via sibling note `russian_korean_programs.md`)
- J58 at Mach 3+: the inlet supplies about **54%** of net thrust, the engine **17%** and the ejector **29%**. The turbomachinery is essentially a gas generator. — [Enginehistory.org, SR-71 Propulsion System](https://enginehistory.org/Convention/2013/SR-71Propul/SR-71Propul.shtml) (via sibling note `propulsion_fuel.md`)

### Inferences
**Method and equation register as implemented** (code file in brackets; T = recalled textbook value, V = verified, A = assumption, L = low confidence):

| # | Item | Equation / coefficients used | Status |
|---|---|---|---|
| 1 | Atmosphere [`atmosphere.py`] | USSA-1976 layers (−6.5 K/km to 11 km; isothermal 216.65 K to 20 km; +1.0 K/km to 32 km; …). R = 287.053, g0 = 9.80665, γ = 1.4, r0 = 6,356,766 m for geometric→geopotential, Sutherland μ | Self-test vs 1976 tables at 0/11/20/25 km passes to <0.1% [Calc] |
| 2 | Simple empty weight | We/W0 = 2.34·W0[lb]^−0.13·Kvs, Kvs = 1.0 | V |
| 3 | Detailed empty weight (Raymer Table 6.1, jet fighter) | We/W0 = a + b·W0^C1·A^C2·(T/W)^C3·(W/S)^C4·Mmax^C5 with **a = −0.02, b = 2.16, C1 = −0.10, C2 = 0.20, C3 = 0.04, C4 = −0.10, C5 = 0.08** (lb, lbf/ft²) | T (not found online). It reproduces MiG-25/MiG-31 We/W0 to within 2% (Q5), which supports the recall |
| 4 | Engine-mass correction (added by this study) | ΔWe = (T/W − 1.0)·W0 / (T/W)_engine; (T/W)_eng = 6 for the Mach 3 engine, 8 for the F119-class engine | A/L. Needed because (T/W)^0.04 barely penalises big engines |
| 5 | Segment fractions | 0.970 takeoff, 0.985 climb, 0.995 landing; descent 0.990 (A) | V / A |
| 6 | Climb/accelerate (Raymer refined sizing) | Wi/W0 = 1.0065 − 0.0325M (M<1); **0.991 − 0.007M − 0.01M² (M>1)** → 0.880 to Mach 3 | T, and extrapolated beyond its likely database. Cross-checked with an energy-state integration: d ln W = −c·T·dh_e / [V(T − D)] |
| 7 | Breguet range / endurance | W_i/W_{i−1} = exp[−R·c/(V·L/D)]; exp[−E·c/(L/D)] | Standard |
| 8 | Constraint master equation (Mattingly) | T_SL/W_TO = (β/α)·{(qS/βW_TO)[K1(nβW_TO/qS)² + K2(nβW_TO/qS) + C_D0 + C_DR] + P_s/V} | T (form verified by citations above) |
| 9 | θ0, δ0 | θ0 = (T/T_SL)(1 + 0.2M²); δ0 = (p/p_SL)(1 + 0.2M²)^3.5 | Standard |
| 10 | Lapse, low-bypass mixed-flow turbofan | max: α = δ0 (θ0 ≤ TR); δ0[1 − 3.5(θ0 − TR)/θ0] (θ0 > TR). dry: 0.6δ0; 0.6δ0[1 − 3.8(θ0 − TR)/θ0] | T |
| 11 | Lapse, afterburning turbojet | max: δ0[1 − 0.3(θ0 − 1) − 0.1√M0], minus δ0·1.5(θ0 − TR)/θ0 if θ0 > TR. dry: 0.8δ0[1 − 0.16√M0], minus 0.8δ0·24(θ0 − TR)/[(9 + M0)θ0] if θ0 > TR | T |
| 12 | TSFC (1/h, ×√θ, θ = T/T_SL) | LBPTF dry 0.9 + 0.30M, max 1.6 + 0.27M; TJ dry 1.1 + 0.30M, max 1.5 + 0.23M | T |
| 13 | Drag polar | C_D0(M) table (0.014 subsonic, 0.028 peak at M1.2, 0.0213 at M3); K1 = 0.18 subsonic; supersonic K = A(M² − 1)cosΛ_LE / [4A√(M² − 1) − 2] (Raymer, no LE suction), A = 2.5, Λ_LE = 50° | C_D0 L; K formula T |
| 14 | Recovery / stagnation temperature | T_aw = T[1 + r(γ − 1)M²/2], r = 0.89 turbulent / 0.84 laminar; T0 with r = 1 | V/T |
| 15 | Convective heating | Eckert reference temperature T*/Te = 1 + 0.032M² + 0.58(Tw/Te − 1); Schultz-Grunow c_f = 0.370(log10 Re*)^−2.584; Colburn St = (c_f/2)Pr^−2/3 | T |
| 16 | Radiative equilibrium | h(T_aw − T_w) = εσ(T_w⁴ − T_∞⁴), inner face adiabatic; Planck band integration for 3–5 and 8–12 µm | Standard physics |
| 17 | Field performance | Ground roll s_G = V_TO²/[2g(αT/W − μ)] + 3 s·V_TO, V_TO = 1.2V_s, μ = 0.03. Landing s_L = 3 s·V_TD + V_TD²/(2gμ_b), V_TD = 1.15V_s | T/A |
| 18 | Reserves | 20 min sea-level loiter + 5% of mission fuel (MIL-C-5011A-style) + 1% trapped | T/A |
| 19 | Sizing solver | W0 = We(W0) + Wf(W0) + W_crew + W_payload, solved by bisection, which is a robust form of Raymer's fixed-point iteration. "No closure" if no root below 400 t; flagged "*" above 60 t | [Calc] |

- **Mattingly's fits break down at Mach 3 for a conventional turbofan** [Calc, `out/step2_constraints.md`]. With TR = 1.07 (F119/F100-class), α_max is 0.250 at M2.0/15 km, 0.10 at M2.1 and **0 from about M2.2 upward** in the stratosphere, so Mach 3 is impossible. Raising TR to 1.8–2.1 restores thrust, but there the LBPTF fit (α = δ0, no ram-drag term) returns non-physical values (α = 1.99 at M3). The turbojet fit with TR = θ0 at M3.0 (2.105, a J58-like design intent: maximum turbine temperature reached at Mach 3 cruise) gives α_max = 0.99 at M3/20 km, 0.70 at 22 km and 0.49 at 24 km. Its dry-power branch exceeds its max branch above M2.8 (1.16 vs 0.99 at M3/20 km), so for M ≥ 2.5 the study always uses the afterburning branch, which matches J58 practice. This is why **engine P2 (high-TR afterburning turbojet / turbo-ramjet-like) is the Mach 3 baseline**, while engine P1 (LBPTF, TR 1.07) is used only to show the cost of the Mach 3 requirement.
- The Mattingly turbojet max-power TSFC at Mach 3 / 21 km is **1.90 per hour** [Calc]. That is the same figure as the AB-cruise TSFC sometimes quoted for the J58 (≈1.9; unverified, see Gaps). The fit's LBPTF afterburning TSFC is 1.60 at sea-level static, against the D-30F6's published 1.863 static, so the fits are in the right range.
- Representative TSFC table (1/h) [Calc from the Mattingly fits]. For comparison, Raymer Table 3.3-type cruise values are 0.9 for a turbojet and 0.8 for a low-bypass turbofan [T].

| Condition | LBPTF dry | LBPTF max | TJ dry | TJ max |
|---|---|---|---|---|
| M0.9, 11 km | 1.01 | 1.60 | 1.19 | 1.48 |
| M1.5, 13 km | 1.17 | 1.74 | 1.34 | 1.60 |
| M2.5, 20 km | 1.43 | 1.97 | 1.60 | 1.80 |
| M3.0, 21 km | 1.56* | 2.09* | 1.74* | 1.90 |
| M3.2, 24 km | 1.63* | 2.16* | 1.80* | 1.96 |
\*Beyond the fit's validity for that engine type.

- Representative drag polar [Calc; C_D0 is an assumption, see Gaps]. (L/D)max is 9.96 subsonic, 6.32 at M1.6, 5.72 at M2.0, 5.24 at M2.5, **4.90 at M3.0** and 4.78 at M3.2. K1 is 0.18 → 0.239 (M1.6) → 0.315 (M2) → **0.489 (M3)**. The A-12/SR-71's sourced 6.6 is an upper reference for a slender, chined layout. Küchemann's 4(M+3)/M = 8 at M3 is an envelope no real aircraft reaches.

### Gaps
- **Raymer Table 6.1 coefficients** (a = −0.02, b = 2.16, C1–C5) and Raymer's supersonic acceleration fit (0.991 − 0.007M − 0.01M²) could not be confirmed online; the searches returned only the simple fit. The detailed fit matches MiG-25/31 well (Q5), but check both against the book (Raymer, *Aircraft Design: A Conceptual Approach*, Ch. 3 and 6).
- **Mattingly lapse and TSFC coefficients** (3.5, 3.8, 0.3/0.1, 0.16, 24/(9 + M), 1.5; TSFC constants) are recalled, not re-verified. Also unverified: Mattingly's generic fighter C_D0(M) and K1(M) tables (K1 ≈ 0.18 subsonic is the commonly used value), and the MIL-E-5007D inlet-recovery formula 1 − 0.075(M − 1)^1.35 (0.809 at M3), which is only tabulated for reference.
- **TSFC anchors:** J58 ≈ 1.9/h at Mach 3.2 (AB), R-15B-300 dry/AB SFC and F119 TSFC were not verified. The sibling propulsion note found no verified TSFC for these engines, and F119 supercruise TSFC is not public. Only the D-30F6 (0.716 / 1.863) is sourced.
- No measured supersonic C_D0(M) for the F-22, MiG-25 or SR-71 was found. The C_D0 table above M2 is the weakest aerodynamic input and is covered by a ±15–20% sensitivity.

## Q2. Atmosphere, aero-heating, dynamic pressure, skin temperature and IR exitance (tasks a–d)

### Takeaway
At Mach 3 in the stratosphere the turbulent recovery temperature is **≈ 291 °C at 20 km and ≈ 301 °C at 24 km**, rising to **≈ 349 °C at Mach 3.2**. Radiation to space lowers equilibrium skin temperature only 45–100 K (to about 220–270 °C), so aluminium and epoxy composites are ruled out, and thin skins soak through within about 2–3 minutes. Mach 3 raises total skin exitance about 18× over Mach 0.9 cruise and **mid-wave IR (3–5 µm) exitance about 1,000×**. A low-ε coating cuts the in-band signal only 2–2.5× and raises skin temperature by about 30–50 K. Mach 3 and IR stealth therefore conflict directly.

### Cited Findings
- SR-71 average surface temperatures at speed were **462–622 °F (≈240–330 °C)**, with some parts near the engines at 1,050 °F. — [Merlin, NASA NTRS 20090007797](https://ntrs.nasa.gov/api/citations/20090007797/downloads/20090007797.pdf) (via sibling note `materials_structures_thermal.md`)
- SR-71 surface temperatures reach **up to 800 °F** during sustained Mach 3 flight. — [NASA Dryden FS-030](https://www.nasa.gov/centers/dryden/pdf/495839main_FS-030_SR-71.pdf)
- Kelly Johnson's design temperatures were **585 °F at the nose, 470 °F at the tail and 1,050 °F at the nacelle**. — [Code One, "SR-71 Blackbird, A Fast History"](https://www.codeonemagazine.com/article.html?item_id=153)
- The MiG-25's steel structure tolerated skin temperatures of **≈300 °C at Mach 2.8**. This is a single secondary source. — [migflug MiG-25](https://migflug.com/aircraft/mig-25-foxbat/)
- Material limits: Ti-6Al-4V offers high strength to 600 °F and service through **750 °F (400 °C)** — [Rolled Alloys datasheet](https://www.rolledalloys.com/wp-content/uploads/6AL4V_Data-sheet.pdf). The 2618-T61 aluminium (the Concorde-type alloy) keeps about 80% of its properties at 400 °F only after short exposure — [DTIC AD0801499](https://apps.dtic.mil/sti/html/tr/AD0801499/index.html). PMR-15 polyimide composites are used at **260–288 °C** — [NASA NTRS 20050187016](https://ntrs.nasa.gov/citations/20050187016) (all via sibling note `materials_structures_thermal.md`).
- Aircraft skin temperatures exceed about 300 K in typical supercruise. Controlling skin temperature and emissivity reduces detectability. — [KAIST/JSASS 2012](https://koasas.kaist.ac.kr/handle/10203/101853). External aircraft surfaces radiate mainly in the LWIR band. — [The Aeronautical Journal 2025](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D14DC72BD1247D01A1D4883B5B17B687/S0001924024001635a.pdf/infrared-signature-of-aero-engine-exhaust-plumes-potential-core-and-aircraft-surface-from-direct-bottom-view.pdf) (via sibling note `signature_reduction.md`)

### Inferences
All results in this section are [Calc] from `calc/step1_atmos_thermal.py` → `calc/out/step1_atmos_thermal.md`, with CSV in `calc/out/step1_isa.csv`.

**(a) 1976 US Standard Atmosphere (geometric altitude input)**

| z (km) | H geopot. (km) | T (K) | p (Pa) | ρ (kg/m³) | a (m/s) |
|---|---|---|---|---|---|
| 0 | 0.000 | 288.15 | 101,325 | 1.22500 | 340.29 |
| 11 | 10.981 | 216.77 | 22,700 | 0.36480 | 295.15 |
| 15 | 14.965 | 216.65 | 12,112 | 0.19476 | 295.07 |
| 18 | 17.949 | 216.65 | 7,565 | 0.12165 | 295.07 |
| 20 | 19.937 | 216.65 | 5,529 | 0.08891 | 295.07 |
| 22 | 21.924 | 218.57 | 4,048 | 0.06451 | 296.38 |
| 24 | 23.910 | 220.56 | 2,972 | 0.04694 | 297.72 |
| 25 | 24.902 | 221.55 | 2,549 | 0.04008 | 298.39 |

**(b) Stagnation T0 / turbulent adiabatic-wall T_aw (r = 0.89), °C.** Rows for 11, 15 and 18 km equal the 20 km row within 1 °C (isothermal layer).

| z (km) | M2.0 | M2.5 | M2.83 | M3.0 | M3.2 |
|---|---|---|---|---|---|
| 0 | 246 / 220 | 375 / 336 | 477 / 426 | 534 / 477 | 605 / 540 |
| 20 | 117 / 98 | 214 / 185 | 291 / 252 | 333 / **291** | 387 / 338 |
| 22 | 120 / 101 | 219 / 189 | 296 / 257 | 339 / 296 | 393 / 344 |
| 24 | 124 / 104 | 223 / 193 | 301 / 262 | 344 / **301** | 399 / **349** |
| 25 | 126 / 106 | 225 / 195 | 303 / 264 | 347 / 303 | 402 / 352 |

The laminar recovery temperature (r = 0.84) is about 20 °C lower at Mach 3 (271 °C at 20 km).

**(c) Dynamic pressure q = 0.7·p·M² (kPa)**

| z (km) | M2.0 | M2.5 | M2.83 | M3.0 | M3.2 |
|---|---|---|---|---|---|
| 11 | 63.6 | 99.3 | 127.3 | 143.0 | 162.7 |
| 15 | 33.9 | 53.0 | 67.9 | 76.3 | 86.8 |
| 18 | 21.2 | 33.1 | 42.4 | 47.7 | 54.2 |
| 20 | 15.5 | 24.2 | 31.0 | **34.8** | 39.6 |
| 22 | 11.3 | 17.7 | 22.7 | 25.5 | 29.0 |
| 24 | 8.3 | 13.0 | 16.7 | **18.7** | 21.3 |
| 25 | 7.1 | 11.2 | 14.3 | 16.1 | 18.3 |

V = 885 m/s at Mach 3 in the isothermal layer (893 m/s at 24 km).

**(d1) Radiative-equilibrium skin temperature** (turbulent flat plate, radiating to ambient, no heat sink inside; °C)

| Case | x (m) | T_aw | h (W/m²K) | T_w, ε = 0.9 | ε = 0.5 | ε = 0.3 |
|---|---|---|---|---|---|---|
| M0.9, 11 km | 5 | −25 | 114 | −26 | −26 | −25 |
| M1.6, 13 km | 5 | 42 | 124 | 39 | 41 | 41 |
| M2.83, 20 km | 5 | 252 | 60 | 208 | 224 | 234 |
| M3.0, 20 km | 1 / 5 | 291 | 79 / 61 | 245 / 236 | 262 / 255 | 272 / 267 |
| M3.0, 24 km | 1 / 5 | 301 | 49 / 37 | 234 / 221 | 256 / 246 | 270 / 262 |
| M3.2, 24 km | 1 / 5 | 349 | 49 / 37 | 265 / 250 | 291 / 279 | 309 / 299 |

- The Mach 3.2 / 24 km values (250–265 °C for ε = 0.9) fall inside the SR-71's published average-skin band of 240–330 °C, which validates the thermal model. Leading edges and noses approach T0 (344–399 °C), which is consistent with the NASA "up to 800 °F" figure on a warm day.
- At higher altitude the lower density cuts h, so radiation removes more: T_aw − T_w is 45–55 K at 20 km and 67–99 K at 24 km for ε = 0.9. Flying high helps skin temperature a little and q a lot (35 → 19 kPa).
- All Mach 3 cases put skins at 220–310 °C. That is above aluminium alloys (the 2618-T61 class is only good to about 200 °C after short exposure) and above epoxy-matrix composites. It is within Ti-6Al-4V (≤400 °C) and at or above the top of the PMR-15 polyimide range (260–288 °C) once leading edges and a hot day are considered. **Mach 3 therefore implies a titanium or polyimide/BMI hot structure**, and any radar-absorbing material (RAM) must survive 250–350 °C.

**(d2) Skin IR exitance** (x = 5 m; ratios relative to Mach 0.9 / 11 km, ε = 0.9)

| Case | ε | T_w (K) | Total εσT⁴ (W/m²) | 3–5 µm (W/m²) | 8–12 µm (W/m²) | Total ratio | MWIR ratio | LWIR ratio |
|---|---|---|---|---|---|---|---|---|
| M0.9, 11 km | 0.9 | 247 | 191 | 0.5 | 38.7 | 1 | 1 | 1 |
| M1.6, 13 km | 0.9 | 312 | 486 | 8.1 | 132 | 2.5 | 15 | 3.4 |
| M2.83, 20 km | 0.9 | 482 | 2,746 | 363 | 727 | 14.4 | 678 | 18.8 |
| **M3.0, 20 km** | 0.9 | 509 | **3,428** | **537** | **867** | **17.9** | **~1,000** | **22.4** |
| M3.0, 20 km | 0.3 | 540 | 1,445 | 266 | 345 | 7.6 | 497 | 8.9 |
| M3.0, 24 km | 0.9 | 494 | 3,047 | 437 | 790 | 16.0 | 817 | 20.4 |
| M3.2, 24 km | 0.9 | 523 | 3,825 | 648 | 943 | 20.0 | 1,210 | 24.4 |
| M3.2, 24 km | 0.3 | 573 | 1,828 | 387 | 410 | 9.6 | 724 | 10.6 |

- **The IR-stealth vs thermal-management conflict, in numbers:** cutting ε from 0.9 to 0.3 at Mach 3 / 20 km raises skin temperature by 31 K (509 → 540 K) and only halves in-band MWIR (537 → 266 W/m²). The Mach 3 skin still emits about 500× the MWIR of the subsonic skin. Mach 3 makes the whole airframe an MWIR/LWIR source visible from every aspect, not just the exhaust.

**(d3) Heat soak.** The lumped time constant τ = ρct / (h_conv + h_rad) at Mach 3 / 20 km is **40 s** for 1.5 mm Ti, 49 s for 1.2 mm steel and 55–56 s for 2 mm aluminium or 3 mm CFRP. The skin is about 95% soaked after roughly 2–3 minutes. A 100 km Mach 3 dash lasts 113 s (≈2–2.8τ, so 87–94% of equilibrium). **A "dash-only" Mach 3 requirement does not avoid hot skins.** It only shortens heat soak into thick structure, fuel and avionics.

### Gaps
- No measured MiG-25 skin temperatures from a primary source, and no quantified effect of the SR-71 black paint, were found (sibling note).
- The heat-transfer model assumes a flat plate, turbulent flow from the leading edge, constant cp and no internal heat sink. Stagnation lines, inlet lips and engine-bay surfaces need dedicated analysis.
- The material properties used for τ are typical handbook values, not verified this session.

## Q3. Constraint analysis: T/W vs W/S and the feasible design point (task e)

### Takeaway
With the Mach-3-capable engine (P2), **Mach 3 cruise needs only T_SL/W ≈ 0.2–0.45 and is not the thrust driver**. The **sustained 5 g turn at Mach 0.9 / 9 km** drives the design: it needs T/W ≈ 1.52 at W/S = 4,000 N/m², and together with a 120 m/s Ps requirement it pushes the design to a very low wing loading. The minimum-T/W point is **W/S ≈ 2,200 N/m² (224 kg/m²), T/W ≈ 1.02**. The point selected by minimum takeoff weight is **W/S = 2,300 N/m², T/W = 1.03**. Landing in 900 m caps W/S at about 4,400 N/m². Relaxing the turn to 4 g moves the optimum to **W/S ≈ 3,550 N/m², T/W ≈ 0.94**. The same constraint set with an F119-class engine and no Mach 3 requirement lands at W/S 3,250 N/m² and T/W 1.20, which is almost exactly the F-22's (3,642 N/m², 1.10).

### Cited Findings
- F-22A: span 13.6 m; empty weight 43,340 lb; MTOW 83,500 lb; 2 × F119 of the 35,000 lb class; supercruise above Mach 1.5 — [af.mil F-22 fact sheet](https://www.af.mil/About-Us/Fact-Sheets/Display/Article/104506/f-22-raptor/). Supercruise Mach 1.82 and maximum speed Mach 2.25 — [USAF Academy "Contrails"](https://www.usafa.af.mil/US-Air-Force-Academy-News/Features/Feature-View/Article/969680/the-contrails-aircraft-weapons-systems-f-22a-raptor/) (via sibling note `us_programs_lockheed_martin.md`)
- MiG-25: R-15B-300 thrust **73.5 kN dry / 100.1 kN AB** per engine — [flugzeuginfo.net](https://www.flugzeuginfo.net/acdata_php/acdata_mig25_en.php). MiG-31: D-30F6 thrust **93.1 kN dry / 151.9 kN AB** — [Baidu Baike MiG-31](https://baike.baidu.com/en/item/MiG-31/1452676); [Army Recognition](https://www.armyrecognition.com/military-products/air/fighter/mig-31-foxhound-mikoyan) (via sibling note `russian_korean_programs.md`)

### Inferences
[Calc] from `calc/step2_constraints.py` → `calc/out/step2_constraints.md`. Plots are in `calc/out/constraint_diagram_P2.png` and `calc/out/constraint_diagram_P1.png`; the selected point is shown in `calc/out/constraint_diagram_P2_selected.png`.

**Requirement set (each value is an assumption unless the brief gave it).** β is the weight fraction at that condition. "max" means afterburner, "dry" means military power.

| Constraint | M | h (km) | n | β | P_s (m/s) | Throttle |
|---|---|---|---|---|---|---|
| Mach 3.0 cruise (three altitudes) | 3.0 | 20 / 22 / 24 | 1 | 0.80 | 0 | max |
| Acceleration margin toward Mach 3 | 2.5 | 18 | 1 | 0.80 | 50 | max |
| Supercruise (dry) | 1.7 / 1.8 | 13 / 15 | 1 | 0.85 | 0 | dry |
| Sustained turn (brief) | 0.9 | 9 | 5 | 0.80 | 0 | max |
| Specific excess power (L) | 0.9 | 9 | 1 | 0.80 | 120 | max |
| Takeoff ground roll incl. 3 s rotation | SL | 0 | – | 1.0 | – | max; C_Lmax 1.2, μ 0.03 |
| Landing roll (sets W/S cap) | SL | 0 | – | 0.65 | – | C_Lmax 1.3, μ_b 0.35 (brakes + chute) |

**Engine P2 (high-TR AB turbojet, TR = 2.105): T_SL/W_TO required**

| Constraint | W/S 2,500 | 3,000 | 3,500 | 4,000 | 5,000 | 6,000 N/m² |
|---|---|---|---|---|---|---|
| M3.0 cruise 20 km | 0.322 | 0.276 | 0.245 | 0.223 | 0.195 | 0.179 |
| M3.0 cruise 22 km | 0.355 | 0.312 | 0.283 | 0.264 | 0.243 | 0.235 |
| M3.0 cruise 24 km | 0.409 | 0.372 | 0.350 | 0.338 | 0.332 | 0.339 |
| P_s 50 m/s, M2.5 / 18 km | 0.461 | 0.404 | 0.365 | 0.337 | 0.300 | 0.279 |
| Supercruise M1.7 / 13 km (dry) | 0.702 | 0.595 | 0.520 | 0.465 | 0.392 | 0.346 |
| Supercruise M1.8 / 15 km (dry) | 0.684 | 0.586 | 0.518 | 0.469 | 0.405 | 0.369 |
| **5 g sustained, M0.9 / 9 km** | **1.085** | **1.221** | **1.368** | **1.521** | **1.840** | **2.167** |
| P_s 120 m/s, M0.9 / 9 km | 0.991 | 0.961 | 0.942 | 0.929 | 0.916 | 0.911 |
| Takeoff 800 m | 0.465 | 0.570 | 0.680 | 0.795 | 1.043 | 1.314 |

- The landing limit (900 m) gives **W_TO/S ≤ 4,407 N/m² (449 kg/m²)**. The 600 m and 900 m takeoff curves are plotted. Takeoff is not active at the selected point: at W/S 2,300 an 800 m roll needs 0.43 and a 600 m roll needs 0.62, both below the design T/W of 1.03.
- Engine P2's lapse is what makes Mach 3 "cheap" in thrust terms: α_max is 0.48 at M0.9/9 km, 0.70 at M1.5/11 km, 0.81 at M2.5/18 km and 0.99 at M3/20 km [Calc]. With a 0.7 installed-thrust knockdown above Mach 2.5, the worst Mach 3 cruise requirement at the minimum-T/W point (W/S 2,200) rises from 0.44 to 0.63, which is still below the turn and Ps lines. At the selected W/S 2,300 it is 0.43 without knockdown.
- **Minimum-T/W design point (P2): W/S 2,200 N/m², T/W 1.017**, with the 5 g and Ps constraints active. Variants:

| Variant | W/S (N/m²) | T/W | Active constraint |
|---|---|---|---|
| Baseline (5 g) | 2,200 | 1.017 | Ps 120 / 5 g |
| 4 g sustained turn | 3,550 | 0.941 | 4 g turn |
| 6 g sustained turn | ≤2,000 (grid edge) | 1.271 | 6 g turn |
| Subsonic K1 0.14 instead of 0.18 | 2,850 | 0.960 | Ps 120 |
| Takeoff roll 600/900 m, C_Lmax,TO 1.0 | unchanged | unchanged | – |

- **Optimum altitude conflict.** At Mach 3, C_L* = 0.209, which needs q* = 0.8·(W/S)/C_L*. That puts the best-L/D altitude at 27.2 km for W/S 3,000, 25.3 km for 4,000 and 22.7 km for 6,000. The low wing loading imposed by the subsonic turn requirement therefore pushes efficient Mach 3 cruise **above 25 km**, outside the brief's 20–24 km band. Within a 25 km ceiling, the W/S 2,300 design cruises at L/D 4.2 instead of 4.9.
- **Engine P1 (F119-class LBPTF, TR 1.07), Mach 3 requirement removed:** design point W/S 3,250 N/m², T/W 1.20, with the 5 g turn and the M1.8/15 km dry supercruise active (supercruise M1.8 needs 1.27 at W/S 3,000). This is close to the F-22 point (3,642 N/m², 1.10), which suggests the constraint set and engine model are realistic. All Mach 3 constraints for P1 are infinite (α = 0).
- Reference aircraft on the same axes: MiG-25P (5,865 N/m², T/W 0.56), MiG-31 (6,527, 0.76), SR-71A (3,936, 0.44), F-22A (3,642, 1.10). The Russian speed references sit far from the stealth-fighter corner: high W/S, low T/W, and no sustained-g capability at Mach 0.9.

### Gaps
- The P_s = 120 m/s requirement, β values, C_Lmax, μ_brake and the K1 = 0.18 subsonic value are assumptions [A/L]. The design point is sensitive to K1 (W/S 2,200 → 2,850 at K1 = 0.14) and to the turn requirement.
- Mattingly's lapse fits for a TR ≈ 2.1 turbojet at Mach 3 are not validated against J58 installed-thrust data. No public J58/SR-71 installed thrust vs Mach figure was retrieved, and NASA YF-12 propulsion reports could not be opened. A pyCycle/NPSS-class cycle model with a MIL-E-5007D recovery schedule should replace the fits in the next phase.

## Q4. Takeoff-weight sizing, fuel fractions, wing area, installed thrust and engine class, with sensitivities (tasks f–g)

### Takeaway
At the selected design point (W/S 2,300 N/m², T/W 1.03) with historical-fit empty weight (K_we = 1.0), the **Mach 3 interceptor (500 km at Mach 3 out, Mach 2.5 back) sizes to ≈ 43.5 t** with Wf/W0 0.38, S ≈ 186 m² and **2 × 221 kN**. That is MiG-31 weight with a larger engine than any fighter engine in service. The **strike/air-superiority mission sizes to ≈ 35 t** with the Mach-3-capable engine, against **≈ 22 t** with an F119-class engine and no Mach 3. The design sits on a **"sizing cliff"**. A 10% empty-weight penalty for stealth or hot structure doubles TOGW, and the F-22-calibrated penalty (K_we ≈ 1.2) does not close at any practical weight. The decisive levers are the 5 g sustained-turn requirement (relaxing to 4 g roughly halves W0 to ≈ 22.6 t), Mach 3 dash versus cruise (−42%), and the empty-weight penalty.

### Cited Findings
- J58: 32,500 lbf (≈145 kN) per engine — [NASA FS-030](https://www.nasa.gov/centers/dryden/pdf/495839main_FS-030_SR-71.pdf). F119: 35,000 lbf class (≈156 kN) — [af.mil](https://www.af.mil/About-Us/Fact-Sheets/Display/Article/104506/f-22-raptor/). D-30F6: 151.9 kN AB — [Baidu Baike](https://baike.baidu.com/en/item/MiG-31/1452676). R-15B-300: 100.1 kN AB — [flugzeuginfo.net](https://www.flugzeuginfo.net/acdata_php/acdata_mig25_en.php) (via sibling notes).
- Engines that have sustained Mach 2.8+ (J58, R-15B-300, D-30F6) trade low overall pressure ratio and high weight for tolerance of high compressor-inlet temperature. The R-15B-300 has OPR 4.75 — [Wikipedia, Tumansky R-15](https://en.wikipedia.org/wiki/Tumansky_R-15). The D-30F6 weighs 2,416 kg for about 152 kN (engine T/W ≈ 6.4) — [Wikipedia, Soloviev D-30](https://en.wikipedia.org/wiki/Soloviev_D-30) (via sibling note `propulsion_fuel.md`)

### Inferences
All results in this section are [Calc] from `calc/step3_sizing.py` → `calc/out/step3_sizing.md` and `calc/out/sizing_summary.json`. Plots are in `calc/out/sizing_radius_vs_W0.png`, `calc/out/sizing_Kwe_vs_W0.png` and `calc/out/sizing_tornado_A.png`.

**Mission profiles** (payload 900 kg internal, all released at combat; crew 100 kg; reserves = 20 min sea-level loiter + 5% of mission fuel + 1% trapped):
- **A, interceptor:** takeoff (0.970) → climb and accelerate to M3.0 (Raymer fit 0.880) → **500 km at M3.0** at the best altitude ≤ 25 km in afterburner → 2 min max-AB combat at M1.5/12 km → release payload → re-accelerate to M2.5 → **500 km back at M2.5** → descent (0.990) → reserves → landing (0.995).
- **A-dash ("Mach 3 dash only"):** 400 km out at M0.9 → accelerate → **100 km dash at M3.0** → combat → 500 km back at M0.9 (same 500 km radius).
- **B, stealth strike / air superiority:** 600 km out at M0.9 → **200 km supercruise at M1.6** (dry if possible) → 3 min max-AB combat at M0.9/9 km → release payload → 200 km at M1.6 → 600 km at M0.9 (800 km radius).
- Cruise altitude is chosen per segment for the best L/D, provided thrust ≥ drag. The bands are M0.9: 9–15 km, M1.6: 11–18 km and M2.5/M3: 17/20–25 km. TSFC comes from the Mattingly fits at the actual altitude and throttle.

**Design-point selection by minimum TOGW along the P2 constraint envelope** (K_we = 1.0). W0 in tonnes; `*` means above 60 t:

| W/S (N/m²) | T/W (envelope) | W0 A | W0 B |
|---|---|---|---|
| 2,000 | 1.039 | 54.3 | 43.1 |
| 2,200 | 1.017 | 44.1 | 35.4 |
| **2,300** | **1.035** | **43.5** | **35.0** |
| 2,600 | 1.111 | 45.7 | 36.7 |
| 3,000 | 1.221 | 52.6 | 42.2 |
| 3,400 | 1.338 | 65.1* | 51.5 |
| 4,000 | 1.521 | 100.6* | 76.3* |
| 4,400 | 1.647 | 143.6* | 105.4* |

Below about 2,300 N/m² the oversized wing (Raymer W/S^−0.10 term) and the poor Mach 3 L/D under a 25 km ceiling dominate. Above it, the engine mass needed for T/W > 1.2 dominates. Without the explicit engine-mass correction, the selection drifts to T/W 1.65 at the landing limit, because Raymer's (T/W)^0.04 term barely penalises engine size.

**(f)/(g) Baseline sizing results** (P2 design point W/S 2,300 N/m², T/W 1.035; P1 point W/S 3,300 N/m², T/W 1.213)

| Case | K_we | W0 (kg) | We/W0 | Wf/W0 | Wf (kg) | S (m²) | T_SL total (kN) | per engine, twin (kN) |
|---|---|---|---|---|---|---|---|---|
| A interceptor, P2 | 1.0 | **43,516** | 0.597 | **0.380** | 16,522 | 186 | 442 | **221** |
| A-dash (100 km M3), P2 | 1.0 | **25,200** | 0.632 | 0.329 | 8,282 | 107 | 256 | 128 |
| B strike/air-sup, P2 | 1.0 | **34,972** | 0.611 | 0.361 | 12,609 | 149 | 355 | 177 |
| B strike/air-sup, P1 (no Mach 3) | 1.0 | **22,095** | 0.622 | 0.333 | 7,360 | 66 | 263 | 131 |
| A interceptor, P2 | 1.2 | 196,501* | 0.613 | 0.382 | 75,055 | 838 | 1,994 | 997 |
| A-dash, P2 | 1.2 | 98,212* | 0.658 | 0.332 | 32,561 | 419 | 996 | 498 |
| B, P2 | 1.2 | 150,817* | 0.630 | 0.363 | 54,821 | 643 | 1,530 | 765 |
| B, P1 (no Mach 3) | 1.2 | 81,624* | 0.650 | 0.338 | 27,551 | 243 | 971 | 485 |

**Segment log, Profile A (K_we = 1.0, W0 = 43,516 kg)**

| Segment | Wi/Wi−1 | Fuel (kg) | Detail |
|---|---|---|---|
| Takeoff | 0.9700 | 1,305 | Raymer |
| Climb + accelerate to M3 | 0.8800 | 5,065 | Raymer fit; the energy method gives 0.8992 (4.5 min) |
| M3.0 cruise 500 km | 0.9315 | 2,544 | 25.0 km, L/D 4.20, C_L 0.118, c = 1.92/h |
| Combat 2 min | 0.9585 | 1,435 | α = 0.598, c = 1.60/h |
| Payload released | – | – | −900 kg |
| Re-accelerate to M2.5 | 0.9509 | 1,583 | Raymer fit |
| M2.5 return 500 km | 0.9289 | 2,182 | 25.0 km, L/D 4.59, c = 1.82/h |
| Descent / reserve loiter / landing | 0.990 / 0.961 / 0.995 | 285 / 1,095 / 136 | Loiter: sea level, M0.27, L/D 9.96, c = 1.18/h |

The climb and acceleration to Mach 3 burns **35% of the mission fuel**, more than the 500 km Mach 3 cruise itself (17%). Mach 3 range is lost mainly in getting there.

**Climb-model uncertainty.** The Raymer fit gives 0.880 and the energy-state integration for this airframe and engine gives 0.899 (4.5 min to Mach 3). That 2-point difference in one segment fraction changes Profile A W0 from **43.5 t to 33.1 t (−24%)**. Results by case, Raymer vs energy: A 43.5 / 33.1; A-dash 25.2 / 19.9; B-P2 35.0 / 37.2; B-P1 22.1 / 20.7 t.

**Engine class.** Profile A at the baseline point needs about **221 kN per engine for a twin**. That is about 40% more than any engine listed (F119 ≈ 156 kN, J58 ≈ 145–151 kN, D-30F6 ≈ 152 kN). A single engine of 256–442 kN would be far beyond any fighter engine. The **twin-engine layout is forced** unless the requirements are relaxed (see S4). With the relaxed 4 g design, A-dash needs only 0.95 × 16.0 t × g ≈ **149 kN in total**, which is single-engine J58/F119-class thrust.

**Sensitivity S1: Profile A W0 (t) vs Mach 3 radius and K_we**

| Radius (km) | K = 1.0 | 1.1 | 1.2 | 1.3 |
|---|---|---|---|---|
| 100 | 18.2 | 33.1 | 63.7* | 125* |
| 200 | 22.1 | 41.8 | 82.9* | 166* |
| 300 | 27.2 | 53.6 | 109* | 222* |
| 400 | 34.1 | 69.7* | 146* | 300* |
| 500 | 43.5 | 92.1* | 197* | no closure |
| 600 | 56.5 | 123* | 268* | no closure |
| 800 | 100* | 230* | no closure | no closure |
| 1,000 | 189* | no closure | no closure | no closure |

**Sensitivity S2: W0 (t) vs K_we** (selected values; full table in `out/step3_sizing.md`)

| Case | K = 0.9 | 1.0 | 1.05 | 1.1 | 1.2 |
|---|---|---|---|---|---|
| A | 21.9 | 43.5 | 63.0* | 92.1* | 197* |
| A-dash | 14.1 | 25.2 | 34.8 | 48.7 | 98.2* |
| B, P2 | 18.3 | 35.0 | 49.9 | 71.9* | 151* |
| B, P1 (no Mach 3) | 12.8 | 22.1 | 30.0 | 41.4 | 81.6* |

**Sensitivity S3: one-at-a-time changes, Profile A baseline 43.5 t**

| Change | W0 (t) | ΔW0 |
|---|---|---|
| K_we 1.0 → 1.2 (F-22-like LO penalty) | 196.5 | +352% |
| Mach 3 radius 500 → 700 km | 74.5 | +71% |
| TSFC ×1.1 | 53.1 | +22% |
| Supersonic C_D0 ×1.2 (L/D_M3 ≈ 4.5) | 52.8 | +21% |
| Combat at M0.9/9 km instead of M1.5/12 km | 47.1 | +8% |
| Payload 900 → 1,000 kg | 44.6 | +2.4% |
| Engine T/W 6 → 5 / 6 → 8 | 44.1 / 42.8 | +1.4% / −1.8% |
| Supersonic thrust knockdown 0.7 | 43.5 | 0% (thrust not limiting) |
| Payload 900 → 700 kg | 41.4 | −4.9% |
| No explicit engine-mass correction | 40.6 | −6.8% |
| Supersonic C_D0 ×0.85 (L/D_M3 ≈ 5.3) | 37.9 | −13% |
| Mach 3 / 2.5 ceiling 25 → 28 km (re-selected 2,200 / 1.02) | 36.9 | −15% |
| TSFC ×0.9 (better high-Mach cycle) | 36.0 | −17% |
| Energy-method climb instead of Raymer fit | 33.1 | −24% |
| Subsonic K1 0.18 → 0.14 (re-selected 2,900 / 0.97) | 27.3 | −37% |
| Mach 3 radius 500 → 300 km | 27.2 | −37% |
| Mach 3 dash 100 km only (A-dash) | 25.2 | −42% |
| Simple Raymer We fit instead of detailed | 22.7 | −48% |
| **Sustained turn 5 g → 4 g (re-selected 3,600 / 0.95)** | **22.6** | **−48%** |

- The weight growth factor is dW0/dW_payload ≈ **10.7 kg per kg of payload** (Profile A, K = 1.0). A typical fighter is around 4–6 (general design knowledge, not sourced). The high value marks the sizing cliff.

**Sensitivity S4: relaxed requirements × K_we (engine P2), W0 in t**

| Design point (W/S / T/W) | K_we | A | A-dash | B | S for A (m²) | A per engine, twin (kN) |
|---|---|---|---|---|---|---|
| 5 g, 25 km ceiling (2,300 / 1.03) | 1.0 / 1.1 / 1.2 | 43.5 / 92.1* / 197* | 25.2 / 48.7 / 98.2* | 35.0 / 71.9* / 151* | 186 / 393 / 838 | 221 / 467 / 997 |
| **4 g turn (3,600 / 0.95)** | 1.0 / 1.1 / 1.2 | **22.6 / 42.7 / 84.9*** | **16.0 / 28.0 / 52.2** | **18.8 / 34.4 / 66.5*** | 61 / 116 / 231 | 105 / 199 / 395 |
| 4 g + 28 km ceiling (3,500 / 0.94) | 1.0 / 1.1 / 1.2 | 22.5 / 42.6 / 84.6* | 16.0 / 28.0 / 52.3 | 18.9 / 34.6 / 67.0* | 63 / 119 / 237 | 104 / 197 / 391 |

- **RAM / stealth penalty in physical terms.** Take the 4 g A-dash concept: 16.0 t, We ≈ 10 t, S ≈ 44 m². An S_wet/S of about 4 is an assumed typical fighter ratio, giving ≈ 175 m². A K_we increase of 0.05 (≈ 500 kg) then equals about **2.8 kg/m² of coating or treatment over the whole wetted surface**, and it raises W0 from 16.0 to roughly 21 t (between the computed K = 1.0 and 1.1 values of 16.0 and 28.0 t). Every kilogram of LO treatment must be "bought" about 10 times over.

### Gaps
- Mission and requirement definitions (radius, combat duration and condition, reserves, payload release, cruise ceilings) are notional study assumptions, not a customer specification.
- Raymer's regressions are not built from Mach 3 low-observable aircraft. K_we = 1.0 assumes MiG-25/31-level structural efficiency with modern materials. K_we = 1.2 assumes the F-22's deviation from the fit is all an "LO penalty", although the F-22 also carries 9 g structure, thrust vectoring and avionics. The real penalty for a hot, LO structure is unknown and is the most important number the team must estimate bottom-up.
- Engine thrust/weight for a Mach 3 engine (6) and for the F119 class (8) are assumptions. F119 weight (≈1,770 kg) is listed as unverified in the sibling propulsion note.
- The S_wet/S ≈ 4 ratio used for the RAM-areal-density conversion is not sourced.

## Q5. Sanity check against MiG-25, MiG-31, SR-71 and F-22 (task h)

### Takeaway
The Raymer fits reproduce the MiG-25 and MiG-31 empty-weight fractions to within 2%, confirming them as the right "Mach 2.8 steel/titanium" baseline. The SR-71 is 5–8% lighter than the fits, and the **F-22 is 19–22% heavier, the best available calibration of a stealth-fighter penalty**. The sized concepts' fuel fractions (0.33–0.38) match the MiG-25/31 (0.38–0.39). Their wing loadings (2,300 N/m²) are far below any reference aircraft, which is a direct consequence of the 5 g turn requirement. Inverse checks bracket the mission model's error. It gives about 30% less radius than the commonly quoted F-22 figure and about 15% more than the quoted MiG-31 figure (both claims unverified).

### Cited Findings
- **MiG-25P:** empty weight 20,000 kg and loaded weight 36,720 kg — [aerocorner](https://aerocorner.com/aircraft/mikoyan-mig-25-foxbat/). Other figures are 19,070 kg empty and 41,200 kg, with internal fuel of 17,700 L ≈ 14,100 kg — [flugzeuginfo.net](https://www.flugzeuginfo.net/acdata_php/acdata_mig25_en.php). The airframe is about 80% nickel steel, 11% aluminium and 9% titanium — [migflug](https://migflug.com/aircraft/mig-25-foxbat/)
- **MiG-31:** MTOW 46,200 kg, crew of two — [Military History Fandom](https://military-history.fandom.com/wiki/Mikoyan_MiG-31). Internal fuel is 35,550 lb ≈ 16,130 kg — [Planehistoria](https://planehistoria.com/mikoyan-mig-31/) (via sibling note `russian_korean_programs.md`)
- **SR-71A:** wing area 1,800 ft² (≈167 m²) and empty weight 67,500 lb — [GlobalSecurity](https://www.globalsecurity.org/intell/systems/sr-71-specs.htm). Sources conflict: 59,000 lb empty and about 80,000 lb fuel — [SR-71.org](https://sr-71.org/blackbird/sr-71). Gross takeoff weight is 140,000 lb and each J58 gives 32,500 lb thrust — [NASA FS-030](https://www.nasa.gov/centers/dryden/pdf/495839main_FS-030_SR-71.pdf) (via sibling note `us_programs_lockheed_martin.md`)
- **F-22A:** empty weight 43,340 lb (19,700 kg) and MTOW 83,500 lb; 2 × 35,000 lb-class F119 — [af.mil](https://www.af.mil/About-Us/Fact-Sheets/Display/Article/104506/f-22-raptor/)
- **(L/D)max of the A-12/SR-71 family is 6.6** — [Mason, VT](https://archive.aoe.vt.edu/mason/Mason_f/SupersonicPres.pdf)

### Inferences
[Calc] from `calc/step4_sanity.py` → `calc/out/step4_sanity.md`.

| Aircraft | W0 used (kg) | We/W0 | Wf/W0 | T_AB/W0 | T_dry/W0 | W0/S (N/m², kg/m²) | AR | Raymer simple: actual/fit | Raymer detailed: actual/fit |
|---|---|---|---|---|---|---|---|---|---|
| MiG-25P | 36,720 | 0.545 | 0.384 | 0.56 | 0.41 | 5,865 (598) | 3.19 | **1.01** | **0.98** |
| MiG-31 | 41,000 | 0.532 | 0.393 | 0.76 | 0.46 | 6,527 (666) | 2.94 | **1.00** | **0.98** |
| SR-71A | 67,104 | 0.456 | 0.541 | 0.44 | 0.34 | 3,936 (401) | 1.72 | 0.92 | 0.95 |
| F-22A | 28,965 | 0.680 | 0.282 | 1.10 | 0.81 | 3,642 (371) | 2.37 | **1.22** | **1.19** |
| *Concept A, P2* | 43,516 | 0.597 | 0.380 | 1.03 | – | 2,300 (235) | 2.5 | – | – |
| *Concept A-dash, P2* | 25,200 | 0.632 | 0.329 | 1.03 | – | 2,300 | 2.5 | – | – |
| *Concept B, P2* | 34,972 | 0.611 | 0.361 | 1.03 | – | 2,300 | 2.5 | – | – |
| *Concept B, P1 (no Mach 3)* | 22,095 | 0.622 | 0.333 | 1.21 | – | 3,300 | 2.5 | – | – |

How W0 was defined for each aircraft (inputs flagged where unverified):
- **MiG-31:** normal takeoff 41,000 kg; empty weight 21,820 kg (unverified); wing area 61.6 m² and span 13.46 m (unverified).
- **MiG-25:** wing area 61.4 m² and span 14.0 m (commonly published, unverified).
- **SR-71:** W0 = empty + 80,000 lb fuel + 2 crew = 147,900 lb, because the NASA 140,000 lb gross is less than empty + full fuel and so implies a partial fuel load. Dry thrust of 25,000 lbf is unverified.
- **F-22:** W0 = empty + about 18,000 lb internal fuel (unverified) + about 1,100 kg pilot and internal AAMs (assumed); wing area 840 ft² (unverified).

- **Calibration of the stealth penalty.** The Mach 2.83 steel/titanium interceptors sit on the Raymer fits (K ≈ 1.0), so Mach 3 hot structure as such is "inside" the regression. The only stealth fighter in the set sits about 20% above it, hence K_we = 1.2 as the pessimistic case. The SR-71 sits 5–8% below. A slender, purpose-built Mach 3 airframe without fighter g-loads can beat the fit.
- **Fuel fraction.** The concepts need Wf/W0 of 0.33–0.38, the same as the MiG-25/31 (0.38–0.39) and well above the F-22 (0.28). A Mach 3 LO fighter therefore needs an interceptor-class fuel fraction and an F-22-class empty fraction at the same time. MiG-25-like values (0.545 + 0.384 = 0.93 of W0) leave only 7% for crew and payload, and F-22-like values (0.68 + 0.38 > 1.0) cannot both be met. **This is the arithmetic behind the sizing cliff.**
- **Inverse checks** (reference aircraft weights flown through this mission model; radius solved so that required fuel equals internal fuel):
  - F-22 on Profile B with the P1 engine model: **527–544 km** radius (0–185 km supercruise each way).
  - MiG-31 (W0 41 t, 16.1 t fuel, 2.85 t payload) out and back at M2.35, using an LBPTF with TR 1.96: **830 km**. Its cruise point is 19.75 km at L/D 5.36 and c = 1.94/h.
  - Against commonly quoted but unverified figures (F-22 ≈ 760 km class; MiG-31 ≈ 720 km at M2.35), the model is about 30% conservative for subsonic/supercruise missions. The likely causes are the Mattingly installed TSFC (1.0–1.2 vs Raymer 0.8), reserves and combat allowance. It is about 15% optimistic at M2.35, likely because the lapse fit has no ram-drag term and the L/D is optimistic.
- **SR-71 Breguet consistency.** Cruise at M3.2/24 km, starting from the end of a Raymer climb (56.4 t) and ending at 33.7 t, gives 5,100–6,850 km for L/D 5.5–6.6 and c = 1.7–1.9/h. The published unrefuelled range of about 2,900–3,200 nmi (5,400–5,900 km; unverified) falls inside this bracket, which supports the high-Mach Breguet and TSFC assumptions.

### Gaps
- These inputs were not verified: MiG-31 empty weight and wing area, MiG-25 wing area and span, F-22 internal fuel and wing area, SR-71 dry thrust, and all published combat radii and ranges. Several sources conflict on the MiG-25 (36.7 vs 41.2 t) and the SR-71 (empty 59,000 vs 67,500 lb). The ratios above move by ±0.02–0.05 accordingly.
- No public time-limit or endurance data at Mach 2.83 was found for the MiG-25/31 (sibling notes).

## Q6. What the numbers imply: design drivers, infeasible combinations and the trade-offs that matter most

### Takeaway
Thrust at Mach 3 is not the problem; with a high-throttle-ratio turbojet / turbo-ramjet it is plentiful. The problem is **weight closure**. Five combinations are infeasible, and the most effective relaxations are listed after them.

**Infeasible combinations**
1. Mach 3 with an F119-class turbofan: the thrust lapse falls to zero.
2. Sustained 5 g at Mach 0.9 / 9 km together with efficient Mach 3 cruise: this forces W/S ≈ 2,300 N/m² and T/W > 1.
3. An F-22-level empty-weight penalty together with a 500 km Mach 3 radius: this does not close.
4. Twin existing engines for the 5 g interceptor: about 221 kN per engine is needed.
5. Low-emissivity IR treatment at Mach 3: the skin still emits about 500× subsonic MWIR.

**Most effective relaxations**, ranked by ΔW0 on the interceptor:
1. Sustained turn 5 g → 4 g: −48%.
2. Mach 3 dash-only instead of Mach 3 cruise: −42%.
3. Hold the empty-weight penalty to ≤ 5%: each +0.1 in K_we roughly doubles W0.
4. Cut the Mach 3 radius 500 → 300 km: −37%.
5. Improve supersonic TSFC or L/D by about 10–15%: −13 to −18%.

### Cited Findings
- Sibling propulsion analysis concludes that a Mach 3 stealth fighter sits outside every production engine's design space. Engines that sustained Mach 2.8+ trade OPR and weight for high-Tt2 tolerance, while fifth-generation engines are optimised for Mach 0.8–2. — [Wikipedia R-15](https://en.wikipedia.org/wiki/Tumansky_R-15); [Wikipedia D-30](https://en.wikipedia.org/wiki/Soloviev_D-30) (via sibling note `propulsion_fuel.md`)
- At Mach 3+ the J58's turbomachinery supplied only about 17% of thrust; the inlet supplied 54% and the ejector 29%. — [Enginehistory.org](https://enginehistory.org/Convention/2013/SR-71Propul/SR-71Propul.shtml)
- The MiG-25's steel structure "necessitated its large wings", and its airframe was about 80% steel. — [migflug](https://migflug.com/aircraft/mig-25-foxbat/) (via sibling note)

### Inferences
**Main design drivers** [Calc, from Q3/Q4]:
1. **Subsonic sustained-turn requirement (5 g at M0.9 / 9 km).** It sets T/W ≈ 1.0–1.5 and W/S ≈ 2,200–2,300 N/m², which is well below the F-22's 3,642 N/m². This gives a wing of about 110–190 m², with matching RCS area, wetted area and structural weight. It also pushes best-L/D Mach 3 cruise above 25 km. Relaxing to 4 g moves the design to W/S ≈ 3,600 N/m² and T/W ≈ 0.95, and roughly halves W0 (43.5 → 22.6 t for A; 35 → 18.8 t for B).
2. **Mach 3 time and distance.** Climbing and accelerating to Mach 3 costs 12% of TOGW by the Raymer fit (10% by the energy method), and 35% of mission fuel. A 500 km Mach 3 radius doubles W0 compared with 200 km. W0 grows non-linearly beyond about 600 km, and nothing closes beyond about 800 km even at K = 1.0.
3. **Empty-weight penalty for LO plus hot structure** (K_we). The concepts sit where dW0/dK ≈ 2–6 t per 0.01 (A: 3.9 t per 0.01 from K 1.00 to 1.05, then 5.8 t; A-dash: 1.9 t). At K = 1.1, Profile A goes from 43 t to 92 t; at K = 1.2 nothing practical closes. Whether the team can design a hot (250–350 °C), RAM-treated titanium/polyimide structure at no more than the MiG-25/31's statistical weight is the single most important feasibility question.
4. **Propulsion cycle.** A conventional low-bypass turbofan cannot do Mach 3; the Mattingly lapse is zero above about M2.2 at TR 1.07. A high-TR turbojet or turbo-ramjet can, but it costs about 18% higher subsonic TSFC (1.19 vs 1.01) and adds weight. That penalises Profile B: 35.0 t with P2 vs 22.1 t with the F119-class P1 engine and no Mach 3 (+58%).

**Infeasible or very poor combinations (study-level)**
- **Mach 3 + conventional (F119-class) turbofan:** infeasible (α → 0).
- **5 g sustained at M0.9/9 km + 500 km Mach 3 radius + any LO weight penalty ≥ 10%:** W0 > 90 t, i.e. not a fighter.
- **F-22-like empty fraction (≈ 0.68) + interceptor fuel fraction (≈ 0.38):** the sum exceeds 1, so no closure at any size.
- **Single engine for the baseline 5 g interceptor:** 442 kN needed, against about 150–190 kN for the largest fighter engines. A twin layout at baseline needs about 221 kN per engine, which no existing engine provides. With the 4 g + dash-only requirement set, the total drops to about 150 kN, so a single J58/F119-class engine becomes conceivable. Single-engine fighters raise survivability and engine-out issues, which have not been analysed.
- **IR stealth at Mach 3:** even ε = 0.3 leaves about 500× the subsonic MWIR skin exitance and raises skin temperature by about 30 K. Low ε and Mach 3 heat rejection pull in opposite directions.

**Trade-offs ranked by effect on TOGW** (interceptor baseline 43.5 t):

| Trade | Effect |
|---|---|
| Sustained turn 5 g → 4 g | −48% (22.6 t); also enables single-engine thrust class for A-dash |
| Mach 3 cruise-out (500 km) → Mach 3 dash 100 km only | −42% (25.2 t); thermal soak still reached (τ ≈ 40–56 s) |
| Mach 3 radius 500 → 300 km | −37% |
| Better subsonic maneuver aero (K1 0.18 → 0.14) | −37% |
| Energy-method climb (better climb schedule, high T/W) | −24% (model uncertainty and an opportunity) |
| TSFC −10% (variable-cycle or TBCC engine) | −17% |
| Cruise ceiling 25 → 28 km | −15% (needs pressure-suit / cabin and engine relight design at 28 km) |
| Supersonic L/D +8% (C_D0 −15%) | −13% |
| Payload 900 → 700 kg | −5% |
| **K_we +0.1 (LO / RAM / hot-structure penalty)** | **+110% (doubles W0)** |

**Recommended framing for the team's next step**, as inference:
- Fix the requirement hierarchy first. The numbers favour a **"Mach 3 dash, Mach 1.6+ supercruise, ≤ 4 g sustained at M0.9/9 km"** concept. It sizes at **≈ 16–19 t (K = 1.0) or ≈ 28–34 t (K = 1.1)** for the dash-only interceptor (A-dash) and the strike mission (B), with S ≈ 44–51 m² and about 150–175 kN of total thrust at K = 1.0. The full Mach 3 cruise interceptor (A) is 22.6 t and 210 kN.
- Treat **K_we (structure + LO mass)** and the **Mach 3 engine cycle** (TR, subsonic TSFC, engine T/W) as the two quantities to estimate bottom-up next.
- Replace the Mattingly fits with a cycle deck (for example pyCycle) and the Raymer climb fit with energy-state integration.

### Gaps
- Not analysed: RCS consequences of the large low-W/S wing, inlet design (a fixed-geometry LO inlet at Mach 3 vs a variable spike), fuel heat-sink capacity, and the volume available for 8–17 t of internal fuel plus internal bays. Each could invalidate the closure.
- The "Mach 3 dash only" thermal benefit is limited to thick structure, fuel and avionics. A transient thermal model of the structure is needed to quantify the benefit.
- All conclusions inherit the unverified Raymer Table 6.1 and Mattingly lapse/TSFC coefficients (Q1 Gaps). The structure of the conclusions (drivers, cliffs, rankings) is robust to them. Individual tonnages are not, and should be quoted as ±25–30%.
