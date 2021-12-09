import pandas as pd
import twitter
import os
import json

#Authorize API with generated keys

def oauth_login():
    #Your keys go here
    CONSUMER_KEY = "dB3bFw9FaHZZIPzblZiVWQFpF"
    CONSUMER_SECRET = "LqvaHy4okTp6Gw8FlhWsV3lIqY68qsBIPLWYfY0zZ6fNTZLuFB"
    OAUTH_TOKEN = "4825730011-yzrM5K96EYBrggIHqCaUeGNmbpUXkYsds4dv3oo"
    OAUTH_TOKEN_SECRET = "hKEa8kVIbMU0QQhHX3ffmSsbEDuJUWxWsOCdLFqy7KJUj"
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

def appendTweets(filename, results):
    if os.path.exists(filename):
        with open(filename, 'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_dat3a with file_data
            file_data += results
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 1)
    else:
        with open(filename, 'w+') as file:
            # convert back to json.
            json.dump(results, file, indent = 1)

t = oauth_login()

appendTweets('tweets_from_elon.json', t.statuses.user_timeline(screen_name='elonmusk', count = 300))