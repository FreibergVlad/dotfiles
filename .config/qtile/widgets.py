"""
Custom Qtile widgets live here
"""
import subprocess

from typing import NamedTuple

from libqtile import widget
from libqtile.widget.battery import BatteryState, BatteryStatus


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


class PipeWireAudioIcon(widget.base.InLoopPollText):
    """
    Base widget to display volume level of PipeWire device using 'wpctl'
    """

    class VolumeState(NamedTuple):
        """
        Representation of volume state independently from OS tools
        """
        percentage: int
        muted: bool

    AUDIO_DEVICE = None
    ICONS = {}

    DEFAULT_STEP_PERCENTAGE = 5
    """
    Default step to raise / lower volume
    """

    SET_VOLUME_SHELL_CMD = 'wpctl set-volume {} {} --limit 1.0'
    TOGGLE_MUTED_SHELL_CMD = 'wpctl set-mute {} toggle'
    GET_VOLUME_STATE_SHELL_CMD = 'wpctl get-volume {}'

    def get_volume_state(self) -> 'PipeWireAudioIcon.VolumeState':
        shell_cmd = self.GET_VOLUME_STATE_SHELL_CMD.format(self.AUDIO_DEVICE)
        output = subprocess.check_output(shell_cmd, shell=True, text=True)
        percentage = int(float(output.split()[1]) * 100)
        muted = '[MUTED]' in output
        return PipeWireAudioIcon.VolumeState(percentage, muted)

    def set_volume(self, step_percentage: int):
        """
        Raise / lower volume
        """
        sign = '+' if step_percentage > 0 else '-'
        step_percentage = abs(step_percentage)
        shell_cmd = self.SET_VOLUME_SHELL_CMD.format(
            self.AUDIO_DEVICE,
            f'{step_percentage}%{sign}'
        )
        subprocess.run(shell_cmd, shell=True, check=True)

    def toggle_volume_mute(self):
        """
        Toggle volume mute
        """
        shell_cmd = self.TOGGLE_MUTED_SHELL_CMD.format(self.AUDIO_DEVICE)
        subprocess.run(shell_cmd, shell=True, check=True)

    def poll(self) -> str:
        """
        Called by Qtile periodically to get widget's display string
        """
        volume_state = self.get_volume_state()
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
        if self.get_volume_state().muted:
            self.toggle_volume_mute()
        self.set_volume(+self.DEFAULT_STEP_PERCENTAGE)
        self.tick()

    def cmd_lower_volume(self):
        """
        Lower volume, method is called by Qtile on external event
        """
        self.set_volume(-self.DEFAULT_STEP_PERCENTAGE)
        self.tick()

    def cmd_toggle_mute_volume(self):
        """
        Mute / unmute volume, method is called by Qtile on external event
        """
        self.toggle_volume_mute()
        self.tick()

    def _get_volume_icon(self, volume: int) -> str:
        if volume <= 0:
            return self.ICONS['muted']
        if volume <= 30:
            return self.ICONS['low']
        if volume < 80:
            return self.ICONS['medium']
        return self.ICONS['high']


class VolumeDynamicIcon(PipeWireAudioIcon):
    """
    Widget to display speakers/headset volume icon depending on volume level
    """

    AUDIO_DEVICE = '@DEFAULT_AUDIO_SINK@'
    ICONS = {
        'muted': '婢',
        'low': '奄',
        'medium': '奔',
        'high': '墳'
    }


class MicrophoneDynamicIcon(VolumeDynamicIcon):
    """
    Widget to display microphone volume icon depending on volume level
    """

    AUDIO_DEVICE = '@DEFAULT_AUDIO_SOURCE@'
    ICONS = {
        'muted': '',
        'low': '',
        'medium': '',
        'high': ''
    }
