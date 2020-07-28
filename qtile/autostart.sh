#!/bin/sh

# -*- WALLPAPERS -*-

# feh --bg-scale ~/.config/qtile/wallpapers/wallpaper1.jpg &
# feh --bg-scale ~/.config/qtile/wallpapers/wallpaper2.png &
# feh --bg-scale ~/.config/qtile/wallpapers/wallpaper3.png &
# feh --bg-scale ~/.config/qtile/wallpapers/wallpaper4.jpg &
# feh --bg-scale ~/.config/qtile/wallpapers/wallpaper5.jpg &
feh --bg-scale ~/.config/qtile/wallpapers/wallpaper6.jpg &

# -*- STARTUP -*-

    #########
    # PICOM #
    #########

    # If picom is running, kill it to prevent multiple instances.
    if ps -A | grep picom; then
        killall -q picom
    fi

    # Load picom
    exec picom --experimental-backends --config ~/.config/picom/picom.conf &
    
    #########
    # DUNST #
    #########

    # If dunst is running, kill it to prevent multiple instances.
    if ps -A | grep dunst; then
        killall -q dunst
    fi
    
    dunst -config ~/.config/dunst/dunstrc/dunstrc &

    #############
    # NM-APPLET #
    #############

    exec --no-startup-id nm-applet
