local ensure_packer = function()
    local fn = vim.fn
    local install_path = fn.stdpath('data') .. '/site/pack/packer/start/packer.nvim'
    if fn.empty(fn.glob(install_path)) > 0 then
        fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
        vim.cmd [[packadd packer.nvim]] return true end
    return false
end

local packer_bootstrap = ensure_packer()

return require('packer').startup(function(use)
    -- let Packer manage itself
    use 'wbthomason/packer.nvim'
    -- color schema
    use 'ellisonleao/gruvbox.nvim'
    -- status line
    use {
        'nvim-lualine/lualine.nvim',
        requires = 'kyazdani42/nvim-web-devicons',
        config = function()
            require('lualine').setup {
                options = {
                    globalstatus = true,
                }
            }
        end
    }
    -- filesystem navigation
    use {
        'kyazdani42/nvim-tree.lua',
        requires = 'kyazdani42/nvim-web-devicons',
        config = function()
            require('nvim-tree.view').View.winopts.cursorline = true
            require('nvim-tree').setup {
                sort_by = 'case_sensitive',
                hijack_cursor = true,
                renderer = {
                    group_empty = true,
                },
            }
        end

    }
    -- comments toggling
    use {
        'terrortylor/nvim-comment',
        config = function() require('nvim_comment').setup {} end
    }
    -- fuzzy finder
    use {
        'nvim-telescope/telescope.nvim', branch = '0.1.x',
        requires = 'nvim-lua/plenary.nvim',
        config = function()
            local telescope_mappings = require('keys').telescope_mappings
            require('telescope').setup {
                defaults = {
                mappings = telescope_mappings
              },
            }
        end
    }
    -- git integration
    use {
        'lewis6991/gitsigns.nvim',
        config = function() require('gitsigns').setup {} end
    }
    -- better syntax highlightning
    use {
        'nvim-treesitter/nvim-treesitter',
        run = function()
            local ts_update = require('nvim-treesitter.install').update({ with_sync = true })
            ts_update()
        end,
        config = function()
            require('nvim-treesitter.configs').setup {
                ensure_installed = { 'lua', 'python', 'go' },
                sync_install = false,
                highlight = {
                    enable = true,
                    additional_vim_regex_highlighting = false,
                },
            }
        end
    }
    use {
        'jose-elias-alvarez/null-ls.nvim',
        config = function()
            local null_ls = require('null-ls')
            null_ls.setup({
                sources = {
                    null_ls.builtins.diagnostics.flake8,
                    null_ls.builtins.diagnostics.golangci_lint
                },
            })
        end
    }
    -- automatically install LSPs
    use {
        'williamboman/mason.nvim',
        config = function() require('mason').setup {} end
    }
    -- mason integration with LSP
    use 'williamboman/mason-lspconfig.nvim'
    -- LSP configuration
    use 'neovim/nvim-lspconfig'
    -- autocompletion plugins
    use 'hrsh7th/cmp-nvim-lsp'
    use 'hrsh7th/cmp-buffer'
    use 'hrsh7th/cmp-path'
    use 'hrsh7th/cmp-cmdline'
    use 'hrsh7th/nvim-cmp'
    use 'L3MON4D3/LuaSnip'
    use 'saadparwaiz1/cmp_luasnip'
    -- copy using OSC52
    use {
        'ojroques/nvim-osc52',
        config = function()
            local function copy()
              if vim.v.event.operator == 'y' and vim.v.event.regname == '' then
                require('osc52').copy_register('"')
              end
            end
            vim.api.nvim_create_autocmd('TextYankPost', {callback = copy})
        end
    }
    -- install packages if it's first start ever
    if packer_bootstrap then
        require('packer').sync()
    end
end)
