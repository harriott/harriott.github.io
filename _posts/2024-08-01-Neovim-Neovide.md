---
# vim: set fdl=1:
# $JHm/_posts/2024-08-01-Neovim-Neovide.md
description: "the advantages of switching to Neovim, and the pleasure of Neovide"
tags: BgInfo eza FD GnuPG less LF LSD Windows winget
title: "switching to Neovim and Neovide"
---

```powershell
winget add Neovim.Neovim
```

Having discovered, over a decade ago, the power of [Vim (text editor)](http://en.wikipedia.org/wiki/Vim_%28text_editor%29) ([ vim and related tools ]({% post_url 2023-01-25-vim_and_related_tools %})), and gotten good at [vim configuration](% post_url 2023-02-05-vim_configurations %), I had some time when I couldn't be at work, and so put several days into updgrading my [vimfiles](https://github.com/harriott/vimfiles) to accomodate the burgeoning power of `Neovim`, and it was tough, like a very long game of chess, but I got there: my [vimfiles](https://github.com/harriott/vimfiles) now work for all flavours of `Vim`, and I've access to the new and improved worls of `Lua` plugins. Here I won't attempt to explain my configurations - go look for yourself if you're looking for yet more radical improvement in how you use your [Von Neumann architecture](http://en.wikipedia.org/wiki/Von_Neumann_architecture) machine. Instead, I just mention a few useful improvements over `gVim`.

## lovely Neovim plugins
- For coding:
    - I'm ambivalent about `nvim-treesitter` ([Code](https://github.com/nvim-treesitter/nvim-treesitter)), perhaps because I'm not enough of a coder, but I managed to curb its enthusiasm ([$vimfiles/nvim/lua/lazy/treesitter.lua](https://github.com/harriott/vimfiles/blob/master/nvim/lua/lazy/treesitter.lua))
    - `Comment.nvim` ([Code](https://github.com/numToStr/Comment.nvim)) just works, and nicely replaces `The NERD Commenter`, which is indispensable in classic `Vim`
    - LSP:
        - `nvim-lspconfig` ([Code](https://github.com/neovim/nvim-lspconfig)) took some figuring out ([$vimfiles/nvim/lua/lazy/nvim-lspconfig.lua](https://github.com/harriott/vimfiles/blob/master/nvim/lua/lazy/nvim-lspconfig.lua)) because it can leverage a huge number of language servers, each with its own quirks
            - I found `Lspsaga` ([Code](https://github.com/nvimdev/lspsaga.nvim)) equally tricky to configure, and now it provides me handy [Breadcrumbs](https://nvimdev.github.io/lspsaga/breadcrumbs/) for a project, and an occasionally useful [Outline](https://nvimdev.github.io/lspsaga/outline/)
            - `mason.nvim` ([Code](https://github.com/williamboman/mason.nvim)) is indispensable for installing and updating language servers on any machine for `Neovim`
                - `mason-lspconfig.nvim` ([Code](https://github.com/williamboman/mason-lspconfig.nvim)) is advised
    - `neogit` ([Code](https://github.com/NeogitOrg/neogit)) is one heck of a machine, but I still rely on `fugitive` ([Code](https://github.com/tpope/vim-fugitive))
    - `nvim-neoclip.lua` ([Code](https://github.com/AckslD/nvim-neoclip.lua)) is sometimes handy ([$vimfiles/nvim/lua/lazy/nvim-neoclip.lua](https://github.com/harriott/vimfiles/blob/master/nvim/lua/lazy/nvim-neoclip.lua))
- For navigating:
    - `fzf-lua` ([Code](https://github.com/ibhagwan/fzf-lua)) I configure ([$vimfiles/nvim/lua/lazy/fzf-lua.lua](https://github.com/harriott/vimfiles/blob/master/nvim/lua/lazy/fzf-lua.lua)) for a few buffer and file-finding cases
    - my `Leap` ([Code](https://github.com/ggandor/leap.nvim)) configuration ([$vimfiles/nvim/lua/lazy/leap.lua](https://github.com/harriott/vimfiles/blob/master/nvim/lua/lazy/leap.lua)) is simple, and extremely useful
    - In directories:
        - `nvim-tree` ([Code](https://github.com/nvim-tree/nvim-tree.lua)) is an improvement on `NERDTree`, and I took the time to rationalise my keymappings ([$vimfiles/nvim/lua/lazy/nvim-tree.lua](https://github.com/harriott/vimfiles/blob/master/nvim/lua/lazy/nvim-tree.lua))
        - `oil.nvim` ([Code](https://github.com/stevearc/oil.nvim)) is a vast improvement on `netrw`, and I set it to my liking ([$vimfiles/nvim/lua/lazy/oil.lua](https://github.com/harriott/vimfiles/blob/master/nvim/lua/lazy/oil.lua))
- Layout:
    - `bufferline.nvim` ([Code](https://github.com/akinsho/bufferline.nvim)) makes life so much easier
    - `gitsigns.nvim` ([Code](https://github.com/lewis6991/gitsigns.nvim)) is discrete and helpful
    - `lualine.nvim` ([Code]()) does the job, with some minor caveats ([$vimfiles/nvim/lua/lazy/lualine.lua](https://github.com/harriott/vimfiles/blob/master/nvim/lua/lazy/lualine.lua))
    - `nvim-scrollview` ([Code](https://github.com/dstein64/nvim-scrollview)) adds a discreet scrollbar
- `nvim-notify` ([Code](https://github.com/rcarriga/nvim-notify)) is sometimes handy ([$vimfiles/nvim/lua/lazy/nvim-notify.lua](https://github.com/harriott/vimfiles/blob/master/nvim/lua/lazy/nvim-notify.lua))
- `Telescope` ([Code](https://github.com/nvim-telescope/telescope.nvim)) adds a wide range of handy "finders" to `Neovim`, and it's become a great boon to my Vim-based workflow. I took time to configure it to my liking ([$vimfiles/nvim/lua/lazy/telescope.lua](https://github.com/harriott/vimfiles/blob/master/nvim/lua/lazy/telescope.lua)).
    - `telescope-frecency.nvim` ([Code](https://github.com/nvim-telescope/telescope-frecency.nvim)) nicely replaces the excellent `ctrlp.vim` that I still use in `Vim` ([$vimfiles/nvim/lua/lazy/telescope-frecency.lua](https://github.com/harriott/vimfiles/blob/master/nvim/lua/lazy/telescope-frecency.lua)), which is quite an achievement - thank you, the developers - I use this hundreds of times a day.
    - `telescope-fzf-native.nvim` ([Code](https://github.com/nvim-telescope/telescope-fzf-native.nvim)) adds handy `fzf` syntax to searches

## sweet Neovide
```powershell
winget add neovide  # only installable to  $Env:ProgramFiles\Neovide
```

[Neovide](https://neovide.dev/) is the GUI that I'd been waiting for, making the whole shift to `Neovim` worthwhile.

