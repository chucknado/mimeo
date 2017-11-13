import json
import arrow

import helpers


with open(helpers.global_map_path, 'r') as f:
    global_map = json.load(f)

for source_article in global_map:
    print('\nChecking source article {}...'.format(source_article['source_id']))
    source_translation = helpers.get_translation(source_article['source_id'], source_article['source_hc'])
    if source_translation is None: 		# problem with the API request
        continue
    source_updated_at = arrow.get(source_translation['updated_at'])
    for copy in source_article['copies']:
        copy_translation = helpers.get_translation(copy['id'], copy['hc'])
        if copy_translation is None:
            continue
        copy_updated_at = arrow.get(copy_translation['updated_at'])
        if source_updated_at > copy_updated_at:
            helpers.sync_replicated_articles(source_translation, copy['id'], copy['hc'])
        else:
            print('  - Copy {} matches source article'.format(copy['id']))
