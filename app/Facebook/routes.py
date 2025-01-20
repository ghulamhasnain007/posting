from fastapi import APIRouter, HTTPException
from app.Facebook.services import upload_image_to_facebook, upload_video_to_facebook


router = APIRouter()

@router.post("/post-to-facebook", tags=["Facebook"])
def post_to_facebook(caption: str = None, image_url: str = None, image_path: str = None):
    return upload_image_to_facebook(image_url, image_path, caption)    

# @router.post("/post-to-facebook", tags=["Facebook"])
# def post_to_facebook(image_url: str, caption: str = None):
#     return upload_image_to_facebook(image_url, caption)

@router.post("/post-to-facebook-video", tags=["Facebook"])
def post_to_facebook_video(description: str, video_url: str = None, video_path: str = None):
    return upload_video_to_facebook(video_url, video_path, description)