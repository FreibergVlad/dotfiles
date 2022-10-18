"""
Various constants and utility functions used across the whole Qtile config
"""
from pathlib import Path

MOD_KEY = 'mod4'
# workaround for VirtualBox
TERMINAL = 'bash -c \'LIBGL_ALWAYS_SOFTWARE=1 alacritty\''
DEFAULT_FONT = 'Hack Nerd Font'

RUN_APP_LAUNCHER_SHELL_CMD = 'rofi -show drun'

ICONS_DIR = str(Path.home() / '.config' / 'qtile' / 'icons')
STARTUP_SCRIPT_PATH = str(Path.home() / '.config' / 'qtile' / 'autostart.sh')

TAKE_SCREENSHOT_SHELL_CMD = '''
    scrot -s \
        -F "$(xdg-user-dir PICTURES)/screenshot_%Y-%m-%d_%H.%M.%S.png" \
        -e 'xclip -selection clipboard -target image/png -i $f'
'''
"""
Shell command to take a screenshot, save it to images directory and copy
it to the clipboard
"""

LOCK_X_SESSION_SHELL_CMD = 'loginctl lock-session'
"""
Shell command to lock X session
"""
