from fastapi import APIRouter, HTTPException
from app.Facebook.services import upload_online_image_to_facebook, upload_local_image_to_facebook, upload_local_video_to_facebook, upload_online_video_to_facebook


router = APIRouter()


@router.post("/post/online-image", tags=["Facebook"])
def post_to_facebook(caption: str, image_url: str):
    return upload_online_image_to_facebook(image_url, caption) 
   
@router.post("/post/local-image", tags=["Facebook"])
def post_to_facebook(caption: str, image_path: str):
    return upload_local_image_to_facebook(image_path, caption)    



@router.post("/post/local-video", tags=["Facebook"])
def post_to_facebook_video(description: str, video_path: str = None):
    return upload_local_video_to_facebook(video_path, description)


@router.post("/post/online-video", tags=["Facebook"])
def post_to_facebook_video(description: str, video_url: str = None):
    return upload_online_video_to_facebook(video_url, description)



# @router.post("/post", tags=["Facebook"])
# def post():
#     return posting()