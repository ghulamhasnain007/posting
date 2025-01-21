from fastapi import APIRouter, HTTPException
import requests
# from app.Instagram.sevices import create_instagram_post
from app.Instagram.sevices import instagram_posting, instagram_local_posting

router = APIRouter()

# @router.post("/local/instagram", tags=["Instagram"])
# def instagram_post(image_url: str = None, image_path: str = None, caption: str = None):
#     return upload_from_computer(image_path, caption)


@router.post("/local/instagram", tags=["Instagram"])
async def instagram_post(media_path: str, caption: str = None, media_type: str = "IMAGE"):
    # return upload_from_computer(media_path, caption, media_type)
    return await instagram_local_posting(media_path, caption, media_type)

# @router.post("/online/photo/instagram", tags=["Instagram"])
# def instagram_post(image_url: str, caption: str = None):
#     return upload_from_url(image_url, caption)


@router.post("/online/instagram", tags=["Instagram"])
async def post_instagram(media_url: str, caption:str = None, media_type: str = "IMAGE"):
    return await instagram_posting(media_url, caption, media_type)
# def instagram_post(media_url: str, caption: str = None, media_type: str = "IMAGE"):
#     """
#     Endpoint to post an image or video to Instagram.
#     :param media_url: Public URL of the media.
#     :param caption: Caption for the post.
#     :param media_type: "IMAGE" or "VIDEO".
#     """
#     media_id = create_instagram_media(media_url, caption, media_type)
#     post_id = publish_instagram_media(media_id)
#     return {"message": "Post published successfully", "post_id": post_id}