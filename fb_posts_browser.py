import time
import facebook
import json
from IPython.display import JSON
startTime = time.time()
# https://developers.facebook.com/tools/explorer/
# /schools.secrets/
# 179264152235008
token = "EAACEdEose0cBAFY7ZA49pyDespHJGsjZBXzMpcZCHfHQnxGIKM2pqyEWjg8DtdZACqP4pxx2HCZCUyZAWO1dVIVFZCREHAqCZBTjmgDtKpCVDn4ZATJiGvAzLs9ZCTk5slabj3Fv6ZBKZCJgBGebfnTIsXYYj5mMlIqNbXSZArWnJZCTrZAJfSe0iYZAdtgDBzT54OBgVKgU9nd2Yv6kAFVsC4ueZCmZA1CqY7RgsNPh8ZD"
graph = facebook.GraphAPI(access_token=token, version=2.12)
id_list = [179264152235008]
comments_list = []
##################################
# for a, idno in enumerate(id_list):
page = graph.get_object(
    id=str(idno), fields='name,id,posts.limit(10){name,id,created_time,message,full_picture,permalink_url,shares,reactions.type(LIKE).limit(0).summary(total_count).as(r_like),reactions.type(LOVE).limit(0).summary(total_count).as(r_love),reactions.type(WOW).limit(0).summary(total_count).as(r_wow),reactions.type(HAHA).limit(0).summary(total_count).as(r_haha),reactions.type(SAD).limit(0).summary(total_count).as(r_sad),reactions.type(ANGRY).limit(0).summary(total_count).as(r_angry),comments.limit(1000){id,message,reactions.type(LIKE).limit(0).summary(total_count).as(r_like),reactions.type(LOVE).limit(0).summary(total_count).as(r_love),reactions.type(WOW).limit(0).summary(total_count).as(r_wow),reactions.type(HAHA).limit(0).summary(total_count).as(r_haha),reactions.type(SAD).limit(0).summary(total_count).as(r_sad),reactions.type(ANGRY).limit(0).summary(total_count).as(r_angry)}}')
# print(page['name'], '|', page['id'])
JSON(page)
with open('fb_parsing.json','w',encoding='utf-8') as fp:
    json.dump(page,fp)
##################################
    posts_id = [page['posts']['data'][n]['id'] for n in range(50)]
    posts_id
    posts = graph.get_objects(
        posts_id,
        fields='name,created_time,message,link,picture,shares,comments.limit(10), reactions.type(LIKE).limit(0).summary(total_count).as(r_like),reactions.type(LOVE).limit(0).summary(total_count).as(r_love),reactions.type(WOW).limit(0).summary(total_count).as(r_wow),reactions.type(HAHA).limit(0).summary(total_count).as(r_haha),reactions.type(SAD).limit(0).summary(total_count).as(r_sad),reactions.type(ANGRY).limit(0).summary(total_count).as(r_angry))'
    )

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
