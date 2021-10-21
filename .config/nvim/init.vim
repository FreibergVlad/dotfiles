" install vim-plug if isn't installed already
let autoload_plug_path = stdpath('data') . '/site/autoload/plug.vim'
if !filereadable(autoload_plug_path)
  silent execute '!curl -fLo ' . autoload_plug_path . ' --create-dirs 
      \ "https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif
unlet autoload_plug_path

" ======== PLUGINS BEGIN =========
call plug#begin(stdpath('data') . '/plugged')
" file browser (https://github.com/preservim/nerdtree)
Plug 'scrooloose/nerdtree'
" asynchronous linter (uses linting tools under the hood,
" e.g. 'pylint', 'flake8') (https://github.com/dense-analysis/ale)
Plug 'dense-analysis/ale'
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
Plug 'deoplete-plugins/deoplete-jedi'
Plug 'davidhalter/jedi-vim'
" Git plugin (https://github.com/tpope/vim-fugitive)
Plug 'tpope/vim-fugitive'
" Indicates modified lines in sign column
Plug 'mhinz/vim-signify'
" CLI fuzzy finder
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
" vim/neovim integration for 'fzf' (to search across
" file contents, Silver Searcher should be installed)
Plug 'junegunn/fzf.vim'
" gruvbox theme
Plug 'morhetz/gruvbox'
call plug#end()
" ======== PLUGINS END ===========

" ====== ACTIVATE GRUVBOX DARK THEME ========  
colorscheme gruvbox
set background=dark 
" ===========================================

set relativenumber " relative line numbers
set clipboard+=unnamedplus " use system clipboard for 'yank'/'paste'
set updatetime=100 " async update interval for 'vim-signify'
" line width marker for Python files
autocmd FileType python setlocal colorcolumn=79

" enable deoplete autocompletion
let g:deoplete#enable_at_startup = 1
" disable autocompletion, because we use deoplete for completion
let g:jedi#completions_enabled = 0

" run search across file names with Ctrl+P
nnoremap <silent> <C-p> :Files<CR>
" run search across file contents with Ctrl+F
nnoremap <silent> <C-f> :Ag<CR>

" ignore *.pyc, *.swp, __pycache__ files and '.git' folder
let NERDTreeIgnore=['\.pyc$', '^__pycache__$', '\.swp$', '\.git$']
" show hidden files
let NERDTreeShowHidden=1
" open NERDTree with 'Ctrl+n'
map <C-n> :NERDTreeToggle<CR>
" show currently opened file in NERDTree
" with 'Ctrl+m'
map <C-m> :NERDTreeFind<CR>
