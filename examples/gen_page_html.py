import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=int, default=2, help='')
parser.add_argument('--end', type=int, default=10, help='')
args = parser.parse_args()

for count in range(args.start, args.end+1):
    with open("page{}.html".format(count), "w") as file:
        file.write('---\nlayout: photo_post_default\ntitle: Home\n---\n\n<!-- Posts Index\n================================================== -->\n<section class="recent-posts">\n    <div class="section-title">\n        <h2><span>Photo Posts</span></h2>\n    </div>\n    <div class="row listrecent">\n        {{% assign page_num = {} %}}\n        {{% assign now_page_minus1 = page_num | minus: 1 %}}\n        {{% assign for_begin = site.paginate | times: now_page_minus1 %}}\n        {{% assign for_end = site.paginate | times: page_num %}}\n        {{% assign for_end = for_end | minus: 1 %}}\n        {{% for index in (for_begin..for_end) %}}\n            {{% if index >= site.photo_posts.size %}}\n                {{% break %}}\n            {{% endif %}}\n            {{% assign post = site.photo_posts[index] %}}\n            {{% include photo_post_postbox.html %}}\n        {{% endfor %}}\n    </div>\n</section>\n<!-- Pagination\n================================================== -->\n<div class="bottompagination">\n<div class="pointerup"><i class="fa fa-caret-up"></i></div>\n<span class="navigation" role="navigation">\n    {{% include photo_post_pagination.html this_page_num=page_num %}}\n</span>\n</div>\n\n'.format(count))
