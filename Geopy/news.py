from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='bef6ecd2d9994b48a7adda36ba062b43')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='space',
                                          category='technology',
                                          language='en',
                                          country='in')

# /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2023-07-25',
#                                       to='2023-08-25',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# /v2/top-headlines/sources
sources = newsapi.get_sources()
i=0
while i < len(top_headlines['articles']):
    author = top_headlines['articles'][i]['author']
    title = top_headlines['articles'][i]['title']
    content = top_headlines['articles'][i]['content']


    i += 1
    print(f"News Published by ",author)
    print(title)
    print(content)
