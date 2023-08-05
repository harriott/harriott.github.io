---
# vim: set fdl=2:
description: "my preferred image management tools"
tags: ExifTool FastStone feh GIMP ImageMagick IrfanView LibreOffice nomacs nsxiv MyPaint Pinta ranger scanimage tikz urxvt
title: "draft: tools for working with images"
---

Being cheap, I manage images on my various machines with a range of free tools, briefly described here.

- [GNU Image Manipulation Program.](http://en.wikipedia.org/wiki/GIMP) can do anything, if you can figure it out, which I can't. Still I've found it handy to crop an image to a specific aspect ratio.
- [ExifTool](http://en.wikipedia.org/wiki/ExifTool) - I mostly use to remove the highly inconsistent orientation tag from images - see my [jpgorhor](https://github.com/harriott/jpgorhor).
- [ImageMagick](http://en.wikipedia.org/wiki/ImageMagick) is another command-line powertool I use, mostly for simple tasks such as montages, borders, text effects, blurring
- [LibreOffice Draw](https://en.wikipedia.org/wiki/LibreOffice_Draw) is handy for creating colourful schematics.
- on Linux
    - [feh (image viewer)](https://en.wikipedia.org/wiki/Feh_%28image_viewer%29)
        - `feh -F -D 4` full screen slide-show, changing every 4 seconds.
    - nomacs has excellent [FEATURES](https://nomacs.org/features/), keyboard controlled, with easy resolution change or cropping of an image, so it's my default viewer.
    - [nsxiv](https://nsxiv.codeberg.page/) has some handy features, in particular recursively thumbnailing images, so I wrap it in my [$Bash/bashrc-wm](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/Bash/bashrc-wm)
    - My [$OSAB/ranger/rc.conf](https://github.com/harriott/OS-ArchBuilds/blob/master/ranger/rc.conf) has a mapping to open the current directory in a new instance of [rxvt-unicode](http://software.schmorp.de/pkg/rxvt-unicode.html) such that I'm out of `tmux`, where I usually am, and I can use `ranger` to rapidly view images, alongside other filetypes, via `w3mimgdisplay`.
    - I wrap [scanimage.1](http://www.sane-project.org/man/scanimage.1.html) in my [$Bash/bashrc-wm](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/Bash/bashrc-wm) for easy scanning from the command line.
- [MyPaint](http://en.wikipedia.org/wiki/MyPaint) has some handy simple painting tools.
- [PGF/TikZ](https://en.wikipedia.org/wiki/PGF/TikZ) can make some stunning graphics, if you're up for learning `LaTeX`, which is in itself a challenge...
- [Pinta (software)](http://en.wikipedia.org/wiki/Pinta_%28software%29) also has some handy features, in particular it shows the pixel position of your mouse pointer within the image.
- on Windows
    - [FastStone Image Viewer](https://en.wikipedia.org/wiki/FastStone_Image_Viewer) I use as my default
        - I always `F12 (= Settings) > Viewer > [ Loop on, Auto-rotate by EXIF off, Default Unit > cm ]`
    - [IrfanView](https://en.wikipedia.org/wiki/IrfanView) is a neat image viewer with some handy editing facilities and ability to access your scanner
        - I always tweak it: `P (= Properties/Settings) > [JPG > Auto-rotate off   Browsing > Cut White]`

