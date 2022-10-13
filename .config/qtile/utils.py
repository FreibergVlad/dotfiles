"""
Various constants and utility functions used across the whole Qtile config
"""
import logging
import os
import re
import subprocess

from pathlib import Path
from typing import NamedTuple

logger = logging.getLogger(__name__)

MOD_KEY = 'mod4'
# workaround for VirtualBox
TERMINAL = 'bash -c \'LIBGL_ALWAYS_SOFTWARE=1 alacritty\''
DEFAULT_FONT = 'Hack Nerd Font'

SET_VOLUME_SHELL_CMD = 'wpctl set-volume @DEFAULT_AUDIO_SINK@ {} --limit 1.0'
TOGGLE_MUTED_SHELL_CMD = 'wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle'
GET_VOLUME_STATE_SHELL_CMD = 'wpctl get-volume @DEFAULT_AUDIO_SINK@'

RUN_APP_LAUNCHER_SHELL_CMD = 'rofi -show drun'

WALLPAPERS_DIR = str(Path.home() / '.wallpapers')
WALLPAPER_REGEX = re.compile(r'(.*\.png$)|(.*\.jpg$)')

TAKE_SCREENSHOT_SHELL_CMD = '''
    scrot -s \
        -F "$(xdg-user-dir PICTURES)/screenshot_%Y-%m-%d_%H.%M.%S.png" \
        -e 'xclip -selection clipboard -target image/png -i $f'
'''


class VolumeState(NamedTuple):
    """
    Representation of volume state independently from OS tools
    """
    percentage: int
    muted: bool


def set_wallpaper(wallpaper_path: str | None = None):
    """
    Set image from given path as a wallpaper. If path is not specified,
    then try to find wallpaper in pre-defined directory
    """
    try:
        wallpaper_path = wallpaper_path or find_wallpaper()
        subprocess.run(f'feh --bg-scale {wallpaper_path}',
                       shell=True, check=True)
    except subprocess.CalledProcessError:
        logger.exception('Error when setting the wallpaper from path "%s"',
                         wallpaper_path)


def find_wallpaper(root_dir: str = WALLPAPERS_DIR) -> str | None:
    """
    Try to find wallpaper in pre-defined directory. Pick the first file
    with .jpg or .png extension
    """
    for _, _, files in os.walk(root_dir):
        for file in files:
            if WALLPAPER_REGEX.match(file):
                return os.path.join(root_dir, file)
    return None


def set_volume(step_percentage: int):
    """
    Raise / lower volume
    """
    sign = '+' if step_percentage > 0 else '-'
    step_percentage = abs(step_percentage)
    shell_cmd = SET_VOLUME_SHELL_CMD.format(f'{step_percentage}%{sign}')
    subprocess.run(shell_cmd, shell=True, check=True)


def toggle_volume_mute():
    """
    Toggle volume mute
    """
    subprocess.run(TOGGLE_MUTED_SHELL_CMD, shell=True, check=True)


def get_volume_state() -> VolumeState:
    """
    Get current volume state
    """
    output = subprocess.check_output(GET_VOLUME_STATE_SHELL_CMD,
                                     shell=True, text=True)
    percentage = int(float(output.split()[1]) * 100)
    muted = '[MUTED]' in output
    return VolumeState(percentage, muted)
