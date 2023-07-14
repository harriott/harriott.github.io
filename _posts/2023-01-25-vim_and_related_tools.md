---
# vim: set fdl=1:
description: "A quick description of how my productivity was boosted by learning vim."
tags: Dropbox emacs LaTeX markdown ODF Vim
title: "vim and related tools"
---

For better or worse, learning `vim` totally transformed my use of IT and allowed me to geek-out to my heart's desire. `vim` has become central to my daily life. I now keep all my personal and work notes in some kind of text file,

- [markdown](http://en.wikipedia.org/wiki/Markdown) for worldly stuff
    - here's a good intro: [Getting Started](https://www.markdownguide.org/getting-started/)
- [Dokuwiki](https://en.wikipedia.org/wiki/Dropbox) for my IT notes, works well on `Linux` too
- [LaTeX](http://en.wikipedia.org/wiki/Markdown) for letters and nicely formatted output
    - the Wikibook, [LaTeX](http://en.wikibooks.org/wiki/LaTeX) is a good start

I regularly convert all of my `markdown` notes to `PDF`, and they get sync'd up to my `Dropbox` and then down onto my Android phones (by the [Dropsync: Autosync for Dropbox](https://play.google.com/store/apps/details?id=com.ttxapps.dropsync) app) where the `PDF` format is much easier to navigate in.

I'm obsessive (for better or worse) about things that interest me, so I note things every day. When I used to use `ODF`s for that (see [wysiwyg document editing packages]({% post_url 2023-06-05-wysiwyg_document_editing_packages %})), I'd find myself needing to install some kind of heavy duty desktop search app that could constantly scan inside my many documents. This was a cumbersome business and `vim` freed me from that.

## millions of words
To illustrate, without going into the configurations details: on one of my `Arch linux` machines, in my `TextNotes` directory, (using sharkdp's [fd](https://github.com/sharkdp/fd),) `$ fd -tf -e md | wc -l` shows I've 510 `markdown` files, then `$ wc -w **/*.md` reports they contain a total of 4,038,098 words - all stuff I've accumulated over the last two decades. That's a lot of words, but easy to search when you've learned how to `grep`. I can for example (using BurntSushi's [ripgrep](https://github.com/BurntSushi/ripgrep), `$ rg -tmd shark` to get a colourful output in my terminal like this sample:

![ripgrep for shark](/assets/2023-01-25-vim_and_related_tools/1-shark.jpg)

Oh, I notice there's a spelling mistake in one of those files, so, here in my `vim` buffer where I'm writing this, I'm configured so that I can search for enough of the mis-spelled word - in this case "wandrer" will do - place my cursor over it and (in vim's normal mode) hit `*`, then I hit `F3` which I've configured to use tpope's excellent [vim-fugitive](https://github.com/tpope/vim-fugitive) command `Ggrep`, and in a flash I'm taken to the file and the line containing the mis-spelled word, already highlighted such that I can hit `n` (`vim` for "jump to next highlighted occurance") then `frx` (`vim` for "find r delete") and it's corrected. With my configuration I then just (still in vim's normal mode) hit `f4` and that `vim` buffer is saved to the originating file, and closed.

## all folded up
Another life-changing functionality is code folding, which I use all over `vim` to fold anything that's getting too long for me. Here's how one of my biggest files opens in my `vim` setup:

![Private notes folded up](/assets/2023-01-25-vim_and_related_tools/2-Private.jpg)

\- it's not code in there, but I use code folding anyway to fold up that huge file in `vim`, and pretty much everything else. I open and close folds with `spacebar`. If a `vim` filetype plugin doesn't include code folding, I write my own.

## for geeks only
The end result is I can whizz around my notes and my code, sometimes jumping over to terminal then back into `vim`, all with incredible ease and speed. But there's a catch. I can only recommend this if you really like coding. Personally of course, I enjoy tweaking my `vim` configuration whenever I find myself repeatedly doing something that could be automated. Sometimes it takes hours, and I need to keep good notes to be able to recall my coded task shortcuts, but, as I say, I enjoy it, like playing a good game of chess.

My `vim` configuration is here: [vimfiles](https://github.com/harriott/vimfiles).

---
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>

---
## ...almost forgot... about emacs...
If you do any serious configuration of  `vim` you'll know that there's also [GNU Emacs](http://en.wikipedia.org/wiki/GNU_Emacs). I was attracted by vim's focus on text, and once I began configuring it there was no need to look elsewhere. Nine years later, I was curious about Emacs' [Org-mode](https://en.wikipedia.org/wiki/Org-mode), so I put in the hours to make my own [init.el](https://github.com/harriott/misc/blob/master/Emacs/init.el), and in doing so discovered that I prefer vim's tighter focus on text and more direct configurability. I got the feeling that `Emacs` focuses more on making you comfortable with a particular task while `vim` focuses on highly configurable text wrangling.

I realised that my own vim-based organisation strategy had become unbeatable.

Still I keep `Emacs` handy for one reason: readability - `Emacs` offers us the super comfort of [Proportional Fonts](https://www.emacswiki.org/emacs/ProportionalFonts). So I added keystrokes in my `vim` configuration to open exactly where I am in a file in `Emacs` (and vice-versa), which is sometimes so so helpful.

