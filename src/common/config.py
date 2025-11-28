"""
Common configuration constants for the Life of a Proton project.

These are intentionally simple defaults; we can tweak them as the
visual style and pacing evolve.
"""

from manim import BLACK

# ----------------------------------------------------------------------
# Timing constants (in seconds)
# ----------------------------------------------------------------------

# Short pauses for small beats/gestures
PAUSE_SHORT = 0.5

# Medium pauses for letting an idea land
PAUSE_MED = 1.0

# Longer pauses for important visuals / narration beats
PAUSE_LONG = 2.0

# Animation run-times (used as guidelines, not strict rules)
ANIM_FAST = 0.7
ANIM_MED = 1.2
ANIM_SLOW = 1.8

# ----------------------------------------------------------------------
# Visual / layout constants
# ----------------------------------------------------------------------

# Background color for most scenes (we can override per scene)
BACKGROUND_COLOR = BLACK

# Logical coordinate ranges for wide shots.
# These assume a standard 16:9 aspect ratio (e.g. 1280x720, 1920x1080).
# Manim's default frame height is 8 units; frame_width ~= 14.22 (16:9).
X_RANGE = (-7.0, 7.0)
Y_RANGE = (-4.0, 4.0)
