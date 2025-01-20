import tweepy
from app.config import TWITTER_ACCESS_TOKEN, TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_SECRET, TWITTER_CLIENT_ID, TWITTER_CLIENT_SECRET, TWIITER_BEARER_TOKEN
from app.utils.twitter_util import verifyCredientials



"""Client( \
        bearer_token=None, consumer_key=None, consumer_secret=None, \
        access_token=None, access_token_secret=None, *, return_type=Response, \
        wait_on_rate_limit=False \
    )"""

def post_tweet_text(tweet_text):
    try:
        client = tweepy.Client(
            consumer_key=TWITTER_API_KEY,
            consumer_secret=TWITTER_API_SECRET,
            access_token=TWITTER_ACCESS_TOKEN,
            access_token_secret=TWITTER_ACCESS_SECRET
        )
        
        response = client.create_tweet(text=tweet_text)
        return {"message": "Tweet posted successfully!", "tweet_id": response.data["id"]}
    
    except Exception as e:
        return {"error": str(e)}


def post_tweet_with_image(tweet_text, image_path):
    try:
        # Authenticate using OAuth 1.0a (required for media uploads)
        auth = tweepy.OAuth1UserHandler(
            TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
        )
        api = tweepy.API(auth)

        # Step 1: Upload the image
        media = api.media_upload(image_path)

        # Step 2: Post a tweet with the uploaded image
        tweet = api.update_status(status=tweet_text, media_ids=[media.media_id])

        return {"message": "Tweet posted successfully!", "tweet_id": tweet.id}
    
    except Exception as e:
        return {"error": str(e)}
