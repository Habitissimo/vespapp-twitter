import tweepy

auth = tweepy.OAuthHandler('qO2wzYilhvmXsRii2zIw3FM1Z', '1YddGeGfM3Wp53NFaGMkvXQwv9ek1colosRXx0nYLiUp72mbE4')
auth.set_access_token('707877442795532288-cnU1gAHKCCLRUbVg8q4e3ofzMSSq79b', 'apNn6kJu9Rq3W8j6TRAdgw2ZSfBys3uDDlmPNnEEvsSsF')

api = tweepy.API(auth)
u = api.update_status('Hey bro!')
print(u)
