set nocompatible              " required
filetype off                  " required
set encoding=utf-8

let python_highlight_all=1
syntax on
set nu
set relativenumber
set mouse=a
set backspace=indent,eol,start

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" PLUGINS BEGIN
Plugin 'sheerun/vim-polyglot' " syntax highlightning
Plugin 'scrooloose/nerdtree' " files browser
Plugin 'Xuyuanp/nerdtree-git-plugin' " Git plugin for NERDTree
Plugin 'junegunn/fzf', { 'do': { -> fzf#install() } } " fuzz search
Plugin 'junegunn/fzf.vim'
Plugin 'tpope/vim-commentary' " allows to comment stuff out
Plugin 'Vimjas/vim-python-pep8-indent' " PEP8 indentation
Plugin 'dense-analysis/ale' " python linter
Plugin 'morhetz/gruvbox' " gruvbox color scheme
Plugin 'https://github.com/tpope/vim-fugitive' " Git plugin
Plugin 'mhinz/vim-signify' " Git signs
Plugin 'davidhalter/jedi-vim' " autocomplete
Plugin 'vim-airline/vim-airline' " vim status line
Plugin 'vim-airline/vim-airline-themes' " themes for the status line
Plugin 'townk/vim-autoclose'
" PLUGINS END

call vundle#end()            " required
filetype plugin indent on    " required

" enable gruvbox dark color scheme
autocmd vimenter * colorscheme gruvbox
set background=dark

" start NERDTree automatically if no files specified
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

" close vim if the only window left open is a NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" open NERDTree with 'Ctrl+n'
map <C-n> :NERDTreeToggle<CR>
" show currently opened file in NERDTree
" with 'Ctrl+m'
map <C-m> :NERDTreeFind<CR>

" line width marker for Python files
autocmd FileType python setlocal colorcolumn=79

" async update time for vim-signify
set updatetime=100

" ignore *.pyc and __pycache__ files
let NERDTreeIgnore = ['\.pyc$', '^__pycache__$']
" show hidden files
let NERDTreeShowHidden=1
