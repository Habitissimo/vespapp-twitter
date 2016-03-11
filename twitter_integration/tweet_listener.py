
import tweepy
import requests
import shutil
import json


class TweetListener(tweepy.StreamListener):
    

    def __init__(self, tweet):
        self.tweet = tweet
        self.url = 'http://web-1.avispamientoweb.d28e17c3.cont.dockerapp.io/api'


    def on_data(self, data):
        # Twitter returns data in JSON format
        tweet = json.loads(data)
            
        if not tweet['in_reply_to_status_id']:  # If tweet is not a reply
            if "extended_entities" in tweet and "media" in tweet['extended_entities']:
                is_photo = True
                for media_object in tweet['extended_entities']['media']:
                    if media_object['type'] != 'photo':
                        is_photo = False
                        break

                if is_photo:
                    payload = {'type': 0}
                    payload['free_text'] = tweet['text'].encode('ascii', 'ignore')
                    if tweet['place']:
                        payload['lat'] = tweet['place']['bounding_box']['coordinates'][0][0][1]
                        payload['lng'] = tweet['place']['bounding_box']['coordinates'][0][0][0]

                    id_sighting = requests.post(self.url + '/sightings/', data=payload)
                    print(id_sighting.text)

                    # Reply the tweet
                    #self.tweet.reply(tweet['user']['screen_name'], "hola", tweet['id_str'])

                    i = 0
                    for media_object in tweet['extended_entities']['media']:
                        image_content = media_object['media_url_https']

                        response = requests.get(image_content, stream=True)
                        file_name = tweet['user']['screen_name'] + str(i) + '.jpg'
                        with open('../images/' + file_name, 'wb+') as out_file:
                            shutil.copyfileobj(response.raw, out_file)
                            r = requests.post(self.url + '/sightings/' + id_sighting.text + '/photos', files={file_name: out_file})
                            print(r.text)

                        del response
                        i = i + 1

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

        return True


    def on_error(self, status):
        print (status)