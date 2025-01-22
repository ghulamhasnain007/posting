# import tweepy

# def verifyCredientials(api_key, api_secret, access_token, access_secret):
#     try:
#         auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
#         api = tweepy.API(auth, wait_on_rate_limit=True)

#         # Verify Credentials
#         user = api.verify_credentials()
#         if user:
#             print(f"Authenticated as {user.screen_name}")   
#             return api
#         else:
#             print("Authentication failed")
#             return None
#     except Exception as e:
#         print(f"Error in authentication: {e}")
#         return None



import tweepy
from app.config import TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET

# Twitter API credentials
# TWITTER_API_KEY = "your_api_key"
# TWITTER_API_SECRET = "your_api_secret"
# TWITTER_ACCESS_TOKEN = "your_access_token"
# TWITTER_ACCESS_SECRET = "your_access_secret"

def get_twitter_api():
    try:
        auth = tweepy.OAuth1UserHandler(
            TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
        )
        api = tweepy.API(auth, wait_on_rate_limit=True)

        # Verify Credentials
        user = api.verify_credentials()
        if user:
            print(f"Authenticated as {user.screen_name}")   
            return api
        else:
            print("Authentication failed")
            return None
    except Exception as e:
        print(f"Error in authentication: {e}")
        return None
