import subprocess

from pathlib import Path

MOD_KEY = 'mod4'
TERMINAL = 'alacritty'
DEFAULT_FONT = 'Hack Nerd Font'

RAISE_VOLUME_SHELL_CMD = 'pulsemixer --change-volume +5'
LOWER_VOLUME_SHELL_CMD = 'pulsemixer --change-volume -5'
TOGGLE_MUTED_SHELL_CMD = 'pulsemixer --toggle-mute'
GET_VOLUME_SHELL_CMD = 'pulsemixer --get-volume | awk \'{print $1}\''
GET_MUTE_STATUS_SHELL_CMD = 'pulsemixer --get-mute'

WALLPAPER_PATH = str(Path.home() / 'wallpaper.jpg')


def set_wallpaper(wallpaper_path: str = WALLPAPER_PATH):
    subprocess.run(f'feh --bg-scale {wallpaper_path}', shell=True)
