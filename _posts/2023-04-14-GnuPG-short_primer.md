---
# vim: set fdl=1:
description: "A very short primer for GNU Privacy Guard."
layout: post
tags: Arch GnuPG Linux pass Windows
title: "GnuPG - short primer"
---

[GNU Privacy Guard](http://en.wikipedia.org/wiki/GNU_Privacy_Guard) is an impressive and heavily documented tool.

My essential use cases are:

- for installing packages on `Arch Linux`
- (along with `Git`) as a prerequisite for [pass](https://www.passwordstore.org/)

There are many good guides online, and the two main references are:

- [Using the GNU Privacy Guard](https://www.gnupg.org/documentation/manuals/gnupg/index.html)
- [The GNU Privacy Handbook](https://www.gnupg.org/gph/en/manual/book1.html)

And the `Arch Linux` manual [GPG(1)](https://man.archlinux.org/man/gpg.1.en) fills in some gaps.

## install
- `Arch linux`: [GnuPG](https://wiki.archlinux.org/index.php/GnuPG)
    1. `export GPG_TTY=$(tty)` in `.bashrc`
    1. [~/.gnupg/gpg-agent.conf](https://github.com/harriott/OS-ArchBuilds/blob/master/jo/gpg-agent.conf) - for one-time entering of passphrase
- `Windows 10 Pro`: [Download](https://www.gpg4win.org/get-gpg4win.html)
    1. off-tick the clunky `Kleopatra`, and install to `C:\Gpg4win`
    1. `where.exe gpg` reports `C:\GnuPG\bin\gpg.exe`

## get going
I say first, `gpg -k` (short for `gpg --list-keys`), which also sets up my local hidden directories if they're not yet made.

- **generate a key**:`gpg --full-gen-key` > `1y` (= "one year before expiry") > `<my_name>` > `<my_email>` > `<key_description>` > `<my_passphrase>` - the terminal output includes the newly generated key's fingerprint.
- **edit my key**:`gpg --edit-key <id>` and can then `adduid`, `deluid`, `expire`, `trust`
- **backup my key**:`gpg -ao backup.asc --export-secret-keys --export-options backup <id>` - this also backs up trusts.
- **import a backup'd key**:If for some reason I'm starting again, `gpg --import backup.asc`. This also brings in my public key.
- **check my private keys**:`gpg -K` (short for `gpg --list-secret-keys`)

## grab public keys
I pull down whatever public keys I might need for software installations to succeed. For example Pierre Schmitz's (which I could only get from [Hockeypuck OpenPGP keyserver](https://keyserver.ubuntu.com)): `gpg --keyserver hkps://keyserver.ubuntu.com --recv-keys 4AA4767BBC9C4B1D18AE28B77F2D434B9741E8AC`, and sign it, `gpg --edit-key pierre@archlinux.de` > `sign` - I need my private key's passphrase, then `save`.

## create an encrypted message
As I have a public key from someone named Adam, I can create an encrypted message for him,
```bash
echo "secret for Adam" | gpg -ase -r adam -o message_for_adam.asc
```
\- breakdown:

- `-a` (`--armor`) create ASCII armored output
- `-e` = `--encrypt`
- `-s` (`--sign`) sign the message
- `-r` = `--recipient`
- `adam` identifies his public key in my keyring, but it could be any suitable id

As I don't have Adam's private key, I can't decrypt `message_for_adam.asc`, so why not try a message to myself, which I can do as I have my own public key in my keyring:
```bash
echo "secret for myself" | gpg -ase -r 13F327EF -o secret.asc
```
\- here I'm id'ing my own public key as recipient with `13F327EF` - the end of my key's fingerprint. As I also have my private key in my keyring, I can easily decrypt the message, `gpg -d secret.asc`.

I've never actually needed to send such an encrypted message, but it could happen...

