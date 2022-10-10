import libqtile.hook

from utils import set_wallpaper


@libqtile.hook.subscribe.startup
def autostart():
    """
    Executed when Qtile starts
    """
    set_wallpaper()
