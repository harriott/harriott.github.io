
'''
adapted from  https://rfong.github.io/rflog/2020/02/28/jekyll-tags/  with thanks
generates tag pages for all your post tags for a Jekyll site
invoked automtically after saving a post by  $Jhm/_plugins/compile_tags.rb
invoke manually:  $Jhm> python _plugins/compile_tags.py
works well, could be replaced by untangled's more compact Ruby code
'''

import glob
import os

POST_DIR = '_posts/'
TAG_DIR = 'tag/'

# Collect all tags from all posts.
all_tags = []
for fname in glob.glob(POST_DIR + '*.md'):
  with open(fname, 'r') as f:
    for line in f:
      # Find tags & cut them.
      if line.startswith('tags: '):
        all_tags += [
          t.strip() for t in line[len("tags: "):].split(' ')]
        break
all_tags = sorted(list(set(all_tags)))
# Remove old tag pages
old_tags = glob.glob(TAG_DIR + '*.md')
for tag in old_tags:
  os.remove(tag)

# Create tag directory if it does not exist
if not os.path.exists(TAG_DIR):
  os.makedirs(TAG_DIR)

# Write new tag pages.
TAG_PAGE_TEMPLATE = '''---
layout: tagpage
tag: {tag}
robots: noindex
---'''
for tag in all_tags:
  with open(TAG_DIR + tag + '.md', 'a') as f:
    f.write(TAG_PAGE_TEMPLATE.format(tag=tag))
