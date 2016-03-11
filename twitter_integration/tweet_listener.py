
import tweepy
import requests
import shutil
import json


class TweetListener(tweepy.StreamListener):
    

    def __init__(self, tweet):
        self.tweet = tweet


    def on_data(self, data):
        # Twitter returns data in JSON format
        tweet = json.loads(data)
            
        if "extended_entities" in tweet and "media" in tweet['extended_entities']:
            if not tweet['in_reply_to_status_id']:  # If tweet is not a reply
                i = 0
                for media_object in tweet['extended_entities']['media']:
                    if media_object['type'] == 'photo':
                        image_content = media_object['media_url_https']

                        response = requests.get(image_content, stream=True)
                        with open('../images/' + tweet['user']['screen_name'] + str(i) + '.jpg', 'wb') as out_file:
                            shutil.copyfileobj(response.raw, out_file)
                        del response
                        i = i + 1

                # Reply the tweet
                #self.tweet.reply(tweet['user']['screen_name'], "hola", tweet['id_str'])

                print(tweet['in_reply_to_status_id'])
                print(tweet['id_str'])
                print(tweet['created_at'])
                print(tweet['user']['name'])
                print(tweet['user']['screen_name'])
                if tweet['place']:
                    print(tweet['place']['name'])
                    print(tweet['place']['country'])
                    print(tweet['place']['bounding_box']['coordinates'][0][0][0])  # Longitude
                    print(tweet['place']['bounding_box']['coordinates'][0][0][1])  # Latitude
                print(tweet['text'].encode('ascii', 'ignore'))
                print("")
        else:
            print("no photo")

        return True


    def on_error(self, status):
        print (status)