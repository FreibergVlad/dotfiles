"""
Various environment specific constants and functions used across the whole
Qtile configuration
"""
from pathlib import Path

MOD_KEY = 'mod4'
TERMINAL = 'alacritty'
DEFAULT_FONT = 'Hack Nerd Font'

AUTOSTART_APPS = [
    # trigger session lock after 5 minutes of inactivity
    'xset s 300',
    # subscribe to systemd events, lock session on them
    'xss-lock -- betterlockscreen -l &',
    # run window compositor (restart if running already)
    'killall -qw picom; picom -b',
    # run notification daemon
    'killall -qw dunst; dunst &',
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

ICONS_DIR = str(Path.home() / '.config' / 'qtile' / 'icons')
WALLPAPER_PATH = str(Path.home() / '.config' / 'wallpapers' / 'spaceman.jpg')

TAKE_SCREENSHOT_SHELL_CMD = '''
    maim -s \
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
IS_MICROPHONE_MUTED_SHELL_CMD = '''
    pactl get-source-mute @DEFAULT_SOURCE@ \
        | grep -q 'no' \
        && echo 0 \
        || echo 1
'''
TOGGLE_MICROPHONE_MUTE_SHELL_CMD = '''
    pactl set-source-mute @DEFAULT_SOURCE@ toggle
'''
