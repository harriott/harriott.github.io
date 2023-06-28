---
# vim: set fdl=2:
description: "my preferred file management tools - mostly cli"
tags: clifm exa fd find fzf jump PCManFM nnn ranger stat
title: "file management in minimalist linux"
---

I prefer a lean Linux install, so I use [awesome (window manager)](https://en.wikipedia.org/wiki/Awesome_%28window_manager%29) on my netbook and [Openbox](https://en.wikipedia.org/wiki/Openbox) on my desktop machines. I prefer minimalist tools, my choices of [File manager](https://en.wikipedia.org/wiki/File_manager) included. Here I briefly describe my favourite file management tools in order of importance.

## nnn
[nnn (file manager)](https://en.wikipedia.org/wiki/Nnn_%28file_manager%29) is my most-used tool, central to all my work on Linux machines. I just find it so whippingly fast to move around directory trees, and to move files and directories around. I configure it a little in my [bashrc-console](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/Bash/bashrc-console).

## launching default applications
This is a fiddly matter, a good reason to not go minimalist like me, but choose a good integrated modern [Desktop environment](https://en.wikipedia.org/wiki/Desktop_environment) like the [GNOME Shell](https://en.wikipedia.org/wiki/GNOME_Shell) or [KDE Plasma 5](https://en.wikipedia.org/wiki/KDE_Plasma_5), both of which are excellent and take care of most of your configurations. I prefer minimal, which takes a little more work. [Default applications](https://wiki.archlinux.org/index.php/default_applications) got me started with [mimeo](https://xyne.dev/projects/mimeo/), which works fine, though I moved onto `handlr`, which ([Is this repo dead? #74](https://github.com/chmln/handlr/issues/74)) still works well.

## PCManFM
[PCMan File Manager](http://en.wikipedia.org/wiki/PCMan_File_Manager) serves my needs on the odd occasion that I want a graphical file manager.

    Edit > Preferences >
      General > Confirm before moving files into "trash can"  off-ticked
      Volume Management > Show available options  off-ticked
      Advanced > Terminal > urxvt

I make bookmarks for certain preferred locations.

In my [bashrc-ob](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/Bash/bashrc-ob) I have
```bash
pf () {
    nohup pcmanfm &
    sleep 2; rm nohup.out
}  # launch  PCManFM  on current directory
```
which lets me launch `PCManFM` from a terminal location.

Although I consider `PCManFM` minimalist, it does have a load of dependencies, as can be seen if I

    pactree -u pcmanfm | tr '\n' '~' | sed 's/~/  /g'; echo

## ranger
Took me a while to teach myself [ranger (file manager)](https://en.wikipedia.org/wiki/Ranger_%28file_manager%29), and it was worth it. It's as fast as `nnn`, and more informative, but clunky for moving things around, so I use it more for looking than for doing. Most of my configuration can be seen in [rc.conf](https://github.com/harriott/OS-ArchBuilds/blob/master/ranger/rc.conf).

## fzf & jump
- [fzf](https://github.com/junegunn/fzf) is another game-changing tool that I rely on. I use it from the command line to quickly home in on something in a directory tree using its implementation of [Approximate string matching](https://en.wikipedia.org/wiki/Approximate_string_matching). More frequently I'm using it via a few keybindings in my [plugins.vim](https://github.com/harriott/vimfiles/blob/master/plugin/plugins.vim) to rapidly fuzzy find in my vast number of text files.
- I [jump](https://github.com/gsamokovarov/jump) all day long to my most used directories.

## find, fd, stat, chown, chmod, exa...
- [find (Unix)](https://en.wikipedia.org/wiki/Find_%28Unix%29) is powerful, though useful `find` commands need some crafting, so I keep notes to remind myself of useful examples such as `find . -type l -ls  # list all symlinks in a directory tree`.
- [fd](https://github.com/sharkdp/fd) is an excellent abstraction of `find`, eg: `fd -tl -HL -X rm  # removes dead links`
- I have a few useful `stat` commands in my [bashrc-generic](https://github.com/harriott/OS-ArchBuilds/blob/master/Bash/bashrc-generic).
- Bring drive `SDSSDA240G` into my control: `# chown -R jo:jo /run/media/jo/SDSSDA240G`
- Make my script executable: `# chmod 755 $Obc/rc/importScreenshot.sh`
- [exa (command-line utility)](https://en.wikipedia.org/wiki/Exa_%28command-line_utility%29) is such a handy file lister that I configure some one-letter commands in my [bashrc-generic](https://github.com/harriott/OS-ArchBuilds/blob/master/Bash/bashrc-generic).
- I've a few more simple commands configured in my [bashrc-generic](https://github.com/harriott/OS-ArchBuilds/blob/master/Bash/bashrc-generic), things that I picked up here and there, such as counting file types.

## CliFM
- [clifm](https://github.com/leo-arch/clifm) is a neat idea based on just listing files while leaving the terminal mostly functional. I tend to use it when I'm in a highly populated directory.  I bind it to `C` in my [bashrc-console](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/Bash/bashrc-console).
- My modest contribution to the project: [cfm filetype conflicts with vim's ColdFusion filetype #146](https://github.com/leo-arch/clifm/issues/146).

