# Aerodynamics and Configuration Design of a Mach 3, Low-Observable, Single-Seat Fighter

> **Research-conditions note for the report writer:** In this session, direct page retrieval (WebFetch) failed for every host tried (ntrs.nasa.gov, enginehistory.org, archive.aoe.vt.edu, en.wikipedia.org, pdas.com), all with DNS "ENOTFOUND", meaning they were outside the session's allowed network domains. The shared web-search budget then ran out (limit 200 per turn). So every "Cited Findings" item below rests on search-result abstracts and snippets of the linked page, not on a full read of the primary PDF. Items marked *(snippet)* or *(attribution uncertain)* should be checked against the PDF before anyone quotes them in a deliverable. **Textbook equations I could not check against a source this session are not mixed into the cited findings. They are in the "Gaps" sub-sections, labelled "unverified-in-session", with a confidence note.** Numbers in "Inferences" are my own calculations (Python script, γ = 1.4, standard compressible-flow relations) built on the cited equations.

---

## Q1. Supersonic aerodynamics essentials for conceptual design (wave drag, drag build-up, lift-curve slope, drag due to lift, (L/D)max, aerodynamic-center shift)

### Takeaway
At Mach 3 the configuration is driven by four things: **volume wave drag**, set by how smooth the longitudinal area distribution is (the Sears–Haack/area-rule logic); **lift-dependent wave drag**, set by lifting length and span; the near-total **loss of leading-edge suction** once the leading edge is supersonic; and a large **aft shift of the aerodynamic center**, which the design must absorb through CG management, forebody lift (chines) or trim surfaces. Real Mach 2–3 aircraft reach (L/D)max of only about 6.5–7.5 (A-12/SR-71 family about 6.6; Concorde about 7.4).

