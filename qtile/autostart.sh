#!/bin/sh

# -*- WALLPAPERS -*-

# feh --bg-scale ~/.config/qtile/wallpapers/wallpaper1.jpg &
feh --bg-scale ~/.config/qtile/wallpapers/wallpaper2.png &

# -*- STARTUP -*-

exec picom --config ~/.config/picom/picom.conf &
exec nm-applet &
insync
