#!/usr/bin/env bash

# trigger session lock after 5 minutes of inactivity
xset s 300
# subscribe to systemd events, lock session on them
xss-lock -- betterlockscreen -l &

# set wallpaper
feh --bg-scale ~/.config/wallpapers/firewatch_1920_1080.png

# run window compositor (restart if running already)
killall -qw picom
picom -b --no-vsync
