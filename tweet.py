import tweepy

class Tweet:

	def __init__(self, api):
		self.api = api

	def write(self, message):
		self.api.update_status(message)

	def reply(self, message, in_reply_to_status_id):
		api.update_status(message, in_reply_to_status_id)

