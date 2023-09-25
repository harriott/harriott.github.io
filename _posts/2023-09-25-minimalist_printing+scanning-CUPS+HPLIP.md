---
# vim: set fdl=2:
description: "running an HP printer on Arch Linux"
tags: CUPS HPLIP
title: "minimalist printing & scanning with CUPS & HPLIP"
---

Wow, was this difficult to figure out: network usage of my [HP ENVY 5532 e-All-in-One Printer](http://support.hp.com/gb-en/product/HP-ENVY-5530-e-All-in-One-Printer-series/5304881/model/5373124) from Arch Linux.

So here are some clues.

I need [CUPS](https://en.wikipedia.org/wiki/CUPS) and [HP Linux Imaging and Printing](https://en.wikipedia.org/wiki/HP_Linux_Imaging_and_Printing) installed.

My printer needs to be on the same WiFi network as my linux computer. I use my mobile phone to provide the internet with a WiFi Hostspot. This works, but with an inconvenient caveat: the printer regularly gets issued a new IP address by my phone, and each time it does, I need to reconfigure my linux computer to be able to communicate with it, which is fiddly.

My [$Imagey/Scan.sh](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/Bash/Imagey/Scan.sh) is the central bit of code I wrote for scanning documents from the command-line, as I do.

When my printer's IP address has changed, to be able to print, I need to do this:

- `hp-setup -r` > Select Printer (tick the old one) > Remove
- `hp-setup 192.168.61.10` (= the new IP address shown on the printer's LCD) > Next > Add Printer
- `hp-toolbox &` (= HP Device Manager > HP Envy 5530 Series) > Printer Control > Set as Default

\- which is a drag, but then my printer works.

Occasionally my printer becomes unresponsive even though it's not changed address. Then I `lpstat -p -d` and if it reports to be paused I `doas cupsenable ENVY_5530`, which often gets it going, though occasionally I need to reboot my computer...

