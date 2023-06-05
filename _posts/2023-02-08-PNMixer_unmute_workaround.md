---
# vim: set fdl=2:
description: "Fix PNMixer in awesome wm."
layout: post
tags: Arch awesomewm Linux
title: "PNMixer unmute workaround"
---

## the PNMixer bug
I'm using [awesome (window manager)](https://en.wikipedia.org/wiki/Awesome_%28window_manager%29) on my cheap `Asus VivoBook W202` that breezes along on `Arch Linux`.

The simplest and most effective tray icon that I can find to show the master volume status is [pnmixer](https://github.com/nicklan/pnmixer). `$ pnmixer` puts a volume icon in the right end of awesome's `wibox`. Then, a right-click on that icon for

```
Preferences >
  Behaviour > Volume Control Command > pavucontrol
  View > Draw Volume Meter on Tray Icon
```

`$ pavucontrol` ([PulseAudio Volume Control 5.0](https://freedesktop.org/software/pulseaudio/pavucontrol/)) opens a sound mixer, and it's through that mixer that `PNMixer` silently does it's magic of showing and controlling the volume.

Except when it doesn't, as is the case in my `awesome` configuration.

Apparently it's a known bug, and there's no developer willing to take it on...

## pactl to the rescue
On `Arch`, [libpulse](https://archlinux.org/packages/extra/x86_64/libpulse/) provides the `pactl` command ([pactl(1)](https://man.archlinux.org/man/pactl.1.en)):
> NAME: pactl - Control a running PulseAudio sound server

\- it can finely control the volume, and, happily, `PNMixer` sees the changes and shows them in the icon.

So my workaround is [awesome / audio](https://github.com/harriott/OS-ArchBuilds/tree/master/AsusW202/jo/awesome/audio) which I symlink to `~/.config/awesome/audio/`, and then my [rc.lua](https://github.com/harriott/OS-ArchBuilds/blob/master/AsusW202/jo/awesome/rc.lua) configures `XF86AudioMute`, `XF86AudioLowerVolume`, and `XF86AudioRaiseVolume` (the keyboard's volume keystrokes) to access the little `Bash` scripts therein.

---
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>

