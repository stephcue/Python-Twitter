

import os
import tweepy

def login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret):
    consumer_key = "[Your Consumer Key]"
    consumer_secret = "[Your Consumer Key Secret]"
    access_token = "[Your Access Token]"
    access_token_secret = "[Your Access Token Secret]"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    ret = {}
    ret['api'] = api
    ret['auth'] = auth
    return api

def SendTweet():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''



    MessList=["I love Star Wars! ","I had pizza for dinner! ","Fleetwood Mac rocks! "]
    for i in range (0,len(MessList)):
        message =MessList[i]+str(i)
        print(message)

        api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret)

        ret = api.update_status(status=message)


def RemoveTweet():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret )
    timeline = api.user_timeline(count=20)
    print("Found %d" % (len(timeline)))
    print(timeline)
    for t in timeline:
        api.destroy_status(t.id)

def Follow():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret)

    api.create_friendship('realDonaldTrump')
    api.create_friendship('POTUS')
    friends = api.friends()

    for friend in friends:
        print(friend.name)


def UnFollow():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret)

    api.destroy_friendship('realDonaldTrump')
    api.destroy_friendship('POTUS')
    friends = api.friends()

    for friend in friends:
        print(friend.name)

def ReTweet():
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    api = login_to_twitter(consumer_key, consumer_secret, access_token, access_token_secret)

    timeline = api.user_timeline(screen_name='POTUS', count=5)
    print("Found %d" % (len(timeline)))
    print(timeline)
    for t in timeline:
        api.retweet(t.id)

if __name__ == '__main__':
    SendTweet()
    Follow()
    ReTweet()
    RemoveTweet()
    UnFollow()
