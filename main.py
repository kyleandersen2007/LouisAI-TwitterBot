import tweepy
import time
import openai

api_key = "API_KEY"
api_secret = "API_SECRETKEY"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"
bearer_token = "BEARER_TOKEN"

openai.api_key = "OPENAIKEY"
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)

api = tweepy.API(auth)

def GenerateGPT3Response():
    prompt = "Generate a response to a mention."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text

def postTweet():
    tweetPost = GenerateGPT3Response()
    client.create_tweet(text=tweetPost)

while True:
    postTweet()
    time.sleep(600)
