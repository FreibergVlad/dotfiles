"""
Top bar configuration lives here
"""
import os

from libqtile import bar, widget
from libqtile.config import Screen

import widgets

from colors import color_schema
from utils import (
    DEFAULT_FONT,
    ICONS_DIR,
    WALLPAPER_PATH,
    KEYBOARD_LAYOUTS,
    BRIGHTNESS_DIR,
    SET_BRIGHTNESS_SHELL_CMD,
    GET_SPEAKERS_VOLUME_SHELL_CMD,
    RAISE_SPEAKERS_VOLUME_SHELL_CMD,
    LOWER_SPEAKERS_VOLUME_SHELL_CMD,
    ARE_SPEAKERS_MUTED_SHELL_CMD,
    TOGGLE_SPEAKERS_MUTE_SHELL_CMD,
    GET_MICROPHONE_VOLUME_SHELL_CMD,
    IS_MICROPHONE_MUTED_SHELL_CMD,
    TOGGLE_MICROPHONE_MUTE_SHELL_CMD,
    BLUETOOTH_DEVICE_HCI_PATH
)

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
        wallpaper=WALLPAPER_PATH,
        wallpaper_mode='fill',
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
                widgets.Bluetooth(
                    hci=BLUETOOTH_DEVICE_HCI_PATH,
                    fmt="{}",
                    fontsize=16
                ),
                widgets.NetworkManager(
                    name='network_manager',
                    icons={
                        '802-3-ethernet': '',
                        '802-11-wireless': ' ',
                    },
                    format_string='{icon}',
                    no_connection_format_string='{icon} {network_name} '
                                                '(no connection)',
                    update_interval=5,
                ),
                separator,
                widgets.Volume(
                    name='speakers_volume',
                    get_volume_shell_cmd=GET_SPEAKERS_VOLUME_SHELL_CMD,
                    raise_volume_shell_cmd=RAISE_SPEAKERS_VOLUME_SHELL_CMD,
                    lower_volume_shell_cmd=LOWER_SPEAKERS_VOLUME_SHELL_CMD,
                    get_muted_status_shell_cmd=ARE_SPEAKERS_MUTED_SHELL_CMD,
                    toggle_mute_shell_cmd=TOGGLE_SPEAKERS_MUTE_SHELL_CMD,
                    icons={
                        'muted': '婢',
                        'low': '奄',
                        'medium': '奔',
                        'high': '墳'
                    },
                    update_interval=1,
                ),
                widgets.Volume(
                    name='microphone_volume',
                    get_volume_shell_cmd=GET_MICROPHONE_VOLUME_SHELL_CMD,
                    get_muted_status_shell_cmd=IS_MICROPHONE_MUTED_SHELL_CMD,
                    toggle_mute_shell_cmd=TOGGLE_MICROPHONE_MUTE_SHELL_CMD,
                    icons={
                        'muted': '',
                        'low': '',
                        'medium': '',
                        'high': ''
                    },
                    update_interval=1
                ),
                separator,
                widgets.Battery(update_interval=60),
                widget.Backlight(
                    backlight_name=BRIGHTNESS_DIR,
                    change_command=SET_BRIGHTNESS_SHELL_CMD,
                    format=' {percent:2.0%}'
                ),
                separator,
                widget.KeyboardLayout(
                    configured_keyboards=KEYBOARD_LAYOUTS,
                    fmt=' {}',
                ),
            ],
            30,
            margin=[5, 5, 0, 5],
        ),
    ),
]
