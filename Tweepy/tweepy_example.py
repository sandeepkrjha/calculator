import time

import urllib.request

import tweepy

def send_to_twitter(message):
	consumer_key= '**********************'
	consumer_secret= '*********************************'
	access_token= '************************************'
	access_token_secret='***********************************'
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	api.update_status('current price is '+str(message))




def get_price():
	page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
	text=page.read().decode("utf8")
	search_=text.find(">$")#we guess that  price will come after  string >$ and try to find its index

	start_=search_+2; # this is beginning of our price string
	end_=start_+4;
	return float(text[start_:end_])

a=input("do u want current price now ? Ener y/n")
if a=='y' or a=='Y':
	send_to_twitter(get_price())
else:
	price=100.0
	while price > 6.0:
		time.sleep(900)
		price=get_price()
	send_to_twitter(price)











