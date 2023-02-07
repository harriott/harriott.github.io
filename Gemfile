
# bundle install  after changes here

source "https://rubygems.org"

# Jekyll:
# gem "jekyll", "~> 4.3.1"
gem "github-pages", group: :jekyll_plugins  # bundle update github-pages
gem "webrick", "~> 1.7"  # instead of using Ruby v2.7.4

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.1", :platforms => [:jruby]  # JH upped the patch to 1

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Plugins:
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end

# Theme-ish:
gem "jekyll-include-cache", group: :jekyll_plugins  # required by  Minimal Mistakes
gem "jekyll-remote-theme"  # to be able to use the latest version of minima theme
gem 'jekyll-seo-tag'
gem "minima", "~> 2.5"  # default theme for new Jekyll sites

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

