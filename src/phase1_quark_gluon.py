"""
Phase 1 – Birth in a Quark–Gluon Plasma

This file defines:
- Independent micro-scenes for each Phase 1 beat (Phase1BeatX_*)
- A combined Phase1QuarkGluonPlasma scene that chains the beats

Right now, everything is a minimal placeholder: simple text + fades.
We will gradually replace each beat's segment with the real animation,
following the physics-first, low-text, beat-by-beat design.
"""

from manim import *

from common.config import (
    BACKGROUND_COLOR,
    PAUSE_SHORT,
    PAUSE_MED,
    PAUSE_LONG,
    ANIM_FAST,
    ANIM_MED,
    ANIM_SLOW,
)


# ======================================================================
# Helper pattern: segment functions + micro-scenes
# ======================================================================
# For each beat we define a *segment* function that takes a Scene.
# Then we wrap it in a Scene subclass so we can render the beat
# independently during development and testing.
#
# Example:
#   def Phase1Beat1_Intro_segment(scene: Scene): ...
#
#   class Phase1Beat1_Intro(Scene):
#       def construct(self):
#           Phase1Beat1_Intro_segment(self)
#
# The combined Phase1QuarkGluonPlasma scene will call the segment
# functions in order, but each beat is written to be self-contained:
# it builds what it needs from scratch and does not rely on previous beats.
# ======================================================================


# ======================================================================
# Phase 1 – Birth in a Quark–Gluon Plasma
# ======================================================================


# ----------------------------------------------------------------------
# Phase 1 – Beat 1: Cosmic Intro & Rewind (placeholder)
# ----------------------------------------------------------------------
def Phase1Beat1_Intro_segment(scene: Scene):
    """
    Beat 1: Cosmic intro & rewind (placeholder version).

    Final intent:
      - Show present-day universe (stars/galaxies)
      - Introduce "the life of a proton"
      - Rewind cosmic history back toward t = 0

    For now:
      - Just show a title card so we can confirm the pipeline works.
    """
    scene.camera.background_color = BACKGROUND_COLOR

    title = Text("Phase 1 – Beat 1: Cosmic Intro & Rewind", font_size=42)
    subtitle = Text("Placeholder scene", font_size=28).next_to(title, DOWN, buff=0.4)

    title.to_edge(UP, buff=1.0)

    scene.play(FadeIn(title, shift=UP * 0.2, run_time=ANIM_MED))
    scene.play(FadeIn(subtitle, run_time=ANIM_FAST))
    scene.wait(PAUSE_LONG)

    scene.play(FadeOut(title, subtitle, run_time=ANIM_FAST))
    scene.wait(PAUSE_SHORT)


class Phase1Beat1_Intro(Scene):
    """Micro-scene: Phase 1 – Beat 1 (cosmic intro & rewind, placeholder)."""

    def construct(self):
        Phase1Beat1_Intro_segment(self)


# ----------------------------------------------------------------------
# Phase 1 – Beat 2: Phase Title & Context (placeholder)
# ----------------------------------------------------------------------
def Phase1Beat2_Title_segment(scene: Scene):
    """
    Beat 2: Show the phase title and some basic early-universe context.

    Final intent:
      - Title: 'Phase 1 – Birth in a Quark–Gluon Plasma'
      - Very short text about time after Big Bang and temperature
      - Minimal on-screen text, narration carries details

    For now:
      - Simple centered title + subtitle.
    """
    scene.camera.background_color = BACKGROUND_COLOR

    title = Text("Phase 1 – Birth in a Quark–Gluon Plasma", font_size=40)
    title.to_edge(UP, buff=0.8)

    subtitle = Text("Early universe: quark–gluon plasma era", font_size=28)
    subtitle.next_to(title, DOWN, buff=0.5)

    scene.play(FadeIn(title, shift=UP * 0.2, run_time=ANIM_MED))
    scene.play(FadeIn(subtitle, shift=UP * 0.1, run_time=ANIM_FAST))
    scene.wait(PAUSE_LONG)

    scene.play(FadeOut(title, subtitle, run_time=ANIM_FAST))
    scene.wait(PAUSE_SHORT)


class Phase1Beat2_Title(Scene):
    """Micro-scene: Phase 1 – Beat 2 (phase title & context, placeholder)."""

    def construct(self):
        Phase1Beat2_Title_segment(self)


