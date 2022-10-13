"""
Custom Qtile widgets live here
"""
from libqtile import widget
from libqtile.widget.battery import BatteryState, BatteryStatus

from utils import get_volume_state, set_volume, toggle_volume_mute


class BatteryDynamicIcon(widget.Battery):
    """
    Widget to display battery icon depending on battery state
    """

    FULL_BATTERY_ICON = ''
    EMPTY_BATTERY_ICON = ''
    UNKNOWN_BATTERY_ICON = ''

    CHARGING_ICONS = {
        10: '',
        20: '',
        30: '',
        40: '',
        50: '',
        60: '',
        70: '',
        80: '',
        90: '',
        100: FULL_BATTERY_ICON
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
        100: FULL_BATTERY_ICON
    }

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
        if state == BatteryState.DISCHARGING:
            return self.DISCHARGING_ICONS[low_boundary]
        assert False, 'unknown battery state'


class VolumeDynamicIcon(widget.base.InLoopPollText):
    """
    Widget to display volume icon depending on volume level
    """

    DEFAULT_STEP_PERCENTAGE = 5
    """
    Default step to raise / lower volume
    """

    ICONS = {
        'muted': '婢',
        'low': '奄',
        'medium': '奔',
        'high': '墳'
    }

    def poll(self):
        volume_state = get_volume_state()
        volume = volume_state.percentage
        if volume_state.muted:
            icon = self.ICONS['muted']
        else:
            icon = self._get_volume_icon(volume)
        return f'{icon} {volume}%'

    # 'cmd' prefix is required by Qtile while
    # looking for the command for execution

    def cmd_raise_volume(self):
        """
        Raise volume, method is called by Qtile on external event
        """
        if get_volume_state().muted:
            toggle_volume_mute()
        set_volume(+self.DEFAULT_STEP_PERCENTAGE)
        self.tick()

    def cmd_lower_volume(self):
        """
        Lower volume, method is called by Qtile on external event
        """
        set_volume(-self.DEFAULT_STEP_PERCENTAGE)
        self.tick()

    def cmd_toggle_mute_volume(self):
        """
        Mute / unmute volume, method is called by Qtile on external event
        """
        toggle_volume_mute()
        self.tick()

    def _get_volume_icon(self, volume: int) -> str:
        if volume <= 0:
            return self.ICONS['muted']
        if volume <= 30:
            return self.ICONS['low']
        if volume < 80:
            return self.ICONS['medium']
        return self.ICONS['high']
