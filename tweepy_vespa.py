import tweepy
import json
import tweet
# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'qO2wzYilhvmXsRii2zIw3FM1Z'
consumer_secret = '1YddGeGfM3Wp53NFaGMkvXQwv9ek1colosRXx0nYLiUp72mbE4'
access_token = '707877442795532288-cnU1gAHKCCLRUbVg8q4e3ofzMSSq79b'
access_token_secret = 'apNn6kJu9Rq3W8j6TRAdgw2ZSfBys3uDDlmPNnEEvsSsF'


class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print ('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
        print ('')
        return True

    def on_error(self, status):
        print (status)



if __name__ == '__main__':
    l = StdOutListener()

    # Create authentication token using our details
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Get API handler
    api = tweepy.API(auth)

    tweet = tweet.Tweet(api)
    tweet.reply()    
    stream = tweepy.Stream(auth, l)
    stream.filter(track=[''])