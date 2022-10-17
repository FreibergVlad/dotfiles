#!/usr/bin/env bash

# set wallpaper
feh --bg-scale ~/.wallpapers/firewatch_1920_1080.png

# run window compositor (restart if running already)
killall -qw picom
picom -b --no-vsync
