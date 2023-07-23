---
# vim: set fdl=2:
description: "my preferred tools for consuming ebooks & PDFs"
tags: Calibre Firefox Foliate Linux Sumatra Zathura Windows
title: "ebooks & PDFs"
---

Among the many many possibilities, I've homed in, over the years, on these few tools, for functionality and freedom:

- [eBook](https://en.wikipedia.org/wiki/Ebook)
    - [Foliate](https://github.com/johnfactotum/foliate) is nice and simple, [Calibre](http://en.wikipedia.org/wiki/Calibre_%28software%29) does it all.
- [PDF](http://en.wikipedia.org/wiki/Portable_Document_Format)
    - [Firefox](http://en.wikipedia.org/wiki/Mozilla_Firefox) does a good job of displaying PDFs, and can show the `Document Outline`.
    - On my `Linux` machines
        - I have [Zathura (document viewer)](http://en.wikipedia.org/wiki/Zathura_%28document_viewer%29), which has many handy keyboard shortcuts.
        - [Poppler](http://en.wikipedia.org/wiki/Poppler_%28software%29) provides some handy tools, including
            - [pdfimages](https://en.wikipedia.org/wiki/pdfimages) to pull out any images
            - [pdftotext](https://en.wikipedia.org/wiki/pdftotext), helps in my [$OSAB/ranger/scope.sh](https://github.com/harriott/OS-ArchBuilds/blob/master/ranger/scope.sh)
    - On my `Windows 10 Pro` laptop: [Microsoft Edge](https://en.wikipedia.org/wiki/Microsoft_Edge) does a good job of displaying PDFs, but I more often use [Sumatra PDF](http://en.wikipedia.org/wiki/Sumatra_PDF).
    - Sometimes I want to convert a PDF to PNG, I wrote myself some functions for that:
        - [$Bash/bashrc-ob](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/Bash/bashrc-ob) contains my wrapper around `gs`
        - [$MSWin10\PSProfile.ps1](https://github.com/harriott/OS-MSWin10/blob/master/PSProfile.ps1) contains my wrapper around `gswin64c`
    - [pdftk](https://en.wikipedia.org/wiki/PDFtk) although dated, still has useful functionality. I use it to
        - burst out PDF to single pages
        - decrypt