# ----------------------------------------------------------------------
# Phase 1 – Beat 3: Quark–Gluon Plasma (wide shot, placeholder)
# ----------------------------------------------------------------------
def Phase1Beat3_QGPWideShot_segment(scene: Scene):
    """
    Beat 3: Quark–gluon plasma wide shot (placeholder).

    Final intent:
      - Dense soup of up/down quark dots with fluid-like motion
      - Gluon 'flashes' between quarks
      - Minimal labels: 'Quark–Gluon Plasma', time/temperature hint

    For now:
      - Simple gradient background + label.
    """
    scene.camera.background_color = BACKGROUND_COLOR

    label = Text("Quark–Gluon Plasma (placeholder wide shot)", font_size=36)
    label.to_edge(UP, buff=0.8)

    scene.play(FadeIn(label, run_time=ANIM_MED))
    scene.wait(PAUSE_LONG)

    scene.play(FadeOut(label, run_time=ANIM_FAST))
    scene.wait(PAUSE_SHORT)


class Phase1Beat3_QGPWideShot(Scene):
    """Micro-scene: Phase 1 – Beat 3 (QGP wide shot, placeholder)."""

    def construct(self):
        Phase1Beat3_QGPWideShot_segment(self)


# ----------------------------------------------------------------------
# Phase 1 – Beat 4: Up/Down Quark Conceptual Pull-Out (placeholder)
# ----------------------------------------------------------------------
def Phase1Beat4_QuarkTypes_segment(scene: Scene):
    """
    Beat 4: Introduce up/down quarks as a conceptual pull-out.

    Final intent:
      - Faint QGP background
      - Pull an 'up quark' dot forward with label and charge
      - Pull a 'down quark' dot forward with label and charge
      - Explicitly explain this is a conceptual visualization

    For now:
      - Two labeled Text objects: up quark, down quark.
    """
    scene.camera.background_color = BACKGROUND_COLOR

    title = Text("Quark Types (placeholder)", font_size=38)
    title.to_edge(UP, buff=0.8)

    up_text = Text("up quark (u): +2/3 e", font_size=30)
    down_text = Text("down quark (d): -1/3 e", font_size=30)

    up_text.next_to(title, DOWN, buff=0.6)
    down_text.next_to(up_text, DOWN, buff=0.3)

    scene.play(FadeIn(title, run_time=ANIM_MED))
    scene.play(FadeIn(up_text, run_time=ANIM_MED))
    scene.play(FadeIn(down_text, run_time=ANIM_MED))
    scene.wait(PAUSE_LONG)

    scene.play(FadeOut(title, up_text, down_text, run_time=ANIM_FAST))
    scene.wait(PAUSE_SHORT)


class Phase1Beat4_QuarkTypes(Scene):
    """Micro-scene: Phase 1 – Beat 4 (quark types, placeholder)."""

    def construct(self):
        Phase1Beat4_QuarkTypes_segment(self)


# ----------------------------------------------------------------------
# Phase 1 – Beat 5: Cartoon Protons & Neutrons (placeholder)
# ----------------------------------------------------------------------
def Phase1Beat5_CartoonHadrons_segment(scene: Scene):
    """
    Beat 5: Show cartoon protons/neutrons built from up/down quarks.

    Final intent:
      - Triangular arrangements of colored dots (uud, udd)
      - Labels: 'proton (p⁺)', 'neutron (n)'
      - Emphasize this is a simplified cartoon of a bound state

    For now:
      - Simple text labels indicating proton/neutron cartoons.
    """
    scene.camera.background_color = BACKGROUND_COLOR

    title = Text("Cartoon Hadrons (placeholder)", font_size=36)
    title.to_edge(UP, buff=0.8)

    proton_text = Text("Proton (p⁺): uud", font_size=30)
    neutron_text = Text("Neutron (n): udd", font_size=30)

    proton_text.next_to(title, DOWN, buff=0.6)
    neutron_text.next_to(proton_text, DOWN, buff=0.3)

    scene.play(FadeIn(title, run_time=ANIM_MED))
    scene.play(FadeIn(proton_text, run_time=ANIM_MED))
    scene.play(FadeIn(neutron_text, run_time=ANIM_MED))
    scene.wait(PAUSE_LONG)

    scene.play(FadeOut(title, proton_text, neutron_text, run_time=ANIM_FAST))
    scene.wait(PAUSE_SHORT)


class Phase1Beat5_CartoonHadrons(Scene):
    """Micro-scene: Phase 1 – Beat 5 (cartoon hadrons, placeholder)."""

    def construct(self):
        Phase1Beat5_CartoonHadrons_segment(self)


