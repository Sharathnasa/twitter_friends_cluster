import oauth2 as oauth
import json
import time

# replace with your keys/owner ID/etc.
conskey = 'IAPzxuI8u5X9yBbAMso7Qy0T8'
conssecret = 'cDrDQHlZ0EVlN6r8GysopLLsN8cHfo4KUSjX0PS8acUf38Je0Q'
token = '866712289876992001-YAoj7jEqsS8QpFZWn0J0S8VydWMtrBU'
tokensecret = 'rGgAQzVLFN6GfYQVwH4aIyGqpQQIqhxqSu2x2jjLJuVtX'
owner = ''
ownerID = ''


consumer = oauth.Consumer(key=conskey, secret=conssecret)
access_token = oauth.Token(key=token, secret=tokensecret)
client = oauth.Client(consumer, access_token)

# get list of followers for Hillary Clinton
follow = "https://api.twitter.com/1.1/followers/ids.json?screen_name=HillaryClinton&count=5000"
response, data = client.request(follow)
tweets = json.loads(data.decode('utf-8'))
print(tweets)
with open ('HillaryClintonFollowers.txt', 'w') as file1:
    json.dump(tweets['ids'], file1)

# get list of followers for Ezekiel Elliot
follow = "https://api.twitter.com/1.1/followers/ids.json?screen_name=EzekielElliott&count=5000"
response, data = client.request(follow)
tweets = json.loads(data.decode('utf-8'))
with open ('EzekielElliottFollowers.txt', 'w') as file2:
    json.dump(tweets['ids'], file2)

# get list of followers for Jimmy Fallon
follow = "https://api.twitter.com/1.1/followers/ids.json?screen_name=nytimes&count=5000"
response, data = client.request(follow)
tweets = json.loads(data.decode('utf-8'))
with open ('NYTimesFollowers.txt', 'w') as file3:
    json.dump(tweets['ids'], file3)