import tweepy
import requests
import shutil
import json


class TweetListener(tweepy.StreamListener):
    def on_data(self, data):
        #avist = avistamientoTweet()

        # Twitter returns data in JSON format - we need to decode it first
        tweet = json.loads(data)

        if ("media") in tweet['entities']:
            if tweet['entities']['media'][0]['type'] == 'photo':
                image_content = tweet['entities']['media'][0]['media_url_https']

                response = requests.get(image_content, stream=True)
                with open('images/' + tweet['user']['screen_name'] + '.jpg', 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response

                print (tweet['id'])
                print (tweet['created_at'])
                print (tweet['user']['name'])
                print (tweet['user']['screen_name'])
                print (tweet['entities']['media'][0]['type'])
                print (tweet['entities']['media'][0]['media_url_https'])
                print (tweet['text'].encode('ascii', 'ignore'))
        else:
            print("non")

                

        #t_write = Tweet()
        #t_write.reply()

        return True

    def on_error(self, status):
        print (status)