# Flight Controls, Flight Dynamics Simulation, Avionics, Single-Seat Cockpit, Life Support and Escape for a Mach 3 Low-Observable Single-Seat Fighter

*How these notes were made (research date 28 Oct 2026):* Page fetching was blocked in this session for ntrs.nasa.gov, apps.dtic.mil, martin-baker.com, sr-71.org, en.wikipedia.org and collinsaerospace.com (DNS not allowed), and the shared web-search budget ran out near the end. Most findings below therefore come from search-engine summaries of the cited pages, not from full reads of the primary documents. Each item says when the source is secondary or weak (forum, blog, dealer). Before the team uses any number as a design input, it should be checked against the primary document, especially the MIL-STD-1797 figures, ejection-seat envelopes and the SR-71 flight-manual items. Older material is dated in brackets.

---

## 1. Fly-by-wire, relaxed static stability, redundancy, control-law approaches, flight-control computers and actuators, control allocation, and stability changes from Mach 0.2 to Mach 3

### Takeaway
The YF-16 and F-16 introduced intentional relaxed static stability (RSS) with full-authority electronic fly-by-wire (FBW), the F-16 entering service in 1978. The F-35 runs a nonlinear dynamic inversion (NDI) control law on three separate vehicle management computers (VMCs) and moves its surfaces with electro-hydrostatic actuators (EHAs) on a 270 VDC "power-by-wire" bus, with no central hydraulic system. Incremental NDI (INDI) is the leading sensor-based successor and has flown on certified aircraft. For a Mach 3 design, the hardest flight-control problem shown by real accidents is departure after an inlet unstart combined with an aft centre of gravity (SR-71, 1966).

