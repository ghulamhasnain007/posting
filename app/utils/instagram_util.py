import requests
from app.config import ACCESS_TOKEN, INSTAGRAM_BUSINESS_ACCOUNT_ID, GRAPH_API_URL

def create_instagram_media(image_url: str, caption: str = None):
    """
    Create a media container for an Instagram post.
    :param image_url: Publicly accessible URL of the image.
    :param caption: Caption for the Instagram post.
    :return: Media container ID.
    """
    media_endpoint = f"{GRAPH_API_URL}/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media"
    media_payload = {
        "image_url": image_url,
        "caption": caption,
        "access_token": ACCESS_TOKEN,
    }

    response = requests.post(media_endpoint, data=media_payload)
    response_data = response.json()

    if "id" not in response_data:
        raise ValueError(f"Error creating media container: {response_data}")

    return response_data["id"]

def publish_instagram_media(media_id: str):
    """
    Publish the media to Instagram.
    :param media_id: Media container ID.
    :return: Published post ID.
    """
    publish_endpoint = f"{GRAPH_API_URL}/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media_publish"
    publish_payload = {
        "creation_id": media_id,
        "access_token": ACCESS_TOKEN,
    }

    response = requests.post(publish_endpoint, data=publish_payload)
    response_data = response.json()

    if "id" not in response_data:
        raise ValueError(f"Error publishing media: {response_data}")

    return response_data["id"]