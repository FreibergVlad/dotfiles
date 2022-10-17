"""
Top bar configuration lives here
"""
import os

from libqtile import bar, widget
from libqtile.config import Screen

import widgets

from colors import color_schema
from utils import DEFAULT_FONT, ICONS_DIR

widget_defaults = dict(
    font=DEFAULT_FONT,
    background=color_schema['bg'],
    foreground=color_schema['fg'],
    fontsize=14,
    padding=6,
)
extension_defaults = widget_defaults.copy()
separator = widget.Sep(size_percent=50, foreground=color_schema['fg3'])

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    disable_drag=True,
                    use_mouse_wheel=False,
                    active=color_schema['fg'],
                    inactive=color_schema['dark-gray'],
                    highlight_method='text',
                    this_current_screen_border=color_schema['dark-yellow'],
                    urgent_alert_method='text',
                    urgent_text=color_schema['dark-red'],
                    fontsize=18
                ),
                separator,
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.join(ICONS_DIR, 'layouts')],
                    scale=0.5,
                    padding=0
                ),
                widget.CurrentLayout(padding=0),
                widget.Spacer(),
                widget.Clock(format='%d %b %I:%M %p'),
                widget.Spacer(),
                widget.Systray(),
                widget.CheckUpdates(
                    distro='Arch_yay',
                    display_format=' {updates}',
                    no_update_string=' 0',
                    initial_text=' ',
                    colour_have_updates=color_schema['dark-red'],
                    colour_no_updates=color_schema['fg']
                ),
                separator,
                widgets.VolumeDynamicIcon(update_interval=1),
                widgets.MicrophoneDynamicIcon(update_interval=1),
                separator,
                widgets.BatteryDynamicIcon(update_interval=60),
                separator,
                widget.KeyboardLayout(
                    configured_keyboards=['us', 'ru'],
                    fmt=' {}',
                ),
            ],
            30,
            margin=[5, 5, 0, 5],
        ),
    ),
]
