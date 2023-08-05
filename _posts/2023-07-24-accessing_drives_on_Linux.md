---
# vim: set fdl=2:
description: "some of my preferred tools for accessing storage on Linux"
tags: blkid chown fstab gphoto lsblk mount NTFS PCManFM udisks
title: "accessing drives on Linux"
---

For the disk partitions permanently installed in a linux box, I have, of course, [fstab](https://wiki.archlinux.org/title/Fstab).

For plugged in USB drives, I rely on `udiskie`, an automounter for [udisks](https://wiki.archlinux.org/index.php/udisks).

When I'm looking for plugged in partitions, I use these two:

    doas blkid -o list  # shows fs_type
    lsblk -f

Of course I sometimes need to `# umount /dev/sdx` or `# mount /dev/sdx`, and `# chown -R jo:jo /run/media/jo/<drive>`.

For the dastardly [NTFS](http://en.wikipedia.org/wiki/NTFS) partitions that I use for easier sharing between operating systems, I've [NTFS-3G](https://wiki.archlinux.org/index.php/NTFS-3G).

For my digital camera, [gPhoto](https://en.wikipedia.org/wiki/GPhoto) gets its storage partition visible in [PCMan File Manager](http://en.wikipedia.org/wiki/PCMan_File_Manager).

