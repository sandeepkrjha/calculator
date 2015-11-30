Using twitter API, we can update status and do some more exciting things.

For that , many libraries are there . You can visit [twitter libraries](https://dev.twitter.com/overview/api/twitter-libraries).

I have used tweepy which is a python library for the same purpose.
```python
pip install tweepy

```
you can also visit http://pythoncentral.io/introduction-to-tweepy-twitter-for-python/ for more help.

As shown in the code you need four things.
 * Consumer_key
 * Consumer_key_secret
 * access_token
 * access_token_secret
For these things you need to create an app [here](https://apps.twitter.com/).

Fill the necessary details and you will get consumer_key and consumer_key_secret.
To get rest of the  two scroll down and you will see **create access tokens** .
Now you will get all four things. Put them in this code.

```python
import tweepy
consumer_key= '************************'
consumer_secret= '******************************************'
access_token= '********************************************'
access_token_secret='**************************************'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status('hello everyone!')
```
and you are good to go.! 
Happy coding. Cheers!