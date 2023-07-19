---
# vim: set fdl=2:
description: "My preferred tools for managing the email deluge."
layout: post
tags: Arch GnuPG Linux pass Windows
title: "email tools across platforms"
---

Ugh, _email_ - modern wonder, and scourge. It's so easy to send that now anyone that's online is saturated with emails that we really should read, but largely don't. I consider myself really bad at reading through my emails - my problem is that I don't read my emails every day. I have a reason for this: No matter how important my incoming emails might be, I want to be in charge of what I do next - I don't want to be a slave to my emails. I'm already a slave to the clock, which I free myself from whenever I can, just to remember what it felt like to have "bags of time".

So, to survive in all our contractual and friendly arrangements, we need our preferred email tools. In my case I've several principal email accounts:

- [Gmail](https://en.wikipedia.org/wiki/Gmail) also gets me a [Google Account](http://en.wikipedia.org/wiki/Google_Account), and in return [Google](https://en.wikipedia.org/wiki/Google) gets to know me in some ways better than I know myself, and [Google Ads](https://en.wikipedia.org/wiki/Google_Ads) follows me around the web. I'm happy with that deal. I use my `Gmail` account for general administration, shopping, and for my son's `Android` phone. I also sometimes have `Gmail` accounts specifically for work. The web browser client is excellent.
- [FastMail](http://en.wikipedia.org/wiki/FastMail) I pay a small annual fee for an email account. I use this for private emails, and some work. I was originally motivated by `Gmail` (some years ago) refusing to send one of my attachments, and somewhat by privacy. The web browser client is excellent.
- [GMX Mail](http://en.wikipedia.org/wiki/GMX_Mail) I've used for years, and keep for legacy reasons. The web interface is a little clunky and interfering, but works well enough.
- [Outlook.com](http://en.wikipedia.org/wiki/Outlook.com) I signed up to originally when it was `Hotmail`, and keep those accounts for my science-related work and for configuring my `Windows 10 Pro` laptop.

I also occasionally use a [Disposable email address](http://en.wikipedia.org/wiki/Disposable_e-mail_address).

## Thunderbird
I use [Thunderbird](http://en.wikipedia.org/wiki/Mozilla_Thunderbird) on both `Linux` and `Windows 10 Pro`. These are the huge advantages:

- I can quickly see the contents of all of my principal email accounts, and drag & drop emails between them.
- I can `Delete` attachments (that I've downloaded) from emails, thus vastly reducing my Archive folders storage size.

### connect to an email account
`alt > f (= File) > n (= New) > e > e (= Existing Mail Account...)` and you'll enter your credentials

If it's a `Gmail` account, `Thunderbird` will pop-up [Sign in with your Google Account](https://accounts.google.com/InteractiveLogin) in its internal web browser where you'll have to re-enter your password to move on to complete your `2-Step Verification` process. (See [Signing in with 2-Step Verification](https://support.google.com/accounts/topic/7189145).)

### global settings
`Thunderbird` has many internal shortcut keys which I can't always remember, so I have my own quick-reference always just a few `Vim` keystrokes away [misc/CrossPlatform/QR/QR.md](https://github.com/harriott/misc/blob/master/CrossPlatform/QR/QR.md#thunderbird). [tbkeys-lite](https://addons.thunderbird.net/en-US/thunderbird/addon/tbkeys-lite/) is a big help.

Occasionally I do `File > Compact Folders`.

Sometimes `Thunderbird` shows the wrong message contents for a folder, which is fixed by right-clicking on the broken folder for `Properties > Repair`.

By default `Thunderbird` threads emails, which I strongly dislike, so I `alt+v (= View) > s (= Sort by) > h (= Unthreaded)`.

### account settings
`Thunderbird` is good at detecting your email account's server settings when you give it your email address.

You'll probably want to tweak your `Account Settings` for each email account.

`Settings > Privacy > Passwords > Saved Passwords... > Show Passwords` gets a small window named `Saved Logins`

#### Gmail
`Gmail` is tricky because it uses labels to represent mail folders, so `Server settings > When I delete > Just mark it as deleted` has the disadvantage of leaving the message in `All Mail`, and so you'll discover that messages you thought you'd deleted are still there, in the less visible `All Mail` folder, but labelled by `Gmail` as deleted. My fix is, for each `Gmail` account, `Server settings > When I delete > Move > Bin`, then I occasionally empty the `Bin`, truly getting rid of all that junk mail. (Remember of course that whatever's on the internet lingers on in hidden corners for years, including our private emails...)

Off-tick Thunderbird's default setting of `Copies & Folders > [ When sending messages, automatically: > Place a copy in:` as `Gmail` handles this with labels effectively placing sent mail in `[Gmail]/Sent Mail` folder.

### syncing my Profile between machines
[Profile backup](https://kb.mozillazine.org/Profile_backup) is easy. If you tweak your `Thunderbird` settings on one machine, you can copy that to another machine to transfer your tweaks. Your `~/.thunderbird/profiles.ini` shows you where your `Thunderbird` profile is installed. I used to do this manually, but now I have Dropbox do it for me.

#### syncing my Profile with Dropbox
On my `Arch linux` machines:
```bash
export Drpbx='<location_of_my_Dropbox_directory>'
export T91="$DJH/T91-default-release"  # where I'd like my Thunderbird v91 profile to be
sed -i "/Name=default-release/,/^$/ { s/IsRelative=1/IsRelative=0/; s:Path=.*:Path=$Thb: }" ~/.thunderbird/profiles.ini
```

On my `Windows 10 Pro` laptop, I run `Thunderbird v91` once, empty `C:\Users\troin\AppData\Roaming\Thunderbird\Profiles\57isrjsc.default-release`, then edit `C:\Users\troin\AppData\Roaming\Thunderbird\profiles.ini`:
```dosini
[Profile0] section:
  IsRelative=0
  Path=C:\Users\Joseph\Dropbox\JH\T91-default-release
```

There's one catch with this - I shouldn't open `Thunderbird` simultaneously on different machines. To help me enforce this I made a few small scripts:

- [OS-ArchBuilds/jo/wm/TS/locks.sh](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/wm/TS/locks.sh)
- [OS-MSWin10/T430i73520M/T91/TaskScheduler/clearParentLock.ps1](https://github.com/harriott/OS-MSWin10/blob/master/T430i73520M/T91/TaskScheduler/clearParentLock.ps1)

## mutt with notmuch
I went down this rabbit hole, which pleased my inner geek, but it ain't for everyone. The result though is amazing: I get command-line control of my emails on my `linux` machines.

[Mutt (email client)](http://en.wikipedia.org/wiki/Mutt_%28email_client%29)
> The Mutt slogan is "All mail clients suck. This one just sucks less."

When you start out you'll be clueless. `mutt` is useless until it's configured. You really have to decide for yourself how you want to do that. Here are some clues:

- [OS-ArchBuilds/jo/clm/neomutt/muttrc-accounts-all](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/clm/neomutt/muttrc-accounts-all) - an entry point into my [NeoMutt](https://neomutt.org/) configuration
- [OS-ArchBuilds/jo/Bash/bashrc-clm](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/Bash/bashrc-clm) - my `Bash` commands for using
    - `mbsync` (see [isync: free IMAP and MailDir mailbox synchronizer](http://isync.sourceforge.net))
        - in my [mbsyncrc-template](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/clm/mbsyncrc-template) you'll see that I use `pass` (see [Pass (software)](https://en.wikipedia.org/wiki/Pass_%28software%29)), for which you might want to look over my [GnuPG - short primer]({% post_url /2023-04-14-GnuPG-short_primer %})
    - `neomutt`, the evolved `mutt`
    - `notmuch` (see [Getting Started with Notmuch](https://notmuchmail.org/getting-started/)).

With this setup I can sync all of my emails from their servers, move them around, sync them again back to the servers, and do powerful regex searches across all of my email accounts.

### providing account password to mbsync
```bash
pass init '<email_associated_with_my_GnuPG_key>'  # sets up ~/.password-store
pass insert <location> # (in ~/.password-store/), then type in your password
```
Then, when `mbysnc` is configured to access your email account's password with `pass`, you'll give your `GnuPG` authentification - I use [pinentry](https://gnupg.org/related_software/pinentry/0) configured to be needed just once per login.

### sending emails
I can send text-only emails for my non-Gmail accounts - see [About msmtp](https://marlam.de/msmtp/).

I did transcribe some handy code that allowed met to send Gmails ([OS-ArchBuilds/jo/clm/msmtprc/oauth2tool.sh](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/clm/msmtprc/oauth2tool.sh)), but then Google decided to stop OAuth out-of-band flow, which effectively excluded `msmtp` from sending Gmails...

