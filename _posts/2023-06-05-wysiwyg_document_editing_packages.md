---
# vim: set fdl=4:
description: "my take on wysiwyg document editing tools"
tags: LibreOffice ODF Vim
title: "wysiwyg document editing packages"
---

I'm old enough to remember using a typewriter. When I was a researcher in environmental acoustics, I got my first computer and began learning how to use [WordPerfect](https://en.wikipedia.org/wiki/WordPerfect). Later I moved on to [Microsoft Word](https://en.wikipedia.org/wiki/Microsoft_Word), and then expanded out to [Microsoft Office](https://en.wikipedia.org/wiki/Microsoft_Office).

Today, if you're not using `Linux`, just pay the annual subscription for [Microsoft 365](https://en.wikipedia.org/wiki/Microsoft_365) - it's the best, and worth it, and installs on `Android` too.

I'm writing briefly here about "What You See Is What You Get" suites [WYSIWYG](https://en.wikipedia.org/wiki/WYSIWYG).

## ODF
As I discovered the happy world of `Linux` and prefer it over `MS Windows`, I switched to free programs that use the [OpenDocument](http://en.wikipedia.org/wiki/OpenDocument) format. I began with what is now [Apache OpenOffice](https://en.wikipedia.org/wiki/Apache_OpenOffice), and later moved on to the more frequently maintained [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice).

### using LibreOffice
- I tweak the toolbars a little, and I do this, `alt+t (= Tools) > AutoCorrect > [ Correct TWo INitial CApitals, Capitalise first letter of every sentence ] > off`, which saves me a load of annoyance.
- One excellent feature is saving to PDF, which I do all the time for excellent cross-platform readability.

#### maintaining LibreOffice across machines
In your current working [LibreOffice user profile](https://wiki.documentfoundation.org/UserProfile), which is

- on `Linux`: `~/.config/libreoffice/4/user/`
- on `MS Windows`: `C:\Users\<username>\AppData\Roaming\LibreOffice\4\user\`

\- you need to backup the directory `config` and the file `registrymodifications.xcu`. When you install `LibreOffice` on a new machine, or just want to bring another installation up-to-date, just replace those two nodes from your backup.

