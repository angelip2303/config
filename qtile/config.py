# My qtile config.

#     _     U _____ u
# U  /'\  u \| ___'|/
#  \/ _ \/   |  _|'
#  / ___ \   | |___
# /_/   \_\  |_____|
#  \\    >>  <<   >>
# (__)  (__)(__) (__)

# -*- IMPORTS -*-

import os, socket, subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
from typing import List

# -*- VARIABLES -*-

mod = 'mod4'
prompt = '{0}@{1}: '.format(os.environ['USER'], socket.gethostname())

wmname = 'LG3D' # Assignment made for the DE to work with some java IDEs.

# -*- FONTS -*-

fonts = {
    'mono-font':    'JetBrainsMono NF',
    'bar-font':     'JetBrainsMonoMedium NF',
}

# -*- COLORS -*-

#Dracula color scheme.
colors = {
    # Background and Foreground.
    'background':       '#282a36',   #  0. grey     -->     bar(bar-background)
    'foreground-hc':    '#f8f8f2',   #  1. white    -->     prompt(foreground-hc)
    'foreground-lc':    '#000000',   #  2. black    -->     bar(foreground-lc)
    # Borders.
    'border-non-focus': '#6272a4',   #  3. dk-grey  -->     border(non-focus)
    'border-focus':     '#e1acff',   #  4. lt-pink  -->     border(focus)
    # Widgets.
    'yellow':           '#f1fa8c',   #  5. yellow   -->     bar(hardware-background)
    'aqua':             '#8be9fd',   #  6. aqua     -->     bar(battery-background)
    'green':            '#50fa7b',   #  7. green    -->     bar(volume-background)
    'red':              '#ff5555',   #  8. red      -->     bar(net-background)
    'orange':           '#ffb86c',   #  9. orange   -->     bar(updates-background)
    'pink':             '#ff79c6',   # 10. pink     -->     bar(systray-background)
}

# -*- APPS -*-

term = 'termite'
browser = 'firefox'
vim = 'neovim'
file_manager = 'thunar'

# -*- STARTUP -*-

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

# -*- KEYBINDINGS -*-

keys = [
    # Switch between windows in current stack pane.
    Key([mod], 'k', lazy.layout.down()),
    Key([mod], 'j', lazy.layout.up()),
   
    # Move windows up or down in current stack.
    Key([mod, 'control'], 'k', lazy.layout.shuffle_down()),
    Key([mod, 'control'], 'j', lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack.
    Key([mod], 'space', lazy.layout.next()),

    # Swap panes of split stack.
    Key([mod, 'shift'], 'space', lazy.layout.rotate()),

    # Open the terminal.
    Key([mod], 'Return', lazy.spawn(term)),

    # Toggle between different layouts as defined below.
    Key([mod], 'Tab', lazy.next_layout()),
    Key([mod], 'w', lazy.window.kill()),

    # Manage the DE.
    Key([mod, 'control'], 'r', lazy.restart()), # --> refresh.
    Key([mod, 'control'], 'q', lazy.shutdown()), # --> shutdown.
    Key([mod], 'r', lazy.spawncmd()), # --> spawn.

    # Spawn rofi d-run.
    Key([mod], 'd', lazy.spawn('rofi -show drun')),

    # Media keys.
    Key([], 'XF86AudioMute', os.system('$~/.config/dunst/dunstrc/volume.sh up')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer -c 1 -q set Master 5%+')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer -c 1 -q set Master 5-')),
    Key([], 'XF86AudioNext', lazy.spawn('mpc next')),
    Key([], 'XF86AudioPrev', lazy.spawn('mpc prev')),
    Key([], 'XF86AudioPlay', lazy.spawn('mpc toggle')),
    Key([], 'XF86AudioStop', lazy.spawn('mpc stop')),

    # Brightness.
    Key([], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl set +2%')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl set 2%-')),

    # Print-screen.
    Key([], 'Print', lazy.spawn('xfce4-screenshooter')),

    # App keys.
    Key([mod], 'b', lazy.spawn(browser)),
    Key([mod], 't', lazy.spawn('task')),
    Key([mod], 'f', lazy.spawn(file_manager)),
]

mouse = [
    Drag([mod], 'Button1', lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], 'Button2', lazy.window.bring_to_front())
]

# -*- GROUPS -*-

dev = 'DEV'
web = 'WEB'
term = 'TERM'

def init_group_names():
    return [
        (dev, {'layout': 'monadtall'}),
        (web, {'layout': 'monadtall'}),
        (term, {'layout': 'monadtall'}),
    ]

def init_groups():
    return [Group(name, **kwargs) for (name, kwargs) in group_names]

if (__name__ in ['config', '__main__']):
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Change to another group.
    keys.append(Key([mod, 'shift'], str(i), lazy.window.togroup(name))) # Send window to group.

# -*- LAYOUTS -*-

layout_theme = {
    'border_width': 2,
    'margin': 6,
    'border_focus':  colors['border-focus'],
    'border_normal': colors['border-non-focus']
}

