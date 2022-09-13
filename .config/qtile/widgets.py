import subprocess

from libqtile import widget
from libqtile.widget.battery import BatteryState, BatteryStatus

from utils import (
    RAISE_VOLUME_SHELL_CMD,
    LOWER_VOLUME_SHELL_CMD,
    TOGGLE_MUTED_SHELL_CMD,
    GET_VOLUME_SHELL_CMD,
    GET_MUTE_STATUS_SHELL_CMD,
)


class Battery(widget.Battery):

    FULL_BATTERY_ICON = ''
    EMPTY_BATTERY_ICON = ''
    UNKNOWN_BATTERY_ICON = ''

    CHARGING_ICONS = {
        10: '',
        20: '',
        30: '',
        40: '',
        50: '',
        60: '',
        70: '',
        80: '',
        90: '',
        100: ''
    }

    DISCHARGING_ICONS = {
        10: '',
        20: '',
        30: '',
        40: '',
        50: '',
        60: '',
        70: '',
        80: '',
        90: '',
        100: ''
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def build_string(self, status: BatteryStatus) -> str:
        """
        Override parent's method to display battery icon dynamically
        depending on battery state
        """
        state: BatteryState = status.state
        percentage = int(status.percent * 100)
        icon = self._get_battery_icon(state, percentage)
        return f'{icon} {percentage}%'

    def _get_battery_icon(self, state: BatteryState, percentage: int) -> str:
        if state == BatteryState.FULL:
            return self.FULL_BATTERY_ICON
        if state == BatteryState.EMPTY:
            return self.EMPTY_BATTERY_ICON
        if state == BatteryState.UNKNOWN:
            return self.UNKNOWN_BATTERY_ICON
        low_boundary = percentage // 10 * 10 if percentage >= 10 else 10
        if state == BatteryState.CHARGING:
            return self.CHARGING_ICONS[low_boundary]
        elif state == BatteryState.DISCHARGING:
            return self.DISCHARGING_ICONS[low_boundary]
        assert False, 'unknown battery state'


class Volume(widget.base.InLoopPollText):

    ICONS = {
        'muted': '婢',
        'low': '奄',
        'medium': '奔',
        'high': '墳'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def poll(self):
        volume = self._get_volume()
        if self._is_muted():
            icon = self.ICONS['muted']
        else:
            icon = self._get_volume_icon(volume)
        return f'{icon} {volume}%'

    # 'cmd' prefix is required by Qtile while
    # looking for the command for execution

    def cmd_raise_volume(self):
        subprocess.run(RAISE_VOLUME_SHELL_CMD, shell=True)
        self.tick()

    def cmd_lower_volume(self):
        subprocess.run(LOWER_VOLUME_SHELL_CMD, shell=True)
        self.tick()

    def cmd_toggle_mute_volume(self):
        subprocess.run(TOGGLE_MUTED_SHELL_CMD, shell=True)
        self.tick()

    def _get_volume_icon(self, volume: int) -> str:
        if volume <= 0:
            return self.ICONS['muted']
        if volume <= 30:
            return self.ICONS['low']
        if volume < 80:
            return self.ICONS['medium']
        return self.ICONS['high']

    @staticmethod
    def _is_muted() -> bool:
        output = subprocess.check_output(GET_MUTE_STATUS_SHELL_CMD,
                                         shell=True, text=True)
        return bool(int(output.strip()))

    @staticmethod
    def _get_volume() -> int:
        output = subprocess.check_output(GET_VOLUME_SHELL_CMD,
                                         shell=True, text=True)
        return int(output.strip())
