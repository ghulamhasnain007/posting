from fastapi import APIRouter, HTTPException
import requests
# from app.Instagram.sevices import create_instagram_post
from app.Instagram.sevices import upload_from_computer, upload_from_url

router = APIRouter()

# @router.post("/local/instagram", tags=["Instagram"])
# def instagram_post(image_url: str = None, image_path: str = None, caption: str = None):
#     return upload_from_computer(image_path, caption)


@router.post("/local/instagram", tags=["Instagram"])
def instagram_post(image_path: str, caption: str = None):
    return upload_from_computer(image_path, caption)

@router.post("/online/instagram", tags=["Instagram"])
def instagram_post(image_url: str, caption: str = None):
    return upload_from_url(image_url, caption)