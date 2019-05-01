import json
import tweepy

with open('keys.json') as json_key:  
  data = json.load(json_key)
  consumerAPI = data["Consumer API Key"]
  consumerSecret = data["Consumer API Secret"]
  accessToken = data["Access Token"]
  accessSecret = data["Access Token Secret"]


auth = tweepy.OAuthHandler(consumerAPI, consumerSecret)
auth.set_access_token(accessToken, accessSecret)

api = tweepy.API(auth)

# Me!
me = api.me()

# api.update_status("Hello World!")

friends = api.followers()

print(friends)

# for friend in friends:
#   print(friend)

