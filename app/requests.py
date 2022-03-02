import urllib.request, json
from .sources_model import Sources, Display
from .articles_model import Articles, Display

api_key = None
base_url = None
cat_url = None


def configure_request(app):
    global api_key, base_url, cat_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    cat_url = app.config['CATE_API_URL']

def get_source():
    get_source_url = base_url.format(api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        if id:
            source_object = Sources(id,name,description, url,category,language,country)
            source_results.append(source_object)

    return source_results

def getarticle_source(id):
    getarticle_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)

    with urllib.request.urlopen(getarticle_source_url) as url:
        article_source_data = url.read()
        article_source_response = json.loads(article_source_data)

        article_source_result = None

        if article_source_response['articles']:
            article_source_list = article_source_response['articles']
            article_source_result = process_articles_results(article_source_list)

    return article_source_result

def process_articles_results(news):
    article_source_result = []
    for article in news:
        id = article.get('id')
        name = article.get('name')
        title = article.get('title')
        urlToimage = article.get('urlToImage')
        author = article.get('title')
        publishedAt = article.get('publishedAt')
        description = article.get('description')

        if urlToimage:
            article_object = Articles(id, name, title, urlToimage, author, publishedAt, description)
            article_source_result.append(article_object)

    return article_source_result

def get_by_category():
    get_category_url = cat_url.format(api_key)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)

        get_category_results = None

        if get_category_response['articles']:
            get_category_list = get_category_response['articles']
            get_category_results = process_articles_results(get_category_list)

    return get_category_results

def get_headlines():
    get_headlines_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'.format(api_key)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        get_headlines_results = None

        if get_headlines_response['articles']:
            get_headlines_list = get_headlines_response['articles']
            get_headlines_results = process_articles_results(get_headlines_list)

    return get_headlines_results