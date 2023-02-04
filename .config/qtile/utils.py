"""
Various environment specific constants and functions used across the whole
Qtile configuration
"""
from pathlib import Path

MOD_KEY = 'mod4'
TERMINAL = 'alacritty'
DEFAULT_FONT = 'Hack Nerd Font'

AUTOSTART_APPS = [
    # set auto-repeat delay and rate
    "xset r rate 300 25",
    # trigger session lock after 5 minutes of inactivity,
    # turn display off 2 minutes later
    'xset s 300; xss-lock -- ~/.local/bin/lock-screen &',
    # run window compositor (restart if running already)
    'killall -qw picom; picom -b',
    # run notification daemon
    'killall -qw dunst; dunst &',
    # run bluetooth daemon
    'killall -qw blueman-applet; blueman-applet &',
    # run daemon to auto-mount USB disks
    'killall -qw udiskie; udiskie &',
]
"""
Shell commands which will be started each time Qtile starts in the order that
they are defined here
"""

RUN_APP_LAUNCHER_SHELL_CMD = 'rofi -show drun'

BRIGHTNESS_DIR = 'amdgpu_bl0'
"""
Directory name in /sys/class/backlight which provides
backlight control interface
"""

SET_BRIGHTNESS_SHELL_CMD = 'brightnessctl set {}%'
"""
Shell command template to set screen brightness
"""

ICONS_DIR = str(Path.home() / '.config' / 'qtile' / 'icons')
WALLPAPER_PATH = str(Path.home() / '.config' / 'wallpapers' / 'spaceman.jpg')

TAKE_SCREENSHOT_SHELL_CMD = '''
    maim -o -s \
        | tee $(xdg-user-dir PICTURES)/screenshot_$(date +%F_%H.%M.%S).png \
        | xclip -selection clipboard -t image/png
'''
"""
Shell command to take a screenshot, save it to images directory and copy
it to the clipboard
"""

LOCK_X_SESSION_SHELL_CMD = 'loginctl lock-session'
"""
Shell command to lock X session
"""

KEYBOARD_LAYOUTS = ['us', 'ru']
"""
List of keyboard layouts which should be available in system
"""

GET_SPEAKERS_VOLUME_SHELL_CMD = '''
    pactl get-sink-volume @DEFAULT_SINK@ \
    | grep -i Volume \
    | awk '{print $5}' \
    | sed 's/%//'
'''
RAISE_SPEAKERS_VOLUME_SHELL_CMD = '''
    pactl set-sink-mute @DEFAULT_SINK@ 0 && \
    pactl set-sink-volume @DEFAULT_SINK@ +5%
'''
LOWER_SPEAKERS_VOLUME_SHELL_CMD = 'pactl set-sink-volume @DEFAULT_SINK@ -5%'
ARE_SPEAKERS_MUTED_SHELL_CMD = '''
    pactl get-sink-mute @DEFAULT_SINK@ \
        | grep -q 'no' \
        && echo 0 \
        || echo 1
'''
TOGGLE_SPEAKERS_MUTE_SHELL_CMD = 'pactl set-sink-mute @DEFAULT_SINK@ toggle'

GET_MICROPHONE_VOLUME_SHELL_CMD = '''
    pactl get-source-volume @DEFAULT_SOURCE@ \
    | grep -i Volume \
    | awk '{print $5}' \
    | sed 's/%//'
'''
RAISE_MICROPHONE_VOLUME_SHELL_CMD = '''
    pactl set-source-mute @DEFAULT_SOURCE@ 0 && \
    pactl set-source-volume @DEFAULT_SOURCE@ +5%
'''
LOWER_MICROPHONE_VOLUME_SHELL_CMD = 'pactl set-source-volume @DEFAULT_SOURCE@ -5%'  # noqa: E501
IS_MICROPHONE_MUTED_SHELL_CMD = '''
    pactl get-source-mute @DEFAULT_SOURCE@ \
        | grep -q 'no' \
        && echo 0 \
        || echo 1
'''
TOGGLE_MICROPHONE_MUTE_SHELL_CMD = '''
    pactl set-source-mute @DEFAULT_SOURCE@ toggle
'''

BLUETOOTH_DEVICE_HCI_PATH = '/dev_88_C9_E8_70_7E_5A'
