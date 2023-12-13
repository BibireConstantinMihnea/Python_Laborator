import requests

def reddit_news_fetch(subject):
    base_url = 'https://www.reddit.com/'
    with open('pw.txt', 'r') as f:
        pw = f.read()
    data = {'grant_type': 'password', 'username': 'Reechyy', 'password': pw}
    auth = requests.auth.HTTPBasicAuth('dLDgu8S4xVHnkfWoDfej_Q', 'd5pDT9sxLrtY4qb-gZlWoUWduIWNWg')
    resp = requests.post(base_url + 'api/v1/access_token',
                         data=data,
                         headers={'User-Agent': 'NewsFeedGUI'},
		                 auth=auth)
    d = resp.json()
    token = 'bearer ' + d['access_token']

    oauth_url = 'https://oauth.reddit.com'

    headers = {'Authorization': token, 'User-Agent': 'NewsFeedGUI'}
    search_params = {'q': subject, 'limit': 10, 'sort': 'new', 'restrict_sr': 'True'}

    news_data = []

    response = requests.get(oauth_url + '/r/news/search', headers=headers, params=search_params)
    if response.status_code == 200:
        news = response.json()
        for post in news['data']['children']:
            post_data = post['data']
            title = post_data['title']
            link = post_data['url']
            source = "Reddit - " + post_data['subreddit_name_prefixed']
            news_data.append((source, title, link))
        
    return news_data

def nyt_news_fetch(subject):
    api_key = '5oGXRF3JyvHUXmaVgzLiNluTq1p8OLys'
    base_url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
    
    params = {
        'q': subject,
        'api-key': api_key,
        'sort': 'relevance',
        'fl': 'web_url,headline,source',
        'fq': subject
    }

    response = requests.get(base_url, params=params)

    news_data = []

    if response.status_code == 200:
        articles = response.json()['response']['docs']
        for article in articles:
            title = article['headline']['main']
            link = article['web_url']
            source = article['source']
            news_data.append((source, title, link))

    return news_data