layouts = [
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# -*- DEFAULT SETTINGS FOR THE WIDGETS -*-

widget_defaults = dict(
    font = fonts['bar-font'],
    fontsize = 12,
    padding = 3,
    background = colors['background']
)

extension_defaults = widget_defaults.copy()

# -*- WIDGETS -*-

def init_widgets_list():
    return [

        # List of groups.
        widget.GroupBox(

            # -*- FONT Config -*-
            font = fonts['mono-font'],
            fontsize = 12,

            # -*- MARGINS and BORDERS -*-
            margin_x = 0,
            margin_y = 3.5,
            padding_x = 5, # Gap between the frame and the letters: x-axis.
            padding_y = 5, # Gap between the frame and the letters: y-axis.
            borderwidth = 3,
            rounded = False, # Rounded frame or not.

            # -*- HIGHLIGHTING -*-
            highlight_method = 'block',
            urgent_alert_method = 'block',

            # -*- COLORS -*-
            active = colors['foreground-hc'],
            inactive = colors['foreground-hc'],
            
            this_current_screen_border = colors['pink'], # Color of the selected workspace.
            # this_screen_border = colors['background'],
            # other_current_screen_border = colors['background'],
            # other_screen_border = colors['background'],

            background = colors['background']
        ),

        # Systray.
        # widget.TextBox(text = '|'),
        widget.Systray(),
        # widget.TextBox(text = ' |'),

        # Prompt.
        widget.Prompt(
            prompt = prompt,
            font = fonts['mono-font'],
            padding = 10,
            foreground = colors['foreground-hc'],
            background = colors['background']
        ),

        # Separator.
        widget.Sep(
            linewidth = 0,  #To make it invisible.
            padding = 6     #Length with respect to the left most border.
        ),

        # Window name.
        widget.WindowName(),

        ######################
        # RIGHT-MOST WIDGETS #
        ######################

        # Hardware USAGE.
            # Memory.
            widget.TextBox(
                text = '  ',
                fontsize = 15,
                foreground = colors['foreground-lc'],
                background = colors['yellow']
            ),
            widget.Memory(
                foreground = colors['foreground-lc'],
                background = colors['yellow']
            ),

            # CPU.
            widget.TextBox(
                text = '  ',
                fontsize = 15,
                foreground = colors['foreground-lc'],
                background = colors['yellow']
            ),
            widget.CPU(
                format = '{freq_current}GHz {load_percent}%',
                foreground = colors['foreground-lc'],
                background = colors['yellow'],
                padding = 5
            ),

        #Separation between widgets.
        widget.Sep(linewidth = 0, padding = 4),

        # Battery.
        widget.TextBox(
            text = '  ',
            foreground = colors['foreground-lc'],
            background = colors['aqua']
        ),
        widget.Battery(
            format = '{percent:2.0%}',
            foreground = colors['foreground-lc'],
            background = colors['aqua'],
            update_delay = 5,
            padding = 5
        ),

        #Separation between widgets.
        widget.Sep(linewidth = 0, padding = 4),

        # Volume.
        widget.TextBox(
            text = str('  '),
            fontsize = 15, 
            foreground = colors['foreground-lc'],
            background = colors['green']
        ),
        widget.Volume(
            foreground = colors['foreground-lc'],
            background = colors['green'],
            padding = 5
        ),

        #Separation between widgets.
        widget.Sep(linewidth = 0, padding = 4),

        # Net.

        # widget.TextBox(
        #     text = '  ',
        #     foreground = colors['foreground-lc'],
        #     background = colors['red']
        # ),
        # widget.Net(
        #     foreground = colors['foreground-lc'],
        #     background = colors['red'],
        #     format = '{down} ↓↑ {up}',
        #     padding = 5
        # ),
        #
        # Separation between widgets.
        # widget.Sep(linewidth = 0, padding = 6),

        # Packages to update.
        widget.TextBox(
            text = '  ',
            fontsize = 18, 
            foreground = colors['foreground-lc'],
            background = colors['orange']
        ),
        widget.Pacman(
            execute = 'alacritty',
            update_interval = 1800,
            foreground = colors['foreground-lc'],
            background = colors['orange'],
            padding = 5
        ),

        #Separation between widgets.
        widget.Sep(linewidth = 0, padding = 4),

        # Clock.
        widget.TextBox(
            text = '  ',
            foreground = colors['foreground-lc'],
            background = colors['pink']
        ),
        widget.Clock(
            format='%A, %B %d [ %H:%M ]',
            foreground = colors['foreground-lc'],
            background = colors['pink'],
            padding = 5
        ),
    ]

# -*- SCREENS -*-

    # --> Im loading the setup for a dual monitor.

def init_widgets_screen1():
    return init_widgets_list()

def init_widgets_screen2():
    return init_widgets_list()

def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0.95, size=20)),
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=0.95, size=20))
    ]

if __name__ in ['config', '__main__']:
    screens = init_screens()

# -*- FLOATING WINDOWS -*-

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = 'smart'
