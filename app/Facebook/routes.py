from fastapi import APIRouter, HTTPException
from app.Facebook.services import upload_online_image_to_facebook, upload_video_to_facebook, upload_local_image_to_facebook


router = APIRouter()


@router.post("/online/post-to-facebook", tags=["Facebook"])
def post_to_facebook(caption: str, image_url: str):
    return upload_online_image_to_facebook(image_url, caption) 
   
@router.post("/local/post-to-facebook", tags=["Facebook"])
def post_to_facebook(caption: str, image_path: str):
    return upload_local_image_to_facebook(image_path, caption)    



@router.post("/post-to-facebook-video", tags=["Facebook"])
def post_to_facebook_video(description: str, video_url: str = None, video_path: str = None):
    return upload_video_to_facebook(video_url, video_path, description)



# @router.post("/post", tags=["Facebook"])
# def post():
#     return posting()