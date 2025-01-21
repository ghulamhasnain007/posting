from fastapi import HTTPException
from app.config import ACCESS_TOKEN, INSTAGRAM_BUSINESS_ACCOUNT_ID, GRAPH_API_URL
import requests
from app.utils.cloudinary_util import upload_to_cloudinary
from app.utils.instagram_util import create_instagram_media, publish_instagram_media




# def create_instagram_post(image_url: str = None, image_path: str = None, caption: str = None):
#     """
#     Post an image and caption to Instagram using the Instagram Graph API.
#     :param image_url: URL of the image to be posted (optional).
#     :param image_path: Path to the local image file to be uploaded (optional).
#     :param caption: Caption for the Instagram post.
#     :return: JSON response with the result.
#     """
#     if not (image_url or image_path):
#         raise ValueError("Either image_url or image_path must be provided.")
    
#     # Step 1: Create Media Object
#     media_endpoint = f"{GRAPH_API_URL}/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media"
#     media_payload = {
#         "caption": caption,
#         "access_token": ACCESS_TOKEN,
#     }

#     # If image_url is provided, include it in the media payload
#     if image_url:
#         media_payload["image_url"] = image_url
#         media_response = requests.post(media_endpoint, data=media_payload)
#     elif image_path:
#         # If image_path is provided, upload the image as a file
#         with open(image_path, "rb") as image_file:
#             media_files = {"image": image_file}
#             media_response = requests.post(media_endpoint, data=media_payload, files=media_files)
    
#     media_data = media_response.json()

#     # Check if media creation was successful
#     if "id" not in media_data:
#         raise HTTPException(status_code=400, detail=f"Error creating media: {media_data}")

#     creation_id = media_data["id"]

#     # Step 2: Publish Media
#     publish_endpoint = f"{GRAPH_API_URL}/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media_publish"
#     publish_payload = {
#         "creation_id": creation_id,
#         "access_token": ACCESS_TOKEN,
#     }

#     try:
#         publish_response = requests.post(publish_endpoint, data=publish_payload)
#         publish_data = publish_response.json()

#         # Check if post publishing was successful
#         if "id" not in publish_data:
#             raise HTTPException(status_code=400, detail=f"Error publishing media: {publish_data}")

#         return {"message": "Post published successfully", "post_id": publish_data["id"]}

#     except requests.exceptions.RequestException as e:
#         raise HTTPException(status_code=500, detail=f"Request failed: {str(e, media_payload)}")








# def create_instagram_post(image_url: str, caption: str):
#     """
#     Post an image and caption to Instagram using the Instagram Graph API.
#     :param image_url: URL of the image to be posted
#     :param caption: Caption for the Instagram post
#     :return: JSON response with the result
#     """
#     # Step 1: Create Media Object
#     media_endpoint = f"{GRAPH_API_URL}/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media"
#     media_payload = {
#         "image_url": image_url,
#         "caption": caption,
#         "access_token": ACCESS_TOKEN,
#     }
    
#     try:
#         media_response = requests.post(media_endpoint, data=media_payload)
#         media_data = media_response.json()

#         if "id" not in media_data:
#             raise HTTPException(status_code=400, detail=f"Error creating media: {media_data}")

#         creation_id = media_data["id"]

#         # Step 2: Publish Media
#         publish_endpoint = f"{GRAPH_API_URL}/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media_publish"
#         publish_payload = {
#             "creation_id": creation_id,
#             "access_token": ACCESS_TOKEN,
#         }
#         publish_response = requests.post(publish_endpoint, data=publish_payload)
#         publish_data = publish_response.json()

#         if "id" not in publish_data:
#             raise HTTPException(status_code=400, detail=f"Error publishing media: {publish_data}")

#         return {"message": "Post published successfully", "post_id": publish_data["id"]}

#     except requests.exceptions.RequestException as e:
#         raise HTTPException(status_code=500, detail=f"Request failed: {str(e)}")


def upload_from_computer(image_path: str, caption: str = None):
    """
    Upload an image from the computer to Instagram via Cloudinary.
    :param image_path: Local path of the image.
    :param caption: Caption for the Instagram post.
    :return: Published post ID.
    """
    image_url = upload_to_cloudinary(image_path)  # Upload image to Cloudinary and get URL
    media_id = create_instagram_media(image_url, caption)
    post_id = publish_instagram_media(media_id)
    return {"message": "Post published successfully", "post_id": post_id}


# def upload_from_url(image_url: str, caption: str = None):
#     """
#     Upload an image to Instagram using a direct image URL.
#     :param image_url: Publicly accessible URL of the image.
#     :param caption: Caption for the Instagram post.
#     :return: Published post ID.
#     """
#     media_id = create_instagram_media(image_url, caption)
#     post_id = publish_instagram_media(media_id)
#     return {"message": "Post published successfully", "post_id": post_id}




async def instagram_posting(media_url: str, caption: str = None, media_type: str = "IMAGE"):
    """
    Endpoint to post an image or video to Instagram.
    :param media_url: Public URL of the media.
    :param caption: Caption for the post.
    :param media_type: "IMAGE" or "VIDEO".
    """
    media_id = await create_instagram_media(media_url, caption, media_type)
    post_id = await publish_instagram_media(media_id)
    return {"message": "Post published successfully", "post_id": post_id}


async def instagram_local_posting(media_path: str, caption: str = None, media_type: str = "IMAGE"):
    """
    Endpoint to post an image or video to Instagram.
    :param media_url: Public URL of the media.
    :param caption: Caption for the post.
    :param media_type: "IMAGE" or "VIDEO".
    """
    media_url = upload_to_cloudinary(media_path)
    media_id = await create_instagram_media(media_url, caption, media_type)
    post_id = await publish_instagram_media(media_id)
    return {"message": "Post published successfully", "post_id": post_id}

# def create_instagram_media(image_url: str, caption: str = None):
#     """
#     Create a media container for an Instagram post.
#     :param image_url: Publicly accessible URL of the image.
#     :param caption: Caption for the Instagram post.
#     :return: Media container ID.
#     """
#     media_endpoint = f"{GRAPH_API_URL}/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media"
#     media_payload = {
#         "image_url": image_url,
#         "caption": caption,
#         "access_token": ACCESS_TOKEN,
#     }

#     response = requests.post(media_endpoint, data=media_payload)
#     response_data = response.json()

#     if "id" not in response_data:
#         raise ValueError(f"Error creating media container: {response_data}")

#     return response_data["id"]

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