from fastapi import FastAPI, HTTPException
from app.Instagram.routes import router as instagram_router 
from app.Facebook.routes import router as facebook_router
from app.Linkedin.routes import router as linkedin_router
from app.Twitter.routes import router as twitter_router
from app.Twitter.callback_routes import router as callback_router

app = FastAPI()

app.include_router( instagram_router, prefix="/instagram")

app.include_router( facebook_router, prefix="/facebook")

app.include_router( linkedin_router, prefix="/linkedin")

app.include_router(twitter_router, prefix='/twitter')

app.include_router(callback_router, prefix='/callback')