local M = {}
local map = vim.keymap.set
local lsp_buf = vim.lsp.buf

-- toggle nvim-tree
map('n', '<leader>n', ':NvimTreeToggle<CR>', {silent = true})
-- move the cursor in the tree for the current buffer
map('n', '<leader>m', ':NvimTreeFindFile<CR>', {silent = true})

-- key bindings to toggle Telescope functions
local telescope = require('telescope.builtin')
map('n', '<leader>ff', telescope.find_files, {})
map('n', '<leader>fg', telescope.live_grep, {})
map('n', '<leader>fb', telescope.buffers, {})

-- exit from 'insert' mode with 'jk' or 'kj'
map('i', 'jk', '<Esc>')
map('i', 'kj', '<Esc>')

-- better tabbing, don't lose selection
-- after manual indentation
map('v', '<', '<gv')
map('v', '>', '>gv')

local telescope_actions = require('telescope.actions')
M.telescope_mappings = {
    i = {
        ['<C-j>'] = telescope_actions.move_selection_next,
        ['<C-k>'] = telescope_actions.move_selection_previous,
    }
}

function M.setup_lsp_keys(bufnr)
    local opts = { buffer = bufnr }
    map('n', 'gD', lsp_buf.declaration, opts)
    map('n', 'gd', lsp_buf.definition, opts)
    map('n', 'K', lsp_buf.hover, opts)
    map('n', 'gi', lsp_buf.implementation, opts)
    map('n', '<leader>sh', lsp_buf.signature_help, opts)
    map('n', '<leader>D', lsp_buf.type_definition, opts)
    map('n', '<leader>rn', lsp_buf.rename, opts)
    map('n', 'gr', lsp_buf.references, opts)
    map('n', '<leader>ca', lsp_buf.code_action, opts)
    map('n', '<leader>so', require('telescope.builtin').lsp_document_symbols, opts)
end

return M
