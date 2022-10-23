"""
Custom Qtile widgets live here
"""
from typing import NamedTuple

from libqtile import widget
from libqtile.widget.battery import BatteryState, BatteryStatus


class Battery(widget.Battery):
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


class Volume(widget.base.InLoopPollText):
    """
    Widget to display volume level. Difference from standard Qtile's
    'widget.Volume' is that it uses Unicode glyphs only and doesn't tightly
    coupled with implementation of various OS tools
    """

    defaults = [
        (
            'get_volume_shell_cmd',
            None,
            'Command to get volume. It should return integer number only '
            'which represents volume level percentage'
        ),
        ('raise_volume_shell_cmd', None, 'Volume up command'),
        ('lower_volume_shell_cmd', None, 'Volume down command'),
        (
            'get_muted_status_shell_cmd',
            None,
            'Command to get muted status. It should only return "1" if '
            'device is muted, "0" otherwise'
        ),
        ('toggle_mute_shell_cmd', None, 'Command to toggle mute status'),
        ('icons', {}, 'Volume level icons'),
    ]

    def __init__(self, **config):
        super().__init__(**config)
        self.add_defaults(self.defaults)

    class VolumeState(NamedTuple):
        """
        Representation of volume state independently from OS tools
        """
        percentage: int
        muted: bool

    def poll(self) -> str:
        """
        Called by Qtile periodically to get widget's display string
        """
        volume_state = self._get_volume_state()
        volume = volume_state.percentage
        if volume_state.muted:
            icon = self.icons['muted']
        else:
            icon = self._get_volume_icon(volume)
        return f'{icon} {volume}%'

    def cmd_raise_volume(self):
        """
        Raise volume, method is called by Qtile on external event
        """
        self.call_process(self.raise_volume_shell_cmd, shell=True)
        self.tick()

    def cmd_lower_volume(self):
        """
        Lower volume, method is called by Qtile on external event
        """
        self.call_process(self.lower_volume_shell_cmd, shell=True)
        self.tick()

    def cmd_toggle_mute_volume(self):
        """
        Mute / unmute volume, method is called by Qtile on external event
        """
        self.call_process(self.toggle_mute_shell_cmd, shell=True)
        self.tick()

    def _get_volume_state(self) -> 'Volume.VolumeState':
        volume = self.call_process(self.get_volume_shell_cmd,
                                   shell=True, text=True)
        muted = self.call_process(self.get_muted_status_shell_cmd,
                                  shell=True, text=True)
        return Volume.VolumeState(int(volume), bool(int(muted)))

    def _get_volume_icon(self, volume: int) -> str:
        if volume <= 0:
            return self.icons['muted']
        if volume <= 30:
            return self.icons['low']
        if volume < 80:
            return self.icons['medium']
        return self.icons['high']
