---
# vim: set fdl=2:
description: "my preferred minimalist tools on Windows 10"
tags: AutoHotkey BRU CapsLock Ditto Explorer Everything Notepad++ PowerToys QuickHash Sysinternals Tixati Windows
title: "minimalist Windows tools"
---

I used to find `Microsoft Windows` lengthy to setup well and to maintain in good order. It's become easier, and `Windows 10` is particularly easy to manage. Being a desktop environment, it comes with a lot of what we might need. Here I run through some minimalist tools that I use to fill in a few gaps:


- [AutoHotkey](http://en.wikipedia.org/wiki/AutoHotkey) - [ $MSwin10\jo.ahk ](https://github.com/harriott/OS-MSWin10/blob/master/jo.ahk) is invaluable!
- [Bulk Rename](http://www.bulkrenameutility.co.uk/) for fast renaming of many files
- [CapsLock](https://www.microsoft.com/en-gb/p/capslock/9nbx19w2pp00) gets me a tray icon, which I need on my `Lenovo ThinkPad T430 i5-3320M` which has no LED indicator...
- `ctrl+shift+esc` = `Task Manager`, which I set to show `Processes` and hide when minimized - very handy
- [Ditto](http://ditto-cp.sourceforge.net) is my preferred clipboard, invaluable to my workflow
- [Everything (software)](https://en.wikipedia.org/wiki/Everything_%28software%29) - for instantly finding files on your system
- [File Explorer](https://en.wikipedia.org/wiki/File_Explorer) is an ever handy tool
    - `alt-d > wt` jumps me out to `Windows Terminal` on the current directory
    - `alt-p` toggles the preview pane, I use my [asAdminWEPreviewPane.ps1](https://github.com/harriott/OS-MSWin10/blob/master/asAdminWEPreviewPane.ps1) to add extra text file types
- [Microsoft PowerToys](https://en.wikipedia.org/wiki/Microsoft_PowerToys) has some nice components - you can see how I configure it in my [ $machine\Win10ProBuild.txt ](https://github.com/harriott/OS-MSWin10/blob/master/T430i73520M/Win10ProBuild.txt).
- [Notepad++](http://en.wikipedia.org/wiki/Notepad%2B%2B) is my go-to editor when I don't want to or can't use a `vim` flavour, or `emacs`.
- [Quick Hash GUI](https://quickhash-gui.org/) is what I use to compute hashes
- [Sysinternals](http://technet.microsoft.com/en-gb/sysinternals) - an excellent collection of small tools, here are some of which I keep the executables in my `C:\Users\troin\AppData\Local\Microsoft\WindowsApps` for direct access from `PowerShell`:
    - [Autoruns for Windows](https://learn.microsoft.com/en-gb/sysinternals/downloads/autoruns)
    - [Disk Usage](https://docs.microsoft.com/en-us/sysinternals/downloads/du) - `du64 -l 1` for a quick list of subdirectory sizes.
    - [Process Explorer](http://en.wikipedia.org/wiki/Process_Explorer) oh yeah, CPU & RAM icons in the tray from startup!
    - [Sigcheck](https://docs.microsoft.com/en-gb/sysinternals/downloads/sigcheck) - for when you're worried...
    - [Streams](https://docs.microsoft.com/en-gb/sysinternals/downloads/streams) - for checking some weird `NTFS` stuff...
    - [Tixati](https://en.wikipedia.org/wiki/Tixati) - my preferred BitTorrent client