# ----------------------------------------------------------------------
# Phase 1 – Beat 6: Cooling & Confinement (Hadronization, placeholder)
# ----------------------------------------------------------------------
def Phase1Beat6_Hadronization_segment(scene: Scene):
    """
    Beat 6: Cooling & confinement (hadronization).

    Final intent:
      - QGP cooling visual (temperature bar, timeline)
      - Quarks smoothly locking into hadrons all across the field
      - Transition from deconfined quarks to a hadron gas

    For now:
      - Text label: 'Hadronization (placeholder)'.
    """
    scene.camera.background_color = BACKGROUND_COLOR

    label = Text("Hadronization (placeholder)", font_size=36)
    label.move_to(ORIGIN)

    scene.play(FadeIn(label, run_time=ANIM_MED))
    scene.wait(PAUSE_LONG)

    scene.play(FadeOut(label, run_time=ANIM_FAST))
    scene.wait(PAUSE_SHORT)


class Phase1Beat6_Hadronization(Scene):
    """Micro-scene: Phase 1 – Beat 6 (hadronization, placeholder)."""

    def construct(self):
        Phase1Beat6_Hadronization_segment(self)


# ----------------------------------------------------------------------
# Phase 1 – Beat 7: Tagging 'Our Proton' (placeholder)
# ----------------------------------------------------------------------
def Phase1Beat7_OurProton_segment(scene: Scene):
    """
    Beat 7: Highlight one proton as 'our proton' to follow.

    Final intent:
      - A field of hadrons (from Beat 6-like visual)
      - One proton gets a bright halo and label 'Our proton'
      - Others fade slightly to emphasize the chosen one

    For now:
      - 'Our proton' text centered on screen.
    """
    scene.camera.background_color = BACKGROUND_COLOR

    label = Text("Our proton (placeholder)", font_size=40)
    label.move_to(ORIGIN)

    scene.play(FadeIn(label, run_time=ANIM_MED))
    scene.wait(PAUSE_LONG)

    scene.play(FadeOut(label, run_time=ANIM_FAST))
    scene.wait(PAUSE_SHORT)


class Phase1Beat7_OurProton(Scene):
    """Micro-scene: Phase 1 – Beat 7 (our proton, placeholder)."""

    def construct(self):
        Phase1Beat7_OurProton_segment(self)


# ----------------------------------------------------------------------
# Phase 1 – Beat 8: Phase Wrap & Bridge to Phase 2 (placeholder)
# ----------------------------------------------------------------------
def Phase1Beat8_Wrap_segment(scene: Scene):
    """
    Beat 8: Wrap up Phase 1 and hint at what's next.

    Final intent:
      - Our proton + early-universe timeline
      - Text/narration: we've finished the 'birth' chapter
      - Tease of primordial nucleosynthesis / first atoms

    For now:
      - Simple 'End of Phase 1 (placeholder)' title.
    """
    scene.camera.background_color = BACKGROUND_COLOR

    title = Text("End of Phase 1 (placeholder)", font_size=40)
    subtitle = Text("Bridge to Phase 2", font_size=28)

    title.to_edge(UP, buff=0.8)
    subtitle.next_to(title, DOWN, buff=0.5)

    scene.play(FadeIn(title, run_time=ANIM_MED))
    scene.play(FadeIn(subtitle, run_time=ANIM_FAST))
    scene.wait(PAUSE_LONG)

    scene.play(FadeOut(title, subtitle, run_time=ANIM_FAST))
    scene.wait(PAUSE_SHORT)


class Phase1Beat8_Wrap(Scene):
    """Micro-scene: Phase 1 – Beat 8 (wrap & bridge, placeholder)."""

    def construct(self):
        Phase1Beat8_Wrap_segment(self)


# ----------------------------------------------------------------------
# Phase 1 – Combined scene (placeholder chaining of beats)
# ----------------------------------------------------------------------
class Phase1QuarkGluonPlasma(Scene):
    """
    Combined Phase 1 scene: calls all Phase 1 beat segments in order.

    Even here, each segment is written to be self-contained. When we
    upgrade individual beats with real visuals, we won't rely on shared
    state across beats; continuity is visual and editorial, not
    implemented via shared scene attributes.
    """

    def construct(self):
        Phase1Beat1_Intro_segment(self)
        Phase1Beat2_Title_segment(self)
        Phase1Beat3_QGPWideShot_segment(self)
        Phase1Beat4_QuarkTypes_segment(self)
        Phase1Beat5_CartoonHadrons_segment(self)
        Phase1Beat6_Hadronization_segment(self)
        Phase1Beat7_OurProton_segment(self)
        Phase1Beat8_Wrap_segment(self)
