# Life of a Proton – Manim Project

A long-form, 3Blue1Brown–style animation built with **Manim Community Edition** that follows the life of a proton from the earliest instants after the Big Bang through its later cosmic roles.

The project emphasizes:

- **Physics-first visuals**: quark–gluon plasma as a fluid, hadronization as a phase transition, realistic stellar/galactic contexts.
- **Pedagogical clarity**: simple, consistent visual metaphors; narration carries most of the story, on-screen text is minimal and purposeful.
- **Modular structure**: each *phase* of the proton’s life is a separate Manim file; each *beat* is a self-contained visual unit (no hidden state between beats).

---

## Project Goals

- Show how a single proton can emerge from a hot early-universe **quark–gluon plasma**.
- Place that proton in the context of:
  - Early-universe expansion and cooling
  - Hadronization (quark confinement into protons/neutrons)
  - Primordial nucleosynthesis and later astrophysical processes (stars, galaxies, etc.)
- Use this “one proton” as a narrative thread to touch many key intro-astronomy topics:
  - Big Bang, cosmic expansion
  - Stellar lives and remnants
  - Galaxies and large-scale structure
- Keep the **underlying physics** honest at a conceptual level while still using simplified, cinematic visuals.

---

## Repository Structure

```text
life-of-a-proton/
├─ src/
│  ├─ common/
│  │  ├─ __init__.py
│  │  ├─ config.py      # global constants: colors, timing, camera ranges, etc.
│  │  ├─ utils.py       # shared helpers: Brownian motion, layout helpers, etc.
│  │  └─ visuals.py     # reusable diagrams: proton icon, timelines, etc.
│  ├─ phase1_quark_gluon.py        # Phase 1: Birth in a Quark–Gluon Plasma
│  ├─ phase2_nucleosynthesis.py    # Phase 2: Primordial nuclei & first atoms (planned)
│  ├─ phase3_stars_and_galaxies.py # later phases (planned)
│  └─ ...                          # additional phases as needed
│
├─ docs/
│  ├─ BEATS_PHASE1.md     # beat-by-beat spec for Phase 1 (narration + visuals)
│  ├─ PHASES_OVERVIEW.md  # outline of all phases of the proton's "life"
│  └─ NOTES.md            # scratch ideas, physics notes, etc.
│
├─ scripts/
│  ├─ render_phase1_dev.bat  # optional helper scripts for rendering
│  └─ ...
│
├─ environment.yml
├─ .gitignore
└─ README.md
