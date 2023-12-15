---
# vim: set fdl=1:
# $JHm/_posts/2023-12-15-stacked_bar_charts_of_my_work_hours.md.md
description: "markdown, Perl, and gnuplot for time tracking"
tags: gnuplot markdown Perl Vim
title: "stacked bar charts of my work hours"
---

## keeping logs of my hours, quick and easy
Back in 2014 I decided to track how I was using my time, so I began logging my hours using my newly acquired skills ([vim and related tools]({% post_url 2023-01-25-vim_and_related_tools %})).  Currently all of my hours are logged in a `markdown` file `roles.md`, which is now huge, but `Vim` handles it easily, and with my [vim configurations]({% post_url 2023-02-05-vim_configurations %}), it's contents look like this:

![roles.md - start of November 2023](/assets/2023-12-15-stacked_bar_charts_of_my_work_hours/roles-nb1-3.jpg){: width="400" }

I coded my work categories, so, for example, `Cz:60` means 60 minutes of work done for Cafézoïde.

## then visualising my hours
For years I thought I'd need to learn [R](https://en.wikipedia.org/wiki/R_%28programming_language%29) to be able to display my hours logs as stacked bar charts. Then I realised I could do it with [pgfplots](https://www.ctan.org/pkg/pgfplots), and, as I got started reading how to do so, I discovered [gnuplot](https://en.wikipedia.org/wiki/Gnuplot), and went with that instead. I needed a few days to sufficiently understand `gnuplot` and to adapt my toolchain, but it feels worth the effort - [misc/CP/workHours/](https://github.com/harriott/misc/tree/master/CP/workHours) - which gets me pages like this:

![bar charts for 2014-2022](/assets/2023-12-15-stacked_bar_charts_of_my_work_hours/ym2014-22.png)
\- at last I can see where my time went this past decade...
