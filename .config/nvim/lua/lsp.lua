local M = {}
local lsp_servers = { 'pyright', 'lua_ls', 'gopls'}

function M.setup_mason_lsp_config()
    require('mason-lspconfig').setup({
        -- list of servers to automatically install
        ensure_installed = lsp_servers,
        -- automatically detect which servers to install (based on which servers are set up via lspconfig)
        automatic_installation = true,
    })
end

function M.setup_cmp()
    local cmp = require('cmp')
    cmp.setup({
        snippet = {
            expand = function(args)
                require('luasnip').lsp_expand(args.body)
            end,
        },
        mapping = cmp.mapping.preset.insert({
            ['<C-b>'] = cmp.mapping.scroll_docs(-4),
            ['<C-f>'] = cmp.mapping.scroll_docs(4),
            ['<C-Space>'] = cmp.mapping.complete(),
            ['<C-e>'] = cmp.mapping.abort(),
            ['<CR>'] = cmp.mapping.confirm({ select = false }),
        }),
        sources = cmp.config.sources({
          { name = 'nvim_lsp' },
          { name = 'luasnip' },
        }, {
          { name = 'buffer' },
        })
    })
end

function M.setup_lsp_config()
    local lspconfig = require('lspconfig')
    local capabilities = require('cmp_nvim_lsp').default_capabilities()
    for _, lsp in ipairs(lsp_servers) do
        lspconfig[lsp].setup {
            on_attach = function(_, bufnr)
                require('keys').setup_lsp_keys(bufnr)
            end,
            capabilities = capabilities
        }
    end
end

M.setup_cmp()
M.setup_lsp_config()

return M
