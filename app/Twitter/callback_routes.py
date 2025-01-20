from fastapi import APIRouter, Request
import tweepy
from app.config import TWITTER_CLIENT_ID, TWITTER_CLIENT_SECRET, TWITTER_REDIRECT_URI
import os

router = APIRouter()

# TWITTER_CLIENT_ID = os.getenv("TWITTER_CLIENT_ID")
# TWITTER_CLIENT_SECRET = os.getenv("TWITTER_CLIENT_SECRET")
# TWITTER_REDIRECT_URI = "http://localhost:8000/auth/callback"

@router.get("/")
def twitter_callback(request: Request, code: str):
    try:
        oauth2_user_handler = tweepy.OAuth2UserHandler(
            TWITTER_CLIENT_ID,
            TWITTER_CLIENT_SECRET,
            TWITTER_REDIRECT_URI
        )

        access_token = oauth2_user_handler.fetch_token(code)
        
        return {"access_token": access_token}
    
    except Exception as e:
        return {"error": str(e)}
