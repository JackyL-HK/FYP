from instagram.client import InstagramAPI

access_token = "265875095.4aa6d97.76c34fbe0dc7410b9bc22e31e5dca07e"
client_secret = "2bdca8e2d94d4435b3a8ba8e976a543d"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id="1047918027", count=10)
for media in recent_media:
   print(media.caption.text)

api = InstagramAPI(client_id='4aa6d977fb1a4036af9ff88be154f7f4', client_secret='2bdca8e2d94d4435b3a8ba8e976a543d')
popular_media = api.media_popular(count=20)
for media in popular_media:
    print(media.images['standard_resolution'].url)



    print(api.tag_search("LEGO", 20))
    print(api.tag("LEGO"))
    print(api.tag_recent_media(20, 1000, "LEGO"))

    api.tag_recent_media()


print("done")

from instagram.client import InstagramAPI
import sys

if len(sys.argv) > 1 and sys.argv[1] == 'local':
    try:
        from test_settings import *

        InstagramAPI.host = test_host
        InstagramAPI.base_path = test_base_path
        InstagramAPI.access_token_field = "access_token"
        InstagramAPI.authorize_url = test_authorize_url
        InstagramAPI.access_token_url = test_access_token_url
        InstagramAPI.protocol = test_protocol
    except Exception:
        pass

# Fix Python 2.x.
try:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')
except (ImportError, AttributeError):
    pass

client_id = input("Client ID: ").strip()
client_secret = input("Client Secret: ").strip()
redirect_uri = input("Redirect URI: ").strip()
raw_scope = input("Requested scope (separated by spaces, blank for just basic read): ").strip()
scope = raw_scope.split(' ')
# For basic, API seems to need to be set explicitly
if not scope or scope == [""]:
    scope = ["basic"]

api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
redirect_uri = api.get_authorize_login_url(scope = scope)

print ("Visit this page and authorize access in your browser: "+ redirect_uri)

code = (str(input("Paste in code in query string after redirect: ").strip()))

access_token = api.exchange_code_for_access_token(code)
print ("access token: " )
print (access_token)



from InstagramAPI import InstagramAPI
import simplejson as json
import codecs
from nested_lookup import nested_lookup as nl

# api = InstagramAPI("hoheilau@gmail.com", "h753159o123a567")
if (api.login()):
    api.getSelfUserFeed()  # get self user feed
    print(api.LastJson)  # print last response JSON
    print("Login succes!")
else:
    print("Can't login!")
# api.getHashtagFeed("LEGO")
# print(api.tagFeed("Like4like"))
api.getHashtagFeed("情人節")
# api.tagFeed("like4like")
dump = api.LastJson
with codecs.open('jsontest.txt', 'w+', 'utf8') as f:
    f.write(json.dumps(dump, sort_keys=True, ensure_ascii=False, indent=4*' '))
    # json.dump(dump, f, ensure_ascii=False)
print(json.dumps(dump, sort_keys=True, indent=4 * ' '))

print('\n'.join(nl('text', dump)))

print(dump['text'])





import requests
dump = ''
dump_maxid = ''
dumptext = []
for _ in range(5):
    r = requests.get(
        'https://www.instagram.com/explore/tags/黃子華/?__a=1'.format(
            '&max_id=' + dump_maxid))
    r.status_code
    dump = r.json()
    # print(dump)
    dumptext.extend(nl('text', dump))
    dump_maxid = nl('end_cursor', dump)[0]
    print(dump_maxid)

# with codecs.open('jsontest.txt', 'w+', 'utf8') as f:
# f.write(json.dumps(dump, sort_keys=True, ensure_ascii=False, indent=4*' '))
# f.write(dumptext)
print(dumptext)
print('\n'.join(dumptext))
for i, n in enumerate(dumptext):
    # if "黃子華" in n:
    print(i)




import facebook
token = "EAACEdEose0cBAIjPnFc5hr3SPydNHDdsR7tZBPdUAeL1DnD59LNw2n0MNZAGMCLVbJj299QGdf6UBTT4yoeRfTCqrFCwjkZArsdIQ90YZCEmhIkeumjBrLzk5psw3Bw0PRI5PAc3PeZA1k3BYcoxbbfqbMZB8LJcksPErACuxZBjIKMyqJTZCzMMLiMmvembACI9gORZCHD3Bk0EoJxrrARkV"
graph = facebook.GraphAPI(access_token = token, version=2.7)
page = graph.get_object(id='105259197447', fields='name,id,posts.limit(50)')
print(page['name'], page['id'])
# posts = page['posts']['data']
posts_id = [page['posts']['data'][n]['id'] for n in range(50)]
posts_id
posts = graph.get_objects(posts_id, fields='name,created_time,message,link,picture,shares,comments.limit(10), reactions.type(LIKE).limit(0).summary(total_count).as(reactions_like),reactions.type(LOVE).limit(0).summary(total_count).as(reactions_love),reactions.type(WOW).limit(0).summary(total_count).as(reactions_wow),reactions.type(HAHA).limit(0).summary(total_count).as(reactions_haha),reactions.type(SAD).limit(0).summary(total_count).as(reactions_sad),reactions.type(ANGRY).limit(0).summary(total_count).as(reactions_angry),reactions.type(THANKFUL).limit(0).summary(total_count).as(reactions_thankful)')
posts
for n in posts_id:
    print('\n', 'id', posts[n]['id'])
    print('created_time', posts[n]['created_time'])
    print('link', posts[n]['link'])
    print('picture', posts[n]['picture'])
    print('shares', posts[n]['shares'])
    # print('name', posts[n]['name'])
    print('message', posts[n]['message'])
    print('angry', posts[n]['reactions_angry']['summary']['total_count']) # -1
    print('haha', posts[n]['reactions_haha']['summary']['total_count']) # 1
    print('like', posts[n]['reactions_like']['summary']['total_count']) # 0
    print('love', posts[n]['reactions_love']['summary']['total_count']) # 1
    print('sad', posts[n]['reactions_sad']['summary']['total_count']) # -1
    print('wow', posts[n]['reactions_wow']['summary']['total_count']) # 0
    print('comments', [posts[n]['comments']['data'][m]['message'] for m in range(len(posts[n]['comments']['data']))])

