import tweepy
import requests
import json
from urllib.request import urlopen
import tweet_utils


class TweetListener(tweepy.StreamListener):

    def __init__(self, tweet):
        self.tweet = tweet
        self.url = 'http://vespa.habitissimo.party/api'

    def on_data(self, data):
        # Twitter returns data in JSON format
        tweet = json.loads(data)

        if tweet_utils.TweetUtils.is_valid(tweet):

            payload = {
                'type': 0,
                'source': 'twitter',
                'free_text': tweet['text'].encode('ascii', 'ignore')
            }
            # Optional arguments
            if tweet['place']:
                payload['lat'] = tweet['place']['bounding_box']['coordinates'][0][0][1]
                payload['lng'] = tweet['place']['bounding_box']['coordinates'][0][0][0]

            # Create sighting
            response = requests.post(self.url + '/sightings/', data=payload)
            sighting = json.loads(response.text)
            sighting_id = sighting['id']

            # Reply the tweet
            nick_name = tweet['user']['screen_name']
            text = 'Gracias por subir la foto'
            in_reply_to_status_id = tweet['id_str']
            self.tweet.reply(nick_name, text, in_reply_to_status_id)

            # Add photos
            for media_object in tweet['extended_entities']['media']:
                file_path = media_object['media_url_https']
                open_file = urlopen(file_path)
                bytes = open_file.read()
                requests.post(self.url + '/sightings/' + str(sighting_id) + '/photos/', files={'file': bytes})

        return True

    def on_error(self, status):
        print (status)
