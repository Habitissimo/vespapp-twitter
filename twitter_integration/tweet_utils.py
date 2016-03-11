
class TweetUtils:

    @classmethod
    def is_valid(cls, tweet):
        is_photo = False
        if not tweet['in_reply_to_status_id']:  # If tweet is not a reply
            if "extended_entities" in tweet and "media" in tweet['extended_entities']:
                is_photo = True
                for media_object in tweet['extended_entities']['media']:
                    if media_object['type'] != 'photo':
                        is_photo = False
                        break
        return is_photo

