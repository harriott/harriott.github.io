# from  https://rfong.github.io/rflog/2020/02/28/jekyll-tags/  with thanks

# Filename: _plugins/compile_tags.rb
# Jekyll post_write hook to run the page generator script
Jekyll::Hooks.register :posts, :post_write do
  system("python _plugins/compile_tags.py")
end
