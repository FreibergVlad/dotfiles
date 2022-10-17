import subprocess

import libqtile.hook

from utils import STARTUP_SCRIPT_PATH


@libqtile.hook.subscribe.startup
def autostart():
    """
    Executed when Qtile starts
    """
    subprocess.run([STARTUP_SCRIPT_PATH])
