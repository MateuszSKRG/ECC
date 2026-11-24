# Toolchain, Public Data Sources, Reference Drawings, Textbooks and "Blueprint" Package for a Two-Person Mach 3 LO Fighter Digital Design Study (status October 2026)

*Research-conditions note for the report writer: this session's shared web-search budget ran out partway through, and direct fetching was blocked for most official domains (openvsp.org, software.nasa.gov, aiaa.org, ntrs.nasa.gov, dtic.mil, cia.gov, asme.org and others failed DNS or proxy checks). Version and license data below therefore come from (a) search-result snippets of official or primary pages and (b) the PyPI JSON API, which could be queried directly on 28 Oct 2026. Anything not confirmed this way is listed under "Gaps", in subsections labeled "Unverified background", with the official URL to check. Do not present those items as verified.*

---

## 1. Open/free software toolchain per discipline: version and status, license, non-US availability, learning effort

### Takeaway
A complete design loop for two people can be built from free, open-source tools that anyone can download worldwide. It runs: OpenVSP (geometry, VSPAERO, wave drag) -> OpenMDAO/Aviary/RCAIDE/AeroSandbox (sizing and MDO) -> pyCycle (engine cycle) -> SU2 or OpenFOAM (CFD) -> CalculiX/Code_Aster/MYSTRAN with pyNastran (structures) -> POFACETS (RCS, needs MATLAB) -> JSBSim/FlightGear (flight dynamics), with FreeCAD for detail CAD. NASA's high-end CFD codes (FUN3D, OVERFLOW, Cart3D) are not open to non-US persons. FUN3D and OVERFLOW are "U.S. Release Only". Cart3D is "U.S. Government Purpose Release", and commercial access goes through a licensee.

### Cited Findings

