"""
Qtile hooks live here
"""
import subprocess

import libqtile.hook

from libqtile.log_utils import logger

from utils import STARTUP_SCRIPT_PATH


@libqtile.hook.subscribe.startup
def autostart():
    """
    Executed when Qtile starts
    """
    try:
        subprocess.run([STARTUP_SCRIPT_PATH], check=True)
    except subprocess.CalledProcessError:
        logger.exception('Error while executing startup hook')
