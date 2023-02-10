---
# vim: set fdl=2:
layout: post
tags: Dropbox RoboCopy rsync vim
title: "managing drive contents"
---

## drives, drives, drives
I run an `Arch Linux` desktop with a few hard drives inside, I have a mini-desktop as backup, also running `Arch Linux`, a cheap laptop that also breezes along on `Arch Linux` and, to stay in touch with `Microsoft Windows`, I have a `ThinkPad` running on `Windows 10 Pro`, then, for backup, I've got a few portable hard drives and a stack of old disk drives left over from various machines. I keep my machines (including my `Android` phones) sync'd with [Dropbox](http://en.wikipedia.org/wiki/Dropbox_%28storage_provider%29) (and [Dropsync](https://play.google.com/store/apps/details?id=com.ttxapps.dropsync)), both of which are worth every penny.

A lot of the digital content I have doesn't need to by sync'd to `Dropbox`, but I do want it duplicated incase a drive fails - which has happened often enough for me to know that it can happy anytime. So I took some time to develop my own backup strategy.

## sync, sync, sync
So `Dropbox` takes care of the essentials with ease - I can't find a better service - and I occasionally resort to their 30-day restore functionality. To manage drives that I don't want to sync up to `Dropbox` I have a few tools.

### Bash, PowerShell, Vim
Before I was able to move most of my digital workflow to the CLI, I tried various GUI drive sync'ing tools, and was always frustrated by their slowness and lack of configurability. Once I was able to learn `Bash`, `PowerShell`, and then move up to `Vim`, most of my digital workflows became a lot easier, and faster. My current data backup strategy depends on these three excellent and ubiquitous toolsets.

### rsync
[rsync](http://en.wikipedia.org/wiki/Rsync) is an indispensable `Unix` utility, and I use it many times in a week. I had to work to learn how, and I still need to refer to my notes, but with my [vimfiles](https://github.com/harriott/vimfiles) setup, that's no obstacle. I sometimes use `rsync` in one-liners, and sometimes via my scripts for regular full-drive backups, [FM-rsync-drives](https://github.com/harriott/FM-rsync-drives).

### RoboCopy
[Robocopy](http://en.wikipedia.org/wiki/Robocopy) is the `Microsoft Windows` native analogue to `rsync`, and I manage to get it to do enough of what I want, occasionally in one-liners, and otherwise via my script, [(File Manage on MicroSoft Windows) sync drives](https://github.com/harriott/FM-MSWin-syncDrives).

## Whats on that disk?
With a load of backup disks sitting in a pile on a shelf, I need to have some sort of compact catalogue of what's on them. I looked at a few available tools, then developed my own strategy:

1. A central directory with one master file listing all my drives and a summary of their contents.
    - On `Linux` I use `df -h` to get the storage size and free space of a disk, and `ncdu` to create a quick summary of the parent directories.
    - On `MSWin` I use `du64 -l 1`.
1. Individual contents files for each disk drive.
    1. I made a `Python` script to save an extremely compact directory listing in the folder that it's run in, [FM-DirLVF](https://github.com/harriott/FM-DirLVF).
    1. Those compact directory listings are only truly compact when used in conjunction with my `Vim` setup - here's an example (all folded up in `Vim`) from my biggest backup drive:

![WD30EZRZ](/assets/2023-02-04-managing_drive_contents/WD30EZRZ.jpg)