**Geometry and conceptual design: NASA OpenVSP**
- OpenVSP 3.44.0 (July 2025) was a major release. NASA's announcement says it represents about 27 months of OpenVSP development and about 18 months of VSPAERO development, and advises caution because of the scale of the change. — [OpenVSP blog, Jul 2025](https://openvsp.org/blogs/2025/07)
- Since then there have been frequent releases. 3.46.0 (Sep 2025) added Routing Geom rounded corners and tire modes. 3.47.0 (Jan 2026) added Swept Volume Analysis and Look-At Visibility Analysis. 3.48.0 (Feb 2026) added Stack shape presets. 3.49.0 (Apr 2026) added stowed/retracted landing gear. 3.51.0 (Jun 2026) added XSec copy/paste and detachable conformal components. 3.51.3 (Aug 2026) made the API examples double as unit tests. These details come from FreeBSD port-update summaries, not full NASA release notes. — [FreeBSD 3.46.0](https://reviews-dev.freebsd.org/R11:55ed9d98799628ffa3c8d4a0fd7bc187daa6c081); [3.47.0](https://reviews-dev.freebsd.org/R11:6cbb8d68c00553f8a044c96a6dc09c814d8ce343); [3.48.0](https://reviews-dev.freebsd.org/R11:7170ba86eca257bf0cca988dfbbd4b9a5dd3617f); [3.49.0](https://reviews-dev.freebsd.org/R11:22677bbb52d2205f9e700399e5ab2a45f878b938); [3.51.0](https://reviews-dev.freebsd.org/R11:0b66a28c1f1509ad1957ba01d285a79a97eb6f66); [3.51.3](https://reviews-dev.freebsd.org/R11:ba6550b37cb3656a59a266977d68dddd16701dd2)
- 3.51.1 was announced on the official OpenVSP Google Group, and the OpenVSP blog has 2026 posts (April and May 2026). — [OpenVSP Google Group: 3.51.1 Released](https://groups.google.com/g/openvsp/c/vRowSOfFdfQ); [OpenVSP blog May 2026](https://openvsp.org/blogs/2026/05); [OpenVSP blog Apr 2026](https://openvsp.org/blogs/2026/04)
- The latest version found was 3.51.3 (August 2026). No release after August 2026 turned up. — [FreeBSD 3.51.3](https://reviews-dev.freebsd.org/R11:ba6550b37cb3656a59a266977d68dddd16701dd2)

**Aircraft sizing and MDO frameworks** (versions from PyPI, queried 28 Oct 2026)
- **OpenMDAO** 3.45.2, released 27 Oct 2026, Apache-2.0. It is NASA Glenn's MDO framework, homepage openmdao.org. — [PyPI openmdao](https://pypi.org/project/openmdao/)
- **NASA Aviary** 1.0.1, released 2 Jul 2026, Apache-2.0. PyPI calls it "NASA's aircraft design tool". It incorporates sizing equations from NASA's predecessor codes GASP and FLOPS, is built on OpenMDAO, and is "used by college level senior design courses, NASA internally, and industry partners". The old PyPI name `om-aviary` (0.9.9) now redirects to `aviary`. — [PyPI aviary](https://pypi.org/project/aviary/); [Aviary overview, NTRS 20240009217](https://ntrs.nasa.gov/citations/20240009217); [Gratz et al. Aviary paper, NTRS 20240007608](https://ntrs.nasa.gov/api/citations/20240007608/downloads/Resubmit_final_62424.pdf)
- **RCAIDE** (PyPI `RCAIDE-LEADS`) 1.5.0, released 25 Jul 2026, AGPL-3.0, "Beta" status, Python >=3.10. It is developed at the University of Illinois Urbana-Champaign and described as "the successor to the globally recognized SUAVE code". It is a multi-fidelity platform with an energy-agnostic powertrain network, and its VLM plus drag build-up is validated with R^2 = 0.96 (C_L) and 0.94 (C_D). — [PyPI RCAIDE-LEADS](https://pypi.org/project/RCAIDE-LEADS/)
- **FAST-OAD** (core) 1.10.0, released 2 Jun 2026, GPL-3.0, "Production/Stable", Python 3.10–3.14. It is maintained by ONERA (author C. David, onera.fr) and ISAE-SUPAERO. Since v1.3.0 its transport-aircraft models live in plugins: FAST-OAD-CS25 0.9.1 (Sep 2026) and FAST-OAD-CS23 1.4.0 for general aviation (Aug 2026). — [PyPI fast-oad](https://pypi.org/project/fast-oad/); [PyPI fast-oad-cs25](https://pypi.org/project/fast-oad-cs25/); [PyPI fast-oad-cs23](https://pypi.org/project/fast-oad-cs23/)
- **AeroSandbox** 4.2.10, released 5 Jul 2026, MIT license ("use AeroSandbox for anything you want, commercial or non-commercial"). Author is Peter Sharpe (MIT). It is a Python aircraft design-optimization package that exports to CAD via STEP. — [PyPI aerosandbox](https://pypi.org/project/aerosandbox/)
- **OpenAeroStruct** 2.12.0, released 6 Oct 2025, BSD-3, from the MDO Lab (coupled VLM and beam aero-structural optimization on OpenMDAO). — [PyPI openaerostruct](https://pypi.org/project/openaerostruct/)
- **Dymos** 1.15.1, released 12 Mar 2026, Apache-2.0: "Open-Source Optimization of Dynamic Multidisciplinary Systems", for trajectory and mission optimization on OpenMDAO. — [PyPI dymos](https://pypi.org/project/dymos/)

**Engine cycle: NASA pyCycle**
- pyCycle (PyPI `om-pycycle`) 4.4.0, released 15 Oct 2025, is the "Thermodynamic Cycle modeling library" built on OpenMDAO. Note: the unrelated PyPI package named `pycycle` is an import-cycle checker. — [PyPI om-pycycle](https://pypi.org/project/om-pycycle/)

**Aerodynamic database: USAF Digital DATCOM**
- The USAF no longer supports Digital DATCOM, and it is now public-domain software. — [Wikipedia: USAF Stability and Control Digital DATCOM](https://en.wikipedia.org/wiki/United_States_Air_Force_Stability_and_Control_Digital_DATCOM)
- Public Domain Aeronautical Software (PDAS) distributes public-domain source code. Its (2009-dated) flyer lists the Digital Datcom users manual (AFFDL-TR-79-3032 Vol. I) and the complete USAF Datcom report. — [PDAS](https://pdas.com/); [PDAS flyer](https://www.pdas.com/flyer.pdf); [PDAS Datcom manuals page](https://www.pdas.com/datcomb.html)
- The users manual (Vol. I, ADA086557) and the implementation of methods (Vol. II, ADA086558) are on DTIC and NTIS. — [DTIC ADA086557](https://apps.dtic.mil/sti/pdfs/ADA086557.pdf); [DTIC ADA086558](https://apps.dtic.mil/sti/pdfs/ADA086558.pdf); [NTIS NTRL ADA086557](https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/ADA086557.xhtml); [IIT Contrails Vol. II](https://contrails.library.iit.edu/item/163381)
- The ecosystem around DATCOM includes a FlightGear wiki page on using DATCOM for flight models, a Scilab DATCOM toolbox, and MATLAB Aerospace Blockset's "Digital DATCOM Forces and Moments" block, which reads DATCOM output. — [FlightGear wiki DATCOM](https://wiki.flightgear.org/DATCOM); [Scilab ATOMS datcom](https://atoms.scilab.org/toolboxes/datcom); [MathWorks Digital DATCOM block](https://la.mathworks.com/help/aeroblks/digitaldatcomforcesandmoments.html)

**CFD: open source**
- **SU2**: stable release 8.5.0, dated 27 April 2026; 8.4.0 "Harrier" came before it. SU2 is a multiphysics solver for compressible and incompressible flow "across all Mach regimes", focused on gradient-based design optimization with continuous and discrete adjoints. Wikipedia lists the license as LGPL-2.1, while a Gitee mirror lists BSD-3-Clause, so the license in the official repository needs checking. — [Wikipedia: SU2 code](https://en.wikipedia.org/wiki/SU2_code); [Gitee mirror of su2code/SU2](https://gitee.com/mirrors_su2code/SU2)
- **OpenFOAM (Foundation line)**: version 13 was released by the OpenFOAM Foundation and produced by CFD Direct. It ships packaged installs for Ubuntu 22.04, 24.04 and 25.04. Windows uses WSL and macOS uses Multipass. It needs a C++14 compiler (tested with GCC 5.5+ and Clang 16+). — [OpenFOAM 13 release](https://openfoam.org/release/13/); [CFD Direct news](https://cfd.direct/news/)
- **OpenFOAM (ESI/OpenCFD line)** uses year-month version names. The only openfoam.com result returned was v2312 (Dec 2023). — [OpenFOAM v2312 announcement](https://www.openfoam.com/news/main-news/openfoam-v2312)
- **PyFoam** (Python utilities for OpenFOAM) 2026.6, released 30 Jun 2026, GPL. — [PyPI PyFoam](https://pypi.org/project/PyFoam/)
- **Gmsh** 4.15.2, released 24 Mar 2026, GPLv2+: a 3D finite-element mesh generator. — [PyPI gmsh](https://pypi.org/project/gmsh/)

**CFD: NASA codes and non-US persons**
- **FUN3D** v14.2 (catalog ID LAR-20188-1) is listed in the NASA Software Catalog with release type **"U.S. Release Only"**. Source code is released and needs a compiler. — [NASA Software Catalog FUN3D v14.2](https://software.nasa.gov/software/LAR-20188-1)
- A NASA challenge page describes FUN3D as "export controlled research code" that only US citizens may apply for, and a CFD Online notice says it "may only be provided to US persons". — [HeroX NASA HPFCC](https://herox.com/hpfcc); [CFD Online FUN3D notice](https://www.cfd-online.com/Forum/news.cgi/read/93460)
- **OVERFLOW** 2.4d (catalog ID LAR-20095-1, 28 Apr 2025) and 2.5.0 (catalog ID LAR-20382-1, 9 Jun 2025, adds GPU support) are both **"U.S. Release Only"**. NASA says OVERFLOW is available to "U.S. companies, universities, and individuals" under a Software Usage Agreement. — [NASA catalog OVERFLOW 2.4D](https://software.nasa.gov/software/LAR-20095-1); [NASA catalog OVERFLOW 2.5.0](https://software.nasa.gov/software/LAR-20382-1); [NASA OVERFLOW CFD page](https://www.nasa.gov/reference/overflow-cfd/)
- **Cart3D** (catalog ID ARC-14275-1) is listed as **"U.S. Government Purpose Release"**, meaning federal employees and contractors only. Commercial access is through SpaceWorks ("Cart3D Plus"). Only the I/O support libraries (catalog ID ARC-18778-1) are open source. — [NASA catalog Cart3D](https://software.nasa.gov/software/ARC-14275-1); [SpaceWorks Cart3D Plus](https://www.spaceworks.aero/software/cart3d-plus/); [NASA catalog ARC-18778-1](https://software.nasa.gov/software/ARC-18778-1)
- Rescale, a cloud vendor, says FUN3D, OVERFLOW and Cart3D are offered as "U.S. Release Only" (citizens, permanent residents and qualified organizations), and that running them on its cloud needs NASA approval. — [Rescale: NASA CFD on Rescale](https://rescale.com/?p=82366)

**CAD and scripting CAD**
- **FreeCAD 1.1** was released on 25 March 2026, with major Part Design, Assembly, FEM and CAM improvements. 1.1.1 followed on 15 April 2026 as a maintenance release. No release newer than 1.1.1 was found. — [FreeCAD blog 1.1](https://blog.freecad.org/2026/03/25/freecad-version-1-1-released/); [FreeCAD blog 1.1.1](https://blog.freecad.org/2026/04/15/freecad-1-1-1-released/); [Phoronix](https://www.phoronix.com/news/FreeCAD-1.1-Released); [AlternativeTo: FEM upgrades](https://alternativeto.net/news/2026/3/freecad-1-1-adds-three-point-lighting-part-design-previews-and-major-fem-upgrades)
- **CadQuery** 2.8.0 (21 Jun 2026, Apache-2.0) and **build123d** 0.13.0 (21 Sep 2026, Apache-2.0) are Python parametric CAD libraries on the OpenCASCADE kernel that can be version-controlled as code. — [PyPI cadquery](https://pypi.org/project/cadquery/); [PyPI build123d](https://pypi.org/project/build123d/)
- **PyVista** 0.49.1 (11 Oct 2026, MIT) handles 3D visualization and mesh analysis. **meshio** 5.3.5 (Jan 2024, older, MIT) converts between mesh formats. — [PyPI pyvista](https://pypi.org/project/pyvista/); [PyPI meshio](https://pypi.org/project/meshio/)

**Structures**
- **MYSTRAN** is "an open-source structural analysis program compatible with NASTRAN". The upstream repository is github.com/MystranSolver/MYSTRANSolver. A third-party pre-built Python wheel `mystran` 18.0.0.1 (22 May 2026, MIT) bundles the executable. — [PyPI mystran](https://pypi.org/project/mystran/)
- **pyNastran** 1.4.1 (26 Mar 2024, older than 2025) reads, edits, writes and views Nastran BDF/F06/OP2/OP4 files. No newer PyPI release was found. — [PyPI pyNastran](https://pypi.org/project/pyNastran/)
- **ccx2paraview** 3.2.0 (Dec 2024, GPL-3.0) converts CalculiX .frd results to VTK/ParaView. — [PyPI ccx2paraview](https://pypi.org/project/ccx2paraview/)
- FreeCAD 1.1 includes "major FEM upgrades". Its FEM workbench is a front end to CalculiX among other solvers. — [AlternativeTo](https://alternativeto.net/news/2026/3/freecad-1-1-adds-three-point-lighting-part-design-previews-and-major-fem-upgrades)

**RCS prediction**
- **POFACETS 4.5** (David Jenn, Naval Postgraduate School) is on MathWorks File Exchange, listed as compatible with any MATLAB release on Windows, macOS and Linux. It computes monostatic or bistatic RCS of faceted targets with physical optics and "does not include multiple reflections, shadowing, or diffractions". — [MathWorks File Exchange POfacets4.5](https://www.mathworks.com/matlabcentral/fileexchange/50602-pofacets4-5)
- Its GUI and method are documented in a 2000 NPS thesis (Garrido), which is publicly available. — [NPS Calhoun thesis](https://calhoun.nps.edu/entities/publication/02a49858-3b2c-4065-a3e9-9dbb51408488); [DTIC ADA383252](https://apps.dtic.mil/sti/pdfs/ADA383252.pdf)
- **Bempp-cl** 0.4.2 (1 Apr 2025, older) is an open boundary-element library for full-wave scattering and can serve as a higher-fidelity check on small parts. — [PyPI bempp-cl](https://pypi.org/project/bempp-cl/)

**Flight dynamics and simulation**
- **JSBSim** 1.3.3, released 16 Oct 2026, LGPL-2.0-or-later, "Production/Stable", with Python bindings (Python >=3.10). — [PyPI jsbsim](https://pypi.org/project/jsbsim/)

**MBSE and data**
- **capellambse** 0.8.1 (20 Jan 2026, Apache-2.0) gives Python access to Eclipse Capella MBSE projects, which helps script requirement and architecture checks. — [PyPI capellambse](https://pypi.org/project/capellambse/)
- **DVC** 3.67.1 (31 Mar 2026, Apache-2.0) is "Git for data scientists" and handles versioning of large CFD and FEA data alongside Git. — [PyPI dvc](https://pypi.org/project/dvc/)
- Caution: the PyPI package `sysmlv2` is an unrelated placeholder, not the OMG pilot implementation. — [PyPI sysmlv2](https://pypi.org/project/sysmlv2/)

### Inferences
- **Suggested two-person stack.** Each entry gives the tool, its learning effort (my judgement) and the Mach 3 / low-observable caveats.
  - Geometry and outer mold line (OML): OpenVSP. Effort: low to medium. Parametric, scriptable through its API, exports STEP/IGES/STL. VSPAERO is linear (VLM/panel), so supersonic and Mach 3 results must be checked with CFD.
  - Sizing: OpenMDAO with Aviary, or RCAIDE, or AeroSandbox. Effort: medium (Python). Aviary and FAST-OAD are oriented to transports and GA. RCAIDE has a broader vehicle library. AeroSandbox is fastest for custom fighter sizing scripts.
  - Engine: pyCycle on OpenMDAO. Effort: medium to high. Needs Mattingly-style cycle knowledge, since a Mach 3 cycle (turbojet, variable cycle or turbo-ramjet) must be built from elements.
  - Aero database: Digital DATCOM plus OpenVSP. Effort: medium (fixed-format Fortran input). Good for early stability derivatives, but body-wing fighter shapes and chines fall outside its methods.
  - CFD: SU2 (Euler/RANS, adjoint shape optimization) or OpenFOAM (rhoCentralFoam and others). Effort: high. SU2 is the more natural fit for compressible external aero and optimization.
  - CAD: FreeCAD 1.1 or CadQuery/build123d. Effort: medium to high. Script-based CAD keeps the model diff-able in Git.
  - Structures: FreeCAD FEM with CalculiX, or MYSTRAN with pyNastran. Effort: medium to high. MYSTRAN plus pyNastran keeps a NASTRAN-style deck, which is the industry idiom.
  - RCS: POFACETS (needs a MATLAB license). Effort: low to medium. Physical optics only: no edge diffraction, cavity (inlet/exhaust) or creeping-wave effects, which dominate a real LO design. Useful for shaping trade studies only.
  - Flight simulation: JSBSim with FlightGear. Effort: medium. JSBSim takes aero tables from DATCOM, VSPAERO or CFD.
- A non-US team can legally use every tool in that stack. Only the NASA high-end CFD codes (FUN3D, OVERFLOW, Cart3D) are closed to them, and SU2 and OpenFOAM are adequate substitutes for a study.
- POFACETS is the only practical free RCS code found, and it needs MATLAB (commercial). A team without MATLAB would need to port or replace it. Bempp-cl is full-wave but too costly in memory for a full aircraft at X-band.
- RCS and IR signature prediction for a full aircraft is the weakest link in the open toolchain: no open code covering high-frequency methods with multiple bounces and edge diffraction was found and verified this session.

### Gaps
- Search budget ran out before targeted searches on Capella, the SysML v2 pilot, Blender, OpenSCAD, Onshape, Git LFS, CalculiX, Code_Aster, FlightGear and other RCS codes. Their status is unverified (below).
- Could not open software.nasa.gov directly to confirm the current FUN3D version beyond v14.2, or whether Cart3D's category has changed.
- SU2's license is ambiguous across sources (LGPL-2.1 vs. BSD-3 on a mirror); check github.com/su2code/SU2/blob/master/LICENSE.md.
- The latest ESI OpenFOAM release (presumably v2506 or v2606) was not confirmed.
- pyCycle license and fighter examples (afterburning or mixed-flow turbofan) were not confirmed; the PyPI license field is empty.

#### Unverified background (model knowledge up to mid-2026, not checked this session; verify at the URL given)
- **OpenVSP**: NASA Open Source Agreement (NOSA 1.3). Freely downloadable worldwide from openvsp.org and github.com/OpenVSP/OpenVSP. Bundles VSPAERO (VLM/panel), Wave Drag (area-rule zero-lift wave drag), CompGeom (wetted area and volume), Parasite Drag, CFD Mesh and FEA Mesh/structure tools. The "VSP Hangar" (hangar.openvsp.org) hosts user-contributed models. A yearly OpenVSP Workshop publishes tutorials, and there is a Google Group. Verify at openvsp.org and openvsp.org/wiki.
- **Onshape Free plan**: free for non-commercial use, but all documents are public, which is unsuitable for anything the team wants kept private. Paid tiers are needed for private documents. Verify at onshape.com/en/pricing.
- **Blender**: GPL. The 4.x LTS and 5.x series (5.0 was expected in late 2025). Use it for visualization and renders only, not for engineering geometry. Verify at blender.org/download/releases.
- **OpenSCAD**: GPL-2. Last formal stable release 2021.01; development snapshots add the Manifold backend. Poor fit for doubly-curved aircraft surfaces. Verify at openscad.org.
- **CalculiX** (G. Dhondt): GPL-2, versions 2.2x. Verify at dhondt.de and calculix.de. **Code_Aster** (EDF): GPL-3, version 17.x or later, often used through Salome-Meca. Verify at code-aster.org.
- **FlightGear**: GPL-2, "2024.1" stable series. Verify at flightgear.org.
- **Eclipse Capella**: EPL-2.0, version 7.x, Arcadia method, free. Verify at mbse-capella.org. **SysML v2**: OMG formally adopted SysML v2 and KerML in 2025. The pilot implementation (github.com/Systems-Modeling/SysML-v2-Pilot-Implementation) provides Eclipse and Jupyter tooling, and Eclipse SysON is an open web-based SysML v2 modeler. Verify release numbers and licenses on GitHub and omg.org.
- **Git LFS**: MIT license. GitHub, GitLab and others meter LFS storage and bandwidth. Verify at git-lfs.com and docs.github.com, as quotas change.
- **Other open RCS and EM codes** (not verified): openEMS (FDTD, GPL-3), NEC-2 (wire-only method of moments), and research PO/SBR codes on GitHub of varying quality.
- **SUAVE** (Stanford, suavecode.github.io): last release 2.5.x around 2022, now superseded by RCAIDE (which is confirmed above).

---

## 2. Legitimate public data sources (reports, histories, manuals, design competitions, courses, dimensioned reference drawings)

### Takeaway
The richest legal sources are the CIA's declassified A-12 OXCART collection, the declassified SR-71 flight manual (free online and in a reprint), DTIC and NTIS public-release reports such as the Digital DATCOM manuals, NASA NTRS, and AIAA student design competition RFPs and winning reports. The 2025–26 AIAA undergraduate team aircraft RFP was itself a next-generation carrier-based strike fighter. Exact OML drawings of current fighters (F-22, F-35, Su-57) are not legally public. Reference modeling has to rely on published dimensions and approximate three-views.

### Cited Findings
- **CIA FOIA Reading Room, "A-12 OXCART Reconnaissance Aircraft Documentation"**: about 1,500 pages in about 350 documents, maps, diagrams and photographs, released with the CIA's unclassified history *Archangel: CIA's Supersonic A-12 Reconnaissance Aircraft* by Chief Historian David Robarge. Individual items include "OXCART Program History and Status". — [CIA collection](https://www.cia.gov/readingroom/collection/12-oxcart-reconnaissance-aircraft-documentation?page=1); [OXCART Program History and Status](https://www.cia.gov/readingroom/node/847175)
- Historical facts in the collection include: concept work began in July 1957 with Lockheed and Convair; 13 A-12s were procured; the aircraft was declared operationally ready in December 1965; a 1965 note records 1,285 flights totaling 1,847 hours at the Nevada test site. Many documents remain redacted. — [CIA collection](https://www.cia.gov/readingroom/collection/12-oxcart-reconnaissance-aircraft-documentation?page=1)
- **SR-71 Flight Manual**: free online at SR-71 Online, which says it was declassified and "made free to the public" and asserts no copyright. A scan of the SR-71A/B manual is on the Internet Archive under Public Domain Mark 1.0. — [sr-71.org manual](https://sr-71.org/blackbird/manual); [Internet Archive scan](https://archive.org/details/0003756-lockheed-sr-71-03)
- A commercial facsimile reprint (Voyageur Press, 2016, with commentary by Col. Richard Graham, USAF Ret.) is also sold. This comes from a bookseller listing. — [TMB Books listing](https://www.tmbbooks.com/en/aviation-books-m-lockheed-ww3-sr-71-blackbird.html)
- **DTIC/NTIS public-release reports**: the Digital DATCOM manuals (ADA086557 and ADA086558) and the POFACETS thesis (ADA383252) are on apps.dtic.mil as public PDFs. — [DTIC ADA086557](https://apps.dtic.mil/sti/pdfs/ADA086557.pdf); [DTIC ADA383252](https://apps.dtic.mil/sti/pdfs/ADA383252.pdf)
- **NASA NTRS** hosts the Aviary documentation and the GASP-era source reports, for example the 1981 GASP report. — [GASP report, NTRS 19810010563](https://ntrs.nasa.gov/api/citations/19810010563/downloads/19810010563.pdf); [Aviary overview NTRS](https://ntrs.nasa.gov/citations/20240009217)
- **AIAA design competitions**:
  - The 2025–2026 undergraduate team aircraft RFP asked for a "next-generation carrier-based strike fighter aircraft", weighing carrier suitability and cost. — [Aerospace America: 2026 AIAA Design Competition Winners](https://aerospaceamerica.aiaa.org/institute/2026-aiaa-design-competition-winners-announced/)
  - In the 2025 competition, Illinois teams took 1st and 2nd. One requirement set included a budget under $25 million, a four-hour loiter and a supersonic dash. — [UIUC Aerospace news](https://aerospace.illinois.edu/news/78344)
  - The 2005–06 undergraduate RFP was a homeland-defense interceptor, won by Cal Poly SLO ("Black Mamba"). The exact source page for this was not confirmed. — [AIAA](https://aiaa.org/?p=4935); [SpaceNews](https://spacenews.com/?p=47830)
  - AIAA hosts year-by-year "Design Competition Winning Reports" pages, for example 2019–2020. — [AIAA 2019-2020 winning reports](https://aiaa.org/get-involved/university-students/design-competitions/2019-2020-design-competition-winning-reports/)
  - Kansas reports more AIAA design-competition podium finishes than any other university. — [KU news](https://news.ku.edu/ku-aerospace-students-claim-more-honors-aircraft-design-competitions); [KU Engineering 2020](https://engr.ku.edu/news/article/2020/10/28/ku-aerospace-engineering-students-earn-acclaim-international-design-competition)
- **Aviary** is "used by college level senior design courses". — [PyPI aviary](https://pypi.org/project/aviary/)

### Inferences
- The AIAA 2025–26 carrier strike fighter RFP and its winning reports are the closest public analogue to the team's project: a requirements document, a design-report format and judged examples. Pair them with the Mattingly textbook's air-to-air fighter running example (unverified below) to build the team's own RFP.
- The A-12/SR-71 material is the main legal source on Mach 3+ operating realities: fuel, thermal, inlet scheduling and procedures. It contains no OML coordinates, and the SR-71's partial radar-cross-section reduction (chines, edge treatments) is described only qualitatively.
- Dimensioned three-views of the F-22, F-35 and Su-57 suitable for "reference modeling" can only be approximate. Use them to check sizes (span, length, wing area, published weights) and proportions, not as engineering truth. Exact OMLs and RCS-relevant geometry details are proprietary or export-controlled, and seeking them would breach the project's constraints.

### Gaps
- Could not open AIAA pages to list every past fighter or supersonic RFP or to confirm 2025–26 winners and the 2026–27 RFP topic. Check AIAA's "Design Competitions" page and the winning-reports archive directly.
- Could not verify university course pages (MIT OCW, Stanford AA241, Virginia Tech, Cranfield): search budget exhausted.
- Could not verify specific legitimate sources of dimensioned three-views for the F-22, F-35, Su-57, MiG-25, MiG-31 and SR-71.

#### Unverified background (verify before citing)
- **University materials**:
  - Stanford AA241 "Aircraft Design: Synthesis and Analysis" (Ilan Kroo) has long been a free online text at adg.stanford.edu/aa241.
  - Virginia Tech's late Prof. W.H. Mason posted free aircraft-design software and "Configuration Aerodynamics" notes (dept.aoe.vt.edu/~mason/Mason_f/MRsoft.html), some of it now archived by VT.
  - MIT OpenCourseWare has free aerospace courses (for example 16.100 Aerodynamics and 16.885J Aircraft Systems Engineering) at ocw.mit.edu.
  - Cranfield's MSc Aerospace Vehicle Design (with a group design project) is a paid degree and has no open materials.
  - TU Delft OpenCourseWare is another free source.
- **Reference-drawing sources that are lawful in principle**:
  - US-government public-domain documents and graphics: NASA Armstrong/Dryden SR-71, YF-12 and F-15/F-16/F-18 research-aircraft three-views in NTRS reports, USAF and National Museum of the USAF fact sheets with dimensions.
  - Wikimedia Commons three-views (check each file's license).
  - Manufacturer fact sheets (Lockheed Martin F-35 and F-22 dimensions; UAC/Sukhoi and MiG brochures).
  - Published monographs: Yefim Gordon's MiG-25/MiG-31/Su-57 books; Crickmore and Jay Miller on the SR-71/A-12.
  - *Jane's All the World's Aircraft* (subscription).
  - User models in the OpenVSP Hangar.
  - Buying documents directly from Russian state exporters may be restricted by current sanctions in many countries; check local law.
- **DTIC**: the public "STINET/Research & Engineering Gateway" split means only Distribution A ("approved for public release") documents are open to everyone. Anything marked Distribution B–F or "export controlled" is off-limits by the project's own rules.

---

## 3. Core textbooks: what each covers and where to buy, borrow or access legally

### Takeaway
No textbook edition, coverage or price could be verified this session (search budget exhausted). The list below is model knowledge. Treat edition years as provisional and confirm at the publisher (AIAA ARC bookstore, Wiley, McGraw-Hill, DARcorporation, SciTech/IET). Legal access routes are publisher purchase, AIAA member discounts, university and public libraries via WorldCat/interlibrary loan, and institutional e-book platforms.

### Cited Findings
- The POFACETS RCS code (Jenn, NPS) is the code associated with Jenn's RCS teaching. Its documentation and the NPS thesis are free. — [MathWorks POfacets4.5](https://www.mathworks.com/matlabcentral/fileexchange/50602-pofacets4-5); [NPS thesis](https://calhoun.nps.edu/entities/publication/02a49858-3b2c-4065-a3e9-9dbb51408488)
- AeroSandbox can export aircraft geometry to CAD tools via STEP, which supports the geometry-to-CAD workflow taught in geometry-focused texts. — [PyPI aerosandbox](https://pypi.org/project/aerosandbox/)
- (No other textbook facts were verified with a source this session; see Gaps.)

### Inferences
- Minimum set for a two-person Mach 3 LO fighter study:
  - Raymer: overall conceptual design process.
  - Nicolai & Carichner: fighter sizing, with low-observable practice from Lockheed experience.
  - Mattingly: engine cycle, inlet and installation for a fighter RFP.
  - Anderson's *Modern Compressible Flow*: supersonic aerodynamics and inlets.
  - Seddon & Goldsmith: inlets.
  - Knott (or Jenn): RCS.
  - Stevens & Lewis: flight dynamics and the simulation model.
  - Niu: airframe structures.
  - Roskam and Torenbeek add depth, but Torenbeek is largely about subsonic civil aircraft.

### Gaps

#### Unverified background: textbook catalogue (model knowledge; verify edition, ISBN and price at the publisher)
- **Raymer, *Aircraft Design: A Conceptual Approach*** (AIAA Education Series; 6th ed. 2018, later editions possible). Covers the full conceptual process: sizing from mission, initial layout and lofting, propulsion integration, aero/weights/performance, stealth basics, cost and trade studies, with worked examples including a fighter. The companion RDS software is sold separately. Buy from AIAA (arc.aiaa.org), with member discounts.
- **Nicolai & Carichner, *Fundamentals of Aircraft and Airship Design, Vol. I – Aircraft Design*** (AIAA, 2010). Strong on fighter and military design (both authors are ex-USAF/Lockheed), with chapters on survivability and low observables plus worked case studies. Available from AIAA.
- **Roskam, *Airplane Design* Parts I–VIII** (DARcorporation; reprints 1985–2000s):
  - I: preliminary sizing
  - II: configuration design and propulsion integration
  - III: layout of cockpit, fuselage, wing and empennage
  - IV: landing gear and systems layout
  - V: component weights
  - VI: aerodynamics, thrust and power
  - VII: stability, control and performance, including military requirements
  - VIII: cost estimation
  
  Sold by DARcorporation (darcorp.com).
- **Mattingly, Heiser & Pratt, *Aircraft Engine Design*** (AIAA, 2nd ed. 2002; check whether a later edition exists). Engine design for an air-to-air fighter RFP worked through the whole book: constraint analysis, mission analysis, parametric and performance cycle analysis, inlet and exhaust design, with AEDsys software. Available from AIAA.
- **Anderson, *Aircraft Performance and Design*** (McGraw-Hill, 1999): introductory performance and design. **Anderson, *Modern Compressible Flow*** (McGraw-Hill, 4th ed. ~2021): shocks, expansion waves, supersonic thin-airfoil and linear theory, method of characteristics, numerical compressible flow. Available from McGraw-Hill.
- **Knott, Shaeffer & Tuley, *Radar Cross Section*** (2nd ed., SciTech Publishing 2004, now IET/SciTech): RCS phenomenology, prediction (PO, GTD/PTD), RAM, shaping and measurement. See also **Jenn, *Radar and Laser Cross Section Engineering*** (AIAA Education Series), the companion to POFACETS. Also relevant: Ball, *The Fundamentals of Aircraft Combat Survivability Analysis and Design* (AIAA).
- **Stevens, Lewis & Johnson, *Aircraft Control and Simulation*** (Wiley, 3rd ed. 2015): 6-DOF equations, an F-16 nonlinear model with aero data tables, trim, linearization and flight control design.
- **Niu, *Airframe Structural Design*** (2nd ed., Adaso/Adastra, ~1999) and the companion *Airframe Stress Analysis and Sizing*: practical structural layout, design details and sizing from Lockheed practice.
- **Whitford, *Design for Air Combat*** (Jane's, 1987; out of print, used copies and libraries): fighter configuration rationale (wings, canards, LERX, intakes, agility). See also Whitford's *Fundamentals of Fighter Design* (Crowood, 2000).
- **Seddon & Goldsmith, *Intake Aerodynamics*** (2nd ed., AIAA/Blackwell, 1999): subsonic and supersonic intakes, pressure recovery, distortion, buzz, boundary-layer diversion. Directly relevant to a Mach 3 inlet.
- **Sóbester & Forrester, *Aircraft Aerodynamic Design: Geometry and Optimization*** (Wiley Aerospace Series, 2014): parametric geometry (curves, surfaces, CST, OpenVSP-style), surrogate-based optimization, with Python/OpenVSP examples.
- **Torenbeek, *Synthesis of Subsonic Airplane Design*** (Delft University Press/Springer, 1982) and ***Advanced Aircraft Design*** (Wiley, 2013): rigorous subsonic civil design and weights. Lower relevance to a Mach 3 fighter, but useful for methods.
- **Legal access**: publisher stores (AIAA ARC, Wiley, McGraw-Hill, DARcorp, IET); university library loans and WorldCat interlibrary loan; institutional subscriptions (AIAA ARC e-books, Wiley Online Library, O'Reilly Learning for some Wiley titles); used-book markets for out-of-print titles (Whitford, Niu). Do not use "free PDF" sites.

---

## 4. What a professional aircraft drawing/data package ("blueprints") consists of, and the governing standards

### Takeaway
A professional "blueprint" package is a controlled set of models, drawings and documents, not a single drawing. It includes the three-view general arrangement (GA), the OML/loft definition, the inboard profile, structural arrangement and part drawings, systems schematics, interface control documents, a drawing tree and parts lists, and weight-and-balance statements. In the US it is governed by ASME Y14.5 (GD&T), ASME Y14.41 (model-based definition) and ASME Y14.100 (drawing practice), and delivered as a technical data package (TDP) under MIL-STD-31000. The current editions found are Y14.5-2018 (reaffirmed 2024), Y14.41-2019 and Y14.100-2017.

### Cited Findings
- **ASME Y14.5-2018** (Dimensioning and Tolerancing, i.e. GD&T) is still current: ANSI lists it as "ASME Y14.5-2018 (R2024)", reaffirmed in 2024. — [ANSI webstore listing](https://webstore.ansi.org/standards/asme/asmey14100dimensioning) (the search tool attributed the "(R2024)" fact to an ANSI "Dimensioning" listing; I could not open it to confirm which URL carries it, so check at asme.org)
- **ASME Y14.41-2019** (Digital Product Definition Data Practices, i.e. model-based definition) is the latest revision, issued 23 Jan 2019. — [Wikipedia: ASME Y14.41](https://en.wikipedia.org/wiki/ASME_Y14.41)
- **ASME Y14.100-2017** (Engineering Drawing Practices) is listed by ANSI as the most recent version. — [ANSI webstore Y14.100-2017](https://webstore.ansi.org/standards/asme/ASMEY141002017); [ASME Y14.100-2017 sell sheet](https://www.asme.org/wwwasmeorg/media/ResourceFiles/Career%20Education/Training/Y14-100-2017-Sell-Sheet.pdf)
- CAD vendors implement Y14.5 rule sets inside MBD tools, for example PTC Creo's ASME Y14.5 rule set for model-based definition. — [PTC Creo ASME Y14.5 rule set](https://support.ptc.com/help/creo/creo_pma/r7.0/usascii/model-based_definition/asme/rule_set.html)

### Inferences
- **Package contents for a digital design study, scaled to two people**:
  1. Three-view GA with principal dimensions, areas and a data block.
  2. OML/loft master geometry, kept as the OpenVSP model plus exported STEP, which is the single source of truth.
  3. Inboard profile showing internal arrangement: cockpit, fuel tanks, weapons bays, engine, inlet duct and landing gear.
  4. Structural arrangement: frames, spars, ribs, longerons, major joints.
  5. Systems schematics: fuel, hydraulic, electrical, environmental control, flight control.
  6. Interface control documents (engine-to-airframe, inlet-to-engine, weapons bay-to-store).
  7. Drawing tree with numbering and a parts list or bill of materials.
  8. Weight and balance statement (group weight breakdown, center-of-gravity envelope).
  9. Configuration and revision control log.
- For a non-manufacturing study, model-based definition (Y14.41-style annotated 3D models) plus a light drawing set is the realistic target. Full Y14.5 GD&T on every part is only needed if parts would be made.
- Buying ASME standards costs money (ANSI/ASME webstores). For a study team, Y14.100 and Y14.41 matter more than deep Y14.5 GD&T.

### Gaps
- MIL-STD-31000 could not be verified (search budget exhausted). Check its current revision (believed to be MIL-STD-31000B, 2018, or later) at ASSIST Quick Search (quicksearch.dla.mil), the free official DoD standards repository.

#### Unverified background (model knowledge; verify)
- **MIL-STD-31000 (Technical Data Packages)** defines TDP elements: 2D drawings and/or 3D models (with model-based TDP options), associated lists, specifications, and TDP data management products. It refers to ASME Y14 standards for drawing and model practice.
- **Related standards to check**:
  - ASME Y14.24 (types and applications of engineering drawings)
  - ASME Y14.34 (associated lists / parts lists)
  - ASME Y14.35 (revision of drawings)
  - ASME Y14.47 (model organization schema)
  - MIL-STD-881 (work breakdown structure; Appendix A covers aircraft systems)
  - MIL-STD-1374 or SAWE Recommended Practices (weight and balance reporting formats)
  - ISO GPS (ISO 1101 family) as the non-US equivalent of Y14.5
  - ATA iSpec 2200 / ATA chapter numbering (civil systems breakdown, often borrowed for system schematics)
- **Classic aircraft design layout documents** (described in Raymer): conceptual layout, inboard profile, loft lines and fuselage cross-sections, then the structural and systems layouts at preliminary design.

---

## 5. CFD compute needs for two people: desktop vs. cloud HPC, rough costs

### Takeaway
No hardware or pricing data could be verified this session: cloud pricing pages and search were unavailable. Sizing guidance below is engineering judgement and must be checked against current vendor price lists. NASA CFD codes running on commercial cloud (Rescale) still need NASA approval and remain US-only.

### Cited Findings
- Running NASA's FUN3D, OVERFLOW or Cart3D on Rescale's cloud requires NASA approval, and these codes are US-release only. — [Rescale: NASA CFD on Rescale](https://rescale.com/?p=82366)
- OVERFLOW 2.5.0 added GPU support (Jun 2025). This shows the trend toward GPU CFD, but the code is US-only. — [NASA catalog OVERFLOW 2.5.0](https://software.nasa.gov/software/LAR-20382-1)
- OpenFOAM 13 runs on Ubuntu, on Windows via WSL and on macOS via Multipass, so a two-person team can run it on ordinary workstations. — [OpenFOAM 13 release](https://openfoam.org/release/13/)

### Inferences
- **Fidelity ladder**:
  - OpenVSP, VSPAERO, Wave Drag and DATCOM run in seconds to minutes on a laptop.
  - SU2 Euler on a half-model (about 1–5 million cells) runs on a 16–32-core desktop with 64–128 GB RAM.
  - SU2 or OpenFOAM RANS on a full fighter with inlet and nozzle (about 20–100 million cells) needs either a 64–96-core workstation with 256–512 GB RAM, or cloud HPC for bursts.
  - Adjoint shape optimization roughly doubles memory needs.
- **Practical recommendation**: one strong workstation (high-core-count AMD or Intel CPU, 128–256 GB ECC RAM, a large NVMe drive; my estimate is about US$4k–10k) for daily work, plus pay-as-you-go cloud HPC for the few large RANS or optimization runs. Keep cloud spend under control with spot/preemptible instances and by sizing meshes with a grid-convergence study.

### Gaps
- Current per-hour prices for AWS HPC instances (hpc7a, hpc6a), Google Cloud H3/C3D/H4D, Azure HBv4/HBv5, and Rescale or other CFD-SaaS were not retrieved. They need to be looked up on the vendors' pricing pages for the team's region.
- No published SU2 or OpenFOAM memory-per-million-cells benchmark was verified this session. The RAM figures above are rules of thumb, not sourced.
- Export-control applicability of LO (RCS/IR) design data in the team's own country (for example Wassenaar Munitions List category ML22 "technology", or ITAR in the US) was not researched. The team should check national rules before publishing detailed signature-reduction results.
