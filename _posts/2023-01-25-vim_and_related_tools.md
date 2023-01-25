---
layout: post
title: "vim and related tools"
categories: Dropbox LaTeX markdown vim

---

For better or worse, learning `vim` totally transformed my use of IT and allowed me to geek-out to my heart's desire. `vim` has become central to my daily life. I now keep all my personal and work notes in some kind of text file - `markdown` for worldly stuff, `Dokuwiki` for my IT notes - and I use `LaTeX` for letters and nicely formatted output. I regularly convert all of my `markdown` notes to `PDF`, and they get sync'd up to my `Dropbox` and then down onto my Android phones by the `Dropysnc` app where the `PDF` format is much easier to navigate in.

I'm obsessive (for better or worse) about things that interest me, so I note things every day. When I used to use `OpenOffice Writer` compatible formats, I'd find myself needing to install some kind of heavy duty desktop search app that could constantly scan inside my many documents. This was a cumbersome business and `vim` freed me from that. To illustrate, on one of my `Arch linux` machines, in my `TextNotes` directory, (using sharkdp's [fd](https://github.com/sharkdp/fd),) `$ fd -tf -e md | wc -l` shows I've 510 `markdown` files, then `wc -w **/*.md` reports they contain a total of 4,038,098 words - all stuff I've accumulated over the last two decades. That's a lot of words, but easy to search when you've learned how to `grep`. I can for example (using BurntSushi's [ripgrep](https://github.com/BurntSushi/ripgrep), `rg -tmd shark` to get a colourful output in my terminal like this sample: ![ripgrep for shark](/assets/2023-01-25-vim_and_related_tools/1-shark.jpg)

Oh, I notice there's a spelling mistake in one of those files, so, here in `vim` where I'm writing this, I'm configured so that I can place my cursor over enough of the mis-spell, in this case "wandrer" will do, and (in vim's normal mode) hit `*`, then I hit `F3` which I've configured to use tpope's excellent [vim-fugitive](https://github.com/tpope/vim-fugitive) command `Ggrep`, and in a flash I'm taken to the file and the line containing the mis-spelled word, already highlighted such that I can hit `n` (`vim` for "jump to next highlighted occurance") then `frx` (`vim` for "find r delete") and it's corrected. With my configuration I then just (still in vim's normal mode) hit `f4` and that `vim` buffer is saved to the originating file, and closed.

Another life-changing functionality is code folding, which I use all over `vim` to fold anything that's getting too long for me. Here's how one of my biggest files opens in my `vim` setup: ![Private notes folded up](/assets/2023-01-25-vim_and_related_tools/2-Private.jpg)

\- it's not code in there, but I use code folding anyway to fold up that huge file, and pretty much everything else. I open and close folds with `spacebar`. If a `vim` filetype plugin doesn't include code folding, I write my own.

The end result is I can whizz around my notes and my code, sometimes jumping over to terminal then back into `vim`, all with incredible ease and speed. But there's a catch. I can only recommend this if you really like coding. Personally of course, I enjoy tweaking my `vim` configuration whenever I find myself repeatedly doing something that could be automated. Sometimes it takes hours, and I need to keep good notes to be able to recall my coded task shortcuts, but, as I say, I enjoy it, like playing a good game of chess.

