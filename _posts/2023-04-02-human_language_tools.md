---
# vim: set fdl=2:
layout: post
tags: Arch Bash Linux vim
title: "human language tools"
---

## Bash
In my Arch boxes I've installed [Dictd](https://wiki.archlinux.org/title/Dictd) and [verbiste](https://aur.archlinux.org/packages/verbiste), and configured some of my own commands to use them in part of my `.bashrc` ([bashrc-console](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/Bash/bashrc-console)).

[DICT](https://en.wikipedia.org/wiki/DICT) - using my configuration:

    $ dmt fuck
    No definitions found for "fuck", perhaps you mean:
    moby-thesaurus:  buck  duck  luck  muck  Puck  ruck  suck  tuck  yuck  funk

    $ dwn fuck
    1 definition found
    From WordNet (r) 3.0 (2006) [wn]:
      fuck
        n 1: slang for sexual intercourse [syn: {fuck}, {fucking},
             {screw}, {screwing}, {ass}, {nooky}, {nookie}, {piece of
             ass}, {piece of tail}, {roll in the hay}, {shag}, {shtup}]
        v 1: have sexual intercourse with; "This student sleeps with
             everyone in her dorm"; "Adam knew Eve"; "Were you ever
             intimate with this man?" [syn: {sleep together}, {roll in
             the hay}, {love}, {make out}, {make love}, {sleep with},
             {get laid}, {have sex}, {know}, {do it}, {be intimate},
             {have intercourse}, {have it away}, {have it off}, {screw},
             {fuck}, {jazz}, {eff}, {hump}, {lie with}, {bed}, {have a
             go at it}, {bang}, {get it on}, {bonk}]

I find `dict` works best when left in the default configuration of accessing the resources online.

`Verbiste` works offline:

    $ decon aimâmes
    aimer, indicative, past, 1, plural

The conjugation output can be long, so I wrote some `Bash` to compress it like so:

![conjugate aimer with Verbiste](/assets/2023-04-02-human_language_tools/con_aimer.jpg)

## online
- [WordReference.com](https://en.wikipedia.org/wiki/WordReference.com) dictionaries are excellent. I refer to them almost daily, either by web page such as [Dictionnaire anglais-français](https://www.wordreference.com/fren/), or through the Android app [WordReference.com dictionaries](https://play.google.com/store/apps/details?id=com.wordreference).

### Google
- [Google Translate](https://translate.google.com/) is of course incredibly useful for deciphering some unknown phrase, maybe in a language I've no competence in such as this song title from Miguel Hernández: "Llegó con tres heridas" --> "He arrived with three wounds".
- I sometimes use it to help find a translation into a foreign language, but with great care, as it can offer unclear translations.
- [Google Translate Alternatives](https://alternativeto.net/software/google-translate/).

## Vim plugins
In my [plugins.vim](https://github.com/harriott/vimfiles/blob/master/plugin/plugins.vim) I `packadd` [thesaurus_query.vim](https://github.com/ron89/thesaurus_query.vim), configured to act on current word with `\th`, which is neat.

### accessing LanguageTool
I write French in a `Vim` scratch buffer that has this modeline:
```
vim: se spl=fr: \aa toggles ALE, \lt for LangTool
```
So words that aren't in `.vim/spell/fr.utf-8.spl` (or associated files) get highlit, but I can get some grammar help with the power of `languagetool-commandline.jar`: `\lt` calls up [vim-langtool](https://github.com/Konfekt/vim-langtool), which takes a while to create location list of suggested corrections so I prefer `\aa` to fire up [ALE](https://github.com/dense-analysis/ale) (the "Asynchronous Lint Engine").

I needed time to figure out how to configure `LanguageTool` to be usefully accessible in flavours of `Vim` in both my `Arch linux` boxes and my `Win10Pro` laptop, but it was well worth it!

