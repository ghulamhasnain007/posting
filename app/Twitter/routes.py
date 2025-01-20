from fastapi import APIRouter, Depends, HTTPException, Request
from app.Twitter.services import post_tweet_text, post_tweet_with_image
import tweepy
from app.config import TWITTER_REDIRECT_URI, TWITTER_CLIENT_ID, TWITTER_CLIENT_SECRET

router = APIRouter()

@router.post("/post/tweets", tags=["Twitter"])
def post_tweet(tweet_text: str):
    return post_tweet_text(tweet_text)

# TWITTER_CLIENT_ID = os.getenv("TWITTER_CLIENT_ID")
# TWITTER_CLIENT_SECRET = os.getenv("TWITTER_CLIENT_SECRET")
# TWITTER_REDIRECT_URI = "http://localhost:8000/callback"  # Change as per your deployment

@router.get("/twitter/auth")
def get_twitter_auth_url():
    oauth2_user_handler = tweepy.OAuth2UserHandler(
        TWITTER_CLIENT_ID,
        TWITTER_CLIENT_SECRET,
        TWITTER_REDIRECT_URI,
        scope=["tweet.read", "tweet.write", "users.read", "offline.access"],  # Required Scopes
    )
    
    authorization_url = oauth2_user_handler.get_authorization_url()
    
    return {"authorization_url": authorization_url}


@router.post("/post/images")
def post_image(tweet_text, image_path):
    return post_tweet_with_image(tweet_text, image_path)



