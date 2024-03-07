---
# vim: set fdl=2:
description: "How I scrape text conversations from mysms and Facebook Messenger."
layout: post
tags: Messenger mysms Perl Windows Vim WhatsApp

title: "grabbing mysms and Messenger conversations with Perl"
---

## mysms
For at least a decade I've been using [mysms](https://www.mysms.com/) to be able to manage my main smartphone's text messages from any browser.

On my smartphone, I need to allow [mysms - Remote Text Messages](https://play.google.com/store/apps/details?id=com.mysms.android.sms) as my default text messaging app, which of course I'm okay with. Then, in any browser, I just need to login to [app.mysms.com](https://app.mysms.com/), and then I can see a message stream, like this:

![mysms in web browser](/assets/2023-06-03-grabbing_mysms_and_messenger_conversations_with_Perl/mysms_in_browser.jpg)

`mysms` defaults to [Short Message Service (SMS)](http://en.wikipedia.org/wiki/Short_Message_Service), but if you paste in an image or a pdf to attach, then it switches to [Multimedia Messaging Service (MMS)](http://en.wikipedia.org/wiki/Multimedia_Messaging_Service).

See that the most recent message is up top, while typically on an Android phone the most recent message is at bottom, above a space to enter your next message.

### scrape off past texts
In my browser, I highlight all my messages - here it would be all the text encircled in pink - and `Copy` that, then `Paste` it into an empty `scrape.md`. It looks like this:
```
Friday, January 13, 2023
Preshila:Hi Joseph, Okay. 11:14 AM
Me:Hello Preshila, could we try this evening? 10:40 AM
Thursday, January 12, 2023
Preshila:I am free only early mornings around 8h-10h or in the evenings when I finish work around 19h30. 5:57 PM
Me:Tomorrow after midday? 5:53 PM
Preshila:Hi Joseph,
Sure, when are you planning to come? 5:40 PM
Me:Hello Preshila, would you have time to help me again with the sink drain ? Joseph 3:14 PM
```
It's all there, but not easily readable, and in reverse order. So I decided to write a `Perl` script to fix this - [mysmsMD.pl](https://github.com/harriott/misc/blob/master/PerlTools/mysmsMD.pl) - and I call it on `scrape.md` in `Vim` with keystroke `\<f7>`, which gets me this:

![mysms messages scraped from web browser](/assets/2023-06-03-grabbing_mysms_and_messenger_conversations_with_Perl/scrape_md.jpg)

\- much neater, in descending order with time - like any text document, and also folded up with my simple `Vim` folding algorithm.

## Facebook Messenger
I then created a similair functionality, [MessengerMd.pl](https://github.com/harriott/misc/blob/master/PerlTools/MessengerMd.pl) for scraping off [Messenger](https://en.wikipedia.org/wiki/Messenger_%28software%29) texts into a nicely folded up `markdown` file.

## my helpful Vim configurations for markdown
- [markdown.vim](https://github.com/harriott/vimfiles/blob/master/ftplugin/markdown.vim) - for folding by `markdown` header marks
- [md.vim](https://github.com/harriott/vimfiles/blob/master/ftplugin/md.vim) - for `\<f7>`

## WhatsApp
Surprisingly straightforward, when you know how - see my [$vimfiles/syntax/whatsapp.vim](https://github.com/harriott/vimfiles/blob/master/syntax/whatsapp.vim).

