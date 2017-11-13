import json

import helpers


with open(helpers.global_map_path, 'r') as f:
    global_map = json.load(f)

with open(helpers.unloader_path, 'r') as f:
    unloader = json.load(f)

source_articles = []
[source_articles.append(article['source_id']) for article in global_map]
if unloader['source_id'] not in source_articles:
    print('Source article not in global map')
    exit()

removed_copies = []
empty_src_index = None
for src_article in global_map:
    if src_article['source_id'] == unloader['source_id']:
        for copy in src_article['copies']:
            if copy['id'] in unloader['removal_list']:
                print('Unreplicating {}'.format(copy['id']))
                response = helpers.remove_copy(copy['id'], copy['hc'])
                if response is None:
                    continue
                removed_copies.append(copy)

    for removed_copy in removed_copies:
        src_article['copies'].remove(removed_copy)  # remove the copy from global map

    if not src_article["copies"]:           # if all the article's copies were removed, flag it
        empty_src_index = global_map.index(src_article)
    break

if empty_src_index is not None:        		# remove article with no copies from global map
    del global_map[empty_src_index]

with open(helpers.global_map_path, 'w') as f:
    json.dump(global_map, f, sort_keys=True, indent=2)
