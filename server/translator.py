import json
import requests


def api_url_base(lang_code):
    return 'https://{0}.wikipedia.org/w/api.php?'.format(lang_code)


def search(input, lang_code):
    # https://www.mediawiki.org/wiki/API:Opensearch
    # api_params = '&limit=15'
    api_url = '{0}action=opensearch&format=json&namespace=0&search={1}'.format(api_url_base(lang_code), input)

    response = requests.get(api_url)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data[1]


def translate(page_name, source_lang_code, target_lang_code):
    # https://www.mediawiki.org/wiki/API:Query
    # https://www.mediawiki.org/wiki/API:Langlinks
    api_params = '&prop=langlinks&llprop=url|langname&lllimit={0}&llinlanguagecode={1}'.format(500, 'en')
    api_url = '{0}action=query&format=json{1}&titles={2}'.format(api_url_base(source_lang_code), api_params, page_name)

    response = requests.get(api_url)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        page_id = list(data['query']['pages'])[0]

        # could be returned in REST call
        lang_links = data['query']['pages'][page_id].get('langlinks')

        if lang_links is None:
            print('No translation available')
            return

        for lang_link in lang_links:
            if lang_link['lang'] == target_lang_code:
                requested_lang = lang_link
                break

        return requested_lang['*']


def get_langlinks(page_name, source_lang_code):
    api_params = '&prop=langlinks&llprop=url|langname&lllimit={0}&llinlanguagecode={1}'.format(500, 'en')
    api_url = '{0}action=query&format=json{1}&titles={2}'.format(api_url_base(source_lang_code), api_params, page_name)

    response = requests.get(api_url)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        page_id = list(data['query']['pages'])[0]

        lang_links = data['query']['pages'][page_id].get('langlinks')

    return lang_links


def test():
    # print(translate('Computer', 'nl', 'pl'))

    search_results = search('comp', 'nl')

    for i in range(len(search_results)):
        print("{}: {}".format(i, search_results[i]))

    selected_page_id = input("Select page (id): ")
    selected_page = search_results[int(selected_page_id)]

    print("Selected page: {}".format(selected_page))

    lang_links = get_langlinks(selected_page, 'nl')

    for i in range(len(lang_links)):
        print("{}: {}".format(lang_links[i].get('lang'), lang_links[i].get('langname')))

    selected_lang_key = input("Select language (code): ")

    # selected_lang_key = 'pl'

    selected_lang = [lang for lang in lang_links if lang.get('lang') == selected_lang_key]

    print(selected_lang)

# test()
