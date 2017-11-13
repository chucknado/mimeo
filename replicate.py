import json
import os

import helpers


if os.path.isfile(helpers.global_map_path):
    with open(helpers.global_map_path, 'r') as f:
        global_map = json.load(f)
else:
    global_map = []   			# no global map yet so create one

with open(helpers.loader_path, 'r') as f:
    loader = json.load(f)

source_article = helpers.get_article(loader['source_id'], loader['source_hc'])
if source_article is None:  	# problem with the API request
    exit()
article_data = {
    'title': source_article['title'],
    'body': source_article['body'],
    'author_id': source_article['author_id']
}

for location in loader['locations']:
    article_data['hc'] = location['hc']
    article_data['section_id'] = location['section_id']
    article_copy = helpers.replicate_article(article_data)
    if article_copy is None:
        continue
    map_update = {
        "source_id": loader['source_id'],
        "source_hc": loader['source_hc'],
        "title": source_article['title'],
        "copies": [{'id': article_copy['id'], 'hc': location['hc']}]
    }
    global_map = helpers.update_global_map(global_map, map_update)

with open(helpers.global_map_path, 'w') as f:
    json.dump(global_map, f, sort_keys=True, indent=2)
