import tweepy

def verifyCredientials(api_key, api_secret, access_token, access_secret):
    try:
        auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
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



