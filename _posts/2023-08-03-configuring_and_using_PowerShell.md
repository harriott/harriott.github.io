---
# vim: set fdl=2:
description: "how I configure and use PowerShell on Windows 10"
tags: fzf Git PowerColorLS PowerShell pt wt ZLocation
title: "draft: configuring and using PowerShell"
---

Command history:
```powershell
gvim (Get-PSReadlineOption).HistorySavePath  # \Users\troin\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
h  # Get-History
```

`PS> ii .` opens [File Explorer](https://en.wikipedia.org/wiki/File_Explorer) on the current directory.

[Windows Terminal](https://en.wikipedia.org/wiki/Windows_Terminal) is a breath of fresh air, with easy configuration, and configurable keyboard shortcuts. I often get to it from [File Explorer](https://en.wikipedia.org/wiki/File_Explorer) by `alt-d` then typing "wt" in the address bar and hitting `enter`.

## configuration
So I take the time to configure [PowerShell](https://en.wikipedia.org/wiki/PowerShell) to my preferences.

### execution policy
If you `Get-ExecutionPolicy` you will see "Restricted", which means you can't run your own scripts, so change that by elevating your instance of `PowerShell` to administrator and `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Confirm`.

### one profile for all
Confusingly, you'll likely also have `Windows PowerShell` on your `Windows` system, as you'll see if you try these:
```powershell
powershell -noprofile -command '"$PSVersionTable"'  # returns  Windows PowerShell  version
pwsh -v  # returns the more modern  PowerShell  version
```

You're better off working with the more up-to-date and cross-platform `PowerShell`.

I keep one [ $MSWin10\PSProfile.ps1 ](https://github.com/harriott/OS-MSWin10/blob/master/PSProfile.ps1) for both of these, and symlink it to the default locations - see my [ $MSwin10\symlinks.ps1 ](https://github.com/harriott/OS-MSWin10/blob/master/symlinks.ps1).

### modules
I also found these confusing, there being some already installed, and various locations for them, as evidenced by `$Env:PSModulePath -split ';'`, but this is where my installs end up:
```
C:\Users\troin\Documents\PowerShell\Modules
C:\Users\troin\Documents\WindowsPowerShell\Modules
```

#### what I install
    Compare-Module | Where UpdateNeeded | Foreach { Update-Module $_.name }  # slow...

- [BurntToast](https://www.powershellgallery.com/packages/BurntToast/) for notifications
- [Pester](https://www.powershellgallery.com/packages/Pester/4.4.0-beta) - I keep updated, but have never needed...
- [PSFzf](https://www.powershellgallery.com/packages/PSFzf/) - adds wicked fuzzy-finding to `Powershell`
- [PSWriteColor](https://www.powershellgallery.com/packages/PSWriteColor) for colourised output
- [PSReadLine](https://www.powershellgallery.com/packages/PSReadLine/) - for easy access to your command history
- [PSScriptTools](https://www.powershellgallery.com/packages/PSScriptTools/) - for a load of handy extra functions
    - `Get-PSScriptTools` for a synopsis of all the functions
    - some I like
        - `$PSSpecialChar` - a quick list
        - Bars in PowerShell: `New-ANSIBar -Range (232..255)` & `New-RedGreenGradient`
        - Directories investigations:
            - `dw` (= Get-DirectoryInfo) a directories count
            - `Get-FolderSizeInfo` I wrap in my [ $MSWin10\PSProfile.ps1 ](https://github.com/harriott/OS-MSWin10/blob/master/PSProfile.ps1)
            - `pstree [n]` (= `Show-Tree`)
        - `Get-MyVariable` - variables list
        - `Get-Process` I wrap in my [ $MSWin10\PSProfile.ps1 ](https://github.com/harriott/OS-MSWin10/blob/master/PSProfile.ps1) for a handy pop-up of running processes
        - `Get-PSSessionInfo`
        - `Get-TZData Europe/Paris`
        - `Get-WhoIs 8.8.8.8`
        - `Test-IsElevated`
- [PackageManagement](https://www.powershellgallery.com/packages/PackageManagement/) is already there (for `Install-Module ...`), and I updated it with `Install-Module PackageManagement -Force`
- [Posh-Git](https://github.com/dahlbyk/posh-git) I import and configure in my [ $MSWin10\PSProfile.ps1 ](https://github.com/harriott/OS-MSWin10/blob/master/PSProfile.ps1)
- [PowerColorLS](https://github.com/gardebring/PowerColorLS) I alias as `pc` for handy colourized directory listing.
- [PowerShellGet](https://www.powershellgallery.com/packages/PowerShellGet/) provides the handy `Get-InstalledModule`
- [Powershell.Chunks](https://www.powershellgallery.com/packages/Powershell.Chunks/1.0.0) for `Get-Chunk` which breaks a long 1-dimensional array into 2nd dimension chunks.
- [Terminal-Icons](https://github.com/devblackops/Terminal-Icons/) adds icons to directory listings.
- [ZLocation](https://www.powershellgallery.com/packages/ZLocation/) - `gal z` shows that it's ready for easy jumping around previous directory visits.

### The Platinum Searcher
- `C:\Users\troin\AppData\Local\Microsoft\WindowsApps\pt.exe` allows me to `pt search .` recursively finding all occurances of "search" inside files.
- [the_platinum_searcher](https://github.com/monochromegane/the_platinum_searcher)

