import json
import sys
import time
from tweepy import OAuthHandler

class TwitterUtils(object):

    def __init__(self):
        self.consumer_key = "IAPzxuI8u5X9yBbAMso7Qy0T8"
        self.consumer_secret = "cDrDQHlZ0EVlN6r8GysopLLsN8cHfo4KUSjX0PS8acUf38Je0Q"
        self.access_token = "866712289876992001-YAoj7jEqsS8QpFZWn0J0S8VydWMtrBU"
        self.access_token_secret = "rGgAQzVLFN6GfYQVwH4aIyGqpQQIqhxqSu2x2jjLJuVtX"
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)