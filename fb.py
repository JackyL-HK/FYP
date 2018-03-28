import time
import facebook
startTime = time.time()

# Permanent Access Token - 2018FYP
# Use with care
token = "---"
graph = facebook.GraphAPI(access_token=token, version=2.7)
id_list = [
    105259197447, 355665009819, 128807942654, 363144660073, 163027013712125,
    116178588425696, 1178706375559427, 835266909851002, 273813022746352,
    348624828219, 218904028237369, 483207852048511
]
comments_list = []
for a, idno in enumerate(id_list):
    page = graph.get_object(id=str(idno), fields='name,id,posts.limit(50)')
    print(page['name'], page['id'])
    posts_id = [page['posts']['data'][n]['id'] for n in range(50)]
    posts_id
    posts = graph.get_objects(
        posts_id,
        fields=
        'name,created_time,message,link,picture,shares,comments.limit(10), reactions.type(LIKE).limit(0).summary(total_count).as(reactions_like),reactions.type(LOVE).limit(0).summary(total_count).as(reactions_love),reactions.type(WOW).limit(0).summary(total_count).as(reactions_wow),reactions.type(HAHA).limit(0).summary(total_count).as(reactions_haha),reactions.type(SAD).limit(0).summary(total_count).as(reactions_sad),reactions.type(ANGRY).limit(0).summary(total_count).as(reactions_angry),reactions.type(THANKFUL).limit(0).summary(total_count).as(reactions_thankful)'
    )

    for b, n in enumerate(posts_id):
        print('\n###{}'.format(b))
        if 'name' in posts[n]: print('name', posts[n]['name'])
        if 'message' in posts[n]: print('message', posts[n]['message'])
        print('vvvvIDvvvv')
        print(posts[n]['id'])
        print('created_time', posts[n]['created_time'])
        if 'link' in posts[n]: print('link', posts[n]['link'])
        if 'picture' in posts[n]: print('picture', posts[n]['picture'])
        if 'share' in posts[n]: print('shares', posts[n]['shares']['count'])
        sum = posts[n]['reactions_angry']['summary']['total_count'] + posts[n]['reactions_haha']['summary']['total_count'] + posts[n]['reactions_like']['summary']['total_count'] + posts[n]['reactions_love']['summary']['total_count'] + posts[n]['reactions_sad']['summary']['total_count'] + posts[n]['reactions_wow']['summary']['total_count']
        index = posts[n]['reactions_angry']['summary']['total_count'] * (
            -1
        ) / sum + posts[n]['reactions_haha']['summary']['total_count'] * (
            1) / sum + posts[n]['reactions_like']['summary']['total_count'] * (
                0
            ) / sum + posts[n]['reactions_love']['summary']['total_count'] * (
                1
            ) / sum + posts[n]['reactions_sad']['summary']['total_count'] * (
                -1
            ) / sum + posts[n]['reactions_wow']['summary']['total_count'] * (
                0) / sum

        print(index)
        print('^^^^INDEX^^^^')
        print('angry',
              posts[n]['reactions_angry']['summary']['total_count'])  # -1
        print('haha',
              posts[n]['reactions_haha']['summary']['total_count'])  # 1
        print('like',
              posts[n]['reactions_like']['summary']['total_count'])  # 0
        print('love',
              posts[n]['reactions_love']['summary']['total_count'])  # 1
        print('sad', posts[n]['reactions_sad']['summary']['total_count'])  # -1
        print('wow', posts[n]['reactions_wow']['summary']['total_count'])  # 0
        if 'comments' in posts[n]:
            # print([posts[n]['comments']['data'][m]['message'] for m in range(len(posts[n]['comments']['data']))])
            comments_list.extend([
                posts[n]['comments']['data'][m]['message']
                for m in range(len(posts[n]['comments']['data']))
            ])

print("Time used:", (time.time() - startTime))
