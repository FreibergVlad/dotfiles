"""
Custom Qtile widgets live here
"""
from typing import NamedTuple

from libqtile import widget
from libqtile.log_utils import logger
from libqtile.widget.battery import BatteryState, BatteryStatus


class Battery(widget.Battery):
    """
    Widget to display battery icon depending on battery state
    """

    FULL_BATTERY_ICON = ''
    EMPTY_BATTERY_ICON = ''

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
        Override parents method to display battery icon dynamically
        depending on battery state
        """
        state: BatteryState = status.state
        percentage = min(int(status.percent * 100), 100)
        icon = self._get_battery_icon(state, percentage)
        return f'{icon} {percentage}%'

    def _get_battery_icon(self, state: BatteryState, percentage: int) -> str:
        if state == BatteryState.FULL:
            return self.FULL_BATTERY_ICON
        if state == BatteryState.EMPTY:
            return self.EMPTY_BATTERY_ICON
        low_boundary = percentage // 10 * 10 if percentage >= 10 else 10
        if state == BatteryState.CHARGING:
            return self.CHARGING_ICONS[low_boundary]
        if state in [BatteryState.DISCHARGING, BatteryState.UNKNOWN]:
            return self.DISCHARGING_ICONS[low_boundary]
        assert False, 'unknown battery state'


class Volume(widget.base.InLoopPollText):
    """
    Widget to display volume level. Difference from standard Qtiles
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
        self.add_callbacks({
            "Button1": self.cmd_toggle_mute_volume,
            "Button4": self.cmd_raise_volume,
            "Button5": self.cmd_lower_volume,
        })

    class VolumeState(NamedTuple):
        """
        Representation of volume state independently from OS tools
        """
        percentage: int
        muted: bool

    def poll(self) -> str:
        """
        Called by Qtile periodically to get widgets display string
        """
        try:
            volume_state = self._get_volume_state()
        except Exception:
            logger.exception('Exception while getting volume state')
            # on Qtile startup audio might no be ready yet, so
            # don't throw an error here hoping that it will
            # succeed at next 'poll' call
            return ''
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


class NetworkManager(widget.base.InLoopPollText):
    """
    Widget which displays networking state according to 'nmcli' output
    """

    GET_ACTIVE_CONNECTION_SHELL_CMD = '''
        nmcli -g NAME,TYPE,DEVICE connection show --active | head -n 1
    '''
    GET_CONNECTIVITY_SHELL_CMD = 'nmcli networking connectivity'

    FIELD_INDICES = {
        'network_name': 0,
        'connection_type': 1,
        'interface_name': 2,
    }

    defaults = [
        (
            'icons',
            {},
            'Network icons. Dictionary where keys are values of '
            'connection.type NetworkManager property'
        ),
        (
            'format_string',
            '',
            'Format string which will be used when host is connected to a'
            'network an has full access to the Internet. Format options are'
            '"network_name", "connection_type", "interface_name", '
            '"connectivity"'
        ),
        (
            'no_connection_format_string',
            '',
            'Format string which will be used when host has no full '
            'Internet access, format options are the same as in '
            '"format_string" parameter'
        ),
    ]

    class NetworkState(NamedTuple):
        """
        Holder of connection state fields outputted from nmcli
        """
        network_name: str
        connection_type: str
        interface_name: str
        connectivity: str

    def __init__(self, **config):
        super().__init__(**config)
        self.add_defaults(self.defaults)

    def poll(self) -> str:
        """
        Called by Qtile periodically to get widgets display string
        """
        net_state = self._get_network_state()
        connection_type = net_state.connection_type
        icon = self.icons.get(connection_type, '')
        kwargs = dict(**net_state._asdict(), icon=icon)
        if net_state.connectivity != 'full':
            return self.no_connection_format_string.format(**kwargs)
        return self.format_string.format(**kwargs)

    def _get_network_state(self) -> 'NetworkManager.NetworkState':
        """
        Call nmcli and parse its output
        """
        output = self.call_process(self.GET_ACTIVE_CONNECTION_SHELL_CMD,
                                   shell=True, text=True)
        fields = output.split(':')
        connectivity = self.call_process(self.GET_CONNECTIVITY_SHELL_CMD,
                                         shell=True, text=True).strip()
        return self.NetworkState(
            network_name=fields[self.FIELD_INDICES['network_name']],
            connection_type=fields[self.FIELD_INDICES['connection_type']],
            interface_name=fields[self.FIELD_INDICES['interface_name']],
            connectivity=connectivity
        )


class Bluetooth(widget.Bluetooth):
    """
    Extension of widget.Bluetooth with custom widget
    string formatting
    """

    DISCONNECTED_ICON = ''
    CONNECTED_ICON = ''

    def update_text(self):
        text = ''
        if not self.powered:
            text = self.DISCONNECTED_ICON
        else:
            if not self.connected:
                text = self.DISCONNECTED_ICON
            else:
                text = self.CONNECTED_ICON
        self.update(text)
