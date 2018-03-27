import simplejson as json
import codecs
from nested_lookup import nested_lookup as nl
import requests

hashtagToSearch = 'TGIF'
searchPage = 5


dump=''
dump_maxid = '';
dumptext = []

for _ in range(searchPage):
    r = requests.get('https://www.instagram.com/explore/tags/{}/?__a=1'.format(hashtagToSearch, '&max_id='+dump_maxid))
    r.status_code
    dump = r.json()
    dumptext.extend(nl('text', dump))
    dump_maxid = nl('end_cursor', dump)[0]
    print(dump_maxid)

# with codecs.open('jsontest.txt', 'w+', 'utf8') as f:
    # f.write(json.dumps(dump, sort_keys=True, ensure_ascii=False, indent=4*' '))
    # f.write(dumptext)
# print(dumptext)
# print('\n'.join(dumptext))
for i,n in enumerate(dumptext):
    # print(i)
    print(n.split('\n'))