com = graph.get_object(posts[n]['id'], fields='')

print(json.dumps(post, sort_keys=True, ensure_ascii=False, indent=4*' '))



print(comments_list)
print('\n'.join(comments_list))

from collections import Counter
c = Counter(''.join(comments_list))
# c.most_common(50)
print('撚', c['撚'])
print('屌', c['屌'])
print('鳩', c['鳩'])

print(set(''.join(comments_list)))

comments_list

import jieba
sent = ''.join(comments_list)
seg_list = jieba.cut(sent)
print(', '.join(seg_list))

from snownlp import SnowNLP
s = SnowNLP(sent)
print(s.words)
# print(s.tags)
print(s.sentiments)
print(s.keywords(3))
print(s.summary(3))

print("value")

import csv
with open("009.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    # for row in spamreader:
    # print(', '.join(row))
    print([*map(float, list(zip(*spamreader))[0])])
    # print([*map(float,list(zip(*spamreader))[1])])


from pytrends.request import TrendReq
import pandas as pd
pytrends = TrendReq(hl='zh-TW',geo='HK')
# pytrends.interest_over_time()

trending_searches_df = pytrends.trending_searches(pn='p10')
print(trending_searches_df)

#         title                                       titleLinkUrl  \
# 0        Glay                     //www.google.com/search?q=Glay
# 1         黃子華  //www.google.com/search?q=%E9%BB%83%E5%AD%90%E...
# 2      悍戰太平洋2  //www.google.com/search?q=%E6%82%8D%E6%88%B0%E...
# 3         髒髒包  //www.google.com/search?q=%E9%AB%92%E9%AB%92%E...
# 4       中英街一號  //www.google.com/search?q=%E4%B8%AD%E8%8B%B1%E...
# 5       地球一小時  //www.google.com/search?q=%E5%9C%B0%E7%90%83%E...
# 6          F1                       //www.google.com/search?q=F1
# 7          派錢       //www.google.com/search?q=%E6%B4%BE%E9%8C%A2
# 8         薪俸稅  //www.google.com/search?q=%E8%96%AA%E4%BF%B8%E...
# 9         貿易戰  //www.google.com/search?q=%E8%B2%BF%E6%98%93%E...
# 10     刑事偵緝檔案  //www.google.com/search?q=%E5%88%91%E4%BA%8B%E...
# 11   派 4000 蚊  //www.google.com/search?q=%E6%B4%BE+4000+%E8%9...
# 12       政府派錢  //www.google.com/search?q=%E6%94%BF%E5%BA%9C%E...
# 13         退稅       //www.google.com/search?q=%E9%80%80%E7%A8%85
# 14  政府 派 4000  //www.google.com/search?q=%E6%94%BF%E5%BA%9C+%...
# 15        久石讓  //www.google.com/search?q=%E4%B9%85%E7%9F%B3%E...
# 16        古巨基  //www.google.com/search?q=%E5%8F%A4%E5%B7%A8%E...
# 17        羅青浩  //www.google.com/search?q=%E7%BE%85%E9%9D%92%E...
# 18        古天樂  //www.google.com/search?q=%E5%8F%A4%E5%A4%A9%E...
# 19        張紫妍  //www.google.com/search?q=%E5%BC%B5%E7%B4%AB%E...
# 20        Exo                      //www.google.com/search?q=Exo
# 21        張景淳  //www.google.com/search?q=%E5%BC%B5%E6%99%AF%E...
# 22        岑麗香  //www.google.com/search?q=%E5%B2%91%E9%BA%97%E...
# 23        安以軒  //www.google.com/search?q=%E5%AE%89%E4%BB%A5%E...
# 24        黃大仙  //www.google.com/search?q=%E9%BB%83%E5%A4%A7%E...
# 25      4000蚊            //www.google.com/search?q=4000%E8%9A%8A
# 26       葵涌廣場  //www.google.com/search?q=%E8%91%B5%E6%B6%8C%E...
