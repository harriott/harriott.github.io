
# from  https://rfong.github.io/rflog/2020/02/28/jekyll-tags/
# - but I can't get this to act...

# Jekyll post_write hook to run the page generator script
Jekyll::Hooks.register :posts, :post_write do |post|
  puts 'post_write  was triggered in _plugins/compile_tags.rb'
  exec("python _plugins/compile_tags.py")
end

