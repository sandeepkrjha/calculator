import tweepy
consumer_key= '93haMQgoxt7jf51Ri0pvSLzZ8'
consumer_secret= 'mjLL7nIfNJU9Lf2fimwcFaZeqBIZCv0f2tBDydJUpcE5n9C1uO'
access_token= '305550579-fuw9MLIpjN5iQxA4ogdxISeN0hCfnPfZ6DqnxjL5'
access_token_secret='UOGynAnf6iYA9EXYrCn00N3HBHLn88NVfIo7l913fWqSD'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status('hello everyone! Good Night!')