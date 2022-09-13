from libqtile.config import Key
from libqtile.lazy import lazy

from groups import groups
from utils import TERMINAL, MOD_KEY

keys = [
    Key([MOD_KEY], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD_KEY], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD_KEY], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD_KEY], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([MOD_KEY, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([MOD_KEY, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([MOD_KEY, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD_KEY, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([MOD_KEY, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([MOD_KEY, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([MOD_KEY, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([MOD_KEY, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([MOD_KEY], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [MOD_KEY, 'shift'],
        'Return',
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack',
    ),
    Key([MOD_KEY], 'Return', lazy.spawn(TERMINAL), desc='Launch terminal'),
    # Toggle between different layouts as defined below
    Key([MOD_KEY], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([MOD_KEY], 'w', lazy.window.kill(), desc='Kill focused window'),
    Key(
        [MOD_KEY, 'control'], 'r',
        lazy.reload_config(),
        desc='Reload the config'
    ),
    Key([MOD_KEY, 'control'], 'q', lazy.shutdown(), desc='Shutdown Qtile'),
    Key(
        [MOD_KEY], 'space',
        lazy.widget['keyboardlayout'].next_keyboard(),
        desc='Change keyboard layout'
    ),
    Key([MOD_KEY], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Manage the volume using special keys
    Key(
        [], 'XF86AudioRaiseVolume',
        lazy.widget['volume'].raise_volume(),
        desc='Increase volume'
    ),
    Key(
        [], 'XF86AudioLowerVolume',
        lazy.widget['volume'].lower_volume(),
        desc='Decrease volume'
    ),
    Key(
        [], 'XF86AudioMute',
        lazy.widget['volume'].toggle_mute_volume(),
        desc='Toggle mute volume'
    ),
]

for index, group in enumerate(groups, 1):
    keys.extend(
        [
            Key(
                [MOD_KEY],
                str(index),
                lazy.group[group.name].toscreen(),
                desc=f'Switch to group {group.name}',
            ),
            Key(
                [MOD_KEY, 'shift'],
                str(index),
                lazy.window.togroup(group.name, switch_group=True),
                desc=f'Switch to & move focused window to group {group.name}'
            ),
        ]
    )
