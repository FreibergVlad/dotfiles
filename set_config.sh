#!/usr/bin/env bash

configs=(
    ".tmux.conf"
    ".alacritty.yml"
    ".config/nvim/init.vim"
)

mkdir -p ${HOME}/.config/nvim

for config in "${configs[@]}";
    do
        src_path="$(pwd)/${config}"
        target_path="${HOME}/${config}"
        echo "Creating symlink to ${src_path} at ${target_path}"
        ln -sf $src_path $target_path
    done
