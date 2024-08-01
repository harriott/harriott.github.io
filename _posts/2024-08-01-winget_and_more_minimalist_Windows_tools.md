---
# vim: set fdl=1:
# $JHm/_posts/2024-08-01-winget_and_more_minimalist_Windows_tools.md
description: "winget, the Windows Package Manager, and other speedy tools"
tags: AltSnap BgInfo C++ Chrome Everything eza FD fzf Git GnuPG ImageMagick IrfanView KeePassXC less LibreOffice LF LSD MiKTeX Notepad++ PowerShell Python Ruby Sumatra Thunderbird Vim Windows winget wt Zig
title: "winget, and more minimalist Windows tools"
---

After my post [minimalist Windows tools]({% post_url 2023-07-27-minimalist_Windows_tools %}), I built up a `Windows 10 Pro` OS & software installation on a French laptop, and discovered yet more hugely useful minimalist tools.

## first, winget
The [Windows Package Manager](https://en.wikipedia.org/wiki/Windows_Package_Manager) is already there, and makes installing software so much faster.

```powershell
winget update --all
```

I configure a `function wl` in my [$MSWin10\PSProfile.ps1](https://github.com/harriott/OS-MSWin10/blob/master/PSProfile.ps1) to easily update lists of packages that I have installed on each machine.

Some packages install to `~\AppData\Local\Microsoft\WinGet\Packages\` and add themselves into the system path which I habitually check with `$env:psmodulepath -split (';')` and I usually see an unneccessary `;` added to the end of the path which I fix like this:
```powershell
$oldPathCU = (gp 'registry::hkcu\environment' path).path; $oldPathCU
$newPathCU = $oldPathCU -replace ';$', ''; $newPathCU
sp 'registry::hkcu\environment' -name path -value $newPathCU
```

## then, more speedy stuff
- `AltSnap` ([Code](https://github.com/RamonUnch/AltSnap)), provides easier moving and resizing of windows. `winget add altsnap`. It sometimes needs to be kicked back into action, so I set a keystroke in my [$MSWin10\AutoHotkey\HPEB840G37.ahk](https://github.com/harriott/OS-MSWin10/blob/master/AutoHotkey/HPEB840G37.ahk).
- [AutoHotkey](http://en.wikipedia.org/wiki/AutoHotkey): `winget add AutoHotkey.AutoHotkey`
- [BgInfo](http://technet.microsoft.com/en-gb/sysinternals/bb897557.aspx) `winget add BgInfo` then I run it, set font down to 8 and Grey 50%, and position it top right
- Coding:
    - ([Code](https://github.com/Kitware/CMake)) `winget add Kitware.CMake`
    - ([Code](https://github.com/koalaman/shellcheck)) `winget add koalaman.shellcheck`
    - ([Installing Node.js via Package Managers](https://nodejs.org/en/download/package-manager/all)) `winget add OpenJS.NodeJS`
    - [MiKTeX](http://en.wikipedia.org/wiki/MiKTeX): `winget add miktex` installs to '~\AppData\Local\Programs\MiKTeX'
    - [Pandoc](http://en.wikipedia.org/wiki/Pandoc): `winget add JohnMacFarlane.Pandoc` installs to `~\AppData\Local\Pandoc\pandoc.exe`
    - [PowerShell](https://en.wikipedia.org/wiki/PowerShell): `winget add Microsoft.PowerShell`
    - [Ruby](https://en.wikipedia.org/wiki/Ruby_%28programming_language%29): `winget add RubyInstallerTeam.Ruby.3.2`
    - [Strawberry Perl](http://en.wikipedia.org/wiki/Strawberry_Perl): `winget add StrawberryPerl.StrawberryPerl` gets me a good-enough `Perl` installation, though `Perl` works better on `Linux`
    - [Windows Terminal](https://en.wikipedia.org/wiki/Windows_Terminal) `winget add 9N0DX20HK701`
- Documenting:
    - [LibreOffice](https://en.wikipedia.org/wiki/LibreOffice): `winget add libreoffice`
    - [Sumatra PDF](http://en.wikipedia.org/wiki/Sumatra_PDF): `winget add SumatraPDF -h -l C:\SumatraPDF`
- File management tools:
    - Alternatives to [Get-ChildItem](https://learn.microsoft.com/en-gb/powershell/module/microsoft.powershell.management/get-childitem):
        - `winget add eza-community.eza` ([Code](https://github.com/eza-community/eza))
        - `winget add lsd` ([Code](https://github.com/Peltoche/lsd))
        - `winget add sharkdp.fd` ([Code](https://github.com/sharkdp/fd))
    - [Everything (software)](https://en.wikipedia.org/wiki/Everything_%28software%29): `winget add voidtools.Everything`
    - [fzf](https://github.com/junegunn/fzf): `winget add fzf`
    - [Git](https://en.wikipedia.org/wiki/Git): `winget add git.git -l C:\Git`
    - gokechan's `LF` ([Code](https://github.com/gokcehan/lf)) lets me zip around my filesystem from within `WT` - another game changer for which I am immensely grateful to the developers
    - [How to install Visual C++ Build tools?](https://stackoverflow.com/questions/40504552/how-to-install-visual-c-build-tools), though I find `winget add Microsoft.VisualStudio.2022.BuildTools` to be enough
        - then I can `winget add rustup`, then `winget add burntsushi.ripgrep.msvc`, oh yeah!
    - `less-Windows` ([Code](https://github.com/jftuga/less-Windows)): `winget install jftuga.less`
    - [Python](http://en.wikipedia.org/wiki/Python_%28programming_language%29): `winget add python.python.3.12`
    - [Zig (programming language)](https://en.wikipedia.org/wiki/Zig_%28programming_language%29): `winget add zig.zig`
- Imagey:
    - [FastStone Image Viewer](https://en.wikipedia.org/wiki/FastStone_Image_Viewer): `winget add FastStone.Viewer`
    - [ImageMagick](http://en.wikipedia.org/wiki/ImageMagick): `winget add imagemagick` (installs `C:\Program Files\ImageMagick-7.1.1-Q16-HDRI`)
    - [IrfanView](https://en.wikipedia.org/wiki/IrfanView): `winget add IrfanSkiljan.IrfanView -h` installs to `C:\Program Files\IrfanView\i_view64.exe`
- Internetworking:
    - Browsing:
        - [Google Chrome](http://en.wikipedia.org/wiki/Google_Chrome): `winget add Google.Chrome.EXE`
        - [Gpg4win](https://en.wikipedia.org/wiki/Gpg4win): `winget add gnupg.gpg4win`
    - [Thunderbird](http://en.wikipedia.org/wiki/Mozilla_Thunderbird): `winget add mozilla.thunderbird -h -l C:\MT`
- [KeePassXC](https://en.wikipedia.org/wiki/KeePassXC): `winget add KeePassXCTeam.KeePassXC`
- Text editing:
    - [Notepad++](http://en.wikipedia.org/wiki/Notepad%2B%2B): `winget add --name notepad++`
    - [Vim (text editor)](http://en.wikipedia.org/wiki/Vim_%28text_editor%29): `winget add vim.vim -l C:\Vim`

