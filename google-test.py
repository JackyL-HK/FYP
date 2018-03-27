query = "Hong Kong Secondary Student"
testurl = "http://www.scmp.com/news/hong-kong/education/article/2133086/long-hours-too-much-homework-and-stressed-pupils-there"

# # google 2.0.1
# # https://github.com/MarioVilas/googlesearch/blob/master/googlesearch/__init__.py
# # return URL only
from googlesearch import search, search_news
# for url in search("Hong Kong Secondary Student", stop=20):
#     print(url)
# print("==============")
urllist = list(search_news("Hong Kong Student", stop=20))
# for url in urllist:
#     print(url)

# # google-search 1.0.2
# # https://github.com/anthonyhseb/googlesearch/pull/10/files#diff-2eeaed663bd0d25b7e608891384b7298
# # failed to get content
# from googlesearch.googlesearch import GoogleSearch
# print(GoogleSearch().search(query).total)
# for result in GoogleSearch().search(query,num_results = 1).results:

#     print("Title: " + result.title)
#     print("Url: " + result.url)
#     print(result.getText()) # SSL Failed
#     print("==============")
#     print(result.getMarkup()) # SSL Failed

# # gsearch 1.6.0
# # https://github.com/aviaryan/python-gsearch/blob/master/gsearch/googlesearch.py
# # Url only (seems faster)
# from gsearch.googlesearch import search
# for result in search(query):
#     print("Title: " + result[0])
#     print("Url: " + result[1])

from bs4 import BeautifulSoup
import requests
import re
for n, url in enumerate(urllist):
    print(n, url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.get_text()
    wordlist = [
        i for i, item in enumerate(text.split()) if re.search('student', item)
    ]
    for n in wordlist:
        print(' '.join(text.split()[n - 8:n + 8]))
