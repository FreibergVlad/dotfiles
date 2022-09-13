from libqtile import bar, widget
from libqtile.config import Screen

from utils import DEFAULT_FONT
from widgets import Battery, Volume

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
                widget.WindowName(),
                widget.Systray(),
                Battery(),
                Volume(update_interval=1),
                widget.KeyboardLayout(
                    configured_keyboards=['us', 'ru'],
                    fmt=' {}'
                ),
                widget.Clock(format=' %Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            24,
        ),
    ),
]
