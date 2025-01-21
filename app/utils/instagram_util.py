import requests
from app.config import ACCESS_TOKEN, INSTAGRAM_BUSINESS_ACCOUNT_ID, GRAPH_API_URL
from fastapi import HTTPException
import aiohttp
import asyncio

# def create_instagram_media(image_url: str, caption: str = None):
#     try:
#         """
#         Create a media container for an Instagram post.
#         :param image_url: Publicly accessible URL of the image.
#         :param caption: Caption for the Instagram post.
#         :return: Media container ID.
#         """
#         media_endpoint = f"{GRAPH_API_URL}/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media"
#         media_payload = {
#             "image_url": image_url,
#             "caption": caption,
#             "access_token": ACCESS_TOKEN,
#         }

#         response = requests.post(media_endpoint, data=media_payload)
#         response_data = response.json()

#         if "id" not in response_data:
#             raise ValueError(f"Error creating media container: {response_data}")

#         return response_data["id"]
#     except Exception as e:
#         raise HTTPException(status_code=200, detail="Cannot create media")

# def publish_instagram_media(media_id: str):
#     """
#     Publish the media to Instagram.
#     :param media_id: Media container ID.
#     :return: Published post ID.
#     """
#     publish_endpoint = f"{GRAPH_API_URL}/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media_publish"
#     publish_payload = {
#         "creation_id": media_id,
#         "access_token": ACCESS_TOKEN,
#     }

#     response = requests.post(publish_endpoint, data=publish_payload)
#     response_data = response.json()

#     if "id" not in response_data:
#         raise ValueError(f"Error publishing media: {response_data}")

#     return response_data["id"]



# def create_instagram_media(media_url: str, caption: str = None, media_type: str = "IMAGE"):
#     """
#     Create a media container for an Instagram post (Image/Video).
#     :param media_url: Publicly accessible URL of the image or video.
#     :param caption: Caption for the Instagram post.
#     :param media_type: "IMAGE" or "VIDEO" to specify media type.
#     :return: Media container ID.
#     """
#     try:
#         media_endpoint = f"{GRAPH_API_URL}/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media"
#         media_payload = {
#             "access_token": ACCESS_TOKEN,
#             "caption": caption,
#         }

#         if media_type == "VIDEO":
#             media_payload["video_url"] = media_url  # For video posts
#             media_payload["media_type"] = "REELS"   # This makes it a Reel
#         else:
#             media_payload["image_url"] = media_url  # For image posts

#         response = requests.post(media_endpoint, data=media_payload)
#         response_data = response.json()

#         if "id" not in response_data:
#             raise ValueError(f"Error creating media container: {response_data}")

#         print(response_data["id"])

#         return response_data["id"]
    
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Cannot create media: {str(e)}")


# def publish_instagram_media(media_id: str):
#     """
#     Publish the media to Instagram.
#     :param media_id: Media container ID.
#     :return: Published post ID.
#     """
#     try:
#         publish_endpoint = f"{GRAPH_API_URL}/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media_publish"
#         publish_payload = {
#             "creation_id": media_id,
#             "access_token": ACCESS_TOKEN,
#         }

#         response = requests.post(publish_endpoint, data=publish_payload)
#         response_data = response.json()

#         if "id" not in response_data:
#             raise ValueError(f"Error publishing media: {response_data}")

#         return response_data["id"]
    
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Cannot publish media: {str(e)}")




async def create_instagram_media(media_url: str, caption: str = None, media_type: str = "IMAGE"):
    """
    Creates a media container for Instagram (Image/Video).
    """
    media_endpoint = f"{GRAPH_API_URL}/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media"
    media_payload = {
        "access_token": ACCESS_TOKEN,
        "caption": caption,
    }

    if media_type == "VIDEO":
        media_payload["video_url"] = media_url
        media_payload["media_type"] = "REELS"  # This makes it a Reel
    else:
        media_payload["image_url"] = media_url

    async with aiohttp.ClientSession() as session:
        async with session.post(media_endpoint, data=media_payload) as response:
            response_data = await response.json()

            if "id" not in response_data:
                raise HTTPException(status_code=400, detail=f"Error creating media: {response_data}")

            return response_data["id"]


async def publish_instagram_media(media_id: str, retries: int = 5, delay: int = 5):
    """
    Publishes media to Instagram, retrying if media is not ready.
    """
    publish_endpoint = f"{GRAPH_API_URL}/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media_publish"
    publish_payload = {
        "creation_id": media_id,
        "access_token": ACCESS_TOKEN,
    }

    async with aiohttp.ClientSession() as session:
        for attempt in range(retries):
            async with session.post(publish_endpoint, data=publish_payload) as response:
                response_data = await response.json()

                if "id" in response_data:
                    return response_data["id"]

                if response_data.get("error", {}).get("error_subcode") == 2207027:
                    print(f"Media not ready. Retrying in {delay} seconds... (Attempt {attempt+1}/{retries})")
                    await asyncio.sleep(delay)  # Non-blocking wait
                else:
                    raise HTTPException(status_code=400, detail=f"Error publishing media: {response_data}")

        raise HTTPException(status_code=400, detail="Max retries reached. Media is still not ready.")









