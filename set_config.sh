#!/usr/bin/env bash

for file_name in '.tmux.conf' '.Xresources' '.config/nvim/init.vim' ;
    do
        src_path="$(pwd)/${file_name}"
        target_path="${HOME}/${file_name}"
        echo "Creating symlink to ${src_path} at ${target_path}..."
        ln -sf $src_path $target_path
    done

echo 'Reloading .Xresources file...'
xrdb ${HOME}/.Xresources
echo 'Done!'
