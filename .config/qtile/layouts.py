"""
Qtile layouts configuration lives here
"""
from libqtile import layout

from colors import color_schema

layout_defaults = dict(
    margin=5,
    border_focus=color_schema['yellow'],
    border_normal=color_schema['bg'],
)
layouts = [
    layout.Max(**layout_defaults),
    layout.Columns(**layout_defaults),
    layout.Floating(**layout_defaults),
]
floating_layout = layout.Floating(
    # Run the utility of `xprop` to see the wm class and name of an X client
    float_rules=[
        *layout.Floating.default_float_rules,
    ]
)
