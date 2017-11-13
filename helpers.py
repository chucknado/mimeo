import os

import requests
import auth


# ----- Variables ----- #

auth = auth.get_auth()
loader_path = os.path.join('maps', 'loader.json')
unloader_path = os.path.join('maps', 'unloader.json')
global_map_path = os.path.join('maps', 'global_map.json')


# ----- Functions ----- #

def get_translation(article_id, hc, locale='en-us'):
    """
    :param article_id: Help Center article id
    :param hc: Help Center subdomain. Example: mondocam in mondocam.zendesk.com/hc
    :param locale: The article locale
    :return: A JSON object with the translation properties
    """
    url = 'https://{}.zendesk.com/api/v2/help_center/articles/{}/translations/{}.json'.format(hc, article_id, locale)
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        return response.json()['translation']
    else:
        print('Failed to get article {} with error {}'.format(article_id, response.status_code))
        return None


def get_article(article_id, hc, locale='en-us'):
    """
    :param article_id: Help Center article id
    :param hc: Help Center subdomain. Example: mondocam in mondocam.zendesk.com/hc
    :param locale: The article locale
    :return: A JSON object with the article properties
    """
    url = 'https://{}.zendesk.com/api/v2/help_center/{}/articles/{}.json'.format(hc, locale, article_id)
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        return response.json()['article']
    else:
        print('Failed to get article {} with error {}'.format(article_id, response.status_code))
        print('Check the loader.json file. Exiting.')
        return None


def replicate_article(article, locale='en-us'):
    """
    :param article: Dictionary data needed to copy a source article in a destination section
    :param locale: The article locale
    :return: A JSON object with the new article properties
    """
    url = 'https://{}.zendesk.com/api/v2/help_center/{}/sections/{}/articles.json'.format(article['hc'], locale,
                                                                                          article['section_id'])
    payload = {'article': {'title': article['title'],
                           'body': article['body'],
                           'author_id': article['author_id'],
                           'label_names': 'readonly'}}
    response = requests.post(url, json=payload, auth=auth)
    if response.status_code == 201:
        print('Successfully created a copy of article in section {}'.format(article['section_id']))
        return response.json()['article']
    else:
        print('Failed to create a copy of the article with error {}'.format(response.status_code))
        print(response.reason)
        return None


def sync_replicated_articles(source, copy_id, hc, locale='en-us'):
    """
    :param source: Translation record of the source article
    :param copy_id: Help Center id of the article copy
    :param hc: Help Center subdomain
    :param locale: The article locale
    :return:
    """
    url = 'https://{}.zendesk.com/api/v2/help_center/articles/{}/translations/{}.json'.format(hc, copy_id, locale)
    payload = {'translation': {'title': source['title'], 'body': source['body']}}
    response = requests.put(url, json=payload, auth=auth)
    if response.status_code == 200:
        print('  - Updated copy {} to match source article'.format(copy_id))
    else:
        print('  - Failed to update copy of source article with error {}'.format(response.status_code))
        print(response.reason)


def remove_copy(copy_id, hc):
    """
    :param copy_id: Help Center id of the article copy
    :param hc: Help Center subdomain
    :return: 204 or None
    """
    url = 'https://{}.zendesk.com/api/v2/help_center/articles/{}.json'.format(hc, copy_id)
    print(url)
    response = requests.delete(url, auth=auth)
    if response.status_code == 204:
        return response.status_code
    else:
        print('Failed to delete article copy {} with error {}'.format(copy_id, response.status_code))
        return None


def update_global_map(global_map, map_update):
    """
    Maps an article copy to a source article in the global map. If the source article isn't found,
    adds the source article and copy to the global map.
    :param global_map: List of articles with associated copies
    :param map_update: Dictionary of data to update the global map
    :return: Updated list of articles
    """
    updated = False
    for article in global_map:
        if article['source_id'] == map_update['source_id']:
            article['copies'].append(map_update['copies'][0])
            updated = True
            break
    if updated is False:            # new source article
        global_map.append(map_update)
    return global_map
