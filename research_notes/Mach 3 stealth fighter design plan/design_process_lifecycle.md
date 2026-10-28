# Fighter Aircraft Pre-Build Development Lifecycle (Mission Analysis to Drawing Release, Before Cutting Metal)

> Research method and limits (read first). Compiled 2026-10-28. Full-page fetching was blocked in this session: the network allowlist rejected aaf.dau.edu, globalsecurity.org, flightglobal.com, dtic.mil, gao.gov, ecfr.gov, eur-lex and others (DNS ENOTFOUND). The shared web-search budget also ran out after about 22 queries. So every "Cited Finding" below comes from search-engine extracts of the cited page, not from a full read. Numbers should be checked against the original before they go into blueprints or calculations. Some well-known facts could not be retrieved. They appear only under "Gaps" with the label UNVERIFIED (background knowledge, not retrieved this session). The report writer should not present them as sourced.
> Recency labels: [CURRENT 2025-26] = policy or news from 2025 to 2026; [HISTORICAL] = older program data, which still serves as a benchmark.

---

## 1. Standard pre-prototype phases and their concrete outputs (Raymer / Roskam / Nicolai & Carichner / Jenkinson)

### Takeaway
The textbook process has three phases: conceptual design (many configurations, rough sizing, narrowing to one), preliminary design (one concept; weights and performance refined; loft/OML defined; the go/no-go decision for full-scale development), and detail design (the actual parts, production and tooling design, ending in drawing release and manufacturing). A requirements/mission-analysis step comes first and feeds conceptual design. For a two-person digital study, the realistic scope is the whole of conceptual design plus the front half of preliminary design.

