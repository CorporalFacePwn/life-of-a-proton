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
# Phase 1 – Beat 1: Cosmic Intro & Rewind (first real version)
# ----------------------------------------------------------------------
def Phase1Beat1_Intro_segment(scene: Scene):
    """
    Beat 1: Cosmic intro & rewind.

    Visual intent:
      - Present-day universe: rich starfield representing galaxies/stars.
      - Title: 'The Life of a Proton' at the top.
      - A simple universe timeline at the bottom with a marker at 'Now'.
      - Rewind: stars uniformly contract toward the center (scale factor
        shrinking), timeline marker runs back toward 'Big Bang', and a
        bright central glow grows to represent the hot early universe.
      - Final frame: stars gone, central glow + labels:
          'Big Bang (extrapolated singularity)', and 't ≈ 0' on the timeline.

    Narration carries the story (not shown as full on-screen text).
    """
    scene.camera.background_color = BACKGROUND_COLOR

    # --------------------------------------------------------------
    # 1) Title at the top
    # --------------------------------------------------------------
    title = Text("The Life of a Proton", font_size=52)
    title.to_edge(UP, buff=0.7)

    # Optional small subtitle (kept subtle)
    subtitle = Text("From the Big Bang to cosmic time", font_size=28)
    subtitle.next_to(title, DOWN, buff=0.3)

    # --------------------------------------------------------------
    # 2) Starfield representing present-day universe
    # --------------------------------------------------------------
    stars = VGroup()

    # Logical ranges; leave room for the timeline near the bottom
    x_min, x_max = -7.0, 7.0
    y_min, y_max = -3.0, 4.0  # keep stars above the timeline region

    # Star colors roughly corresponding to stellar types
    star_colors = [BLUE_C, BLUE_E, WHITE, YELLOW_E, GOLD, RED_E]

    np.random.seed(1)  # deterministic layout

    N_STARS = 260
    for _ in range(N_STARS):
        x = np.random.uniform(x_min, x_max)
        y = np.random.uniform(y_min, y_max)

        color = np.random.choice(star_colors)
        radius = np.random.uniform(0.02, 0.06)
        opacity = np.random.uniform(0.4, 1.0)

        star = Dot(point=[x, y, 0.0], radius=radius, color=color)
        star.set_opacity(opacity)
        stars.add(star)

    # --------------------------------------------------------------
    # 3) Universe timeline at the bottom
    # --------------------------------------------------------------
    timeline_y = -3.6  # safely inside a 16:9 frame
    timeline_left = np.array([x_min + 0.8, timeline_y, 0.0])
    timeline_right = np.array([x_max - 0.8, timeline_y, 0.0])

    timeline = Line(timeline_left, timeline_right)

    # Labels for ends of the timeline
    bigbang_label = Text("Big Bang", font_size=22)
    now_label = Text("Now", font_size=22)

    bigbang_label.next_to(timeline_left, DOWN, buff=0.15)
    now_label.next_to(timeline_right, DOWN, buff=0.15)

    # Timeline marker (triangle) initially at "Now"
    marker = Triangle(color=YELLOW, fill_opacity=1.0)
    marker.scale(0.18)
    marker.next_to(timeline_right, UP, buff=0.08)

    # Small label above the timeline line
    time_axis_label = Text("Time since Big Bang", font_size=24)
    time_axis_label.next_to(timeline, UP, buff=0.25)

    # --------------------------------------------------------------
    # 4) Central glow that will grow during rewind
    # --------------------------------------------------------------
    glow = Circle(radius=0.4, color=YELLOW)
    glow.set_fill(YELLOW, opacity=0.0)
    glow.set_stroke(width=0.0)
    glow.move_to(ORIGIN)

    # --------------------------------------------------------------
    # 5) Intro: fade in title + stars
    # --------------------------------------------------------------
    scene.play(
        FadeIn(stars, run_time=2.5),
        FadeIn(title, shift=UP * 0.2, run_time=2.0),
        FadeIn(subtitle, run_time=2.0),
    )
    scene.wait(PAUSE_MED)

    # Fade subtitle early to reduce clutter before the rewind
    scene.play(FadeOut(subtitle, run_time=ANIM_FAST))
    scene.wait(PAUSE_SHORT)

    # --------------------------------------------------------------
    # 6) Introduce the timeline at the bottom
    # --------------------------------------------------------------
    scene.play(
        Create(timeline, run_time=ANIM_MED),
        FadeIn(time_axis_label, run_time=ANIM_MED),
    )
    scene.play(
        FadeIn(bigbang_label, now_label, marker, run_time=ANIM_MED),
    )
    scene.wait(PAUSE_MED)

    # --------------------------------------------------------------
    # 7) Rewind animation
    #    - Stars contract toward center (scale factor shrinking)
    #    - Timeline marker moves from 'Now' toward 'Big Bang'
    #    - Central glow expands and brightens
    # --------------------------------------------------------------
    scene.add(glow)

    rewind_run_time = 10.0

    # Target position for the marker: just above the left side of the timeline
    marker_target = timeline_left + np.array([0.0, 0.15, 0.0])

    scene.play(
        # Stars uniformly contract toward the origin
        stars.animate.scale(0.12),
        # Marker moves from 'Now' back toward 'Big Bang'
        marker.animate.move_to(marker_target),
        # Glow grows and brightens to dominate the frame
        glow.animate.scale(30.0).set_fill(YELLOW, opacity=0.85),
        # Fade the title gently during the rewind so we end with just the glow + timeline
        FadeOut(title, run_time=rewind_run_time * 0.5),
        run_time=rewind_run_time,
        rate_func=smooth,
    )

    # Remove individual stars once they're effectively merged into the glow
    scene.remove(stars)
    scene.wait(PAUSE_SHORT)

    # --------------------------------------------------------------
    # 8) Final labels at t ≈ 0
    # --------------------------------------------------------------
    singularity_label = Text(
        "Big Bang (extrapolated singularity)",
        font_size=28,
    )
    singularity_label.next_to(ORIGIN, UP, buff=0.4)

    t0_label = Text("t ≈ 0", font_size=22)
    t0_label.next_to(timeline_left, DOWN, buff=0.15)

    scene.play(
        FadeIn(singularity_label, run_time=ANIM_MED),
        FadeIn(t0_label, run_time=ANIM_MED),
    )
    scene.wait(PAUSE_LONG)


class Phase1Beat1_Intro(Scene):
    """Micro-scene: Phase 1 – Beat 1 (cosmic intro & rewind)."""

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