### Cited Findings
**FBW and RSS history**
- The YF-16 used an all-electronic FBW flight control system instead of a hydromechanical one with linkages and cables. Its designers reasoned that FBW reliability and redundancy made free-airframe static stability unnecessary — [Code One, "F-16 Design Origins"](https://www.codeonemagazine.com/article.html?item_id=131)
- The YF-16 is credited as the world's first aircraft intentionally designed to be slightly aerodynamically unstable — [Wikipedia, Fourth-generation fighter](https://en.wikipedia.org/wiki/Fourth-generation_fighter)
- The first operational, fully authoritative FBW system was developed for the F-16, which entered service in 1978 — [Wikipedia, Aviation in the Digital Age](https://en.wikipedia.org/wiki/Aviation_in_the_Digital_Age)
- The YF-16 (first flight January 1974) was designed from the start as an RSS aircraft with quadruplex analogue FBW, with four independent flight control computers voting on each command. This is a weak source (blog); no primary confirmation of the quadruplex analog architecture was found — [MigFlug blog, "How Fly-by-Wire Replaced Cables"](https://migflug.com/afterburner/how-fly-by-wire-changed-fighter-jet-airliner-design/)

**Redundancy: F-35 triplex VMCs versus legacy quad**
- The F-35's flight control laws run on three identical, separate VMCs built by BAE Systems (Endicott, NY). They are physically spread out for survivability, act as network controllers, and replace heavy dedicated wiring with high-speed serial buses. BAE said older quad-redundant fighters routed everything through one central flight control computer [2012 article] — [Avionics International, "Tailored to Trap" (Dec 2012)](https://www.aviationtoday.com/2012/12/01/tailored-to-trap/)
- A next-generation quad-core-processor VMC was flight-tested at NAS Patuxent River and Edwards AFB (BAE release 6 Sep 2023). It applies to all three F-35 variants, addresses obsolescence, and enables JPALS and Auto-GCAS — [Seapower Magazine](https://seapowermagazine.org/bae-systems-successfully-flight-tests-next-generation-vehicle-management-computer-for-the-f-35-lightning-ii/); [Aerospace Testing International](https://www.aerospacetestinginternational.com/news/avionics/bae-systems-flight-tests-new-vehicle-management-computer-for-f-35.html)
- Lockheed Martin has received BAE's 3,000th F-35 VMC. The VMC and the active inceptor system are built in Endicott and Rochester (UK) — [Airforce Technology](https://www.airforce-technology.com/news/bae-systems-flight-critical/)
- In the generic triplex principle, three flight computers vote and the majority command goes to the actuators. This comes from a patent and is not F-35-specific — [USPTO patent 9977432, "Distributed flight control system"](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9977432)

**Control-law approaches**
- NDI-based multivariable flight control flew on the X-35 and X-38 and is in production on the F-35 — [Bosworth, IEEE CSS "Impact of Control Technology" (2019 compilation)](https://www.ieeecss.org/sites/ieeecss/files/2019-06/IoCT2-SS-Bosworth-1.pdf)
- Honeywell and Lockheed Martin developed the X-35 dynamic-inversion controller, and Lockheed Martin built the production F-35 version — [NASA NTRS 20110008197](https://ntrs.nasa.gov/citations/20110008197) (abstract seen via search; full text not fetched)
- NDI needs an accurate onboard model, and modelling uncertainty degrades its performance (2025 review) — [Kim & Hur, Int. J. Aeronautical & Space Sciences, via GNU repository](https://scholarworks.gnu.ac.kr/handle/sw.gnu/79458?mode=full)
- INDI is sensor-based. It replaces much of the onboard model with measured signals (mainly angular acceleration), which makes it more robust to modelling error than NDI. Flight tests on a Cessna Citation II were reported as the first successful demonstration of INDI on a CS-25-certified aircraft, and INDI clearly outperformed classical NDI in those tests — [Grondman et al., "Design and Flight Testing of INDI-based Control Laws for a Passenger Aircraft" (AIAA 2018)](https://www.researchgate.net/publication/322308968_Design_and_Flight_Testing_of_Incremental_Nonlinear_Dynamic_Inversion-based_Control_Laws_for_a_Passenger_Aircraft)
- A DLR/AIAA study adapted an INDI law to command actuator servo current instead of surface angle, for electromechanical actuators, and flight-tested it — [DLR elib 128284](https://elib.dlr.de/128284); [ResearchGate](https://www.researchgate.net/publication/330196362_Design_and_flight_testing_of_flight_control_laws_integrating_incremental_nonlinear_dynamic_inversion_and_servo_current_control)
- Known INDI issues:
  - Differentiating to get angular acceleration adds time delay and amplifies noise. Proposed fixes include filtering, delay compensation, and "hybrid" INDI that blends sensor-based and model-based acceleration estimates — [Springer, Hybrid INDI (2024)](https://link.springer.com/article/10.1007/s12555-024-0539-3)
  - INDI can couple with low-frequency structural modes — [TU Delft, INDI–structural vibration coupling](https://resolver.tudelft.nl/66c34a84-5b47-49dd-b560-2836d9696e3c)
  - The INDI inner loop can be related to PI(D) gain tuning — [Acquatella et al., IFAC 2017 / arXiv 1701.08981](https://arxiv.org/pdf/1701.08981)

**Actuators: hydraulic versus EHA**
- Parker Aerospace states that EHAs are the sole means of flight control actuation on the F-35 and are fully qualified and in production — [Parker, Electrohydrostatic Actuation](https://ph.parker.com/ca/en/product-list/electrohydrostatic-actuation)
- EHAs drive the F-35 horizontal tails, flaperons, rudders and leading-edge flaps. The first EHA replaced a standard F/A-18 left aileron actuator in 1997 — [ASME J. Mech. Design review of high-speed EHA pumps](https://asmedigitalcollection.asme.org/mechanicaldesign/article/141/5/050801/449140/A-Review-of-High-Speed-Electro-Hydrostatic); [GlobalSpec/Moog, aircraft actuation technologies](https://insights.globalspec.com/article/12930/aircraft-actuation-technologies-how-do-electrohydraulic-electrohydrostatic-and-electromechanical-actuators-work)
- An EHA is a self-contained unit in which an electric motor drives a hydraulic pump that pressurises a local actuator. The F-35 therefore has full power-by-wire with no centralised hydraulic network — [GlobalSpec](https://insights.globalspec.com/article/12930/aircraft-actuation-technologies-how-do-electrohydraulic-electrohydrostatic-and-electromechanical-actuators-work)
- The F-35 electrical system provides 270 VDC, 28 VDC and 115 VAC. JSF risk reduction (J/IST) matured electro-hydrostatic actuation system (EHAS) integration — [Lockheed Martin, F-35 Air Vehicle Technology Overview (c. 2018)](https://www.lockheedmartin.com/content/dam/lockheed-martin/eo/documents/webt/F-35_Air_Vehicle_Technology_Overview.pdf)

**Mach 3 control lesson: SR-71 61-7952 breakup**
- On 25 Jan 1966 (some sources say 26 Jan), at about Mach 3.18 and 78,800 ft (some sources say 78,000 ft), a right-engine inlet unstart caused a violent yaw and pitch-up and the aircraft broke up. Pilot Bill Weaver survived without ejecting; RSO Jim Zwayer was killed (neck broken during the breakup). Accounts state that the stability augmentation system could not restore control, in part because of aft-CG longitudinal instability — [Aviation Safety Network wikibase 162372](https://cdn.aviation-safety.net/wikibase/162372); [The Aviationist (2015)](https://theaviationist.com/2015/03/17/sr-71-mid-air-disintegration/); [Weaver's first-hand account, EAA chapter newsletter](https://chapters.eaa.org/eaa10/-/media/9c4eaaa9dca04ed5b6a13f37a2d50767.ashx)

### Inferences
- For a two-person study, a practical control-law path is: (1) classical gain-scheduled linear laws (pitch-rate/C* or g-command) on trimmed linearisations across a Mach–altitude grid, used as the baseline and for handling-qualities checks; then (2) NDI or INDI with a control-allocation layer, as on the F-35 (NDI) and in current research (INDI). INDI suits a team whose aero database will be uncertain, because it depends less on model accuracy. The price is good angular-acceleration estimation and attention to actuator bandwidth, sensor delay and structural modes.
- For LO and tailless shapes (no vertical tail, or reduced or canted tails), control allocation becomes central: split drag-rudders or spoilerons, differential canted tails, thrust vectoring. No open source on an allocation scheme for a fielded LO fighter was found. The team should plan on established methods (pseudo-inverse, redistributed pseudo-inverse, linear and quadratic programming allocation) from the open literature.
- Mach 0.2 to Mach 3 stability change: subsonic-to-supersonic aerodynamic-centre movement typically makes an RSS airframe that is unstable when subsonic become strongly stable when supersonic. Meanwhile, surface effectiveness and directional stability fall at high Mach. The SR-71 accident shows that at Mach 3 an asymmetric inlet or propulsion event, combined with aft CG, can exceed the authority and bandwidth of the stability augmentation. This argues for: CG management (fuel transfer) scheduled with Mach; integrated propulsion–flight control; inlet unstart detection with automatic yaw compensation; and full-authority digital laws with angle-of-attack, sideslip and load-factor limiting. This is engineering reasoning, not a cited source.
- The F-35's move from a quad-redundant central computer to three distributed VMCs plus EHAs with no central hydraulics is a credible baseline for a new LO fighter. The thermal management of EHAs at Mach 3 (motor and fluid heat in a hot airframe) is an open risk.

### Gaps
- The exact F-35 VMC redundancy and voting logic, and the EHA power ratings, were not publicly found.
- No primary source (General Dynamics or USAF) was retrieved confirming the F-16's original quadruplex analog architecture or its later digital conversion (F-16C/D Block 40 digital FBW). These are widely reported but unverified here.
- No open source was found on control allocation for a specific fielded tailless or LO fighter, or on published Mach-dependent static-margin data for any Mach 3 aircraft. The SR-71 flight manual (Section V, Operating Limitations) at [sr-71.org](https://sr-71.org/blackbird/manual/5) holds the CG, Mach and KEAS limits but could not be fetched (host blocked).
- NASA NTRS full text on F-35/X-35 NDI design (20110008197) could not be read (host blocked).

---

## 2. Handling-qualities criteria: MIL-STD-1797A/B, Cooper–Harper scale, CAP, Neal–Smith and flying-qualities levels

### Takeaway
Flying-qualities Levels 1, 2 and 3 map to Cooper–Harper ratings (HQR) of 1–3 (or ≤3.5), 4–6 (3.5–6.5) and 7–9, with 10 meaning uncontrollable. MIL-STD-1797A/B carries the short-period criteria: the control anticipation parameter (CAP) with damping, equivalent time delay, Neal–Smith and bandwidth. The exact Level 1 numeric boundaries could not be retrieved from the standard in this session; commonly cited values are listed under Gaps for verification.

### Cited Findings
- **CAP definition:** the ratio of initial pitch acceleration to the steady-state change in normal load factor, both about the instantaneous CG. Level 1 requires CAP to be relatively large (landing phase). The CAP boundaries in MIL-STD-1797A are given as a figure — [DTIC ADA319509, "Comparison of the CAP and the Bandwidth Criterion"](https://apps.dtic.mil/sti/tr/pdf/ADA319509.pdf); [Stengel, Princeton MAE331 Lecture 21, "Flying Qualities Criteria"](https://stengel.mycpanel.princeton.edu/MAE331Lecture21.pdf)
- **Neal–Smith:** the criterion is included in MIL-STD-1797. Its boundaries came from correlating the DiFranco, Neal–Smith and LAHOS data — [DTIC ADA102626 (NADC, 1981)](https://apps.dtic.mil/sti/tr/pdf/ADA102626.pdf)
- **Task dependence:** Level 1 boundaries for tracking differ from those for acquisition at the same angle of attack (NASA high-alpha flying-qualities research) — [NASA TM-4773, High-Alpha Handling Qualities Flight Research](https://citeseerx.ist.psu.edu/document?doi=84e2420c64c90bfd7e7bb5515ce88876f083f2a3&repid=rep1&type=pdf)
- **MIL-STD-1797B:** specifies equivalent CAP, short-period damping and equivalent time delay. It has been applied, for example, to UAS flying-qualities evaluation with a stitched Learjet model — [AIAA J. Guidance, Control & Dynamics, doi 10.2514/1.G004748](https://arc.aiaa.org/doi/10.2514/1.G004748)
- **Cooper–Harper to Levels:** Level 1 is satisfactory without improvement (HQR 1–3); Level 3 aircraft (HQR 7–9) have significant deficiencies — [NASA TM-2009-215767, Cooper-Harper Experience Report](https://ntrs.nasa.gov/api/citations/20090025299/downloads/20090025299.pdf?attachment=true); [412th TW, DTIC ADA616887](https://apps.dtic.mil/sti/tr/pdf/ADA616887.pdf)
- **Averaged-rating cutoffs:** one course note citing MIL-F-8785C and MIL-STD-1797A gives Level 1 = HQR 1 to 3.5 and Level 2 = HQR 3.5 to 6.5, used for averaged ratings. These cutoffs were not confirmed in the standard's own text — [UFMG course notes, "Flying and Handling Qualities"](http://www.cpdee.ufmg.br/~torres/wp-content/uploads/2018/02/flying_handling_qualities.pdf)
- **Scale anchors:** HQR 1 is excellent, with pilot compensation not a factor; HQR 2 is good, with negligible deficiencies; HQR 3 is fair, with minimal pilot compensation. HQR 1 requires the "desired" performance standard — [ScienceDirect, "Pilot Opinion" topic](https://www.sciencedirect.com/topics/engineering/pilot-opinion); [Fifty Years of the Cooper-Harper Scale (AIAA 2019)](https://www.researchgate.net/publication/330197628_Fifty_Years_of_the_Cooper-Harper_Scale)
- **Test practice:** USAF Test Pilot School flying-qualities test methods (Vol IV Ch 13) are publicly available via a reposted PDF — [CAFE Foundation copy](https://cafe.foundation/v2/pdf_tech/Flying.Qualities/PAV.FlyingQual.TestGuide.pdf)

### Inferences
- For a design study, the minimum handling-qualities toolset is:
  - Lower-order equivalent systems (LOES) matching of the closed-loop pitch response, to get the equivalent short-period frequency, damping and time delay.
  - The CAP and damping thumbprint.
  - Bandwidth and phase delay (preferred for highly augmented FBW aircraft, where CAP can mislead).
  - Neal–Smith, using a pilot model.
  - Gibson dropback, as a supplementary check.
- Check all of these at every Mach/altitude grid point, including Mach 2.5–3 cruise. At high dynamic pressure, short-period frequency rises and the pilot-induced oscillation (PIO) risk from actuator rate limits grows.
- Piloted-simulation Cooper–Harper ratings (Section 3) are needed to close the loop. Analytical criteria alone are not enough for an unconventional LO shape.

### Gaps
- The actual MIL-STD-1797A/B numerical tables were not retrieved. The following values are well known in the open literature but were **not verified in this session**; check them against MIL-STD-1797A and MIL-F-8785C (1980) before use:
  - Category A (fighter manoeuvring), Level 1: CAP about 0.28–3.6 g⁻¹s⁻² with short-period damping about 0.35–1.30.
  - Level 2: CAP about 0.16–10 with damping about 0.25–2.0.
  - Equivalent time delay limits: about 0.10 s (Level 1), 0.20 s (Level 2), 0.25 s (Level 3).
  - Neal–Smith fighter tracking: bandwidth about 3.5 rad/s, with droop and resonance limits.
- MIL-STD-1797B (2012) changes versus 1797A were not obtained. DTIC and NTRS hosts were blocked in this session.

---

## 3. Flight-dynamics modelling and simulation: 6-DOF equations of motion, aero databases, JSBSim/FlightGear, Stevens & Lewis, MATLAB/Simulink alternatives, pilot-in-the-loop

### Takeaway
A credible open toolchain exists: the JSBSim nonlinear 6-DOF FDM (C++ with a Python module, XML aircraft definitions, WGS84 Earth, ISA 1976 atmosphere) visualised in FlightGear; the Stevens, Lewis & Johnson (3rd ed., Wiley 2015) text and its F-16 model as a validation benchmark; and Python implementations of that F-16 model. No Julia port of the Stevens & Lewis model was found.

### Cited Findings
- JSBSim is an open-source, nonlinear 6-DOF flight dynamics model for aircraft and rockets. It has no native graphics and can run in batch mode. It models Earth rotation (Coriolis and centrifugal terms), uses the 1976 standard atmosphere and the WGS84 geodetic system, and describes aircraft (FCS, aero, propulsion, gear) in XML. Output can go to screen, file or socket — [JSBSim project site](https://jsbsim.sourceforge.net/); [JSBSim GitHub](https://github.com/JSBSim-Team/jsbsim)
- JSBSim has a Python module with the same features as the C++ library (documentation v1.3.3) — [JSBSim Python docs](https://jsbsim-team.github.io/jsbsim/python/index.html)
- JSBSim is incorporated into FlightGear (development dates to 1996; runs on Linux, macOS, Windows) and is also used by Outerra and OpenEaagles. The FlightGear interface protocol is in data_output/flightgear.xml. The JSBSim Reference Manual documents each XML element and property — [FlightGear wiki, JSBSim](https://wiki.flightgear.org/JSBSim); [Berndt, "JSBSim: An Open Source Flight Dynamics Model in C++" (AIAA 2004)](https://jsbsim.sourceforge.net/JSBSimAnOpenSourceFlightDynamicsModelinCPP.pdf)
- Stevens, Lewis & Johnson, *Aircraft Control and Simulation: Dynamics, Controls Design, and Autonomous Systems*, 3rd ed. (Wiley, 2015), includes Appendix A "F-16 Model" and Appendix B "Software", with MATLAB calculations and FORTRAN code — [Wiley](https://www.wiley.com/en-us/Aircraft+Control+and+Simulation:+Dynamics,+Controls+Design,+and+Autonomous+Systems,+3rd+Edition-p-9781118870983); [Penn State record](https://pure.psu.edu/en/publications/aircraft-control-and-simulation-dynamics-controls-design-and-auto/)
- The open-source C++ implementation of the Stevens & Lewis F-16 model, with Python bindings (`f16dynamics`), is EthanJamesLew/f16-flight-dynamics — [GitHub](https://github.com/EthanJamesLew/f16-flight-dynamics)
- An example of flight-control design and simulation with handling-qualities assessment, using Cooper–Harper ratings in piloted simulation (rotorcraft context), is the VFS 2019 Berger et al. paper — [SJSU/VFS 2019 Berger](https://www.sjsu.edu/researchfoundation/docs/VFS_2019_Berger.pdf)

### Inferences
- Suggested pipeline:
  1. Write the 6-DOF rigid-body equations of motion (flat-Earth for control design, WGS84/rotating Earth via JSBSim for Mach 3 / high-altitude navigation-quality runs).
  2. Build the aero database as tables in Mach, alpha, beta and control deflections, from DATCOM-class methods, then CFD, then wind-tunnel data as available.
  3. Validate the whole toolchain first by reproducing the Stevens & Lewis F-16 trim and linearisation results.
  4. Port the database to JSBSim XML for FlightGear pilot-in-the-loop work.
  5. Run linear analysis and control design in Python (`python-control`, SciPy) or Julia.
- At Mach 3, add to the model: aerothermal effects on structure (aeroelastic stiffness loss), inlet/propulsion coupling (unstart model), and variable mass and CG from fuel burn and transfer. The SR-71 accident (Section 1) shows these couplings are flight-critical.

### Gaps
- No sources were retrieved on the Python Control Systems Library (`python-control`), Julia tools (ModelingToolkit, ControlSystems.jl), or open aero-prediction tools (USAF Digital DATCOM, OpenVSP/VSPAERO). Their existence is common knowledge, but they were not cited here.
- The basis of the Stevens & Lewis F-16 data (commonly cited as NASA TP-1538, Nguyen et al., 1979, valid to about 45 deg AoA, subsonic) could not be verified because NTRS was blocked. It is not a supersonic or Mach 3 database.
- No open Mach 3 fighter aero database was found. Possible open sources to search: NASA SR-71 and XB-70 flight research reports on NTRS (blocked here).

---

## 4. Avionics architecture: IMA, sensor fusion (F-22/F-35), AESA, IRST, EW, datalinks, OMS/MOSA, software size, DO-178C

### Takeaway
Fifth-generation avionics centralise processing: the F-22 has two Raytheon common integrated processors (CIPs), and the F-35 uses integrated core processing. Fusion correlates radar, passive RF and datalink tracks, taking each parameter from the most accurate sensor, and is tied to emission control. US policy now pushes MOSA, OMS/UCI, FACE and SOSA. F-35 software is usually quoted at "over 8 million lines" (not confirmed by DOT&E), and its TR-3/Block 4 software is the program's main schedule problem in 2024–2026. Military flight software is certified against MIL-HDBK-516C airworthiness criteria, which commonly use DO-178C objectives (DAL A for flight control).

### Cited Findings
**F-22 integrated avionics and fusion**
- All F-22 sensor processing runs in two Raytheon CIPs. The radar processing residing in the CIP was described with 10 signal-processing elements and 4 data-processing elements [mid-1990s development-era paper] — [FlightGlobal, "Sense from confusion" (1999)](https://www.flightglobal.com/systems-interiors/1999/06/sense-from-confusion/); [Malas (USAF), "F-22 Radar Development," IEEE](http://www.mycity-military.com/uploads2/154453_575645487_IEEE%20MALAS%20F-22%20RADAR%20DEVELOPMENT.pdf)
- APG-77, ALR-94 and datalink data are correlated in azimuth, elevation and range. Each parameter in the fused track comes from the most accurate sensor (passive RF for bearing, radar for range). CIP software controls APG-77 emissions by emission-control principles. This is a forum source; the summary is consistent with FlightGlobal — [F-16.net forum, "F-22 sensor fusion"](https://www.f-16.net/forum/viewtopic.php?t=9268)
- The APG-77 AESA module count is reported as about 1,200 and about 1,500 by different sources. The ALR-94 passive suite uses more than 30 antennas in the wings and fuselage — [Wikipedia, AN/APG-77](https://en.wikipedia.org/wiki/AN/APG-77); [AeroCorner F-22 page](https://aerocorner.com/aircraft/lockheed-martin-f-22-raptor/)

**Open architectures**
- OMS is a non-proprietary, USAF-originated architecture that uses commercial service-oriented architecture and middleware — [Tokar, "A Comparison of Avionics Open System Architectures" (HILT 2016)](https://sigada.org/conf/hilt2016/paper-Tokar.pdf)
- OMS focuses on the interfaces between software services and hardware subsystems — [NAVAIR MOSA page](https://www.navair.navy.mil/MOSA)
- An Oct 2018 SAF/AQ memo required OMS/UCI "to the maximum extent practicable". The 2019 Tri-Service MOSA memo did not mandate a single standard and named SOSA, FACE and VICTORY as encouraged standards — [Air & Space Power Journal, Winter 2019](https://www.airuniversity.af.edu/Portals/10/ASPJ/journals/Volume-33_Issue-4/V-Brown_et_al.pdf); [AFMC Guidebook for Implementing MOSA v2.0 (2023, Distribution A)](https://guide.dafdto.com/wp-content/uploads/2023/11/AFMC-Guidebook-for-Implementing-MOSA-in-Weapon-Systems_V2.0_Distro_A.pdf)
- OMS/UCI is in use on several programmes, mainly for **non-safety-critical** subsystem-to-platform interfaces — [AFMC MOSA Guidebook](https://guide.dafdto.com/wp-content/uploads/2023/11/AFMC-Guidebook-for-Implementing-MOSA-in-Weapon-Systems_V2.0_Distro_A.pdf)

**F-35 software size and status (current to 2026)**
- The F-35 is "long said to run on over 8 million lines of code". This figure was not confirmed in DOT&E text — [The Aviationist, 25 Mar 2026](https://theaviationist.com/2026/03/25/tr-3-f-35s-delivered/)
- DOT&E FY2025 says no combat-capable TR-3 F-35s were delivered in FY2025. 158 aircraft were delivered in TR-3 configuration, out of 812 produced in any configuration — [The Aviationist, 25 Mar 2026](https://theaviationist.com/2026/03/25/tr-3-f-35s-delivered/)
- TR-3 build 40R02 was judged "unsuitable for dedicated OT", and TR-2 build 30R08 was "predominantly unusable" for most of FY25. The programme produced a truncated build that disabled previously fielded capabilities to stabilise TR-3 — [Defence Blog](https://defence-blog.com/f-35-fielded-no-new-combat-capability-in-fy25-due-to-software-problems/); [DOT&E FY2024 F-35 report](https://www.dote.osd.mil/Portals/97/pub/reports/FY2024/dod/2024f-35jsf.pdf)
- The USAF stopped accepting F-35A deliveries in July 2023 pending TR-3 software — [CRS R48304](https://www.congress.gov/crs-product/R48304)
- Background on the modernisation schedule: [GAO-21-226](https://www.gao.gov/assets/gao-21-226.pdf)

**Safety-critical software**
- Military airworthiness assurance follows MIL-HDBK-516C (airworthiness certification criteria) and MIL-STD-882E (system safety) — [LDRA, "DO-178C and MIL-HDBK-516 in tandem"](https://resources.ldra.com/course/do-178c-and-mil-hdbk-516-in-tandem/)
- A Korean study maps MIL-HDBK-516C software criteria (Chapter 15) to DO-178C objectives using a matching-ratio formula — [KoreaScience JAKO202124553144032](https://www.koreascience.kr/article/JAKO202124553144032.pdf)
- DAL A is the most stringent DO-178C level. It applies to catastrophic failure conditions, such as flight-control software failure — [Lynx DO-178C datasheet](https://www.lynx.com/hubfs/Data%20sheets/D0-178C%20Certification%20Datasheet.pdf); [Parasoft DO-178C e-book](https://alm.parasoft.com/hubfs/ebook-DO-178C-Software-Compliance-Aerospace-Defense.pdf)
- DO-178C combined with the FACE technical standard is a combination used for reusable high-assurance military avionics — [Military Embedded Systems](https://militaryembedded.com/avionics/safety-certification/do-178c-meets-the-face-technical-standard-high-assurance-and-reusability-for-airborne-software)

### Inferences
- Reference architecture for the study:
  - A partitioned, flight-critical domain: triplex or quad VMCs, DAL A, kept physically and logically separate from a MOSA/OMS-compliant mission-systems domain (integrated core processors, AESA, passive RF/ESM, IRST/EO-DAS, LPI/LPD datalinks).
  - Fusion driving emission control, to protect the radar and IR signature.
- At Mach 3, aerodynamic heating constrains antenna and aperture placement and coolant capacity: avionics heat must go to fuel, as in the SR-71 (Section 6).
- The F-35 TR-3 experience shows that software, not airframe, is now the schedule-critical path. A small team should budget for model-based, auto-coded control laws and keep mission software modest.

### Gaps
- No source was found on: F-35 integrated core processor specifics, AN/APG-81 or AN/AAQ-37 DAS numbers, AN/ASQ-239 EW, F-35 EOTS/IRST, the MADL datalink, the F-22 lacking a production IRST, or Russian (MiG-31 Zaslon PESA, Su-57 Byelka) avionics.
- The F-35 "8 million lines" figure is unconfirmed by a government primary source in this session. GAO reports historically cited figures in the 8–10 million SLOC range, but this was not verified here.

---

## 5. Single-seat cockpit: HMD (F-35 Gen III), large-area displays, HOTAS, voice control, workload management, autonomy and AI assistance (DARPA ACE, X-62A, CCA)

### Takeaway
The F-35 Gen III HMDS (Collins/Elbit) has a 30×40 deg binocular display with 100% overlap, integrated digital night vision, and DAS imagery from six IR cameras that lets the pilot "look through" the airframe. It is rated for ejection to 550 KEAS. AI flew an X-62A VISTA in within-visual-range dogfights against a crewed F-16 in 2023 (announced April 2024). CCA Increment 1 reached its production decision on 17 June 2026 (General Atomics FQ-42A and Anduril FQ-44A). A 2030s single-seat fighter design should assume a pilot managing teamed uncrewed aircraft.

### Cited Findings
**F-35 Gen III HMDS**
- The display is binocular with a 30×40 deg field of view and 100% overlap. Older press releases describe it as 40×30 deg; the orientation differs between sources — [element14](https://community.element14.com/learn/publications/b/blog/posts/look-and-shoot-the-f-35-gen-iii-helmet-mounted-display-system); [Military Embedded Systems](https://militaryembedded.com/avionics/displays/f-35-gen-iii-helmet-mounted-display-system-delivered-for-software-integration-to-lockheed-martin)
- The Gen III night camera gives performance equivalent to ANVIS-9 NVGs. Northrop Grumman DAS streams imagery from six IR cameras around the aircraft to the helmet. The "360-degree" coverage claimed is helmet plus DAS, not the display FOV — [element14](https://community.element14.com/learn/publications/b/blog/posts/look-and-shoot-the-f-35-gen-iii-helmet-mounted-display-system); [Simple Flying](https://simpleflying.com/how-f-35-pilots-avoid-situational-blind-spots-helment-mounted-displays/)
- Collins lists ejection capability to 550 KEAS and multiple interpupillary-distance settings — [Collins Aerospace / RTX, F-35 Gen III HMDS product page](https://www.rtx.com/collinsaerospace/what-we-do/industries/military-and-defense/displays-and-controls/airborne/helmet-mounted-displays/f-35-gen-iii-helmet-mounted-display-system)
- Each F-35 helmet is custom-fitted to the pilot (head scan and fit process) — [U.S. Air Force, "An inside look at F-35 pilot helmet fittings"](https://www.af.mil/News/Article-Display/Article/2719003/an-inside-look-at-f-35-pilot-helmet-fittings/)

**AI and autonomy: DARPA ACE and X-62A VISTA**
- AI agents flew the X-62A VISTA (a modified F-16) in dogfights against a crewed F-16 at Edwards AFB, mostly in 2023, with the first in September 2023. The tests were announced in April 2024 as the first "machine-learning-based autonomy in flight-critical systems" — [CSIAC/DTIC](https://csiac.dtic.mil/articles/dod-artificial-intelligence-agents-successfully-pilot-fighter-jet/); [ExecutiveGov, Apr 2024](https://executivegov.com/2024/04/air-force-darpa-demo-machine-learning-based-autonomy-using-x62a-vista-aircraft/)
- Safety pilots were aboard and did not need to disengage the AI during the dogfights. The AI flew offensive and defensive manoeuvres, closing to about 2,000 ft at about 1,200 mph (closure). The release did not say who won — [Fox Business](https://www.foxbusiness.com/technology/us-air-force-confirms-first-successful-ai-dogfight); [Flying Magazine](https://flyingmag.com/darpa-achieves-major-breakthrough-with-ai-controlled-aircraft); [Military Embedded Systems](https://mil-embedded.com/ai/deep-learning/ai-piloted-f-16-dogfights-human-pilot-in-darpa-test)
- In the earlier simulation-only AlphaDogfight Trials (2020), an AI agent beat a human F-16 pilot 5–0 — [Gizmodo](https://gizmodo.com/darpa-tests-ai-dogfighting-computer-skynet-x-62a-vista-1851419381)

**CCA teaming (current to Oct 2026)**
- The YFQ-42A (General Atomics) first flew in August 2025; an Air Force article dated 27 Aug 2025 is cited — [The War Zone](https://www.twz.com/air/yfq-42-fighter-drone-collaborative-combat-aircraft-has-flown-for-the-first-time); [Wikipedia, YFQ-42 Dark Merlin](https://en.wikipedia.org/wiki/General_Atomics_YFQ-42_Dark_Merlin)
- On 17 June 2026 the USAF announced CCA Increment 1 production awards to both General Atomics (FQ-42A) and Anduril (FQ-44A), four months ahead of schedule — [Military Times, 18 Jun 2026](https://www.militarytimes.com/industry/techwatch/2026/06/18/us-air-force-awards-first-cca-production-contracts-to-general-atomics-anduril/); [Air & Space Forces Magazine](https://www.airandspaceforces.com/air-force-general-atomics-anduril-cca-production-contracts/)
- In late July 2026, GA-ASI declared FQ-42A "full-scale manufacturing underway", and Anduril rolled out the first FQ-44A from its Arsenal-1 plant in Ohio — [The Aviationist, 29 Jul 2026](https://theaviationist.com/2026/07/29/fq-42a-fq-44a-ccas-serial-production/); [Defense News, 28 Jul 2026](https://www.defensenews.com/industry/techwatch/2026/07/28/first-anduril-yfq-44a-rolls-off-production-line-for-us-cca-program/)
- Increment 1 was earlier stated as 100–150 aircraft. Cost figures (about $4.5B procurement) are third-party estimates — [Shephard, CCA Increment 1](https://plus.shephardmedia.com/programmes/detail/collaborative-combat-aircraft-cca-usa/)

### Inferences
- Cockpit baseline for a single-seat Mach 3 LO fighter:
  - A panoramic large-area touchscreen display with a helmet-mounted display as the primary flight reference.
  - DAS-style distributed IR apertures, which also reduce canopy-size demands. This matters because a Mach 3 canopy is a heat and RCS problem; see Section 8.
  - HOTAS kept for time-critical functions; voice input as a supplement.
  - An AI "copilot" for systems management, autonomous recovery (Auto-GCAS heritage) and CCA tasking.
- The HMD must be qualified for the seat's maximum ejection KEAS. The Gen III limit of 550 KEAS is below the US16E's 600 KEAS (Section 7), and the helmet has driven seat neck-load issues on the F-35. Any Mach 3 escape concept must budget helmet mass and centre of gravity.

### Gaps
- No sources were retrieved on: F-35 panoramic cockpit display size (commonly 20×8 in), F-35 voice recognition status, quantitative single-pilot workload studies, X-62A flight counts or software-change counts, or ACE follow-on (VENOM, the 2025–26 F-16 autonomy testbeds). The search budget ran out.
- No data was found on the F-47 (NGAD) cockpit concept.

---

## 6. Life support at Mach 3 and high altitude: pressure-suit thresholds, SR-71 S1030/S1031, MiG-25 VKK-6/VKK-15, cockpit pressurisation, OBOGS, anti-g, cockpit cooling, F-22 hypoxia lessons

### Takeaway
The Armstrong limit is about 63,000 ft (body-temperature boiling of fluids), and full pressure suits are customarily required at about 50,000 ft and above. Both the SR-71 (cruise about 80,000+ ft) and MiG-25 crews wore full pressure suits: the David Clark S1030 for the SR-71, and the VKK-6 with GSh-6 helmet for the MiG-25, rated to about 100,000 ft (or 40 km per one listing). SR-71 cockpits were held at 26,000 ft (or 10,000 ft) cabin altitude with heat dumped into fuel. The F-22 "hypoxia-like" crisis (2010–2012; restrictions in May 2012) was traced mainly to the upper pressure garment valve and oxygen-delivery hardware rather than OBOGS chemistry. Fixes included removing the C2A1 filter, adding an automatic backup oxygen system, and imposing altitude limits.

### Cited Findings
**Altitude thresholds**
- The Armstrong limit is about 63,000 ft, where water boils at body temperature; one reference gives about 63,550 ft. Above it, fluids in the throat and lungs boil — [Wikipedia, Armstrong limit](https://en.wikipedia.org/wiki/Armstrong_limit); [Wikipedia, Pressure suit](https://en.wikipedia.org/wiki/Pressure_suit)
- A pressure suit is customarily required at about 50,000 ft (another source: about 49,000 ft). F-22 and F-35 pilots, who operate to about 59,000–60,000 ft, wear a counter-pressure garment and rely on positive-pressure breathing after decompression rather than a full suit. These are weak sources (forum and fitness site) — [ww2aircraft.net forum](https://ww2aircraft.net/forum/threads/armstrong-limit-high-altitude-flight.31868/); [BootCamp Military Fitness Institute](https://bootcampmilitaryfitnessinstitute.com/2024/08/06/what-is-the-armstrong-limit/)
- Authoritative history of US pressure suits from Wiley Post to the Shuttle: NASA's *Dressing for Altitude* (Jenkins, 2012) — [NASA e-book PDF](https://www.nasa.gov/wp-content/uploads/2015/04/dressing-for-altitude-ebook_tagged.pdf) (located but not read)

**SR-71**
- The S1030 full pressure suit was developed in the 1970s for SR-71 operations, evolving from the S901. It has redundant breathing and pressure-control systems and multi-layer thermal protection, including against aerodynamic heating during ejection — [Gizmodo](https://gizmodo.com/the-most-badass-plane-ever-had-an-equally-awesome-fligh-5994110); [Flight Test Museum, pressure suits](https://flighttestmuseum.org/pressure-suits/); [SR-71 webmaster suit page](http://www.wvi.com/~sr71webmaster/press_suit001.html)
- The SR-71 cockpit was pressurised to 10,000 ft or 26,000 ft cabin altitude using engine 9th-stage compressor bleed. 26,000 ft was preferred because it gave more airflow and cooling. This is a forum post quoting the flight manual — [PPRuNe forum](https://www.pprune.org/military-aviation/616733-sr-71-blackbird-3.html)
- The cabin needed heavy cooling: Mach 3.2 cruise heats the external surface well beyond 500 °F, and the air conditioner dumps cockpit heat into the fuel via a heat exchanger. The aircraft carried about 262 L of liquid nitrogen for fuel-tank pressurisation and inerting. These are secondary wiki sources — [NASA Fandom, Lockheed SR-71](https://nasa.fandom.com/wiki/Lockheed_SR-71_Blackbird)

**MiG-25 (speed reference)**
- The VKK-6 (VKK-6M) partial-pressure (compensating) suit is used with the GSh-6 pressure helmet, PK-1 compensating gloves and KN socks above 14 km (about 46,000 ft). It gives at least 4 min of operating time at 14 km and is quoted for flights up to 40 km. It inflates automatically on cockpit pressure loss — [Catawiki VKK-6M listing](https://catawiki.com/zh-Hans/l/85624691-ussr-vkk-6m-1960-1970); [IMA-USA listing](https://www.ima-usa.com/products/original-cold-war-soviet-mig-jet-fighter-cased-gsh-6-high-altitude-flying-helmet-with-vkk-6m-pressure-suit)
- The VKK-6 is rated to 100,000 ft and −50 to +50 °C, and is associated with MiG-25 and MiG-31 crews. The GSh-6 has a metal neck ring sealing to the suit and an electrically heated visor — [Wikipedia, VKK flight suit](https://en.wikipedia.org/wiki/VKK_flight_suit); [Berlin museum-digital object record](https://berlin.museum-digital.de/pdf/object/869.pdf?lang=en)
- Conflict: 100,000 ft (about 30.5 km) versus 40 km. Both come from dealer or encyclopedia sources and should be checked against a primary Zvezda or Russian technical document.

**F-22 hypoxia episode (2008/2010–2013) [older information]**
- USAF SAB Quick-Look Study SAB-TR-11-04 (dated 1 Feb 2012) examined oxygen generation on the F-22, A-10, F-15E, F-16, F-35, B-1, B-2, CV-22 and T-6. It did not find a root cause and made 9 findings and 14 recommendations in three areas: acquisition, organisation and equipment — [DTIC ADA567568 (SAB report)](https://apps.dtic.mil/sti/pdfs/ADA567568.pdf); [Military.com, 28 Feb 2012](https://www.military.com/dodbuzz/2012/02/28/f-22-raptor-smoking-gun-not-found); [AFNS via GlobalSecurity, 30 Mar 2012](https://www.globalsecurity.org/military/library/news/2012/03/mil-120330-afns03.htm)
- Contributing factors cited: a leaky cooling system (path into OBOGS unconfirmed) and problems with the breathing regulator/anti-G (BRAG) valve — [AIN, 30 Mar 2012](https://backend.ainonline.com/aviation-news/defense/2012-03-30/root-cause-f-22-incidents-still-eludes-air-force)
- In July 2012 the USAF named a valve in the upper pressure garment as the main cause: the vest inflated and stayed inflated when it should not, restricting breathing. Oxygen hoses, quick-connects and occasionally the C2A1 filter canister also contributed. The filter was removed to increase flow. An altitude restriction was imposed so pilots would not need the vest. The Secretary of Defense directed expedited installation of an automatic backup oxygen system. Restrictions imposed in May 2012 were lifted gradually — [JBLE/AF, "DoD approves plan to lift F-22 restrictions" (Jul 2012)](https://www.jble.af.mil/News/Article-Display/Article/110758/dod-approves-plan-to-lift-f-22-restrictions/); [Airforce Technology](https://www.airforce-technology.com/news/newsroot-cause-f22-raptor-hypoxia-identified-usaf/); [Anchorage Daily News, 24 Jul 2012](https://www.adn.com/alaska-news/article/faulty-valve-blamed-oxygen-deprivation-among-f-22-pilots/2012/07/24/)
- Lockheed was awarded about $19M (June 2012) for the automatic backup oxygen system, with deliveries to complete by 30 Apr 2013. A patent document dates the return to unrestricted flight to 4 Apr 2013 — [Airforce Technology](https://www.airforce-technology.com/news/newsroot-cause-f22-raptor-hypoxia-identified-usaf/); [USPTO 10772562](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10772562)
- The HASC subcommittee hearing on F-22 pilot physiological issues was held on 13 Sep 2012; the USAF admitted mistakes to Congress — [House hearing record CHRG-112hhrg76215](https://www.govinfo.gov/content/pkg/CHRG-112hhrg76215/html/CHRG-112hhrg76215.htm); [Military.com, 14 Sep 2012](https://www.military.com/defensetech/2012/09/14/af-admits-f-22-mistakes-to-congress)
- A follow-on standards effort produced MIL-STD-3050 (aircraft crew breathing systems using OBOGS) — [DLA Standardization Program Journal](https://www.dsp.dla.mil/Portals/26/Documents/Publications/Journal/160301-DSPJ-06.pdf)
- USAF medical measures included pilot physiological monitoring (pulse oximetry) — [U.S. Air Force, medical official explains F-22 pilot-protection efforts](https://www.af.mil/News/Article-Display/Article/111190/medical-official-explains-f-22-pilot-protection-efforts/)

### Inferences
- A Mach 3 fighter that cruises above about 63,000 ft must treat cockpit decompression (battle damage, canopy failure, or ejection) as needing **full-pressure-suit-level protection**. A G-suit plus vest ensemble (the F-22/F-35 approach, limited to about 60,000 ft) is not enough above the Armstrong limit for more than a very short time.
- Options:
  - (a) A lightweight full-pressure suit (S1030-class or VKK-class), with a workload and comfort penalty for a fighter pilot pulling 9 g.
  - (b) An altitude-limited mission profile below about 60,000 ft.
  - (c) A pressurised escape capsule (Section 7).
- The F-22 lesson: treat the whole breathing system as one safety-critical system under a single standard (MIL-STD-3050), including garment valves, hoses, filters, regulator, backup oxygen and physiological sensing. Test integrated breathing performance under g and altitude, not only OBOGS output purity.
- Cockpit cooling at Mach 3: recovery temperatures of about 600 °F at the skin mean the environmental control system must reject canopy radiant and conductive heat, avionics heat and pilot metabolic heat into fuel. The fuel's heat-sink capacity then becomes a mission-length limit, as on the SR-71.

### Gaps
- No primary source was found for the S1031 suit (whether it exists as a distinct model or as an S1030 variant), or for VKK-15 specifics.
- No numerical fighter cockpit pressurisation schedule was found (for example, MIL-STD or F-15/F-22 schedules, typically isobaric to about 8,000 ft and then a 5 psi differential). This is unverified and must come from MIL-E-18927 / JSSG-2009 or a flight manual.
- No data was found on F-35 OBOGS performance or on 2017–2018 F-35/T-6/F/A-18 physiological-episode outcomes.
- The SR-71 flight manual (sr-71.org) could not be fetched for primary suit and cabin data.

---

## 7. Escape at Mach 3: SR-71 SR-1 seat, the 1966 breakup, K-36D-3.5, Martin-Baker US16E, Collins ACES 5, encapsulated seats and capsules (B-58, XB-70, F-111)

### Takeaway
No open-ejection seat in service is qualified anywhere near Mach 3 at cruise dynamic pressure:
- US16E (F-35): 600 KEAS / 50,000 ft.
- ACES family: about 600 kt / 60,000 ft (marketing).
- K-36D: rated 0–755 KEAS, with operational ejections reported at about 729 KEAS and Mach 2.6.
- SR-1 (SR-71): qualified to about 450 KEAS, consistent with SR-71 cruise near that dynamic pressure.

Mach 3 escape has been addressed by (a) a low-KEAS, high-altitude flight profile combined with full-pressure-suit protection (SR-71), or (b) encapsulated seats or crew modules: B-58 at Mach 2 above 40,000 ft, XB-70 designed to Mach 3 above 70,000 ft, and the F-111 module at about 3,000 lb. The 1966 SR-71 breakup at Mach 3.18 and 78,800 ft was survived only because the suit protected the pilot after he was thrown clear.

### Cited Findings
**Martin-Baker US16E (F-35)**
- The 2026 data sheet gives a maximum ejection speed of 600 KEAS, an operating ceiling of 50,000 ft, zero/zero in near-level flight, and a crew boarding mass of 103–245 lb (46.7–111.1 kg) with a light-crew switch at 150 lb. Seen via search; martin-baker.com fetch blocked — [Martin-Baker US16E 2026 Data Sheet](https://martin-baker.com/wp-content/uploads/2023/06/US16E-2026-Data-Sheet.pdf)
- A 2011 release says the seat is qualified from 0 kt/0 ft to 600 kt at 50,000 ft. A 2010 report said 550 kt was qualified for the full pilot range, 50 kt short of the specification — [Airframer release 13106 (2011)](https://www.airframer.com/news/release/13106); [F-16.net forum, US16E](https://www.f-16.net/forum/viewtopic.php?p=304190)
- A 2015 finding of increased neck-injury risk for lightweight pilots at low speed led to a temporary weight restriction. Whether and how it was lifted was not confirmed in the sources found — [F-16.net forum](https://www.f-16.net/forum/viewtopic.php?p=182689)
- Martin-Baker developed an advanced electronic sequencer (2019) — [Janes, 6 Mar 2019](https://www.janes.com/defence-news/news-detail/martin-baker-develops-advanced-sequencer-for-ejection-seats)

**Collins ACES 5**
- The ACES family envelope is quoted as up to 600 kt and 60,000 ft; at IDEX 2021 Collins stressed improved survivability at 450 kt. These are marketing figures; no published ACES 5 envelope chart was found — [Times Aerospace, IDEX 2021](https://www.timesaerospace.aero:443/news/defence/idex-collins-aerospace-targets-middle-east-fighter-seats); [Aerotech News](https://www.aerotechnews.com/?p=74935)
- Features: head, neck, arm and leg flail prevention; a load-compensating catapult that adjusts to occupant weight. Collins claims ejection-related major injuries below 5% and spinal injuries below 1%. Compliant with MIL-HDBK-516C. Platforms: F-15, F-16, F-22, B-1, B-2, A-10, T-7A — [Collins, ACES 5 product page](https://www.collinsaerospace.com/what-we-do/Military-And-Defense/Interiors/Aces-5-Next-Generation-Ejection-Seat); [Shephard, USAF selects ACES 5 for F-15](https://shephardmedia.com/news/air-warfare/usaf-selects-aces-5-ejection-seat-f-15-fleet); [Aviation Week, Collins ramp-up](https://ngstage.aviationweek.com/defense/aircraft-propulsion/collins-readies-historic-us-ejection-seat-ramp)

**NPP Zvezda K-36D family**
- The K-36D is rated for survivable ejections from 0 to 755 KEAS, including rocket-sled runs up to that speed. This comes from an Armstrong Laboratory / USAF evaluation of the K-36D (1990s), seen via search; DTIC fetch blocked — [DTIC ADA321294](https://apps.dtic.mil/sti/pdfs/ADA321294.pdf)
- Operational K-36D ejections are reported at 729 KEAS and Mach 2.6 (forum, weak). Envelope claims vary: tests from a MiG-25 up to Mach 2.5 at 56,000 ft (forum), versus up to 82,000 ft MSL and Mach 2.5 (SOFREP) — [army.ca forum](https://army.ca/forums/threads/pilot-ejection-fighter-crash.37422/); [DCS forum](https://forum.dcs.world/profile/6663-congo/content/page/2); [SOFREP](https://sofrep.com/news/downed-russian-su-24m-aircrew-escape-and-survival)
- The K-36D-3.5 (designed and manufactured in early 2001) mainly improves anthropometric accommodation, for sitting heights of 810–980 mm; no separate published envelope was found — [Wikipedia, NPP Zvezda K-36](https://en.wikipedia.org/wiki/NPP_Zvezda_K-36); [Google Arts & Culture, Zvezda exhibit](https://artsandculture.google.com/exhibit/wRgo-XRc)

**SR-71 SR-1 seat and the 1966 breakup**
- The SR-71 ejection seat was qualified for about 230 m/s (450 KEAS) for the Air Force application (NASA document on Shuttle Orbiter seat heritage) — [NASA NTRS 19800015008](https://ntrs.nasa.gov/api/citations/19800015008/downloads/19800015008.pdf)
- The SR-1 is described as a low-q seat; the aircraft essentially never exceeded about 450 KEAS (forum) — [F-16.net forum, "High-Q bailouts"](https://www.f-16.net/forum/viewtopic.php?p=8328)
- Breakup on 25 Jan 1966, SR-71 61-7952, at Mach 3.18 and 78,800 ft, after an inlet unstart. Weaver survived without ejecting; by his own account he was thrown clear of the disintegrating aircraft, protected by his pressure suit. Zwayer's parachute functioned, but his neck was broken during the breakup. Weaver's survival should not be read as evidence that a Mach 3 breakup is generally survivable — [Aviation Safety Network](https://cdn.aviation-safety.net/wikibase/162372); [The Aviationist](https://theaviationist.com/2015/03/17/sr-71-mid-air-disintegration/); [Weaver account (EAA)](https://chapters.eaa.org/eaa10/-/media/9c4eaaa9dca04ed5b6a13f37a2d50767.ashx); [Gigazine summary](https://gigazine.net/gsc_news/en/20220611-sr-71-pilot-accident)
- An essay on survivability of high-altitude, high-Mach ejection: [Rob Tow, "Cold Equation Ejection"](https://www.tauzero.com/Rob_Tow/essays/cold-equation-ejection.pdf)

**Encapsulated seats and crew modules [1960s–1990s]**
- **B-58:** the first production aircraft with escape capsules. Individual encapsulated seats were provided because conventional seats were unusable at Mach 2 above 40,000 ft. Each capsule had a control stick, oxygen bottle and drogue chute — [Wikipedia, Escape crew capsule](https://en.wikipedia.org/wiki/Escape_crew_capsule); [AerospaceWeb, B-58](https://aerospaceweb.org/aircraft/bomber/b58/)
- **XB-70:** individual clamshell encapsulated seats, rocket-sled tested and pressurised, designed for ejection up to Mach 3 at above 70,000 ft. In the 8 Jun 1966 collision with an F-104, Al White ejected in his capsule but was seriously injured when his arm was caught in the closing clamshell. Carl Cross did not survive: either his seat did not retract into the capsule, or he could not reach the handle under spin loads (sources differ) — [Virginia Tech XB-70 presentation](https://archive.aoe.vt.edu/mason/Mason_f/XB70PresS07.pdf); [National Interest](https://nationalinterest.org/blog/buzz/xb-70-valkyrie-rise-and-fall-americas-mach-3-bomber-207853); [Ejection Site, NAA](http://www.ejectionsite.com/naa.htm); [Military Wiki, Escape crew capsule](https://military-history.fandom.com/wiki/Escape_crew_capsule)
- **F-111:** whole-cabin ejection. Both side-by-side seats sit in a single module of about 3,000 lb that rockets clear, descends under parachute, and serves as a survival shelter — [Wikipedia, Escape crew capsule](https://en.wikipedia.org/wiki/Escape_crew_capsule)

### Inferences
- **Design implication:**
  - At Mach 3 and 75,000–80,000 ft, dynamic pressure is about 400–450 KEAS (SR-71 class). That is inside the US16E, ACES 5 and K-36 KEAS ratings, but **above all their altitude ceilings** of 50,000–60,000 ft.
  - The issues at Mach 3 are aerodynamic heating of the occupant (stagnation temperatures of several hundred °C), deceleration from very high true airspeed, and the time spent above the Armstrong limit.
  - An open seat therefore needs a full pressure suit plus a stabilised free-fall and aneroid-delayed parachute deployment. Without a suit, a capsule is needed.
  - At low altitude and Mach 1.5+, KEAS exceeds 600–750 KEAS, so the flight-control system or envelope protection must keep the jet within the seat's KEAS limit when escape is likely. Alternatively, accept a non-survivable corner of the envelope, as legacy designs did.
- **Trade for a single-seat LO fighter:**
  - Capsule: large weight and volume penalty (F-111 module about 3,000 lb for two seats) plus LO-shaping constraints on the module separation lines. Historical reliability was poor (XB-70).
  - Advanced seat with full pressure suit: SR-71 precedent, lighter, but a pilot comfort and g-tolerance penalty.
- Seat and helmet mass must be integrated. The US16E has a 103–245 lb occupant range and the HMD is limited to 550 KEAS.

### Gaps
- The SR-71 SR-1 seat's full envelope (minimum altitude, maximum Mach, sequence timing) was not retrieved; sr-71.org and NTRS fetches were blocked.
- No primary Zvezda envelope for the K-36D-3.5 was found. The KM-1 seat on the MiG-25 (the speed reference) could not be searched because the budget was exhausted.
- No published ACES 5 envelope chart (KEAS versus altitude) was found.
- No numerical B-58 capsule or F-111 module KEAS/Mach envelope was found. Widely quoted B-58 tests (including a bear ejected at supersonic speed in 1962) were not verified.
- No data was found on occupant heating during Mach 3 open-seat ejection.

---

## 8. Canopy and windshield at Mach 3 (temperatures, materials, optics), LO canopy coatings, human g-tolerance and G-LOC

### Takeaway
SR-71 windshields reached about 600–620 °F at Mach 3+ cruise and used solid quartz (often quoted as 1.25 in thick, unverified) to avoid optical distortion, with Corning-developed glass. Relaxed human g-tolerance is about 4.9 g at slow onset (secondary source), rising to 8–9 g with anti-g straining (AGSM), pressure breathing (Combat Edge) and suits. Rapid onset removes cardiovascular compensation time and causes abrupt G-LOC. No open source was found on LO canopy coating specifics, which is expected given security restrictions.

### Cited Findings
**SR-71 windshield and canopy**
- During sustained Mach 3 flight, surface temperatures were about 800 °F (427 °C) at the nose, 1,200 °F (649 °C) at the engine cowlings and 620 °F (327 °C) at the cockpit windshield (secondary) — [Simple Flying](https://simpleflying.com/how-sr-71-blackbird-flew-so-fast-windshield-hot-cook-food/)
- The airframe ran at 600–900 °F depending on altitude — [Smithsonian NASM, Ask an Explainer](https://howthingsfly.si.edu/ask-an-explainer/when-sr-71-blackbird-mach-3-how-hot-airframe)
- The titanium skin ran at about 620 °F at Mach 3.2, and the aircraft grew 3–4 in in length — [19FortyFive, Sep 2026](https://www.19fortyfive.com/2026/09/the-lockheed-sr-71-blackbird-came-back-from-every-mission-3-to-4-inches-longer-than-it-took-off-at-mach-3-2-the-titanium-skin-ran-around-620-degrees-fahrenheit-so-lockheed-built-the-panels-loose-on/)
- Skunk Works chose solid quartz for the windshield to prevent blur and distortion, after Corning spent years developing it. The canopy is quoted as 1.25 in solid quartz, hot to the touch from inside; crews could not keep gloved hands near the glass for more than a few seconds. Thickness comes from secondary or social-media sources and is unverified — [Simple Flying](https://simpleflying.com/how-sr-71-blackbird-flew-so-fast-windshield-hot-cook-food/); [The Aviation Geek Club](https://theaviationgeekclub.com/did-you-know-the-solid-quartz-glass-of-the-canopy-of-the-sr-71-blackbird-cockpit-was-1-25-inches-thick-and-was-hot-to-the-touch-from-the-inside/)
- NASA's SR-71 fact sheet and a CIA reading-room document confirm the Mach 3+ envelope but not the window specifics — [NASA Dryden FS-030](https://www.nasa.gov/centers/dryden/pdf/495839main_FS-030_SR-71.pdf); [CIA Reading Room, "SR-71 impressive in high-speed regime"](https://www.cia.gov/readingroom/node/1698307)

**g-tolerance and G-LOC**
- Subjects can tolerate 8–9 g "relaxed" or with minimal AGSM when protected (Morgan, 1992, guidelines for a high-sustained-g R&D programme) — [PubMed 11538544](https://pubmed.ncbi.nlm.nih.gov/11538544)
- Under slow-onset centrifuge testing, mean relaxed tolerance is about 4.9 g and straining tolerance about 7.9 g (secondary, unverified) — [Biology Insights](https://biologyinsights.com/how-to-withstand-g-force-training-and-techniques/)
- Combat Edge combines positive pressure breathing with a counter-pressure vest. It reduces fatigue and extends g-duration tolerance, but carries a lung over-inflation risk — [Air & Space Forces Magazine, "G-Lock and the Fighter Jock"](https://www.airandspaceforces.com/article/1091glock/); [PubMed 11538544](https://pubmed.ncbi.nlm.nih.gov/11538544)
- AGSM: maximal contraction of skeletal muscles combined with a breathing cycle (about 3 s breath-hold and strain, then rapid exhale and inhale). Rapid-onset snap manoeuvres leave no time for cardiovascular compensation — [Navy P-868, AGSM](https://navyflightmanuals.tpub.com/P-868/The-Anti-G-Straining-Maneuver-94.htm); [Air & Space Forces Magazine](https://www.airandspaceforces.com/article/1091glock/)
- Anti-g suit history and principles (USAF ALS/AFE) — [USAF ALS-AFE, "The Anti-G Suit"](https://usafals-afe.net/wp-content/uploads/2014/02/The-Anti-G-Suit.pdf); [AGSM narrative review (2024)](https://www.researchgate.net/publication/384292267_Anti-G_Straining_Maneuver_a_narrative_review)

### Inferences
- A Mach 3 LO canopy must meet four conflicting demands:
  - Withstand about 300–330 °C outer-surface temperatures.
  - Keep optical distortion low enough for an HMD, HUD and DAS-aligned symbology.
  - Carry an RCS-reducing conductive (metallised, for example ITO or gold) film. The F-22/F-35 use such films, but no open data was found.
  - Remain compatible with through-canopy or canopy-jettison ejection at up to Mach 3.
- Stretched acrylic and polycarbonate (current fighters) soften well below SR-71 windshield temperatures. Fused silica or quartz, or glass-ceramic, front windscreens with a small, heavily framed canopy, as on the SR-71 and MiG-25, are the historical answer. This trades away pilot visibility, which DAS-style sensors and an HMD can partly restore (Section 5).
- G-protection design: plan the full ATAGS/Combat Edge-class ensemble plus a pressure suit for altitude. The combined garment must work at both 9 g and above 63,000 ft without the valve and inflation failure modes seen on the F-22 (Section 6). Flight-control law onset-rate limiting (g-onset rate, as with F-16 and F-22 limiters) is a design lever against G-LOC, along with Auto-GCAS-style recovery.

### Gaps
- No open source was found on LO canopy coatings (materials, sheet resistance, optical transmission) for the F-22, F-35 or F-117. Such data is likely restricted, and the team should not seek it beyond public literature.
- No primary data on SR-71 windshield construction (layers, thickness) or MiG-25 windscreen temperatures and materials was retrieved; sr-71.org fetch was blocked and the search budget was exhausted.
- No primary centrifuge data on relaxed g tolerance versus onset rate was found (the 4.9/7.9 g figures are secondary). No data was found on the MiG-25 g-limit (commonly 4.5 g supersonic); unverified.
- No source was found on cockpit thermal comfort limits (for example, wet-bulb globe temperature) for Mach 3 cockpits.
