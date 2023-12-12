import requests

def reddit_news_fetch(subject):
    base_url = 'https://www.reddit.com/'
    with open('pw.txt', 'r') as f:
        pw = f.read()
    data = {'grant_type': 'password', 'username': 'Reechyy', 'password': pw}
    auth = requests.auth.HTTPBasicAuth('i91C4OUnzMQ5MZRA40NKeA', '4AJCAox0saa_4O59WIXHqoaq-GLI3g')
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
    index = 0

    response = requests.get(oauth_url + '/r/news/search', headers=headers, params=search_params)
    if response.status_code == 200:
        news = response.json()
        for post in news['data']['children']:
            index += 1
            post_data = post['data']
            title = post_data['title']
            link = post_data['url']
            source = "Reddit - " + post_data['subreddit_name_prefixed']
            news_data.append((index, source, title, link))
        
    return news_data

def other_news_fetch():
    pass
