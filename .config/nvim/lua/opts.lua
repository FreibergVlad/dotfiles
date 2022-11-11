local opt = vim.opt
local cmd = vim.cmd

-- [[ Context ]]
-- show line numbers
opt.number = true
-- show relative line numbers
opt.relativenumber = true
-- min num lines of context
opt.scrolloff = 4
-- show the sign column
opt.signcolumn = 'yes'
-- don't create .swp files
opt.swapfile = false
-- use system clipboard
opt.clipboard = 'unnamed,unnamedplus'

-- [[ File types ]]
-- string encoding to use
opt.encoding = 'utf8'
-- file encoding to use
opt.fileencoding = 'utf8'
-- line ending format
opt.fileformat = 'unix'

-- [[ Theme ]]
-- allow syntax higlightning
opt.syntax = 'ON'
-- enable 24-bit RGB color in the TUI
opt.termguicolors = true
-- hide current mode since it's already shown by  Lualine
opt.showmode = false
-- don't show last executed command
opt.showcmd = false
-- set colorscheme
cmd('colorscheme gruvbox')

-- [[ Search ]]
-- ignore case in search patters
opt.ignorecase = true
-- override ignrecase if search contains capitals
opt.smartcase = true
-- use incremental search
opt.incsearch = true
-- highlight search matches
opt.hlsearch = true

-- [[ Whitespace ]]
-- use spaces instead of tabs
opt.expandtab = true
-- size of indent
opt.shiftwidth = 4
-- number of spaces tabs count for in insert mode
opt.softtabstop = 4
-- number of spaces tabs count for
opt.tabstop = 4
-- copy indent from current line when starting a new line
opt.autoindent = true

-- [[ Splits ]]
-- place new window to the right of current one in case of vertical split
opt.splitright = true
-- place new window below the current one in case of horizontal split
opt.splitbelow = true
