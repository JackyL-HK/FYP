import time
import facebook
import json
from IPython.display import JSON
import requests
startTime = time.time()
# https://developers.facebook.com/tools/explorer/
# /schools.secrets/
# 179264152235008
token = "EAACEdEose0cBAOWRaxsjeeu5Ux6wBmvLOdppSjjgdPtiEuKtTjtFVdPsIEV8BJ1q8JAy6eP9Tg2rCiiVZAeqWots32SFnp9aQwi58D6ifupUlZCh93mdM2EYyvvNgW1ZA1A1F56CA6D6hkYruGT8ZBYqCjzbiItrhZArwmUnnMN7uAsGJMYrZCPl0qHXZBmN7BAjACAYeSIq5JQ9bvZA4CQE"
graph = facebook.GraphAPI(access_token=token, version=2.12)
id_list = [179264152235008]
comments_list = []

# for a, idno in enumerate(id_list):
page = graph.get_object(
    id=str(id_list[0]), fields='name,id,posts.limit(100){name,id,created_time,message,full_picture,permalink_url,shares,reactions.type(LIKE).limit(0).summary(total_count).as(r_like),reactions.type(LOVE).limit(0).summary(total_count).as(r_love),reactions.type(WOW).limit(0).summary(total_count).as(r_wow),reactions.type(HAHA).limit(0).summary(total_count).as(r_haha),reactions.type(SAD).limit(0).summary(total_count).as(r_sad),reactions.type(ANGRY).limit(0).summary(total_count).as(r_angry),comments.limit(1000){id,message,reactions.type(LIKE).limit(0).summary(total_count).as(r_like),reactions.type(LOVE).limit(0).summary(total_count).as(r_love),reactions.type(WOW).limit(0).summary(total_count).as(r_wow),reactions.type(HAHA).limit(0).summary(total_count).as(r_haha),reactions.type(SAD).limit(0).summary(total_count).as(r_sad),reactions.type(ANGRY).limit(0).summary(total_count).as(r_angry)}}')
next = page['posts']['paging']['next']
for _ in range(9):
    next_json = requests.get(next).json()
    next = next_json['paging']['next']
    for n in next_json['data']:
        page['posts']['data'].append(n)

print(len(page['posts']['data']))

print("Time used:", (time.time() - startTime))
    # posts.limit(1000) - AT MOST
    # comments.limit(150) - AT MOST
    # print("posts+comments(100x10)", 12.228018045425415*10) # tested: 127.85498380661011
    # print("posts(1000)+comments(100x10)", 16.739154815673828+10.867603063583374*10) # 125.41518545150757
with open('fb_parsing.json', 'w+', encoding='utf-8') as fp:
    json.dump(page, fp)

with open('fb_parsing.json', 'r', encoding='utf-8') as fp:
    page = json.load(fp)

    for b, n in enumerate(posts_id):
        print('\n###{}'.format(b))
        if 'name' in posts[n]:
            print('name', posts[n]['name'])
        if 'message' in posts[n]:
            print('message', posts[n]['message'])
        print('vvvvIDvvvv')
        print(posts[n]['id'])
        print('created_time', posts[n]['created_time'])
        if 'link' in posts[n]:
            print('link', posts[n]['link'])
        if 'picture' in posts[n]:
            print('picture', posts[n]['picture'])
        if 'share' in posts[n]:
            print('shares', posts[n]['shares']['count'])
        sum = posts[n]['r_angry']['summary']['total_count'] + posts[n]['r_haha']['summary']['total_count'] + posts[n]['r_like']['summary']['total_count'] + \
            posts[n]['r_love']['summary']['total_count'] + \
            posts[n]['r_sad']['summary']['total_count'] + \
            posts[n]['r_wow']['summary']['total_count']
        index = posts[n]['r_angry']['summary']['total_count'] * (
            -1
        ) / sum + posts[n]['r_haha']['summary']['total_count'] * (
            1) / sum + posts[n]['r_like']['summary']['total_count'] * (
                0
            ) / sum + posts[n]['r_love']['summary']['total_count'] * (
                1
            ) / sum + posts[n]['r_sad']['summary']['total_count'] * (
                -1
            ) / sum + posts[n]['r_wow']['summary']['total_count'] * (
                0) / sum

        print(index)
        print('^^^^INDEX^^^^')
        print('angry',
              posts[n]['r_angry']['summary']['total_count'])  # -1
        print('haha',
              posts[n]['r_haha']['summary']['total_count'])  # 1
        print('like',
              posts[n]['r_like']['summary']['total_count'])  # 0
        print('love',
              posts[n]['r_love']['summary']['total_count'])  # 1
        print('sad', posts[n]['r_sad']['summary']['total_count'])  # -1
        print('wow', posts[n]['r_wow']['summary']['total_count'])  # 0
        if 'comments' in posts[n]:
            # print([posts[n]['comments']['data'][m]['message'] for m in range(len(posts[n]['comments']['data']))])
            comments_list.extend([
                posts[n]['comments']['data'][m]['message']
                for m in range(len(posts[n]['comments']['data']))
            ])

print("Time used:", (time.time() - startTime))

JSON(data=open('fb_parsing.json', 'r', encoding='utf-8').read())
