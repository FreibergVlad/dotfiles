"""
Qtile hooks live here
"""
import subprocess

import libqtile.hook

from libqtile.log_utils import logger

from utils import AUTOSTART_APPS


@libqtile.hook.subscribe.startup
def autostart():
    """
    Executed when Qtile starts
    """
    for app_cmd in AUTOSTART_APPS:
        try:
            subprocess.run(app_cmd, check=True, shell=True)
        except subprocess.CalledProcessError:
            logger.exception('Error while autostarting "%s" command', app_cmd)
