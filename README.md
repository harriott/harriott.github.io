    vim: fdl=2:

    $JHm/README.md

GitHub Pages automatically builds my site https://harriott.github.io from this repository.

[List of supported languages and lexers](https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers)

1. in `$JHm/_drafts` create a `yyyy-mm-dd-post_name.md`, when ready move it into `$JHm/_posts`
1. `$JHm/_config.yml` can set `show_drafts`

# in $JHm
    $JHm/Gemfile

## sequence
    rbenv install 3.3.4
    cd $JHm
    rbenv local 3.3.4
    gem up
    gem ins -v 232 github-pages
    rm Gemfile.lock  # clear out any crap
    gem cl  # remove unnecessary packages
    bundle ins  # regenerates  Gemfile.lock, and pulls in needed gems
    bundle ou
    bundle up --all  # doesn't do all
    jekyll s  # takes a while to generate

