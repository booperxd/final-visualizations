from twitter import *
from twitter import oauth


t = Twitter(auth=OAuth("4825730011-yzrM5K96EYBrggIHqCaUeGNmbpUXkYsds4dv3oo",
"hKEa8kVIbMU0QQhHX3ffmSsbEDuJUWxWsOCdLFqy7KJUj",
"dB3bFw9FaHZZIPzblZiVWQFpF",
"LqvaHy4okTp6Gw8FlhWsV3lIqY68qsBIPLWYfY0zZ6fNTZLuFB"))

result = t.geo.search(query='USA', granularity = 'country', count = 20)
place_id = result['result']['places'][0]['id']

result = t.search.tweets(q='place:%s' % place_id)
result = t.search.tweets(q="\"TSLA\"")
for tweet in result['statuses']:
    print((tweet['text'].encode('utf-8')))
    if (tweet['place']['name']):        
        print(tweet['place']['name'])
    #else: print("Undefined place")