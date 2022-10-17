"""
Core Qtile config
"""
import hooks

from groups import groups
from keys import keys, mouse
from layouts import layouts, floating_layout
from screens import screens, widget_defaults

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True
wmname = "Qtile"
