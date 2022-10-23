"""
All key bindings and mouse configuration live here
"""
from libqtile.config import Key, Click, Drag
from libqtile.lazy import lazy
from libqtile.widget.backlight import ChangeDirection

from groups import groups
from utils import (
    TERMINAL,
    MOD_KEY,
    RUN_APP_LAUNCHER_SHELL_CMD,
    TAKE_SCREENSHOT_SHELL_CMD,
    LOCK_X_SESSION_SHELL_CMD
)

keys = [
    Key([MOD_KEY], 'h', lazy.layout.left(), desc='Move focus to left'),
    Key([MOD_KEY], 'l', lazy.layout.right(), desc='Move focus to right'),
    Key([MOD_KEY], 'j', lazy.layout.down(), desc='Move focus down'),
    Key([MOD_KEY], 'k', lazy.layout.up(), desc='Move focus up'),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [MOD_KEY, 'shift'], 'h',
        lazy.layout.shuffle_left(),
        desc='Move window to the left'
    ),
    Key(
        [MOD_KEY, 'shift'], 'l',
        lazy.layout.shuffle_right(),
        desc='Move window to the right'
    ),
    Key(
        [MOD_KEY, 'shift'], 'j',
        lazy.layout.shuffle_down(),
        desc='Move window down'
    ),
    Key(
        [MOD_KEY, 'shift'], 'k',
        lazy.layout.shuffle_up(),
        desc='Move window up'
    ),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [MOD_KEY, 'control'], 'h',
        lazy.layout.grow_left(),
        desc='Grow window to the left'
    ),
    Key(
        [MOD_KEY, 'control'], 'l',
        lazy.layout.grow_right(),
        desc='Grow window to the right'
    ),
    Key(
        [MOD_KEY, 'control'], 'j',
        lazy.layout.grow_down(),
        desc='Grow window down'
    ),
    Key(
        [MOD_KEY, 'control'], 'k',
        lazy.layout.grow_up(),
        desc='Grow window up'
    ),
    Key(
        [MOD_KEY], 'n',
        lazy.layout.normalize(),
        desc='Reset all window sizes'
    ),
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
    Key([MOD_KEY], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),
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
    Key(
        [MOD_KEY], 'r',
        lazy.spawn(RUN_APP_LAUNCHER_SHELL_CMD),
        desc='Run application launcher'
    ),
    Key(
        [MOD_KEY], 'Print',
        lazy.spawn(TAKE_SCREENSHOT_SHELL_CMD, shell=True),
        desc='Take a screenshot'
    ),
    Key(
        [MOD_KEY], 'l',
        lazy.spawn(LOCK_X_SESSION_SHELL_CMD),
        desc='Lock X session'
    ),
    Key(
        [], 'XF86AudioRaiseVolume',
        lazy.widget['speakers_volume'].raise_volume(),
        desc='Increase speakers volume'
    ),
    Key(
        [], 'XF86AudioLowerVolume',
        lazy.widget['speakers_volume'].lower_volume(),
        desc='Decrease speakers volume'
    ),
    Key(
        [], 'XF86AudioMute',
        lazy.widget['speakers_volume'].toggle_mute_volume(),
        desc='Toggle mute speakers volume'
    ),
    Key(
        [], 'XF86AudioMicMute',
        lazy.widget['microphone_volume'].toggle_mute_volume(),
        desc='Toggle mute microphone volume'
    ),
    Key(
        [], 'XF86MonBrightnessUp',
        lazy.widget['backlight'].change_backlight(ChangeDirection.UP),
        desc='Increase screen brightness'
    ),
    Key(
        [], 'XF86MonBrightnessDown',
        lazy.widget['backlight'].change_backlight(ChangeDirection.DOWN),
        desc='Decrease screen brightness'
    )
]

# Key bindings to switch between groups
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

# Drag floating layouts.
mouse = [
    Drag(
        [MOD_KEY], 'Button1',
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [MOD_KEY], 'Button3',
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([MOD_KEY], 'Button2', lazy.window.bring_to_front()),
]