### Cited Findings
**Wave drag / area rule**
- The Sears–Haack body is the shape with the lowest theoretical wave drag for a given length and volume. Its derivation holds only in the slender-body limit and starts from the Prandtl–Glauert / Ackeret small-disturbance equations. Primary sources are Sears (1947, *Quarterly of Applied Mathematics*, "On projectiles of minimum wave drag") and Haack (1941). — [Wikipedia: Sears–Haack body](https://en.wikipedia.org/wiki/Sears%E2%80%93Haack_body) *(snippet)*
- An aircraft whose longitudinal cross-sectional area distribution matches a Sears–Haack body has about the same wave drag as that body, largely independent of the actual shape. The Sears–Haack shape is not the theoretical optimum for a lifting aircraft. The area rule calls for reducing body volume where wings, tails or other projections add area, so the total area distribution has no discontinuities. — [Wikipedia: Area rule](https://en.wikipedia.org/wiki/Area_rule) *(snippet)*; [Cal Poly thesis via search](https://digitalcommons.calpoly.edu/theses/1435)
- **Supersonic area rule (Harris method):** NASA TM X-947, "An Analysis and Correlation of Aircraft Wave Drag" (Roy V. Harris Jr., NASA Langley, March 1964), slices the configuration with parallel cutting planes into a set of equivalent bodies of revolution. The method is approximate but usually captures most of the wave drag. (From general knowledge, not the snippet: the planes are inclined at the Mach angle, and the result is averaged over roll angle.) — [PDAS copy of TM X-947](https://www.pdas.com/refs/tmx947.pdf); [PDAS wave-drag bibliography](https://www.pdas.com/wavedragrefs.html)
- Jones introduced the supersonic area rule in 1956. Harris's 1963 Boeing-written program made it practical for general configurations. — [Jumper, USAFA/DTIC ADA128248](https://apps.dtic.mil/sti/pdfs/ADA128248.pdf)
- Harris's NASA TN D-3586 (1966) extends the wave-drag analysis to **lifting** conditions. It relates wave drag to the second derivative of the equivalent-body area distribution, with the area adjusted for lift. — [NTRS 19660029117](https://ntrs.nasa.gov/citations/19660029117); [NTRS scan 19750065533](https://ntrs.nasa.gov/api/citations/19750065533/downloads/19750065533.pdf)

**Lift-curve slope and aerodynamic center**
- Linearized (Ackeret) supersonic thin-airfoil theory gives section lift **C_l = 4α/√(M² − 1)** (α in radians), with the aerodynamic center ("focus") at **mid-chord**. — [Univ. of Texas, Fitzpatrick fluid-mechanics notes §](https://farside.ph.utexas.edu/teaching/336L/Fluid/node212.html)
- For diamond airfoils, the center of pressure approaches 50% chord as M → 1. In thicker airfoils it moves forward as supersonic Mach number rises, so 50% chord is a thin-airfoil linear-theory result. — [NACA/NASA report on diamond airfoils, NTRS 19930081950](https://ntrs.nasa.gov/api/citations/19930081950/downloads/19930081950.pdf) *(attribution uncertain: the finding came from a search summary covering several NTRS records)*
- Exact (non-linearized) analysis of finite-thickness symmetric airfoils shows that leading-edge shocks can reverse the sign of the lift-curve slope at Mach numbers just above 1.0. The 4/√(M²−1) formula is therefore unreliable near M = 1. — [Li, Caltech thesis 1947](https://thesis.caltech.edu/17692)

**Drag due to lift and leading-edge suction**
- Approximate supersonic measurements of the induced-drag factor K suggest that **virtually all leading-edge suction on the wing is lost beyond M = 1.0**. — [Cranfield AERADE report](https://aerade.cranfield.ac.uk/handle/1826.2/4005) *(snippet)*
- Sharp leading edges give poor drag-due-to-lift at subsonic speeds. Suction depends on leading-edge radius and Reynolds number. Wings with leading-edge radii show **about 90% suction at M < 0.3 when the Reynolds number based on leading-edge radius exceeds 20,000**. — NASA report in search results for "supersonic drag due to lift" (e.g. [NTRS 19930081984](https://ntrs.nasa.gov/api/citations/19930081984/downloads/19930081984.pdf)) *(attribution uncertain)*
- For supersonic thin triangular wings, a leading-edge suction force exists, but the incompressible suction formula needs a compressibility correction. — NACA work by Brown, in the same search results *(attribution uncertain)*
- NASA TP-3202 (1992) surveys research on minimizing supersonic drag-due-to-lift and assesses current design and analysis methods. It is the recommended entry point for supersonic drag-due-to-lift methods. — [NTRS 19920024412](https://ntrs.nasa.gov/api/citations/19920024412/downloads/19920024412.pdf) *(record-to-ID mapping likely but not confirmed)*

**(L/D)max of real supersonic aircraft**
- Concorde's maximum L/D was **7.4**; the A-12 family (which includes the SR-71) reached **6.6**. — [W.H. Mason, Virginia Tech supersonic aerodynamics presentation](https://archive.aoe.vt.edu/mason/Mason_f/SupersonicPres.pdf) *(snippet)*
- Concorde's L/D was about **7 at Mach 2**, against about 17 for a 747 at M 0.85. The L/D of most supersonic aircraft falls with Mach number, and Concorde was relatively good at holding L/D through the supersonic range. — [Wikipedia: Lift-to-drag ratio](https://en.wikipedia.org/wiki/Lift-to-drag_ratio) *(snippet)*
- XB-70 flight-measured lift, drag and angle of attack, with drag polars, lift-curve slopes and **maximum L/D**, were reported for M = 0.72–3.07 at about 7,620–21,340 m (25,000–70,000 ft) in NASA TM X-3532 (Arnaiz, 1977). The numeric values could not be retrieved. — [NTRS 19770017156](https://ntrs.nasa.gov/api/citations/19770017156/downloads/19770017156.pdf) *(abstract only)*
- A companion NASA study compares predictions from a 0.03-scale XB-70 wind-tunnel model, built to the **aeroelastically deformed Mach 2.5 cruise shape**, against flight data at 14 conditions from M 0.76 to 2.56. — [NTRS 19800009724](https://ntrs.nasa.gov/citations/19800009724)
- It may be correct that the XB-70 had the highest L/D of any *supersonic* manned aircraft. The broader claim of the highest L/D of any manned aircraft is popular belief. — [Wikipedia-derived XB-70 article](https://wikipedia2006.classicistranieri.com/en/x/b/-/XB-70_Valkyrie_677d.html) *(secondary)*

**Aerodynamic-center shift and trim**
- On the SR-71, the chines' lift rises with roughly the **square of the Mach number**, which offsets the rearward supersonic shift of the main wing's lift. — [Wikipedia: Chine (aeronautics)](https://en.wikipedia.org/wiki/Chine_(aeronautics))
- A declassified CIA document on A-12/SR-71 flight characteristics says the chines provide lift and **remove the need for canards or special nose-up trim devices at supersonic speed**. It also says **fuel-tank sequencing moves the CG aft during acceleration** to follow the aft movement of the center of lift with Mach. — [CIA Reading Room, "Flight characteristics"](https://www.cia.gov/readingroom/docs/flight%20characteristics%5B15271431%5D.pdf)

### Inferences
- **Lift-curve slope collapse with Mach** (from C_l = 4α/β, β = √(M²−1), my calculation):

  | M | β | 4/β (per rad) | per deg | 2-D flat-plate K = β/4 (no suction) |
  |---|---|---|---|---|
  | 1.5 | 1.118 | 3.58 | 0.0624 | 0.280 |
  | 2.0 | 1.732 | 2.31 | 0.0403 | 0.433 |
  | 2.5 | 2.291 | 1.75 | 0.0305 | 0.573 |
  | 3.0 | 2.828 | 1.41 | 0.0247 | 0.707 |
  | 3.2 | 3.040 | 1.32 | 0.0230 | 0.760 |

  With zero leading-edge suction (the Cranfield finding), drag due to lift is C_D,L = C_L·α = C_L²/C_Lα, so K = 1/C_Lα. At Mach 3, K is about 0.7 for a 2-D flat plate, versus about 0.1–0.2 for a subsonic fighter wing. That is why cruise C_L and lifting length dominate Mach 3 range and turn performance.
- **Bounding (L/D)max at Mach 3** with (L/D)max = 1/(2√(K·C_D0)) and the 2-D K = β/4: C_D0 = 0.010 gives (L/D)max ≈ 5.95; 0.015 gives 4.85; 0.020 gives 4.2. At Mach 2: 0.010 gives 7.6; 0.020 gives 5.4. The sourced A-12/SR-71 value of 6.6 implies C_D0 around 0.008 combined with this K, or a K well below β/4 from forebody/chine lift and a slender layout. Expect **(L/D)max ≈ 4–5.5 at M 3** for a stealth fighter with internal weapons, carried as a conceptual-design planning range.
- **Ideal lower bound on drag due to lift** (R.T. Jones far-field result; equation is in Gaps): for a notional fighter with S = 75 m², span 13 m and lifting length 20 m, K_min ≈ 0.18 (M 1.5), 0.23 (M 2), 0.30 (M 2.5), 0.38 (M 3). The β² S/(2π l²) term dominates at Mach 3, so a **long lifting length (chines/LEX/forebody lift running far forward)** is worth more than span at Mach 3.
- **Aerodynamic-center shift:** subsonic aerodynamic center ≈ 25% MAC versus thin-airfoil supersonic ≈ 50% chord, a theoretical shift of up to about 25% MAC. Low-aspect-ratio deltas show less in practice. A relaxed-stability fighter that is neutral subsonically could become strongly stable at Mach 3, with large trim drag. SR-71-style mitigations: **forebody chine lift (∝ M²) plus aft fuel transfer**.

### Gaps
- **Measured XB-70 (L/D)max vs Mach, C_D0(M) and C_Lα(M):** in NASA TM X-3532, but the PDF could not be retrieved. Popular figures (e.g. "L/D ≈ 7.2 at M 2.5") could not be verified.
- **MiG-25 (L/D)max at Mach 2.5–2.8:** no open source found this session.
- **SR-71 cruise L/D at Mach 3.2:** only the A-12-family maximum of 6.6 was found.
- **Unverified-in-session textbook relations** (high confidence; check against Raymer *Aircraft Design: A Conceptual Approach*, Ch. 12 and Nicolai & Carichner before use):
  - Sears–Haack volume wave drag: **D/q = (9π/2)(A_max/l)² = 128 V²/(π l⁴)**. I checked numerically that the two forms are consistent using V = (3π/16)·A_max·l. The search tool's background suggestion of "(9π²/2)·ρV²·(A²/L²)" is wrongly normalized; do not use it.
  - Raymer's empirical wave drag: (D/q)_wave = E_WD·[1 − 0.386(M − 1.2)^0.57·(1 − π·Λ_LE^0.77/100)]·(D/q)_Sears-Haack, with E_WD ≈ 1.2 for very clean supersonic designs and about 1.8–3 for typical fighters (E_WD values are memory-based and less certain).
  - Component drag build-up: C_D0 = Σ(C_f·FF·Q·S_wet)/S_ref + C_D,misc + C_D,L&P + C_D,wave. Turbulent flat-plate C_f = 0.455/[(log₁₀Re)^2.58·(1 + 0.144M²)^0.65]. Equivalent skin-friction C_fe ≈ 0.0035 (USAF fighter), 0.0040 (Navy fighter), 0.0025 (clean supersonic cruise aircraft).
  - Subsonic lift-curve slope (DATCOM/Helmbold form): C_Lα = 2πA / {2 + √[4 + (A²β²/η²)(1 + tan²Λ_t,max/β²)]}·(S_exp/S_ref)·F, where β² = 1 − M². Supersonic, supersonic leading edge: C_Lα ≈ 4/β (3-D corrections from DATCOM charts).
  - Supersonic K with no suction (Raymer): K = A(M² − 1)cosΛ_LE / (4A√(M² − 1) − 2), valid for supersonic leading edges only. For A = 2.36, Λ_LE = 42°: K ≈ 0.37 (M 2) and 0.57 (M 3) (my calculation).
  - Jones minimum drag due to lift: C_D,L,min = C_L²·S·[1/(π b²) + β²/(2π l²)] (NACA Report 1284 lineage).
  - Küchemann empirical (L/D)max ≈ 4(M + 3)/M, giving 10 at M 2 and 8 at M 3, an upper envelope that real aircraft fall below.

---

## Q2. Configuration options and trade-offs (delta, cranked arrow, trapezoidal, chined forebody, twin canted tails vs tailless; sweep vs Mach angle; stealth planform alignment)

### Takeaway
Mach 3 pushes toward **highly swept (≥70° to keep a subsonic leading edge), slender, long configurations with forebody lift**. Fighter agility and stealth push toward **moderate-sweep (about 40–50°) trapezoidal wings with aligned edges** (F-22: 42° LE, −17° TE). No real aircraft has achieved both. Any credible concept is a compromise, likely a **chined, blended, cranked/trapezoidal planform with LE sweep around 50–65°, edge-aligned to a few angles**, accepting a supersonic leading edge at Mach 3 and relying on thin sections, conical camber and forebody lift.

### Cited Findings
- **F-22 planform:** LE sweep **42°**, TE sweep **−17°** (forward-swept), quarter-chord sweep **30.9°**. — [Virginia Tech student F-22 presentations (Mason course)](https://archive.aoe.vt.edu/mason/Mason_f/F22Spr09.pdf); [F22Spr11](https://archive.aoe.vt.edu/mason/Mason_f/F22Spr11.pdf) *(student work, snippets)*
- The production F-22 wing's LE sweep was **reduced from 48° (YF-22) to 42°**. — same VT search results *(snippet; source deck not pinned down)*
- F-22: **AR 2.357**, wing area **840 ft²**, span **44.5 ft**, W/S **71.43** (lb/ft²). Another VT deck gives AR 2.1. — [VT F22S05](https://archive.aoe.vt.edu/mason/Mason_f/F22S05.pdf) *(student work)*; conflicting AR in [F22S06](https://archive.aoe.vt.edu/mason/Mason_f/F22S06.pdf)
- **SR-71 chined forebody:** the chines run about 40% of the aircraft length and give useful extra lift at supersonic speed. Lift rises with M², offsetting the aft wing-lift shift, and directional stability improves with angle of attack. — [Wikipedia: Chine (aeronautics)](https://en.wikipedia.org/wiki/Chine_(aeronautics))
- SR-71 forebody/chine lift is about **17–20% of total lift** (a figure attributed to AIAA 2008-6228). TWZ says the side-fairings produced **almost 20%**. — [Wikipedia: Chine](https://en.wikipedia.org/wiki/Chine_(aeronautics)) *(snippet partly garbled)*; [The War Zone](https://www.twz.com/sr-71-blackbirds-predecessor-looked-even-more-sinister-with-canards)
- Chines removed the need for canards or special supersonic nose-up trim devices on the A-12/SR-71. — [CIA Reading Room](https://www.cia.gov/readingroom/docs/flight%20characteristics%5B15271431%5D.pdf)
- **XB-70 folding wingtips:** about **25° droop subsonic**, folded to **65° above roughly Mach 1.4**. The fold restored the directional stability a slender delta loses at high Mach, added side area aft of the CG, and trapped shock pressure under the wing (compression lift). — [MiGFlug XB-70 page](https://migflug.com/aircraft/xb-70-valkyrie/) *(single secondary source)*

### Inferences
- **Mach angle and the "subsonic leading edge" rule** (μ = arcsin 1/M; the leading edge is subsonic while Λ_LE > 90° − μ, i.e. it becomes sonic at M = 1/cos Λ_LE; my calculation):

  | M | μ (deg) | Λ_LE needed for subsonic LE |
  |---|---|---|
  | 1.5 | 41.8 | > 48.2° |
  | 2.0 | 30.0 | > 60.0° |
  | 2.5 | 23.6 | > 66.4° |
  | 2.83 (MiG-25 limit) | 20.7 | > 69.3° |
  | 3.0 | **19.47** | **> 70.5°** |
  | 3.2 | 18.2 | > 71.8° |

  Sweep at which the LE goes sonic: 42° → M 1.35 (F-22); 48° → M 1.49 (YF-22); 55° → M 1.74; 60° → M 2.0; 65.6° → M 2.42 (approximately the XB-70 wing); 70° → M 2.92; 72° → M 3.24.
  **Implication:** a 42°-sweep F-22-style wing has a supersonic leading edge above about M 1.35 and loses LE suction entirely at Mach 3. Keeping the LE subsonic at Mach 3 needs **≥ 71–72° sweep**, which badly hurts low-speed C_Lα, landing attitude and sustained subsonic turn. **Recommended trade study:** compare a cranked arrow (inboard ≈ 70–75°, outboard ≈ 50–60°) with a 55–60° trapezoid using thin (t/c ≈ 3–4%) sections. The cranked arrow suits supersonic L/D; the trapezoid suits agility and RCS edge alignment.
- **F-22 geometry cross-check:** b²/S = 44.5²/840 = 2.357, consistent with the VT AR of 2.357, so the 2.1 figure is probably an error or uses a different reference area. In SI: S = 78.0 m², b = 13.56 m, W/S 71.4 lb/ft² ≈ 349 kg/m².
- **Twin canted tails vs tailless at Mach 3:** directional stability C_nβ from vertical surfaces falls roughly as their C_Lα (∝ 1/β), so at Mach 3 a fin is about 0.61× as effective as at Mach 2 (1.41/2.31). This explains the XB-70's tip fold and the SR-71's large canted, all-moving fins. A tailless design (B-2/X-47 style) would need very strong yaw control at Mach 3 (split drag rudders, differential thrust or yaw TVC). That is a high-risk choice at Mach 3, so **canted twin tails (or folding/canted outer panels) are the lower-risk baseline**.
- **Stealth planform alignment** (general LO practice, not verified this session; see Gaps): it limits the design to a few edge orientations, with LE, TE, tail edges, inlet lips and panel lines parallel to each other, which constrains crank and sweep choices. The design sweep must be picked jointly for RCS spike placement, Mach 3 drag and high-alpha lift.

### Gaps
- **Stealth planform-alignment rules** (edge alignment to a small number of angles, sawtooth panel edges, canted tails about 27° on the F-22): the search budget ran out before these could be sourced. They are widely described in open LO literature (e.g. Knott, *Radar Cross Section*) but **unverified in this session**.
- **SR-71 / XB-70 planform numbers** (SR-71 wing LE sweep; XB-70 wing LE sweep ≈ 65.57° and wing area 6,297 ft² from memory): **unverified in this session**.
- The **cranked-arrow fighter** literature (F-16XL, NASA supersonic-cruise fighter studies) was not retrieved. NASA's F-16XL program is the closest public data set for a cranked-arrow fighter (LE sweep 70° inboard / 50° outboard from memory, unverified).
- No public source was found that quantifies the RCS penalty of chines versus a conventional forebody. Chines are generally considered LO-friendly (the SR-71/A-12 used them partly for RCS), but this is unverified this session.

---

## Q3. Compression lift, waverider concepts (XB-70 folding wingtips) and blended wing-body

### Takeaway
Compression lift is real but modest and Mach-specific. Its claimed share of XB-70 lift (about 30–34%) comes only from popular sources and is **contested**. It moves (L/D)max to lower α and raises it, mainly at the design Mach number. For a fighter that must also manoeuvre subsonically, compression lift and waverider-like lower surfaces are best treated as a **secondary refinement of a blended, chined lower surface** with the inlets underneath, not as the main configuration driver.

### Cited Findings
- On the XB-70, compression lift shifts the lift curve and **moves the (L/D)max point to a lower angle of attack while raising its maximum value** (qualitative; no number in the snippet). — [Mason, VT XB-70 presentation](https://archive.aoe.vt.edu/mason/Mason_f/XB70PresS07.pdf) *(snippet)*
- Compression lift is still described as a **controversial theory as applied to the XB-70**. — [Wikipedia-derived XB-70 article](https://wikipedia2006.classicistranieri.com/en/x/b/-/XB-70_Valkyrie_677d.html)
- Popular sources claim compression lift made the XB-70 "30 percent more effective" or added "34%" lift. These figures **conflict and are not supported by NASA data** found this session. — search summary of [roadrunnersinternationale.com](https://m.roadrunnersinternationale.com/xb70story.html) and related pages *(low reliability)*
- The XB-70 tips folded to 65° above about M 1.4 to trap the shock under the wing, boost compression lift, cut drag and restore directional stability at Mach 3. — [MiGFlug](https://migflug.com/aircraft/xb-70-valkyrie/) *(secondary)*
- Flight history conflict: one NASA-related account says air vehicle 1 never exceeded **Mach 2.55** during NASA FRC research (1967–69). The **second aircraft first reached Mach 3 on 3 January 1966**. — search summary (NASM / NASA history pages) *(snippet)*

### Inferences
- **Mechanism for design:** at Mach 3 the inlet/fuselage shock under a flat or gently anhedral wing raises lower-surface pressure. Lift gained at fixed α means a lower cruise α, and so less drag due to lift (C_L·α). The pay-off depends on keeping the shock under the wing, which only happens near one design Mach number. Hence the XB-70's variable tip fold.
- **For a stealth fighter:** a **flat, chined, blended lower surface with the inlets underneath or at the chine** can use the forebody shock for both inlet pre-compression and compression lift. This matches F-22/YF-23 practice of shielding inlets with the forebody and suits LO (no right angles, smooth blending). The **blended wing-body** also helps the area distribution (Q1) and internal volume for weapons bays and fuel.
- **Waveriders** (lower surface built from a known shock field) give high L/D at one Mach number but poor low-speed and high-α behaviour. For a dogfighting-capable fighter, treat a waverider forebody as a "chine + flat underbody" approximation, not a pure waverider.

### Gaps
- **Quantified compression-lift fraction for the XB-70** from NASA flight data (TM X-3532 / the 1980 correlation study): not retrievable this session.
- **Waverider fighter studies** (Nonweiler caret waverider, NASA/USAF waverider-derived fighter concepts): the search budget ran out before any source was found. **Unsourced.**
- **Blended wing-body supersonic fighter data:** no specific open study retrieved.

---

## Q4. Inlets for Mach 3 (external vs mixed compression, MiG-25 2-D ramps, SR-71 spike, bleed/bypass, unstart, recovery, mass-flow matching, stealth compatibility)

### Takeaway
Above about Mach 2.2, **mixed compression** is the most efficient inlet type (YF-12/SR-71). It needs a translating centrebody or variable ramps, throat bleed, forward/aft bypass and an unstart-recovery control system. The MIL-E-5007 recovery standard falls from 0.925 (M 2) to 0.809 (M 3) and 0.783 (M 3.2). A fixed single-ramp or DSI inlet at Mach 3 would recover only about 0.45–0.55. **DSI is demonstrated only to about Mach 2**, so a Mach 3 LO fighter needs a **variable-geometry 2-D (caret/trapezoidal) mixed-compression inlet**, shielded under the forebody, with a serpentine duct and/or radar blocker. That is a major weight, volume and LO integration challenge.

### Cited Findings
**Recovery standard**
- Mil. Spec. inlet recovery: **p_t2/p_t0 = η_i·[1 − 0.075·(M − 1)^1.35] for M > 1**, and η_i·1 for M < 1. η_i covers boundary-layer and duct-separation losses. It is a good first estimate; real inlets may exceed it but usually fall short. — [NASA Glenn "Inlet Performance" page](https://www.grc.nasa.gov/WWW/BGH/inleth.html)
- The association of these nominal inlet requirements with **MIL-E-5007** is shown in a USPTO patent figure. — [USPTO patent 7334990](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7334990)

**SR-71 / YF-12 mixed-compression axisymmetric inlet**
- The SR-71 is the only operational aircraft to fly sustained cruise at **M = 3.2**, and inlet pressure recovery grows in importance with Mach. — [Anderson, Lockheed Martin, "How Supersonic Inlets Work" (2014)](https://enginehistory.org/Convention/2014/SR-71Inlts/SR-71Inlts.shtml) *(snippet)*
- NASA Ames (S. Brown, TM X-62,245) simulation of YF-12 supersonic-cruise dynamics: the **mixed-compression inlet is the most efficient type for Mach numbers above about 2.2**. Pressure recovery is defined as diffuser-exit total pressure over free-stream total pressure. — NTRS records [19730015310](https://ntrs.nasa.gov/citations/19730015310) / [19740030201](https://ntrs.nasa.gov/citations/19740030201) *(report-to-ID mapping uncertain)*
- NASA TN D-6987 (Johnson & Montoya, 1973) measured flow at the YF-12A spike tip from M 1.6–3.0. Impact-pressure ratio and mass-flow ratio rose with Mach above 2.2. AIAA 73-1314 (Burcham et al.) found inlet/engine compatibility good over most of the envelope to Mach 3.0. NASA TM X-56039 (1976) is a YF-12 propulsion research status report. — [NTRS 19760012064](https://ntrs.nasa.gov/citations/19760012064); [NASA Glenn YF-12 history](https://www.nasa.gov/centers-and-facilities/glenn/nasa-center-boosted-yf-12-supersonic-engine-research/)
- The SR-71 cone **translates aft at higher speeds**, because the required area ratio grows with Mach number. That is why it travels so far to cover low speed through Mach 3.2. — [Wikipedia: Inlet cone](https://en.wikipedia.org/wiki/Inlet_cone)
- **Thrust split at Mach 3.2:** **54% inlet** (pressure differential on spike/cowl), **17% engine**, **29% ejector**. — [enginehistory.org, "SR-71 Propulsion System" (2013)](https://enginehistory.org/Convention/2013/SR-71Propul/SR-71Propul.shtml). Another source gives 54% / 17.6% / 28.4% at Mach 3+ and **13% / 73% / 14% at Mach 2.2**. — [thesr71blackbird.com](https://www.thesr71blackbird.com/Aircraft/Engines/j58-the-powerplant-for-the-blackbirds). **Conflict:** a separate enginehistory thrust diagram gives about 70% (subsonic diffuser), about 17% engine and 27% ejector. — [enginehistory thrust diagram](https://enginehistory.org/members/images/SR-71/(2)J58Engine/sr71thrustdiagram.html)

**2-D variable-ramp inlets (Concorde, MiG-25)**
- Concorde's variable ramps angle the oblique shocks onto the lip, and a converging ramp is followed by a diverging one. Good recovery is credited up to about M 2.2. — [Wikipedia: Intake ramp](https://en.wikipedia.org/wiki/Intake_ramp)
- A **bleed slot** was considered essential to Concorde intake performance (cited in a NASA 2022 paper). Throat bleed weakens the terminal shock and improves recovery. — [Slater, NASA, ISABE 2022](https://ntrs.nasa.gov/api/citations/20220009243/downloads/Slater_ISABE_2022_Conf%20Paper-v4_Final.pdf); [USPTO 9334801](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9334801)
- **Modern benchmark:** a NASA CFD design of a Mach 2 external-compression inlet reached **about 95% total-pressure recovery with about 5% bleed**. — [Slater, ISABE 2022](https://ntrs.nasa.gov/api/citations/20220009243/downloads/Slater_ISABE_2022_Conf%20Paper-v4_Final.pdf)
- For Mach 2 flight, **variable-ramp external-compression inlets have been preferred over normal-shock inlets** on recovery grounds. — search summary of [ASU AIAA-2016-3463](https://labs.engineering.asu.edu/aircraft-design/wp-content/uploads/sites/115/2023/05/AIAA-2016-3463.pdf) *(snippet)*
- **MiG-25:** the intakes are **rectangular 2-D intakes** with a sharp leading edge raked steeply aft in side view. Wikipedia's intake-ramp article lists the MiG-25 as a 2-D intake example. A forum source says it used a **moveable wedge ramp inspired by the A-5 Vigilante**. — [Wikipedia: Intake ramp](https://en.wikipedia.org/wiki/Intake_ramp); [Scribd MiG-25 technical text](https://www.scribd.com/doc/244886200/MiG-25); [secretprojects forum](https://www.secretprojects.co.uk/threads/russian-aircraft-variable-geometry-inlet-use-cold-war-predominantly.4092/latest) *(weak)*. **Conflict:** the Wikipedia *Inlet cone* article lists the MiG-25 (and Concorde, F-15, A-5) as using a "simple fixed-geometry pitot intake". That is contradicted for Concorde by the *Intake ramp* article and is probably mis-worded. — [Wikipedia: Inlet cone](https://en.wikipedia.org/wiki/Inlet_cone)
- MiG-25 operational top speed was limited to **Mach 2.83**. It used twin **Tumansky R-15** turbojets (R-15BD-300 per a forum post), and a forum post mentions **water/methanol injection in the inlet** for added mass flow. — [Wikipedia: MiG-25](https://en.wikipedia.org/wiki/Mikoyan-Gurevich_MiG-25); forum claim weak

**DSI and caret inlets (stealth compatibility)**
- The DSI replaces the boundary-layer diverter with a compression "bump" that pushes the boundary layer aside. It first flew **11 December 1996 on a Block 30 F-16**, which reached **Mach 2.0**, then flew on the X-35 (2000) and F-35. — [Wikipedia: DSI](https://en.wikipedia.org/wiki/Diverterless_supersonic_inlet); [GlobalSecurity DSI](https://www.globalsecurity.org/military/systems/aircraft/dsi.htm)
- At speeds up to about Mach 2, the inlet shape alone can slow much of the supersonic flow before it enters. — [Air & Space, "How Things Work: Supersonic Inlets"](https://www.airspacemag.com/military-aviation/how-things-work-supersonic-inlets-35428453/)
- The F-35 is rated to **Mach 1.6** with a fixed-geometry inlet. Whether the DSI sets that limit is **not established** by authoritative sources (only forum claims). — [Wikipedia: DSI](https://en.wikipedia.org/wiki/Diverterless_supersonic_inlet)
- Patents describe **caret inlet systems** and an **extendible leading-edge slat on caret inlets** for off-design performance, showing variable-geometry caret inlets are an active concept. — [USPTO 9964038](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9964038); [USPTO 9874144](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9874144)

### Inferences
- **MIL-E-5007 recovery targets** (my calculation from the NASA Glenn formula), compared with a single normal shock:

  | M | MIL recovery | Normal-shock-only (pitot) recovery |
  |---|---|---|
  | 1.5 | 0.971 | 0.930 |
  | 2.0 | 0.925 | 0.721 |
  | 2.2 | 0.904 | 0.628 |
  | 2.5 | 0.870 | 0.499 |
  | 2.83 | 0.830 | 0.380 |
  | 3.0 | **0.809** | 0.328 |
  | 3.2 | 0.783 | 0.276 |

- **Why fixed or DSI inlets fail at Mach 3** (oblique + normal shock relations, my calculation): one 10° wedge plus terminal normal shock at M 3 gives total recovery ≈ **0.48** (wedge 0.963 × normal shock at M 2.5). A 15° wedge gives ≈ 0.54. Even four 6° external ramps (to M ≈ 1.96) plus a normal shock give only ≈ **0.72**, short of the 0.81 MIL target. Meeting MIL at Mach 3 needs **mixed compression**: further internal compression to a throat Mach number around 1.2–1.3 before a weak terminal shock (recovery ≈ 0.98–0.99), with throat bleed to stabilise the shock. This agrees with the sourced statement that mixed compression is most efficient above M ≈ 2.2.
- **Mass-flow matching:** capture area must be sized for the Mach 3 design point. At lower Mach, the excess inlet flow must be spilled (spillage drag) or bypassed. On the SR-71 the forward/aft bypass doors and translating spike do this. The thrust-split data (inlet 54% of net thrust at M 3.2 versus 13% at M 2.2) shows that **at Mach 3 the inlet is the dominant thrust and drag component**. The design team must model it (and its unstart transient) together with the engine from the start.
- **Unstart:** in a mixed-compression inlet, the terminal shock can be expelled forward when back-pressure or angle of attack changes. The result is a sudden loss of recovery and a large asymmetric yaw/roll moment on a twin-engine aircraft. Design consequences are a fast bleed/bypass control loop, adequate stability margin, and inlets placed (e.g. under a chined forebody) where local flow angles vary little with α and β.
- **Stealth integration:** a Mach 3 inlet adds moving ramps/spikes, bleed slots and bypass doors, all potential RCS sources. A practical LO approach is **2-D caret/trapezoidal inlets with edge-aligned, swept lips; ramp, bleed and bypass surfaces treated with RAM or aligned edges; a serpentine duct hiding the compressor face** (or a radar blocker if the duct cannot be long enough). The duct length also helps distortion recovery. Duct offset and blocker losses come straight off the 0.81 recovery budget.

### Gaps
- **Measured SR-71/YF-12 recovery at Mach 3.2:** a figure exists in the Anderson paper table and the NASA YF-12 reports, but could not be retrieved. Commonly quoted values of about 0.80–0.85 are **unverified this session**.
- **MiG-25 measured recovery and ramp schedule:** no authoritative open source found.
- **F-22 inlet type:** commonly described in open literature as fixed-geometry caret-type with bleed and bypass, but **not confirmed** this session (search found only S-duct references).
- **Serpentine-duct and radar-blocker recovery and distortion penalties** at supersonic flight: no source retrieved.
- **Inlet bleed/bypass fractions for a Mach 3 mixed-compression inlet:** not retrieved. The NASA Mach 2 study's ~5% is the only sourced bleed number.

---

## Q5. Nozzles (2-D thrust vectoring vs axisymmetric, ejector nozzles at Mach 3, nozzle/afterbody drag)

### Takeaway
At Mach 3 the nozzle/ejector system supplies a large share of net thrust (SR-71: about 28–29% from the ejector at M 3.2). Fighter agility and LO favour **2-D convergent-divergent vectoring nozzles** (F-22 F119: ±20° pitch, +50% roll rate, LO-friendly shaping). A Mach 3 fighter needs a nozzle with a **very high expansion ratio** at cruise, plus IR suppression and a smooth afterbody, which are conflicting requirements.

### Cited Findings
- The F119 **2-D C-D nozzle vectors thrust up to 20° up or down**. Nozzle position is integrated with the flight control system and run by the FADEC. — [Pratt & Whitney F119 product page](https://www.rtx.com/prattwhitney/products/military-engines/f119)
- F-22 vectoring **raises roll rate by 50%**, and the nozzle has features that support the stealth requirement. — [GlobalSecurity F-22 F119](https://www.globalsecurity.org/military/systems/aircraft/f-22-f119.htm)
- The YF119 was developed by P&W in the 1980s for the ATF, and the F119 was selected for the F-22 in **April 1991**. — [National Museum of the USAF](https://www.nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Display/Article/196077)
- **SR-71 ejector nozzle:** about **29% of net thrust at Mach 3.2** (17% engine, 54% inlet), against **14% at Mach 2.2**. — [enginehistory.org](https://enginehistory.org/Convention/2013/SR-71Propul/SR-71Propul.shtml); [thesr71blackbird.com](https://www.thesr71blackbird.com/Aircraft/Engines/j58-the-powerplant-for-the-blackbirds)
- **Base-pressure context:** in large-scale flight measurements on a wing-body from M 0.8–1.6, base pressure coefficients stayed near zero up to about M 1.2, then levelled off at about **−0.035** above M 1.2. — [NASA memo, NTRS 19930086620](https://ntrs.nasa.gov/api/citations/19930086620/downloads/19930086620.pdf) *(snippet)*

### Inferences
- **Ejector vs C-D:** an ejector or "blow-in-door" nozzle (J58-style) uses secondary (bypass/cooling) air to fill the base and fit the large exit area needed at Mach 3, while keeping boat-tail drag low at lower Mach. A 2-D C-D vectoring nozzle (F119-style) gives agility and a lower-RCS, flatter plume but is heavier. At Mach 3 the required exit-to-throat area ratio is large, so the divergent flaps must open far, which affects afterbody shape and base drag. **Suggested trade:** a 2-D C-D nozzle with variable expansion flaps plus secondary-air cooling (for IR) versus an axisymmetric ejector, compared on installed thrust minus afterbody drag at M 0.9, 1.5 and 3.0.
- **Afterbody drag:** close-spaced twin 2-D nozzles with a flat "beavertail" between them (F-22-like) reduce interfairing base area and help the area rule. A gap or base area of a few percent of S_ref at C_p ≈ −0.035 to −0.1 adds measurable C_D0 (order 0.001 per 1% of S_ref per 0.1 ΔC_p; my estimate).
- **IR stealth at Mach 3:** at Mach 3, stagnation temperature (about 600 K at altitude, standard relation T_0 = T(1 + 0.2M²) ≈ 217 K × 2.8) heats the whole airframe. **Skin heating, not just the plume, becomes an IR signature driver.** Nozzle shielding by the tails or a beavertail helps only against plume and hot-part views.

### Gaps
- **Nozzle/afterbody drag data** for 2-D vs axisymmetric fighter nozzles (NASA Langley 16-ft transonic tunnel studies): not retrieved this session.
- **Mach 3 ejector geometry and J58 blow-in door schedule:** not retrieved.
- Expansion ratio for a Mach 3 turbojet or low-bypass turbofan nozzle (from memory, about 2.5–3.5 at full expansion): **unverified**.
- The ±20° vectoring range is quoted without the envelope (Mach or q limits) where it applies.

---

## Q6. Low-speed takeoff/landing, high-alpha manoeuvring (LEX, vortex lift) and control power across Mach 0.2–3

### Takeaway
Highly swept, low-aspect-ratio wings get usable low-speed lift from **leading-edge vortex lift** (Polhamus suction analogy), which LEX/strakes enhance and stabilise (F-16, F/A-18). Control power falls with Mach roughly as C_Lα (∝ 1/β), so surfaces sized for Mach 3 are often oversized subsonically. Large supersonic stability margins make supersonic trim and manoeuvre the sizing case. Thrust vectoring is the main lever to cover both ends.

### Cited Findings
- **Polhamus leading-edge suction analogy** (NASA TN D-3767, 1966): when flow separates at a sharp edge, the attached-flow leading-edge suction force is turned into a normal force. This predicts vortex lift on sharp-edged delta wings and later extended to side edges and wing-strake combinations. — [Luckring, "A career in vortices and edge forces", Aeronautical Journal](https://www.cambridge.org/core/journals/aeronautical-journal/article/career-in-vortices-and-edge-forces/9B97B48030742759901B6D53907662DC); [NTRS 19720025347](https://ntrs.nasa.gov/api/citations/19720025347/downloads/19720025347.pdf); [Luckring 2016, NTRS 20160010101](https://ntrs.nasa.gov/api/citations/20160010101/downloads/20160010101.pdf)
- Polhamus worked with industry to develop wing-root **strakes / leading-edge extensions** that enhance and strengthen beneficial vortex lift. — [NASA Langley biography of Edward C. Polhamus](https://www.nasa.gov/centers-and-facilities/langley/edward-c-polhamus)
- Strakes let flow separate at high α into strong leading-edge vortices. These produce **vortex lift** that rises rapidly at high α and is less prone to normal stall. The **F-16 and F-18** are cited examples. — [strake reference page](https://static-as-mhp.semcs.net/content/strake/658600) *(general reference, low authority)*
- **Thrust vectoring** on the F-22 gives +50% roll rate. — [GlobalSecurity](https://www.globalsecurity.org/military/systems/aircraft/f-22-f119.htm)
- Digital DATCOM **does not implement rudder** effectiveness and only covers longitudinal power and ground effects. Lateral-directional control power at high α must come from other methods or tests. — [Wikipedia: Digital DATCOM](https://en.wikipedia.org/wiki/United_States_Air_Force_Stability_and_Control_Digital_DATCOM)

### Inferences
- **Control effectiveness vs Mach:** a surface's lift effectiveness scales roughly with its C_Lα. Subsonic finite-wing values for low-AR fighter surfaces are about 0.05–0.06/deg. Linear-theory supersonic values are 0.040/deg (M 2) and 0.025/deg (M 3), so at Mach 3 a surface gives about **40–50% of its subsonic per-degree force**. Meanwhile the aerodynamic center moves aft (Q1), so required trim moments grow. **Mach 3 trim, 1-g and pull-up, and directional stability at Mach 3 are likely to size the horizontal and vertical surfaces.** The low-speed high-α case (nose-down recovery at α ≈ 30–60°) sizes pitch authority. TVC (±20°) eases both.
- **Takeoff and landing with Λ_LE ≥ 60°:** C_Lα is low, so landing C_L needs high α. Vortex lift helps, but tail-scrape and pilot-view geometry limit usable α (the Concorde and Tu-144 used drooping noses, the XB-70 a visor). For a fighter, **LEX/chine vortex lift plus TVC and a moderate (≈50–60°) outer-panel sweep** is the practical route to acceptable approach speeds. Flaps on swept trailing edges have reduced effectiveness.
- **Chines vs LEX:** an SR-71-style chine acts as a long, highly swept LEX. It gives vortex lift at high α, forebody lift at supersonic speed, and better high-α directional stability (sourced in Q2). For a Mach 3 stealth fighter, a **chine-LEX blend** serves agility, supersonic trim and LO together.

### Gaps
- **Quantitative vortex-lift data** (K_p, K_v coefficients for the Polhamus formula C_L = K_p sinα cos²α + K_v cosα sin²α): the equation is from memory (high confidence), and the K_p and K_v charts were not retrieved. **Unverified in this session.**
- **High-α data for F-22/F-16/F-18** (C_Lmax, α at C_Lmax, departure boundaries): not retrieved.
- **Takeoff/landing speeds and attitudes for the SR-71/XB-70/MiG-25:** not retrieved.
- **Control power requirements standards** (MIL-STD-1797 and its high-α pitch-down criteria): not retrieved this session.

---

## Q7. Representative numbers (C_D0 subsonic and supersonic; K vs Mach; wing loadings and aspect ratios)

### Takeaway
Reliable public **measured** C_D0 and K data for the F-15, F-16 and F-22 were **not found** this session. Only illustrative textbook-style values (C_D0 ≈ 0.018 subsonic) surfaced, and they are low-reliability. Usable anchors are the F-22 geometry (AR ≈ 2.36, S = 840 ft², W/S ≈ 66–80 lb/ft²), the A-12/SR-71 and Concorde (L/D)max (6.6 and 7.4), and theoretical K(M) bounds computed in Q1.

### Cited Findings
- **C_D0 for F-15 and F-16:** two homework-style sources list **C_D0 ≈ 0.018** subsonic for both. These are illustrative problem inputs, not measured data. — search summary (e.g. [Berkeley drag & performance notes](https://msol.berkeley.edu/wp-content/uploads/2020/10/Airplane-Drag-and-Performance-Analysis.pdf)) *(low reliability)*
- F-15 scale-model wind-tunnel tests showed that the **zero-lift pressure drag coefficient depends on both Reynolds number and Mach number**. — [DTIC AD0915551](https://apps.dtic.mil/sti/pdfs/AD0915551.pdf) *(snippet)*
- Zero-lift drag coefficient definition and role as a measure of parasitic "cleanliness". — [Wikipedia: Zero-lift drag coefficient](https://en.wikipedia.org/wiki/Zero-lift_drag_coefficient)
- **F-22:** AR 2.357, S 840 ft², b 44.5 ft, W/S 71.43 lb/ft² (VT student deck). Published values range from about **66 to about 80 lb/ft²** depending on the weight used. — [VT F22S05](https://archive.aoe.vt.edu/mason/Mason_f/F22S05.pdf); [F-16.net forum](https://www.f-16.net/forum/viewtopic.php?p=99942) *(weak)*
- **(L/D)max:** Concorde 7.4; A-12/SR-71 family 6.6 — [Mason VT](https://archive.aoe.vt.edu/mason/Mason_f/SupersonicPres.pdf). Concorde about 7 at M 2 — [Wikipedia L/D](https://en.wikipedia.org/wiki/Lift-to-drag_ratio)
- **SR-71 chine lift** ≈ 17–20% of total — [Wikipedia: Chine](https://en.wikipedia.org/wiki/Chine_(aeronautics))
- **MiG-25** operational limit Mach 2.83 — [Wikipedia: MiG-25](https://en.wikipedia.org/wiki/Mikoyan-Gurevich_MiG-25)

### Inferences
- **K vs Mach planning values** (computed; see Q1 table): theoretical no-suction 2-D K = β/4 gives 0.43 (M 2) and 0.71 (M 3). Raymer-type 3-D no-suction K for AR 2.36 with a 42° LE (formula unverified) gives 0.37 (M 2) and 0.57 (M 3). The Jones ideal bound for a notional 75 m², 13 m span, 20 m length layout gives 0.23 (M 2) and 0.38 (M 3). **Planning value for a Mach 3 stealth fighter: K ≈ 0.4–0.6 at M 3.** Subsonic K (with partial suction) is typically about 0.1–0.2 for AR 2–3 (memory-based; verify against Raymer's leading-edge-suction method).
- **C_D0 planning values** (memory-based, **unverified**; replace with the team's own component build-up): subsonic about 0.015–0.022 for clean fighters, with internal-carriage LO designs at the clean end; transonic peak about 0.035–0.05 near M 1.1–1.2; falling to about 0.025–0.035 at M 2. For a Mach 3 design, a supersonic C_D0 ≈ 0.015–0.022 at M 3 is needed to reach L/D ≈ 4.5–5 (from the Q1 L/D bound). **That requires an area-ruled, slender, low-E_WD design**, which conflicts with fighter-style volume for internal weapons.
- **SI conversions for F-22 anchors:** S = 78.0 m², b = 13.56 m, W/S ≈ 322–391 kg/m² (66–80 lb/ft²).

### Gaps
- **Measured C_D0(M) curves for the F-15, F-16 and F-22:** not found. Candidate open sources: NASA F-15 / F-16XL flight reports, Raymer worked examples, and Nicolai & Carichner's F-16-type examples. Search budget ran out before these could be found.
- **SR-71 C_D0 at Mach 3:** not found.
- **XB-70 C_D0 and K vs Mach** (NASA TM X-3532): not retrieved.
- **Typical wing loadings and ARs across fighters** (F-15 ≈ 66 lb/ft², AR ≈ 3.0; F-16 ≈ 88 lb/ft², AR ≈ 3.2; MiG-25 AR ≈ 3.2; all from memory): **unverified** this session.

---

## Q8. Methods and tools (Digital DATCOM, Raymer/Nicolai empirical methods, panel methods PANAIR/A502 and VSPAERO, OpenVSP wave drag, Euler/RANS CFD SU2/OpenFOAM, NASA Cart3D/FUN3D availability, wind-tunnel practice and campaign sizes)

### Takeaway
A two-person team can build a fully open toolchain in four layers. (1) **OpenVSP** for parametric geometry, with its built-in **area-rule wave-drag tool** (since v3.7.0, area distribution plus Eminton–Lord) and parasite-drag build-up. (2) **VSPAERO** for vortex-lattice analysis; only its VLM, not its panel solver, handles supersonic flow. (3) **Digital DATCOM** (public domain, unsupported) for stability derivatives, faired through the transonic regime. (4) **SU2 v8.x** (or OpenFOAM rhoCentralFoam) for Euler/RANS. NASA **FUN3D is US-release-only** and **Cart3D is Government-Purpose release / licence**, so neither is reliably available to private non-US-government users. Harris's wave-drag program (D2500) is public domain. For scale: the F-22 program logged about **43,900 wind-tunnel hours**.

### Cited Findings
**Geometry and wave drag**
- **OpenVSP 3.7.0** added "**Wave drag estimation by area distribution and Eminton Lord calculation**", described as long requested. — [OpenVSP blog, 3.7.0 release](https://openvsp.org/blogs/?p=435)
- A Cal Poly MS thesis (2015) built an interactive OpenVSP-based tool for **zero-lift wave drag**, using a method used in industry for decades. OpenVSP's quick geometry changes allow rapid design-space reanalysis. — [Cal Poly Digital Commons, thesis 1435](https://digitalcommons.calpoly.edu/theses/1435)
- **VSPAERO** is a thin-surface code for inviscid subsonic and supersonic aero. It has a **panel method and a VLM**, but **only the VLM can analyse supersonic flow**. — [ICAS 2022 paper 0858](https://www.icas.org/ICAS_ARCHIVE/ICAS2022/data/papers/ICAS2022_0858_paper.pdf); [OpenVSP 3.1.0 and VSPAERO release](https://openvsp.org/blogs/?p=321)
- **Harris wave-drag program** (TM X-947, 1964; lifting extension TN D-3586, 1966) is distributed as **D2500**, with public-domain source and a 1996 NASA-released copy included. — [PDAS flyer](https://www.pdas.com/flyer.pdf); [PDAS wavedrag page](https://www.pdas.com/wavedrag.html); [TM X-947](https://www.pdas.com/refs/tmx947.pdf)

**Empirical / handbook**
- **Digital DATCOM** implements Sections 4–7 of the USAF Stability and Control DATCOM for static stability, control and dynamic derivatives. It handles **subsonic and supersonic** analysis and has hypersonic control-effectiveness modules. — [Wikipedia: Digital DATCOM](https://en.wikipedia.org/wiki/United_States_Air_Force_Stability_and_Control_Digital_DATCOM); [PDAS Datcom description](https://pdas.com/datcomDescription.html)
- **Digital DATCOM limitations:** no rigorous transonic treatment (fair between subsonic and supersonic solutions); **rudder not implemented**; **inlets, external stores and protuberances cannot be modelled** (the fuselage is a simple body); power and ground effects are longitudinal only. The user manual warns against relying on its drag methods. It is **no longer supported by the USAF and is public domain**. — [Wikipedia: Digital DATCOM](https://en.wikipedia.org/wiki/United_States_Air_Force_Stability_and_Control_Digital_DATCOM); [DTIC ADA086557 user manual](https://apps.dtic.mil/sti/pdfs/ADA086557.pdf)
- MathWorks Aerospace Blockset includes a **Digital DATCOM Forces and Moments** block, which supports a DATCOM-to-6-DOF-simulation workflow. — [MathWorks documentation](https://www.mathworks.com/help/aeroblks/digitaldatcomforcesandmoments.html)

**CFD**
- **SU2 v8.0.0 "Harrier"** made **SST-2003m the default** turbulence model. Many features come with validation cases in the TestCases folder. Releases **v8.1.0, v8.2.0, v8.3.0** follow. — [CFD Online SU2 v8.0.0 announcement](https://cfd-online.com/Forums/su2-news-announcements/251634-su2-v8-0-0-out.html); [SU2 GitHub releases (mirror)](https://github-redirect.dependabot.com/su2code/SU2/releases)
- University of Calgary thesis: **verification and validation of rhoCentralFoam (OpenFOAM) and SU2 on supersonic test cases** for supersonic aircraft analysis. — [PRISM, U Calgary](https://prism.ucalgary.ca/handle/1880/113512)
- Cranfield study: SU2 on a **Mach 5** shock interaction case, with discrepancies growing at higher shock-generator angles. — [Cranfield CERES](https://dspace.lib.cranfield.ac.uk/handle/1826/18704)
- **FUN3D v14.2** is **U.S. Release Only**. Every v13-or-earlier user must re-apply for a Software Usage Agreement for v14. Cloud use of U.S.-only codes needs NASA approval. — [NASA Software Catalog LAR-20188-1](https://software.nasa.gov/software/LAR-20188-1); [FUN3D 2023 session slides](https://fun3d.larc.nasa.gov/session1_2023.pdf); [Rescale](https://rescale.com/?p=82366)
- **Cart3D** (ARC-14275-1) is a **U.S. Government Purpose Release**, also available under a **copyright licence**. A commercial derivative, **Cart3D Plus**, is sold on an annual licence. — [NASA Software Catalog ARC-14275-1](https://software.nasa.gov/software/ARC-14275-1); [SpaceWorks Cart3D Plus](https://www.spaceworks.aero/software/cart3d-plus/)

**Wind-tunnel practice**
- **F-22 program:** the EMD phase ran **76 wind-tunnel tests with 23 models in 15 tunnels, for 17,689 test hours**. YF-22 and F-22 work together totals **43,889 hours**. — [GlobalSecurity F-22 test](https://www.globalsecurity.org/military/systems/aircraft/f-22-test.htm)
- **NASA Langley Unitary Plan Wind Tunnel:** two **4 ft × 4 ft × 7 ft** test sections. **TS1 runs about M 1.5–2.9 and TS2 about M 2.3–4.6**, calibrated from M 1.47–4.63. A NASA document says almost every US fighter of the preceding 30 years was tested there. — [NASA AETC UPWT characteristics](https://www.nasa.gov/directorates/armd/aetc/4-foot-supersonic-unitary-plan-wind-tunnel-characteristics); [NTRS 20010021112](https://ntrs.nasa.gov/api/citations/20010021112/downloads/20010021112.pdf) *(snippet)*

### Inferences
- **Recommended open toolchain and fidelity ladder** for the team:
  1. **Sizing and constraint analysis** with Raymer/Nicolai empirical drag build-up plus the MIL inlet recovery formula, implemented in a script or spreadsheet.
  2. **OpenVSP parametric model**: CompGeom for S_wet and volume, Parasite Drag tool for C_D0 build-up, **Wave Drag tool** for area distribution and E_WD versus Sears–Haack at M 1.2–3.0. Iterate the area distribution here.
  3. **VSPAERO VLM** (subsonic and supersonic) for C_Lα, aerodynamic-center position, K and control derivatives versus Mach. Cross-check with **Digital DATCOM** (sub/supersonic), faired through M 0.9–1.2.
  4. **Harris D2500** as an independent wave-drag check.
  5. **SU2 Euler** for supersonic cruise (M 2–3.2), including the forebody/inlet shock structure and compression lift. Then **SU2 RANS (SST)** for drag, inlet ramp/bleed behaviour, high-α vortex flow and nozzle/afterbody. OpenFOAM rhoCentralFoam is the alternative.
  6. Optional: **PANAIR/A502** (linear higher-order panel, sub/supersonic) via PDAS, if VLM thin-surface modelling is not enough. Status unverified, see Gaps.
- **Wind-tunnel scale reference:** the F-22's ~44,000 hours is a full-program number for a production fighter. A student or academic campaign would be a few hundred hours at most, in a facility such as a university supersonic blow-down tunnel. CFD validation should lean on **public NASA data sets** (XB-70 TM X-3532 flight data at M 0.72–3.07; YF-12 inlet data; the Langley UPWT literature).
- **Export-control and availability note:** FUN3D is restricted to US persons and Cart3D to government purpose or licence. A non-US-government two-person team should plan around **SU2, OpenFOAM, OpenVSP/VSPAERO, Digital DATCOM and D2500**, which are all open or public domain.

### Gaps
- **PANAIR/A502** current distribution status (PDAS or NASA Software Catalog) and suitability: search budget ran out. PANAIR is commonly described as a higher-order linear panel code for subsonic and supersonic potential flow (Boeing for NASA, late 1970s–80s), but this is **unverified in this session**.
- **Current OpenVSP and VSPAERO versions as of October 2026**, and whether VSPAERO's supersonic VLM was improved after the ICAS 2022 assessment: not verified. Check openvsp.org before relying on version-specific features.
- **Current SU2 release** (later than v8.3.0?) **and FUN3D release** (later than v14.2?) as of October 2026: not verified.
- **NASA OpenVSP-integrated tools** (e.g. "VSP-wavedrag" accuracy against Harris D2500 or CFD): no accuracy study retrieved.
- **Typical wind-tunnel campaign sizes for other fighters** (F-15, F-16, YF-23), and typical model scales and Reynolds numbers for supersonic fighter tests (often about 1–5% scale in a 4 ft tunnel): **unsourced**.
