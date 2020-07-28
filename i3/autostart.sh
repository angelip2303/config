#!/bin/sh

#     _     U _____ u
# U  /'\  u \| ___'|/
#  \/ _ \/   |  _|'
#  / ___ \   | |___
# /_/   \_\  |_____|
#  \\    >>  <<   >>
# (__)  (__)(__) (__)


#   ___        _            _             _   
#  / _ \      | |          | |           | |  
# / /_\ \_   _| |_ ___  ___| |_ __ _ _ __| |_ 
# |  _  | | | | __/ _ \/ __| __/ _` | '__| __|
# | | | | |_| | || (_) \__ \ || (_| | |  | |_ 
# \_| |_/\__,_|\__\___/|___/\__\__,_|_|   \__|                                     


##############################
#                            #
#     -*- WALLPAPERS -*-     #
#                            #
##############################

# feh --bg-scale ~/.config/qtile/wallpapers/wallpaper1.jpg &
feh --bg-scale ~/.config/qtile/wallpapers/wallpaper2.png &
# feh --bg-scale ~/.config/qtile/wallpapers/wallpaper3.png &
# feh --bg-scale ~/.config/qtile/wallpapers/wallpaper4.jpg &
# feh --bg-scale ~/.config/qtile/wallpapers/wallpaper5.jpg &
# feh --bg-scale ~/.config/qtile/wallpapers/wallpaper6.jpg &

###########################
#                         #
#     -*- STARTUP -*-     #
#                         #
###########################

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

    ###########
    # POLYBAR #
    ###########

    # Terminate already running bar instances
    killall -q polybar

    # Wait until the processes have been shut down
    while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

    # Launch bar1 and bar2
    polybar -c ~/.config/polybar/my-polybar/config.ini main