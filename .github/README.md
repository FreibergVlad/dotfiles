## Dependencies

Here is a list of tools and libraries which dotfiles depend on. I aim to keep it up-to-date,
but I can not guarantee that I haven't missed anything:
- [qtile](https://github.com/qtile/qtile) - obviously. Window manager which all my desktop is build around
- [alacritty](https://github.com/alacritty/alacritty) - terminal emulator
- [Hack Nerd Font](https://github.com/ryanoasis/nerd-fonts) - font which is used across the whole repository
- [rofi](https://github.com/davatorium/rofi) - application launcher
- [picom](https://github.com/yshui/picom) - X window compositor
- [dunst](https://github.com/dunst-project/dunst) - notification daemon
- [maim](https://github.com/naelstrof/maim) - tool to take desktop screenshots
- [xclip](https://github.com/astrand/xclip) - CLI to the X11 clipboard
- pactl - volume control tool, required by `Volume` Qtile widget
- xss-lock - use external locker as X screen saver
- [betterlockscreen](https://github.com/betterlockscreen/betterlockscreen) - lock screen, `i3lock` wrapper
- [nmcli](https://networkmanager.dev/) - required by `NetworkManager` Qtile widget
- [brightnessctl](https://github.com/Hummer12007/brightnessctl) - required by `Backlight` Qtile widget, used to set screen brightness
- [ripgrep](https://github.com/BurntSushi/ripgrep) - required by Telescope Neovim plugin
- [fd](https://github.com/sharkdp/fd) - required by Telescope Neovim plugin
- [dbus-next](https://pypi.org/project/dbus-next/) - DBus library, required by some of Qtile widgets
- [blueman](https://github.com/blueman-project/blueman) - Bluetooth manager
- [udiskie](https://github.com/coldfix/udiskie) - USB disks manager

## Installation

I prefer manage dotfiles using a bare Git repositories. It's simple and requires no extra tools and symlinks.
You can read more about this approach [here](https://www.atlassian.com/git/tutorials/dotfiles). First, make sure
you have this alias defined. Put it in your `.bashrc` (or `.zshrc`, whatever shell you're using) to make it persistent:
```sh
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
```
Usually using this approach we need to add source repo to `.gitignore` so that we don't create weird recursion problems.
This repo has `.gitignore` already so we don't have to do it.
Next, clone dotfiles into a bare repository in a "dot" folder of your $HOME:
```sh
git clone --bare https://github.com/FreibergVlad/dotfiles.git $HOME/.dotfiles
```
Don't show untracked files by default:
```sh
dotfiles config --local status.showUntrackedFiles no
```
Checkout the actual content from the bare repository to your $HOME. This step may fail, if your $HOME already has some
configuration files which would be overwritten by `git`. In this case just backup problematic files and run
command again.
```sh
dotfiles checkout
```

## Configuration

Most of the Qtile environment specific stuff lives in [utils.py](/.config/qtile/utils.py). I try to keep all shell commands
and references to system files there so it will be easy to change something.

## Screenshots

![Qtile screenshot](/.github/qtile_screenshot.jpg?raw=true)