### Cited Findings
- Raymer's *Aircraft Design: A Conceptual Approach* is the standard citation for splitting aircraft design into **conceptual, preliminary, and detailed design** — [engrXiv preprint](https://engrxiv.org/preprint/view/4286/version/5841/7448)
- Conceptual phase: "take the vague idea of an aircraft, work up a bunch of different alternatives, and finally narrow down to one main configuration to take forward" — [Project Raven (Substack)](https://projectraven.substack.com/p/conceptual-design-part-2-towards)
- In Raymer's design flow chart, preliminary design starts when a **"single concept [is] selected"**, and its goal is to **finalize weight and performance estimates** — [Raymer, "How Raymer Wrote ADACA" slide deck, aircraftdesign.com](https://aircraftdesign.com/wp-content/uploads/2024/04/HowRaymerWroteADACA.pdf)
- Preliminary design should give confidence that the aircraft **can be built on time and at the estimated cost**. Detail design includes **production design**, where specialists decide how the aircraft will be fabricated, and it **ends with manufacturing** — summarised from [engrXiv preprint](https://engrxiv.org/preprint/view/4286/version/5841/7448) and [Project Raven](https://projectraven.substack.com/p/conceptual-design-part-2-towards). The search tool did not say which of the two made which claim.
- Raymer's table of contents has a dedicated topic **"Configuration layout and loft"**, placed after the early conceptual sizing chapters — [CiNii catalog record, Raymer](https://ci.nii.ac.jp/ncid/BD08545725); [aircraftdesign.com deck](https://aircraftdesign.com/wp-content/uploads/2024/04/HowRaymerWroteADACA.pdf)
- A Russian design bureau uses the same idea under different names. Ilyushin engineers argue that contradictions and excessive requirements in the customer's tactical-technical assignment (TTZ) should be found **already at the technical-proposal and avanproekt stages**, to cut the risk of project failure — [Vestnik SSAU (Samara Univ.) article by Ilyushin Aviation Complex authors](https://journals.ssau.ru/vestnik/article/download/2288/2309)

### Inferences
- A concrete set of deliverables per phase can be put together from the sources above. The Gaps section adds more detail from standard texts, but that part is unverified.
  - **Requirements/mission analysis**: ConOps, design mission profile(s), threat and signature goals, threshold/objective requirement table.
  - **Conceptual design**: constraint diagram (T/W against W/S), first-cut sizing (fuel fraction and takeoff gross weight), several candidate layouts, trade studies, a down-select to one configuration, and a three-view plus inboard profile.
  - **Preliminary design**: lofted OML, structural arrangement, refined weights/CG, aero and propulsion decks, performance and cost estimates, wind-tunnel and CFD validation, then configuration freeze.
  - **Detail design**: part drawings and models, tooling, manufacturing planning, and drawing release.
- Raymer's flow chart puts the "single concept selected" point at the boundary between conceptual and preliminary design. Configuration freeze is therefore an *output* of late conceptual or early preliminary design, not of detail design.

### Gaps
- Full Raymer / Roskam / Nicolai & Carichner / Jenkinson phase text could not be retrieved, because the books are not openly accessible and fetching was blocked. **UNVERIFIED (background knowledge):**
  - Raymer Ch. 2 says preliminary design "begins when the major changes are over" (for example, canard vs aft tail is already decided). Its key activities are **lofting**, structural and subsystem design by specialists, wind-tunnel testing and CFD, and an actual cost estimate. Raymer describes the end of preliminary design as the point where the company "bets the company" on full-scale development.
  - In Raymer's account, detail design designs the real parts (ribs, spars, skins), the tooling and fabrication processes, and test hardware such as flight simulators and "iron bird" systems rigs.
  - Roskam's *Airplane Design* Parts I–VIII follows a Class I → Class II method structure (weight sizing → configuration → Class II weight/drag/stability).
  - Nicolai & Carichner (*Fundamentals of Aircraft and Airship Design*, AIAA, 2010) begins with mission requirements and constraint analysis.
  - Jenkinson, Simpkin & Rhodes (*Aircraft Design Projects*, 2003) gives the project phases as problem definition → concept → preliminary → detailed.
  - None of these were confirmed this session.
- No open source was found for typical person-hours by phase from these textbooks.

---

## 2. US DoD structure (Adaptive Acquisition Framework, DoDI 5000.02 / 5000.85; MSA–TMRR–EMD; Milestones A/B/C) and technical reviews (ASR, SRR, SFR, PDR, CDR, TRR, PRR)

### Takeaway
In DoD terms, "everything before a physical prototype" covers Materiel Solution Analysis (MSA, ending at Milestone A) and Technology Maturation & Risk Reduction (TMRR, which includes SRR, SFR and normally PDR before Milestone B). CDR, the design-freeze and drawing-release gate, sits early in EMD. [CURRENT 2025-26] The framework is being restructured. JCIDS was terminated by memos in August and November 2025. PEOs are being reorganized into Portfolio Acquisition Executives. DAU logged a Change 2 to DoDI 5000.02 on 8 Apr 2026. The MSA/TMRR/EMD logic and the review sequence remain the reference model for engineering.

### Cited Findings
- **Milestone A** approves entry into TMRR, approves the program acquisition strategy, and authorizes release of the final RFP for TMRR. It also sets the **exit criteria for TMRR and entrance criteria for EMD** — [DAU AAF, Milestone A](https://aaf.dau.edu/mca/milestone-a/)
- **PDR before Milestone B**: "Unless waived by the MDA, a preliminary design review (PDR) will be conducted prior to Milestone B" — [DAU AAF, Milestone B](https://aaf.dau.edu/mca/milestone-b/)
- **Milestone B** authorizes entry into EMD and commits the investment needed to award phase contracts. The MDA "formally initiate[s] the program by approving the acquisition program baseline (APB)" — [DAU AAF, Milestone B](https://aaf.dau.edu/mca/milestone-b/)
- At Milestone B, T&E tells the MDA whether technology, engineering, integration and safety risks "are understood and have been adequately mitigated", and whether the system "has met or exceeds all T&E-related TMRR phase exit criteria" — [OSD T&E Enterprise Guidebook, Ch. 4](https://www.test-evaluation.osd.mil/Portals/120/Documents/TE%20Enterprise%20Guidebook/Ch4%20from%20TE%20Enterprise%20Guidebook%208.02.pdf)
- The DoDI 5000.85 copy found is dated **6 Aug 2020, Change 1 dated 4 Nov 2021** — [DoDI 5000.85 (WHS)](https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500085p.pdf); [DAF supplement copy](https://static.e-publishing.af.mil/production/1/saf_aq/publication/dodi5000.85_dafi63-151/dodi5000.85_dafi63-151.pdf). [Possibly superseded; see below]
- [CURRENT 2026] The DAU policy change log lists **"8 Apr 2026 – DOWI 5000.02 Operation of the Adaptive Acquisition Framework (Change 2)"**. "DOWI" probably reflects the "Department of War" renaming; it is an incremental change, not a rewrite — [DAU AAF Policies Change Log](https://aaf.dau.edu/aaf/policies-change-log/)
- [CURRENT 2025] An Aug 2025 memo from SecDef Hegseth and DepSecDef Feinberg called for **terminating JCIDS** — [Breaking Defense, Aug 2025](https://breakingdefense.com/2025/08/pentagon-terminating-jcids-process-as-part-of-larger-acquisition-reform-memo/). The Nov 2025 memo "Reforming the Joint Requirements Process to Accelerate Fielding of Warfighting Capabilities" directs removal of JCIDS references from the DoDD 5000-series and DoDD 7045.20, and calls for a new Capability Portfolio Management instruction — [DoD memo PDF](https://media.defense.gov/2025/Nov/10/2003819442/-1/-1/1/REFORMING-THE-JOINT-REQUIREMENTS-PROCESS-TO-ACCELERATE-FIELDING-OF-WARFIGHTING-CAPABILITIES.PDF); [ExecutiveGov](https://executivegov.com/articles/dod-jcids-joint-requirements-process-reform). A new board ties requirements directly to money — [Inside Defense](https://insidedefense.com/node/224995); [MeriTalk](https://www.meritalk.com/articles/pentagon-ends-jcids-in-major-requirements-reform/)
- [CURRENT 2025] The 7 Nov 2025 memo **"Transforming the Warfighting Acquisition System"** sets up **Portfolio Acquisition Executives (PAEs)** by reorganizing PEOs. PAEs report directly to the Service Acquisition Executive and can shift funds and make trade-offs. The memo also renames DAU the Warfighting Acquisition University — [Holland & Knight, Nov 2025](https://www.hklaw.com/en/insights/publications/2025/11/war-secretary-announces-strategy-regarding-defense-acquisition-reform); [GovCIO Media](https://govciomedia.com/speed-to-capability-hegseths-plan-to-change-how-the-pentagon-buys-tech/). One summary says the DoD 5000 policy is to be updated **within 150 days** to "simplify reviews and consolidate milestones", with portfolio scorecards **within 180 days** — [ExecutiveGov](https://www.executivegov.com/?p=278784)
- Systems engineering technical reviews (SETRs) "establish the technical baselines, assess the system's technical maturity, and review and assess technical risks" — [DAU AAF, Technical Reviews](https://aaf.dau.edu/aaf/mca/tech-reviews/)
- Reviews are **event-driven**. They are held when entrance criteria documented in the **Systems Engineering Plan (SEP)** are met (IEEE 15288.2-derived guidance). SRR should wait until the Chief Engineer's SEP criteria are met and prior reviews are closed — [AcqNotes, SE Technical Reviews](https://acqnotes.com/acqnote/careerfields/se-technical-reviews-and-audits); [AcqNotes, SRR](https://acqnotes.com/acqNote/system-requirements-reviewsrrse)
- **ASR** follows concept studies, when a preferred system concept is selected — [DAU *Systems Engineering Fundamentals* (2001) via ez-pdh](https://cdn.ez-pdh.com/course-material/Systems-Engineering-Fundamentals-Part-2.pdf) [HISTORICAL text]
- **SRR** confirms "that the developer understands the system requirements and is ready to proceed with the initial system design" — [AcqNotes, SRR](https://acqnotes.com/acqNote/system-requirements-reviewsrrse)
- **SFR** typically takes place in TMRR. A successful SFR "reduces the risk of continuing the technical effort toward the PDR". DAU cites IEEE 15288.2 as a resource — [DAU AAF, SFR](https://aaf.dau.edu/aaf/mca/sfr)
- **PDR** focuses on subsystem and configuration-item design at the **allocated baseline** — [NDIA 2009 SE conference slides](https://ndia.dtic.mil/wp-content/uploads/2009/systemengr/8883WednesdayTrack4Eischens.pdf) [HISTORICAL]
- In Korea's KF-21 program (non-US example), the **CDR ran 24–26 Sept 2019**. About **390 technical data items** were reviewed "to ensure that the military requirements were properly reflected in the design", and the review cleared the program for prototype production — [FlightGlobal](https://www.flightglobal.com/k-fx-cdr-sets-stage-for-prototype-production/134497.article)

### Inferences
- Mapping to the team's study:
  - The mission/ConOps and requirements work corresponds to the analytic content of MSA through an internal ASR/SRR.
  - The configuration down-select and functional allocation correspond to SFR.
  - A lofted, sized and weighed configuration with subsystem allocations corresponds to PDR-level maturity.
  - CDR-level maturity (an approved build-to design with drawings released) is the stated end-state "blueprints".
  - A two-person team can borrow the *entry/exit checklist discipline* of these reviews, held as self-reviews or with outside peers, without any contractual meaning.
- Because the 2025-26 reforms promise to "consolidate milestones", the report should present Milestones A/B/C as the long-standing reference model and note that the formal milestone structure is changing in 2026.

### Gaps
- No full-text entry/exit criteria for CDR, TRR, PRR, SVR/FCA or PCA were retrieved; fetching DAU was blocked. **UNVERIFIED (background knowledge):**
  - SRR establishes the **functional baseline** (system spec); PDR establishes the **allocated baseline**; CDR establishes the **initial product baseline** ("build-to" design, with roughly 75–90% of drawings released, a common rule of thumb).
  - TRR comes before formal test.
  - PRR (Production Readiness Review) assesses manufacturing readiness before Milestone C/LRIP.
  - **MIL-STD-1521B** (1985) defined SRR, SDR, SSR, PDR, CDR, TRR, FCA, PCA, FQR and PRR, and was cancelled in 1995.
  - **IEEE 15288.2-2014** ("Technical Reviews and Audits on Defense Programs") was adopted by DoD around 2015 as its replacement.
  - The current **DoD Systems Engineering Guidebook** (OUSD(R&E), Feb 2022) and DoDI 5000.88 (Engineering of Defense Systems, Nov 2020) hold the current review descriptions.
- Whether the promised 150-day rewrite of DoD 5000 policy (with consolidated milestones) was published by Oct 2026 could not be confirmed. Only the 8 Apr 2026 "Change 2" entry was found.
- The final FY2026 NDAA text on JROC/requirements could not be confirmed.

---

## 3. Requirements definition: ICD/CDD/KPPs, how fighter requirements are traded (ATF → F-22), and trade-study documentation

### Takeaway
Fighter requirements typically start as a capability gap. They are then refined through industry RFIs and concept studies into a requirements set with threshold/objective values. The ATF case shows the pattern: an RFI in 1981, 19 industry concepts, requirements that settled by late 1984 (50,000 lb takeoff gross weight, 800 mi radius, Mach 1.4–1.5 supercruise, 2,000 ft runway), and stealth sharply raised in Dec 1985. The ATF requirement for sustained speed was supercruise around Mach 1.5, not Mach 3, and affordability ($35M flyaway goal) was used during Dem/Val to decide which capability could be bought. [CURRENT 2025-26] The US formal JCIDS ICD/CDD system was terminated in 2025.

### Cited Findings
- The ATF concept dates to **1971**. The USAF issued an ATF **RFI in 1981** (June per some sources, May per others) to **9 companies**; **7 responded with 19 concepts** — [Wikipedia, Advanced Tactical Fighter (pointer)](https://en.wikipedia.org/wiki/Advanced_Tactical_Fighter); [AFMC History Office, "Flashback: Northrop YF-23"](https://www.afsc.af.mil/News/Article/2919531/flashback-northrop-yf-23-black-widow-ii/) [HISTORICAL]
- The design parameters evolved from **"Reduced RCS" to "Low Observability"**, and supercruise, advanced avionics/radar and high maneuverability were added. "Stealth requirements were **drastically increased in December 1985**" — [Wikipedia, ATF](https://en.wikipedia.org/wiki/Advanced_Tactical_Fighter)
- By late 1984 the requirements had settled on **50,000 lb (23,000 kg) MTOW, 800 mi (1,300 km) mission radius, supercruise Mach 1.4–1.5, and a 2,000 ft (610 m) runway**. One popular source says the runway was later changed to 910 m, so treat that detail with caution — [Wikipedia, ATF](https://en.wikipedia.org/wiki/Advanced_Tactical_Fighter); [Defencyclopedia](https://defencyclopedia.com/2015/04/18/f-22-raptor-the-story-of-the-worlds-deadliest-fighter/)
- The Dem/Val RFP was issued in **Sept 1985**. The Lockheed team won the EMD contract in **Aug 1991** — [Wikipedia, ATF](https://en.wikipedia.org/wiki/Advanced_Tactical_Fighter)
- Air Force History Office: both YF-22 and YF-23 met ATF requirements, but the USAF "had more confidence in Lockheed and Pratt & Whitney to 'manage' the program". Program-management credibility was a selection factor — [AFMC Flashback (article)](https://www.afsc.af.mil/News/Article/2919531/flashback-northrop-yf-23-black-widow-ii/); [PDF](https://media.defense.gov/2022/Feb/01/2002931130/-1/-1/1/YF-23%20FLASHBACK%20(1).PDF)
- Dem/Val "became a means to determine what capability could be afforded within the **$35 million flyaway-cost goal**" — [GlobalSecurity, F-22 cost](https://www.globalsecurity.org/military/systems//aircraft/f-22-cost.htm) [HISTORICAL; then-year dollars]
- Russian practice: Ilyushin authors recommend finding contradictions, inconsistencies and **excessive requirements in the TTZ** early, at the technical proposal and avanproekt stages — [Vestnik SSAU](https://journals.ssau.ru/vestnik/article/download/2288/2309)
- [CURRENT 2025] JCIDS (the Joint Staff process "used to identify gaps in military capabilities and validate joint requirements") is being terminated and replaced by a requirements/resourcing alignment board and capability portfolio management — [Breaking Defense](https://breakingdefense.com/2025/08/pentagon-terminating-jcids-process-as-part-of-larger-acquisition-reform-memo/); [DoD Nov 2025 memo](https://media.defense.gov/2025/Nov/10/2003819442/-1/-1/1/REFORMING-THE-JOINT-REQUIREMENTS-PROCESS-TO-ACCELERATE-FIELDING-OF-WARFIGHTING-CAPABILITIES.PDF)

### Inferences
- The ATF history is the closest real precedent for the team's speed-vs-stealth tension. When stealth was "drastically increased" (Dec 1985), the speed requirement stayed at **supercruise Mach 1.4–1.5**, not Mach 2+ dash as the primary sizing driver. A Mach 3 + radar/IR LO requirement is therefore outside any precedent in these sources. The team's requirements document should record speed against signature as an explicit threshold/objective trade rather than treating both as fixed.
- The ATF also used a cost target ($35M flyaway) as a requirement that Dem/Val traded against. A two-person study can do the same with an explicit weight or cost cap.
- A recommended structure for trade studies (inferred, since no source on trade documentation was retrieved): objective, alternatives, evaluation criteria with weights tied to requirement IDs, method and data, scoring and sensitivity, recommendation, and decision record.

### Gaps
- No primary source was retrieved for ICD/CDD/KPP/KSA definitions (CJCSI 5123.01 / JCIDS Manual), or for which documents replace them after the 2025 termination. **UNVERIFIED (background knowledge):**
  - ICD = Initial Capabilities Document (the gap). CDD = Capability Development Document (performance attributes with threshold/objective values).
  - KPPs are the attributes whose threshold failure triggers program re-evaluation. The JCIDS Manual listed mandatory KPPs including Force Protection, System Survivability, Sustainment, Energy, Net-Ready and Training.
  - KSAs are a second tier of attributes.
- Detailed ATF trade data (for example, how many supercruise vs maneuverability vs LO trade points were studied, or the 1987 weight growth) could not be retrieved.
- No open source on standard trade-study templates (for example, the DAU trade study guide or INCOSE handbook) was retrieved.

---

## 4. Digital engineering and MBSE (digital thread, digital twin, SysML; T-7A eSeries, NGAD/F-47, Lockheed Martin)

### Takeaway
The publicly reported pre-build product of a "digital-first" program is a model-based definition: a 3D master model, integrated analysis models, and model-based systems engineering. The aim is to catch problems before metal is cut. Boeing says the T-7 went from firm concept to first flight in 36 months, with 75% better first-time quality and 80% fewer assembly hours. These are company claims. The USAF Secretary said in 2023 that digital engineering had been "overhyped". [CURRENT 2025-26] F-47 (NGAD) received EMD in Mar 2025, construction began in 2025, and first flight is targeted for 2028, partly enabled by earlier NGAD X-plane flying.

### Cited Findings
- The T-7A completed its first flight with the USAF on **28 June 2023** — [Mobility Engineering Tech](https://www.mobilityengineeringtech.com/component/content/article/48967-boeing-t-7a-completes-first-flight); [Manufacturing.net](https://www.manufacturing.net/aerospace/news/22866210/boeing-completes-t7a-first-flight-with-us-air-force)
- Boeing says it went "from the concept of what would become the T-7 to its first flight in **three years**" using model-based engineering tools and advanced manufacturing — [Defense News, Dec 2021](https://www.defensenews.com/air/2021/12/17/the-t-7-takes-shape-inside-the-factory-where-the-air-forces-next-trainer-is-being-built)
- Boeing claims model-based engineering, 3D design and advanced manufacturing **increased first-time quality by 75%** and **reduced assembly hours by 80%**. Model-based engineering "enabled testing throughout the aircraft's design and build to help ensure safety before the first flight" (company-reported, not independently verified) — [Aerospace Manufacturing & Design](https://www.aerospacemanufacturinganddesign.com/news/boeing-t-7a-completes-first-flight-us-air-force); [Defence Connect](https://defenceconnect.com.au/air/12265-boeing-completes-inaugural-t7-trainer-flight-for-us-air-force)
- Boeing said it resolved a **wing-rock issue at high angle of attack** partly through digital engineering. The War Zone notes the benefits look "less revolutionary than early hype", and that SecAF **Frank Kendall said in May 2023 that digital engineering had been "overhyped"** — [The War Zone](https://www.twz.com/the-t-7a-red-hawk-jet-trainer-has-taken-its-first-flight)
- [CURRENT 2025] On **21 Mar 2025** the Department of the Air Force awarded Boeing the **EMD contract for the NGAD platform (F-47)**. Lockheed Martin was the only remaining rival after Northrop Grumman withdrew — [Wikipedia, Boeing F-47 (pointer)](https://en.wikipedia.org/wiki/Boeing_F-47); [GovExec/Defense One](https://spaceproject.govexec.com/defense/2025/03/boeing-wins-air-forces-next-gen-fighter-contract/403957)
- [CURRENT 2025-26] In Sept 2025 Gen. Allvin said Boeing had begun building the first F-47, with first flight expected in **2028**. Air Force leaders reiterated in **July 2026** that the first F-47 is "on track to fly in 2028" — [Janes, AFA 2025](https://www.janes.com/defence-intelligence-insights/defence-news/air/afa-2025-usaf-targets-2028-for-first-flight-of-f-47); [The Defense Post](https://thedefensepost.com/2025/09/23/first-f47-flight-2028/amp/); [ClearanceJobs](https://news.clearancejobs.com/2025/09/24/race-with-china-accelerates-as-boeing-starts-work-on-f-47-fighter/). One source says "by end of term, early 2029", a minor discrepancy.
- The F-47's accelerated pace was "made possible by NGAD X-plane efforts", meaning full-scale demonstrators flown before EMD — [The War Zone](https://www.twz.com/air/f-47-programs-accelerated-pace-made-possible-by-ngad-x-plane-efforts.md)
- A headline reports the F-47 "will fly three years before its new engine is ready" (headline only; lower-quality outlet) — [SOFREP](https://sofrep.com/news/americas-first-sixth-generation-fighter-will-fly-three-years-before-its-new-engine-is-ready/)

### Inferences
- The "36 months" T-7 figure most likely refers to the original Boeing–Saab T-X demonstrator (concept ~2013 → first flight Dec 2016), not to the June 2023 USAF production-representative flight. The two should not be conflated. This is inferred from the dates; the source did not say so explicitly.
- For a two-person digital study, "digital-first" in practice means:
  - one parametric master geometry (OML loft) that every analysis references;
  - a requirements model, possibly in SysML, with traceability from each requirement to the analyses and parts that satisfy it;
  - version-controlled analysis decks (weights, aero, propulsion, performance, RCS/IR);
  - documented verification evidence.
  These are scaled-down versions of a digital thread.

### Gaps
- No source on the DoD Digital Engineering Strategy (June 2018), DoDI 5000.97 *Digital Engineering* (Dec 2023), or official definitions of digital thread and digital twin could be retrieved because the search budget ran out. **UNVERIFIED (background knowledge):**
  - The 2018 Strategy lists five goals: formalize model use; provide an authoritative source of truth; incorporate technological innovation; establish infrastructure and environments; transform culture and workforce.
  - DoDI 5000.97 (21 Dec 2023) requires digital engineering on new programs unless waived.
  - The "eSeries" label (eT-7A, then NGAD/F-47 and the GBSD/Sentinel) came from then-ASAF(AT&L) Will Roper's 2020 paper "There Is No Spoon: The New Digital Acquisition Reality".
- No retrieved source covers Lockheed Martin's specific digital-engineering practices (e.g., F-35 digital thread, Skunk Works) or SysML usage on fighter programs.
- No GAO report on NGAD/F-47 digital engineering was retrieved.

---

## 5. Verification before first flight (wind tunnel, CFD, RCS, engine test cells, iron bird/SIL, static/fatigue, simulators, MIL-STD-882E, MIL-HDBK-516C, TRL/MRL)

### Takeaway
Before first flight, programs build up evidence on several fronts at once:
- **Wind-tunnel campaigns** lasting tens of thousands of hours. F-22 lineage: ~7,000 h pre-Dem/Val, ~19,200 h Dem/Val on the YF-22 configuration, ~17,700 h in early EMD, ~43,900 h total. KF-21: a 13,000 h plan, ≥2,000 h subsonic at KARI and >3,000 h transonic at Calspan.
- **Airworthiness** assessed against MIL-HDBK-516C (current Change Notice 9, Nov 2024) or its European derivative EMACC.
- **System safety** under MIL-STD-882E's 4×6 severity/probability Risk Assessment Code scheme.
- **Technology maturity gates**: TRL 6 for critical technologies by Milestone B, and about MRL 6 for manufacturing.

### Cited Findings
- **F-22 wind-tunnel hours** [HISTORICAL]: **7,005 h** pre-Dem/Val; **19,195 h** during Dem/Val on the YF-22 configuration; **17,689 h** in the 1991–1996 F-22 (EMD) test program; grand total **43,889 h** on YF-22/F-22 configurations — [GlobalSecurity, F-22 test](https://www.globalsecurity.org/military/systems/aircraft/f-22-test.htm). Code One gives "nearly **44,000** wind tunnel test hours" — [Code One, "F-22 Milestones, Part 1"](https://www.codeonemagazine.com/article.html?item_id=88). Separately, search extracts say the Lockheed team "would conduct nearly **18,000** hours" in Dem/Val. The extract did not make clear which page this came from; candidates are [Code One](https://www.codeonemagazine.com/f35_article.html?item_id=88) or [Wikipedia, F-22](https://en.wikipedia.org/wiki/Lockheed_Martin_F-22_Raptor). It is consistent with the 19,195 h Dem/Val actual.
- **KF-21 wind tunnel** [2016–2022]:
  - **13,000 h** of combined wind-tunnel testing was planned in 2016, with the final design to be completed in about two years — [Korea Times, 22 Jun 2016](https://www.koreatimes.co.kr/amp/southkorea/defense/20160622/s-korea-conducts-wind-tunnel-testing-for-kf-x-jet)
  - KARI ran subsonic wind-tunnel tests **five times totalling 2,000 h** from 2016, from the C-103 model to the prototype — [Asia Economy (asiae), 2021](https://cm.asiae.co.kr/en/article/2021062610075468503) (attribution from search extract; verify)
  - Calspan: "over the last five years … more than **3,000 hours of transonic wind tunnel testing** for KAI" — [Calspan news release](https://calspan.com/company/news/calspan-partners-kai-development-kf-21)
- **KF-21 flight test** [CURRENT Jan 2026]: development flight testing completed with about **1,600 accident-free flights** — [Herald Corp (Korean), 12 Jan 2026](https://www.heraldk.com/article/2026011216453904931); [Hankyung, 13 Jan 2026](https://www.hankyung.com/article/2026011383071)
- **MIL-HDBK-516C** "establishes the airworthiness certification criteria to be used in the determination of airworthiness of all manned and unmanned, fixed and rotary wing air vehicle systems". Sections include **6 Flight Technology, 9 Crew Systems (9.1 escape/egress), 15 Computer Resources** — [EverySpec, MIL-HDBK-516C](https://everyspec.com/MIL-HDBK/MIL-HDBK-0500-0599/MIL-HDBK-516C_52120/); [Dayton Aerospace USAF airworthiness library](https://www.daytonaero.com/usaf-airworthiness-certification-library)
- [CURRENT] The USAF library lists **MIL-HDBK-516C Change Notice 9, dated 25 Nov 2024**. USAF policy: new air systems "must utilize the current version of MIL-HDBK-516 … and its approved Change Notices" — [Dayton Aerospace USAF airworthiness library](https://www.daytonaero.com/usaf-airworthiness-certification-library)
- Section 15 (software) has been compared with USAF **AC-17-01** and **DO-178C** in the academic literature — [Gyeongsang National Univ. scholarworks record](https://scholarworks.gnu.ac.kr/handle/sw.gnu/5296)
- The European equivalent is the **EMACC Handbook** (European Military Airworthiness Certification Criteria), **Edition 3.1 endorsed 25 Sep 2018** by the European Defence Agency. This matters for an EU/Polish team — [EDA EMACC Handbook Ed. 3.1](https://eda.europa.eu/docs/default-source/documents/emacc-hdbk-edition-3-1-endorsed-20180925.pdf)
- **MIL-STD-882E** risk scheme:
  - A Risk Assessment Code (RAC) is "a combination of one severity category and one probability level" (e.g., 1D, 3B).
  - **Severity** levels are 1 Catastrophic to 4 Negligible. **Probability** levels are A Frequent to F Eliminated; F was new in 882E.
  - Matrix cells map to **High / Serious / Medium / Low**, each with a defined risk-acceptance authority (High → Component Acquisition Executive).
  - Tables I–III must be used unless a tailored matrix is formally approved. Programs may add quantitative probability definitions but not change severity definitions.
  - Sources: [DAU SE Brainbook, ESOH Risk Assessment](https://content1.dau.edu/DAUMIG_se-brainbook_189/content/Management%20Processes/ESOH%20Risk%20Assessment.html); [AcqNotes, Assess and Document Risk](https://acqnotes.com/acqnote/tasks/element-3-assess-and-document-risk); [NDIA 2012 system safety slides](https://ndia.dtic.mil/wp-content/uploads/2012/system/track914789.pdf)
- **TRL 6 at Milestone B**: DoD defines readiness as "TRL of 6 for all critical technology elements by MS B". The statute (then 10 U.S.C. 2366b) required the MDA to certify that MDAP technology "has been demonstrated in a relevant environment (TRL 6)" before Milestone B. A TRL alone "is not a comprehensive technology assessment" — [NDIA 2015 slides (Flitter)](https://ndia.dtic.mil/wp-content/uploads/2015/system/17966_Flitter.pdf); [TRA Deskbook record (SE Goldmine)](https://segoldmine.ppi-int.com/node/72226) [statute citation is pre-2021 numbering]
- **MRL at Milestone B**: one vendor guide says MRL 6 ("manufacturing processes are capable and in control in a pilot environment"); another vendor table says MRL 5–6. These are not official DoD policy — [Modus Advanced MRL guide](https://www.modusadvanced.com/manufacturing-readiness-levels-the-complete-guide-for-aerospace-and-defense-engineers); [Modus Advanced MRL vs TRL](https://www.modusadvanced.com/resources/blog/mrl-vs-trl-understanding-the-difference-between-technology-and-manufacturing-readiness)

### Inferences
- The F-22 figures add up exactly: 7,005 + 19,195 + 17,689 = 43,889 h. About 60% of all F-22-lineage tunnel hours (26,200 of 43,889) were logged *before* the EMD contract. Most aerodynamic validation therefore happens in the concept/Dem-Val period, which is the period the team is emulating.
- A two-person team cannot run tunnel or RCS-range testing. The digital substitutes are:
  - CFD across the Mach range, with verification on public validation cases;
  - physical-optics/PO-based RCS estimation;
  - IR signature estimation of the plume and aero-heated skin;
  - a written verification matrix that maps each requirement to its method (analysis, inspection, demonstration, test), following the 516C/EMACC section structure.
- A simplified MIL-STD-882E hazard log (hazard → severity → probability → RAC → mitigation) is cheap to keep and well suited to a design study.

### Gaps
- Not retrieved (search budget exhausted, fetches blocked), with **UNVERIFIED (background knowledge)** notes:
  - **F-35 pre-flight wind-tunnel hours and test articles**: commonly cited F-35 static and durability test airframes are AG-1/BG-1/CG-1 static and AJ-1/BH-1/CJ-1 durability, built after first flight in parallel.
  - **F-22 structural test articles**: dedicated static and fatigue airframes, details not retrieved.
  - **F119/F120 engine ground-test hours before YF-22/YF-23 flight**: not retrieved.
  - **RCS pole testing**: full-scale RCS pole models were tested at outdoor ranges (e.g., Helendale CA, RATSCAT at White Sands) for F-117, F-22 and F-35.
  - **Iron bird / Vehicle Systems Integration labs**, **avionics integration labs**, and **flying testbeds** (e.g., the Boeing 757 F-22 avionics flying testbed, the "CATBird" for F-35).
  - **Engineering/pilot-in-the-loop simulators**.
  - None of these could be sourced this session.
- The current official TRA Deskbook (2023) and DoD MRL Deskbook (2022) were not retrieved. **UNVERIFIED:** TRL 6 = system/subsystem prototype demonstrated in a relevant environment; MRL 6 = capability to produce a prototype in a production-relevant environment; MRL 8 targeted at Milestone C. After 2021 recodification the TRL 6 certification moved from 10 U.S.C. 2366b to 10 U.S.C. 4252.
- No source specific to Mach 3 (aero-thermal test needs, e.g., the SR-71/MiG-25 heating precedent) was retrieved for this note.

---

## 6. Soviet/Russian OKB process (tekhnicheskoe predlozhenie → avanproekt → eskizny proekt → maket/mock-up commission → rabochy proekt → state trials) and TsAGI, CIAM, VIAM, LII

### Takeaway
Russian aviation teaching and professional standards name the pre-build stages as technical proposal → avanproekt → eskizny proekt (preliminary design) → **maket** (full-scale mock-up reviewed by a customer **mock-up commission**) → technical/working design (rabochy proekt), after which prototypes are built. The mock-up commission is the formal gate before prototype construction; for the Yak-152 it was held in Sept 2014. Historically TsAGI reviewed design-bureau plans and models, ran wind-tunnel and structural breaking tests, and issued industry-wide design rules (1949). Su-57/PAK FA: tender April 2002, exterior design approved 10 Dec 2004, design stage declared complete in 2007, first flight 29 Jan 2010, service Dec 2020.

### Cited Findings
- A Novosibirsk State Technical University syllabus on "Organization of an OKB" names the design stages as **"research of the avanproekt, eskizny proekt, rabochy proekt"** — [NSTU course programme](https://www.nstu.ru/studies/study/edu_plans/disc_list/disc_program/download_wp?id=81848)
- A Russian aviation professional standard lists one labour function as "organization of development of the **technical proposal, avanproekt, eskizny proekt, maket and technical project** of an aircraft, its modernization or modification". The page is marked as no longer in force — [ppt.ru professional standard](https://ppt.ru/docs/profstandarts/details/90); [ppt.ru related standard](https://ppt.ru/docs/profstandarts/details/106)
- An avanproekt is described as "preliminary elaboration (fairly coarse, i.e., by units and systems) of the product". This comes from a rocketry/electronics context — [russianelectronics.ru PDF](https://russianelectronics.ru/wp-content/uploads/2022/06/250070.pdf)
- **Mock-up commission example**: for the **Yak-152** trainer, the mock-up commission was held at the Yakovlev OKB in **Sept 2014**. It "confirmed the correctness of the main decisions on the aircraft and complex" and marked "completion of an important stage of preparation for the construction of prototype aircraft". It also proposed considering an **alternative engine to reduce overall project risk** — [DCS forum thread quoting the press release](https://forum.dcs.world/topic/110750-jak-152/) (secondary; verify against UAC/Irkut release)
- A Russian space-industry regulation allows stages to be **skipped or combined** "with appropriate justification and agreement" (space-sector analogy) — [dnaop.com regulation text](https://dnaop.com/html/79185_4.html)
- **TsAGI's role** [HISTORICAL, 1950s CIA report]:
  - Chief designers forwarded "design plans, models, or model parts to TsAGI for inspection and, if required, for modification". TsAGI returned the plans, and "one or two construction models and structural parts for breaking point tests were built".
  - Prototypes were first flown by test pilots assigned to the designers.
  - TsAGI-developed "Construction Directives for the Aircraft Industry" were published in **1949**.
  - Source: [CIA FOIA Reading Room doc 947703](https://www.cia.gov/readingroom/node/947703)
- Sukhoi worked with TsAGI from 1946 "to determine the aerodynamic appearance of an interceptor fighter". TsAGI was involved at the configuration stage — [GlobalSecurity, Sukhoi history](https://www.globalsecurity.org/military/world/russia/sukhoi-history.htm)
- **PAK FA / Su-57 timeline**:
  - The Sukhoi design bureau "started project development of the aircraft after it received the tender in **April 2002**"; **Alexander Davidenko** was named chief designer in 2002.
  - The "new fighter's **exterior design was approved on December 10, 2004**".
  - A 2007 statement said the **design stage was complete**, with three flyable prototypes planned by 2009; the maiden flight was "repeatedly postponed from early 2007".
  - First flight **29 Jan 2010** (47 min, KnAAPO Dzemgi, pilot Sergey Bogdan); second prototype **3 Mar 2011**; service entry **Dec 2020**.
  - Sources: [Airforce Technology](https://www.airforce-technology.com/?p=14874); [DefenceTalk](https://defencetalk.com/pak-fa-russias-fifth-generation-fighter-t-50-23940); [Wikipedia, Su-57 (pointer)](https://en.wikipedia.org/wiki/Sukhoi_Su-57); [GlobalSecurity, PAK FA program](https://www.globalsecurity.org/military/world/russia/pak-fa-program.htm); [RIA Novosti via GlobalSecurity, 29 Jan 2010](https://www.globalsecurity.org/wmd/library/news/russia/2010/russia-100129-rianovosti01.htm)
  - The search tool did not say which outlet made which claim; verify.

### Inferences
- The Russian sequence maps closely onto the Western one: avanproekt ≈ conceptual design/ASR; eskizny proekt ≈ preliminary design/PDR; maket commission ≈ a customer configuration and ergonomics review before CDR; rabochy proekt ≈ detail design and drawing release; state joint trials ≈ DT/OT. The **full-scale mock-up commission** is a gate with no exact US equivalent today. For a digital team, a full-scale *virtual* mock-up (cockpit reach/vision, maintenance access, weapons-bay fit) reviewed against a checklist is the analogue.
- PAK FA took about **2.3 years from tender to approved external shape** (Apr 2002 → Dec 2004) and about **7.8 years from tender to first flight** (Apr 2002 → Jan 2010).

### Gaps
- No retrieved source describes the specific roles of **CIAM** (engines), **VIAM** (materials) or **LII** (flight research, Zhukovsky), or the state-trials organization. **UNVERIFIED (background knowledge):**
  - CIAM (Central Institute of Aviation Motors) runs engine altitude test facilities and engine certification.
  - VIAM (All-Russian Institute of Aviation Materials) develops and qualifies alloys, composites and RAM/coatings.
  - LII (Gromov Flight Research Institute) runs flight research and test-pilot training.
  - State Joint Tests (GSI) were run with the Air Force's GLITs/929th State Flight Test Centre at Akhtubinsk.
  - The detailed Su-27 (T-10) and MiG-29 eskizny proekt / mock-up commission dates were not retrieved.
- Su-57 development cost is contested: estimates range from **US$8–10 bn to ~US$20 bn**, and India's share is reported as 25% in one source vs "state financing … not more than 20–22%" in another — [Wikipedia, Su-57](https://en.wikipedia.org/wiki/Sukhoi_Su-57); [Quwa](https://quwa.org/2017/08/06/indian-defence-ministry-panel-recommends-pak-fa-involvement/). No reliable primary Russian figure was found.

---

## 7. Typical timelines, team sizes and costs per phase (ATF Dem/Val, JSF CDP, KF-21, Su-57, T-7, F-47)

### Takeaway
From first requirement to prototype flight, open sources give these spans:
- ATF: RFI 1981 → Dem/Val award Oct 1986 → Dem/Val about 5 years at ~$3.8 bn total, with each team on a $691M fixed-price contract and the companies investing heavily of their own money.
- JSF: CDP awards Nov 1996 at $750M per team for two demonstrators each; down-select Oct 2001, about 5 years.
- PAK FA: tender to first flight about 7.8 years.
- KF-21: CDR Sept 2019 → first flight 2022 → about 1,600 flight tests completed by Jan 2026.
- T-7: about 3 years concept to flight (company claim).
- F-47: EMD Mar 2025 → first flight targeted 2028.
Open sources give almost no numbers on team size.

### Cited Findings
- **ATF Dem/Val** [HISTORICAL]: on **31 Oct 1986** each team (Lockheed/Boeing/General Dynamics; Northrop/McDonnell Douglas) received a **$691 million fixed-price contract** to build two prototypes — [Code One, F-22 Milestones Pt 1](https://www.codeonemagazine.com/article.html?item_id=88); [Wikipedia, F-22 (pointer)](https://en.wikipedia.org/wiki/Lockheed_Martin_F-22_Raptor). Dem/Val (1986–91) cost **$3.8 bn** in total — [GlobalSecurity, F-22 cost table](https://www.globalsecurity.org/military/systems//aircraft/f-22-cost.htm). An overview of the ATF as a project-management case is at [PMI paper](https://www.pmi.org/learning/library/us-fighter-jet-project-overview-3750)
- **ATF overall**: RFI 1981 → Dem/Val RFP Sept 1985 → Dem/Val award Oct 1986 → EMD award Aug 1991 — [Wikipedia, ATF](https://en.wikipedia.org/wiki/Advanced_Tactical_Fighter)
- **JSF Concept Demonstration Phase** [HISTORICAL]:
  - On **16 Nov 1996** Boeing and Lockheed Martin each received **$750 million** to build two concept demonstrators and define the Preferred Weapon System Concept.
  - Each built **two demonstrators** (X-32A/B; X-35A/B/C).
  - The companies were **prohibited from using their own money** to finance development.
  - The UK paid **$200 million (10% of CDP)**; Canada paid **US$10 million** (1997).
  - X-35 declared winner on **26 Oct 2001**.
  - Sources: [Wikipedia, JSF program (pointer)](https://en.wikipedia.org/wiki/Joint_Strike_Fighter_program); [Wikipedia, X-35](https://en.wikipedia.org/wiki/Lockheed_Martin_X-35); [GlobalSecurity, JSF status](https://www.globalsecurity.org/military/systems/aircraft/jsf-status.htm)
- **KF-21**: CDR 24–26 Sept 2019 cleared prototype production — [FlightGlobal](https://www.flightglobal.com/k-fx-cdr-sets-stage-for-prototype-production/134497.article). The 2016 plan was a final design in about two years after a 13,000 h tunnel campaign — [Korea Times](https://www.koreatimes.co.kr/amp/southkorea/defense/20160622/s-korea-conducts-wind-tunnel-testing-for-kf-x-jet). First flight is reported by [CNN Japan](https://www.cnn.co.jp/world/35190702.html) and [Aviation Week](https://ngtest.aviationweek.com/defense-space/aircraft-propulsion/south-korean-kf-21-fighter-performs-well-flight-tests). Flight testing was complete with about 1,600 accident-free flights by **Jan 2026** — [Hankyung](https://www.hankyung.com/article/2026011383071)
- **Su-57**: tender Apr 2002 → exterior design approved Dec 2004 → first flight 29 Jan 2010 → service Dec 2020 (see Section 6) — [Airforce Technology](https://www.airforce-technology.com/?p=14874); [GlobalSecurity, PAK FA](https://www.globalsecurity.org/military/world/russia/pak-fa-program.htm)
- **T-7**: "concept … to its first flight in three years" (Boeing claim) — [Defense News](https://www.defensenews.com/air/2021/12/17/the-t-7-takes-shape-inside-the-factory-where-the-air-forces-next-trainer-is-being-built)
- **F-47** [CURRENT]: EMD award 21 Mar 2025 → first flight targeted 2028, reaffirmed July 2026 — [Janes](https://www.janes.com/defence-intelligence-insights/defence-news/air/afa-2025-usaf-targets-2028-for-first-flight-of-f-47); [Defence Matters EU](https://defencematters.eu/manufacturing-of-f-47-next-generation-fighter-underway/)

### Inferences
- Benchmarks for pre-build or "pre-EMD" spans:
  - ATF requirements to Dem/Val award: about 5.5 years (1981 → Oct 1986).
  - Dem/Val with flying prototypes: about 4.5–5 years.
  - JSF CDP: about 5 years.
  - PAK FA tender to external shape approval: about 2.7 years.
  - KF-21: the 2016 plan allowed about 2 years for design finalization.
- All of these involve organizations of hundreds to thousands of engineers. A two-person digital study should therefore target **conceptual design plus an early-preliminary-design package**, not a CDR-level drawing set for a complete fighter. The latter typically involves tens of thousands of drawings (unverified order of magnitude).
- ATF Dem/Val cost per team: $691M fixed-price contract against a $3.8 bn phase total. The $3.8 bn may include government, engine (YF119/YF120) and other costs, so per-team contractor investment cannot be derived from these sources.

### Gaps
- **Team sizes**: no retrieved source gave numbers of engineers for ATF Dem/Val, JSF CDP, KF-21 (KAI) or Su-57. **UNVERIFIED (background knowledge):** major fighter programs peak at several thousand engineers in EMD, while early conceptual teams are small (tens of people).
- **KF-21 development cost** (widely reported as about ₩8.8 trillion for development, program launch Dec 2015) and **KF-21 PDR date** (June 2018), **rollout** (9 Apr 2021) and **first flight** (19 Jul 2022): UNVERIFIED this session (first-flight reports exist via CNN Japan / AvWeek links above, but the exact date was not extracted).
- **YF-22/YF-23 first flight dates** (UNVERIFIED: YF-23 27 Aug 1990, YF-22 29 Sept 1990) and **JSF X-32/X-35 first flights** (UNVERIFIED: X-32A 18 Sep 2000; X-35A 24 Oct 2000) were not retrieved.
- No GAO report numbers on F-22, F-35 or NGAD cost were retrieved (gao.gov fetch blocked; search budget exhausted).

---

## 8. Legal/regulatory context for a small private (Polish) team doing military-type aircraft design (informational only, not legal advice)

### Takeaway
Original design data for a fighter is likely to fall under military-list "technology" controls: EU Common Military List **ML10 (aircraft)** and **ML22 (technology)**; in the US, **USML Category VIII (aircraft) and XIX (gas-turbine engines)** and the EAR 600-series (9x610/9x619). In Poland, any *transfer abroad* (including electronic, such as email or cloud) of controlled goods or technology goes through the **Act of 29 Nov 2000 on foreign trade in strategic goods** (consolidated text Dz.U. 2023 poz. 1582, amended by Dz.U. 2026 poz. 471). Information that is genuinely public-domain or basic research is generally carved out. The team should rely only on published sources and treat its own outputs as potentially controlled before sharing them across borders.

### Cited Findings
- **US ITAR**:
  - The USML covers defense articles **and related technical data**. "Technical data" is defined at **22 CFR 120.33**; the pre-2022 numbering was 120.10.
  - **Public domain** is defined at **22 CFR 120.34**: information "which is published and which is generally accessible or available to the public", including release at conferences and in published patents.
  - Sources: [Univ. of Arkansas ITAR policy](https://rsic.uark.edu/exportcontrol/itar-compliance.php); [Stony Brook ITAR guide](https://www.stonybrook.edu/research-security/export-controls/reference_guides/itar.html); [UNLV ITAR policy](https://www.unlv.edu/policies/international-traffic-arms-regulations-itar-compliance-policy)
- **Fundamental research** at accredited US universities is treated as public domain. This status is **lost if publication restrictions are accepted**. "DoD funding alone does not make a research project subject to the ITAR". Even an "autopilot system used in basic robotics research may be controlled under the ITAR" — [Stony Brook](https://www.stonybrook.edu/research-security/export-controls/reference_guides/itar.html); [U. Arkansas](https://rsic.uark.edu/exportcontrol/itar-compliance.php)
- **USML Cat VIII and XIX / EAR 600-series**: a final rule at **81 FR 83127 (21 Nov 2016)** revised USML **Category VIII (aircraft and related articles)** and **XIX (gas turbine engines and associated equipment)**. It added **9E610.b.15** (technology "required" for development, production, operation … of military gas-turbine engine items in 9A619/9B619). A 9C619 note releases materials used in *production* engines that are not otherwise enumerated — [Federal Register via GovInfo](https://www.govinfo.gov/content/pkg/FR-2016-11-21/pdf/2016-27775.pdf) [rule from 2016; later amendments not checked]
- **EU Common Military List**: Directive 2009/43/EC (intra-EU transfers of defence-related products) lists **ML10 (aircraft)** and **ML22 (technology)**. ML22 covers "technology 'required' for the 'development', 'production', operation, installation, maintenance …" of listed items, and ML22 Note 2 lists exclusions — [legislation.gov.uk copy of Directive 2009/43/EC](https://www.legislation.gov.uk/european/directive/2009/0043?view=plain). The Directive's annex was aligned to the updated CML by **Commission Delegated Directive (EU) 2023/277** — [Bulgarian Ministry of Innovation export-control page](https://exportcontrol.mi.government.bg/Modulen.php?id=1322)
- **EU Dual-Use Regulation (EU) 2021/821** applies from **9 Sept 2021** and replaced Reg. 428/2009 — [Austrian Ministry (BMWET), Dual-Use](https://www.bmwet.gv.at/en/Topics/Export-Control/Export/Dual-Use.html). It covers export, brokering, transit and technical assistance, including **transfer of software/technology by electronic means** (email, cloud) — [CustomsClearance.net](https://www.customsclearance.net/lt/articles/new-dual-use-regulation-what-are-the-changes-in-the-rules-of-the-game?print=1); [Octagon glossary](https://octagonpeople.com/glossary/dual-use-controls). The latest Annex I update found is **Delegated Regulation (EU) 2025/2003 (published 14 Nov 2025)** — [BMWET](https://www.bmwet.gv.at/en/Topics/Export-Control/Export/Dual-Use.html). A secondary site mentions a 14 Sept 2026 delegated regulation; this is **unverified** — [NewSpace Economy](https://newspaceeconomy.ca/2026/10/23/how-do-european-union-import-and-export-laws-govern-space-technology/)
- **Poland**:
  - The Act of **29 Nov 2000** on foreign trade in goods, technologies and services of strategic importance for state security and for maintaining international peace and security (**Dz.U. 2000 nr 119 poz. 1250**) governs foreign trade in strategic goods, its control and record-keeping, and liability for illegal trade — [Infor.pl act text](https://www.infor.pl/akt-prawny/DZU.2000.119.0001250,ustawa-o-obrocie-z-zagranica-towarami-technologiami-i-uslugami-o-znaczeniu-strategicznym-dla-bezpieczenstwa-panstwa-a-takze-dla-utrzymania-miedzynarodowego-pokoju-i-bezpieczenstwa-oraz-o-zmianie-niekt.html)
  - Consolidated text: **Dz.U. 2023 poz. 1582** — [ELI](https://eli.gov.pl/eli/DU/2023/1582/ogl/pol/pdf); [Sejm API](https://api.sejm.gov.pl/eli/acts/DU/2023/1582/text/T/D20231582L.pdf)
  - "Strategic goods" = **dual-use items and armaments (uzbrojenie)** — [ELI Dz.U. 2020 poz. 509](https://eli.gov.pl/api/acts/DU/2020/509/text/U/D20200509Lj.pdf)
  - An **individual permit** is issued on application with a declaration that no exclusionary circumstances exist, a description of the goods, and end-user/destination data. **Global permits** also exist — [Infor.pl](https://www.infor.pl/akt-prawny/DZU.2000.119.0001250,ustawa-o-obrocie-z-zagranica-towarami-technologiami-i-uslugami-o-znaczeniu-strategicznym-dla-bezpieczenstwa-panstwa-a-takze-dla-utrzymania-miedzynarodowego-pokoju-i-bezpieczenstwa-oraz-o-zmianie-niekt.html); [Sejm print 2119](https://api.sejm.gov.pl/sejm/term10/prints/2119/2119.pdf)
  - A 2022 regulation created **national general permits** (e.g., **ZG-PL-U-1** intra-EU transfer, **ZG-PL-U-2** export) — [ELI Dz.U. 2022 poz. 1567](https://eli.gov.pl/api/acts/DU/2022/1567/text/I/D20221567.pdf)
  - [CURRENT 2026] The **Act of 13 Mar 2026 (Dz.U. 2026 poz. 471)** amends the law, including definitions, and adds the national general permit as a statutory permit type. Its entry-into-force date was not confirmed — [Sejm API, Dz.U. 2026 poz. 471](https://api.sejm.gov.pl/eli/acts/DU/2026/471/text.pdf); [ELI](https://eli.gov.pl/api/acts/DU/2026/471/text/T/D20260471L.pdf)

### Inferences
- For a two-person team in Poland working only from published sources and keeping its work in Poland, the main legal exposure is **transfer**: sending design files abroad (non-EU collaborators, foreign cloud regions, public posting of detailed military-relevant technical data) and any later move toward *manufacturing* military technology. Purely domestic paper design from public sources is less clearly regulated, but this needs legal confirmation.
- Importing or using **US-origin ITAR/EAR technical data** (e.g., non-public F-22/F-35 documents, export-controlled software) would bring in US re-export rules. That is another reason to restrict the project to textbooks, NTRS and DTIC "Distribution A" material.
- If the team ever publishes its design openly (e.g., a paper or public repository), the public-domain carve-outs (ITAR 120.34 / CML-ML22 notes) may apply to what *is published*. Whether publishing new military-aircraft design technology is itself a controlled "export" is a question for a Polish export-control lawyer or the Department of Export Control at the Ministry of Development and Technology (MRiT). That is a judgment call, not established by these sources.

### Gaps
- **Polish licensing (koncesja) law**: not retrieved because the search budget was exhausted. **UNVERIFIED (background knowledge):** the *Act of 13 June 2019 on conducting business activity in the manufacture and trade of explosives, weapons, ammunition and products and technology for military or police purposes* (Dz.U. 2019 poz. 1214) requires a **concession from the Minister of the Interior (MSWiA)** for *business activity* in manufacturing or trading military technology. A private, non-commercial design study may fall outside it, but this must be checked with counsel.
- **Exact ML10/ML22 wording and exclusions**. UNVERIFIED: ML22 Note 2 excludes technology "in the public domain", "basic scientific research", and the minimum necessary for patent applications. Exact **USML VIII(i)** text and **EAR 9E610** aircraft paragraphs: not retrieved (eCFR/EUR-Lex fetch blocked).
- **Civil experimental / amateur-built rules for a scaled demonstrator**: not retrieved. **UNVERIFIED (background knowledge):**
  - **US**: FAA experimental amateur-built certificate under 14 CFR 21.191(g), with the "major portion" (≥51%) built by amateurs for education/recreation (AC 20-27G); jet-powered amateur-builts need additional operating limitations. Small unmanned scaled models fall under 14 CFR Part 107 (<55 lb).
  - **EU**: under Regulation (EU) 2018/1139, Annex I, aircraft at least 51% amateur-built are excluded from EASA rules and handled nationally. In Poland that means the Civil Aviation Authority (**ULC**) and its *specjalny certyfikat/pozwolenie na wykonywanie lotów* regime.
  - Unmanned scaled demonstrators fall under the EU UAS Regulations 2019/947 and 2019/945 (open/specific categories).
  - A flying scaled demonstrator of a military-styled LO fighter could also raise export-control and "military UAS" classification questions (CML ML10 covers some UAVs). Not verified.

---
*End of notes. Source quality key: DAU/AAF, DoD memos, OSD T&E, Federal Register, EDA, Polish ELI/Sejm = primary; Code One, Janes, Breaking Defense, Defense News, FlightGlobal, Korea Times = reputable press/manufacturer; GlobalSecurity, Wikipedia, vendor blogs, forums = secondary/pointers, verify before use.*
