query = "Hong Kong Secondary Student"
# testurl = "http://www.scmp.com/news/hong-kong/education/article/2133086/long-hours-too-much-homework-and-stressed-pupils-there"
testurl = "http://www.scmp.com/news/hong-kong/education/article/2137893/volunteering-gift-keeps-giving-students-cvs"
# urllist = [testurl]
from googlesearch import search, search_news
from textblob import TextBlob
# for url in search("Hong Kong Secondary Student", stop=20):
#     print(url)
# print("==============")
# urllist = list(search_news("Hong Kong Student", stop=50))
# print('\n'.join(urllist))

from bs4 import BeautifulSoup
import requests
import re
# for n,url in enumerate(urllist):
#     print("\n", n, url)
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     text = ' '.join(map(BeautifulSoup.get_text,soup.find_all('p')))
#
#     wordlist = [
#         i for i, item in enumerate(text.split()) if re.search('student', item)
#     ]
#     for n in wordlist:
#         print(' '.join(text.split()[n - 8:n + 8]))
    # print(text)
#
with open("test.txt") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    # print(*map(BeautifulSoup.get_text,soup.find_all('p')))
    testtext = ' '.join(map(BeautifulSoup.get_text,soup.find_all('p')))
    print(testtext)


from wordcloud import WordCloud
# text = open('test.txt').read()
text = testtext
# %matplotlib tk
import matplotlib.pyplot as plt
import cv2

wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
cv2.imshow('wordcloud', wordcloud.to_array())
cv2.waitKey(0)
cv2.destroyAllWindows()
# lower max_font_size
# wordcloud = WordCloud(width=1920, height=1080).generate(text)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()

# for i,n in enumerate(urllist):
#     print(i)