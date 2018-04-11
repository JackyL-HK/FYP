import time
import facebook
import json
from IPython.display import JSON
import requests
from snownlp import SnowNLP
import re


def start():
    global startTime
    startTime = time.time()


def end():
    print("Time used:", (time.time() - startTime))


# https://developers.facebook.com/tools/explorer/
# /schools.secrets/
# 179264152235008
token = "EAACEdEose0cBADxJPwf6I38dEoWxrjUnP353lMnzUaBrTeU9e30VYJIYfSrBoogwDGyaG653fZBI0jFxojMXUk177vHezCPiKptCvYNpBtjzaDn1ZB8TzoX184Sq97Sjb1n8LZAfZCcfMZB7Tg4m7qYuqZA2mOQyuFvZCfO7ozn1i6p5XN6DWdS40BLUfi75y30vxKJ1iSlhT7oVFj9sZCfZB"
graph = facebook.GraphAPI(access_token=token, version=2.12)
id_list = [179264152235008]
comments_list = []

start()
print('Requesting... {}'.format(1))
page = graph.get_object(
    id=str(id_list[0]), fields='name, id, posts.limit(100){name, id, created_time, message, full_picture, shares, reactions.type(LIKE).limit(0).summary(total_count).as(r_like), reactions.type(LOVE).limit(0).summary(total_count).as(r_love), reactions.type(WOW).limit(0).summary(total_count).as(r_wow), reactions.type(HAHA).limit(0).summary(total_count).as(r_haha), reactions.type(SAD).limit(0).summary(total_count).as(r_sad), reactions.type(ANGRY).limit(0).summary(total_count).as(r_angry), comments.limit(1000){id, message, full_picture, reactions.type(LIKE).limit(0).summary(total_count).as(r_like), reactions.type(LOVE).limit(0).summary(total_count).as(r_love), reactions.type(WOW).limit(0).summary(total_count).as(r_wow), reactions.type(HAHA).limit(0).summary(total_count).as(r_haha), reactions.type(SAD).limit(0).summary(total_count).as(r_sad), reactions.type(ANGRY).limit(0).summary(total_count).as(r_angry), comments.limit(1000){id, message, full_picture}}}')
next = page['posts']['paging']['next']
for i in range(9):
    print('Requesting... {}'.format(i+2))
    try:
        next_json = requests.get(next).json()
        next = next_json['paging']['next']
        for n in next_json['data']:
            page['posts']['data'].append(n)
    except KeyError:
        break
end()
print(len(page['posts']['data']))

JSON((page['posts']['data'][0]))

print("Time used:", (time.time() - startTime))

with open('fb_parsing.json', 'w+', encoding='utf-8') as fp:
    json.dump(page, fp)

with open('fb_parsing.json', 'r', encoding='utf-8') as fp:
    page = json.load(fp)

ss_test = []
ss_sent = []
chi_list = ['想死', '想喊', '壓力', '自殺', '攰']
for msg in page['posts']['data']:
    if 'message' in msg:
        ss_test.append(msg['message']) if any(x in msg['message']
                                              for x in chi_list) else ''
ss_test = ' '.join(ss_test)
snlp = SnowNLP(ss_test)
for sent in snlp.sentences:
    # regex: sorry, sor, for, 1999, (,),（,）,「,」,[.],#
    ss_sent.append(re.sub(r'(sorry|sor|for|1999|（|）|\(|\)|「|」|\[.*\]|#)', '', sent, flags=re.IGNORECASE)
                   if any(x in sent for x in chi_list) else '')
for sent in ss_sent:
    if sent:
        s = SnowNLP(sent)
        print(sent, ' | ', s.sentiments)

with open("fbContent.txt", 'w+', encoding='utf-8') as fp:
    fpwrite=[]
    for sent in ss_sent:
        if sent:
            fpwrite.append(sent)
    fp.write('\n'.join(fpwrite))


# page['name']
# page['id']
# page['posts']
# page['posts']['data']
# page['posts']['data'][n]
# page['posts']['data'][n]['name'] / ['id'] / ['created_time'] / \
#     ['message'] / ['full_picture'] / ['permalink_url'] / ['shares']['count']
# page['posts']['data'][n]['r_like']['summary']['total_count']
# page['posts']['data'][n]['r_love']['summary']['total_count']
# page['posts']['data'][n]['r_wow']['summary']['total_count']
# page['posts']['data'][n]['r_haha']['summary']['total_count']
# page['posts']['data'][n]['r_sad']['summary']['total_count']
# page['posts']['data'][n]['r_angry']['summary']['total_count']
# page['posts']['data'][n]['comments']
# page['posts']['data'][n]['comments']['data']
# page['posts']['data'][n]['comments']['data'][m]
# page['posts']['data'][n]['comments']['data'][m]['id'] / ['message'] / ['full_picture']
# page['posts']['data'][n]['comments']['data'][m]['r_like']['summary']['total_count']
# page['posts']['data'][n]['comments']['data'][m]['r_love']['summary']['total_count']
# page['posts']['data'][n]['comments']['data'][m]['r_wow']['summary']['total_count']
# page['posts']['data'][n]['comments']['data'][m]['r_haha']['summary']['total_count']
# page['posts']['data'][n]['comments']['data'][m]['r_sad']['summary']['total_count']
# page['posts']['data'][n]['comments']['data'][m]['r_angry']['summary']['total_count']
# page['posts']['data'][n]['comments']['data'][m]['comments']
# page['posts']['data'][n]['comments']['data'][m]['comments']['data']
# page['posts']['data'][n]['comments']['data'][m]['comments']['data'][p]
# page['posts']['data'][n]['comments']['data'][m]['comments']['data'][p]['id'] / ['message'] / ['full_picture']

# JSON(data=open('fb_parsing.json', 'r', encoding='utf-8').read())
