"""
Top bar configuration lives here
"""
from libqtile import bar, widget
from libqtile.config import Screen

import widgets

from utils import DEFAULT_FONT

widget_defaults = dict(
    font=DEFAULT_FONT,
    fontsize=14,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.Spacer(),
                widget.Clock(format='%d %b %I:%M %p'),
                widget.Spacer(),
                widget.Systray(),
                widget.CheckUpdates(
                    distro='Arch_yay',
                    display_format=' {updates}'
                ),
                widgets.VolumeDynamicIcon(update_interval=1),
                widgets.BatteryDynamicIcon(),
                widget.KeyboardLayout(
                    configured_keyboards=['us', 'ru'],
                    fmt=' {}'
                ),
            ],
            24,
        ),
    ),
]
