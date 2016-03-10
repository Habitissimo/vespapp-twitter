import tweepy
import tweet_listener

from keys import keys

# Authentication details. To  obtain these visit dev.twitter.com
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']


if __name__ == '__main__':
    t_list = tweet_listener.TweetListener()

    # Create authentication token using our details
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Get API handler
    #api = tweepy.API(auth)

    #print ("Tweeting hello world...")
    #print ("Check https://twitter.com/c4107142 to see the result")

    # Let's tweet something!
    # Since we can't tweet two identical statuses, we'll tweet our time aswell
    #api.update_status('Hello world from tweepy 4!')

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, t_list)
    stream.filter(track=['photo'])