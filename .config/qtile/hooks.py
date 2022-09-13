import libqtile.hook

from utils import set_wallpaper


@libqtile.hook.subscribe.startup_once
def autostart():
    set_wallpaper()
