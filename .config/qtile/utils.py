"""
Various constants and utility functions used across the whole Qtile config
"""
import subprocess

from pathlib import Path
from typing import NamedTuple

MOD_KEY = 'mod4'
# workaround for VirtualBox
TERMINAL = 'bash -c \'LIBGL_ALWAYS_SOFTWARE=1 alacritty\''
DEFAULT_FONT = 'Hack Nerd Font'

SET_VOLUME_SHELL_CMD = 'wpctl set-volume @DEFAULT_AUDIO_SINK@ {} --limit 1.0'
TOGGLE_MUTED_SHELL_CMD = 'wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle'
GET_VOLUME_STATE_SHELL_CMD = 'wpctl get-volume @DEFAULT_AUDIO_SINK@'

WALLPAPER_PATH = str(Path.home() / 'wallpaper.png')


class VolumeState(NamedTuple):
    """
    Representation of volume state independently from OS tools
    """
    percentage: int
    muted: bool


def set_wallpaper(wallpaper_path: str = WALLPAPER_PATH):
    """
    Set image from given path as a wallpaper
    """
    subprocess.run(f'feh --bg-scale {wallpaper_path}', shell=True, check=True)


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
