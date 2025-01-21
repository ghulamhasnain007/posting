import cloudinary
import cloudinary.uploader
import cloudinary.api
from app.config import CLOUD_NAME, CLOUD_API_KEY, CLOUD_API_SECRET
import os

# Configure Cloudinary with your credentials
cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=CLOUD_API_KEY,
    api_secret=CLOUD_API_SECRET
)

# def upload_to_cloudinary(media_path: str):
#     """
#     Upload an image to Cloudinary and return the public URL.
#     :param image_path: Local path of the image.
#     :return: Publicly accessible URL of the uploaded image.
#     """
#     try:
#         response = cloudinary.uploader.upload(media_path)
#         return response.get("secure_url")  # Get the secure URL from the response
#     except Exception as e:
#         raise ValueError(f"Error uploading to Cloudinary: {e}")

def upload_to_cloudinary(media_path: str, media_type: str = "image"):
    """
    Upload an image or video to Cloudinary and return the public URL.
    :param media_path: Local path of the file.
    :param media_type: "image" or "video".
    :return: Publicly accessible URL of the uploaded file.
    """
    if not os.path.exists(media_path):
        raise ValueError(f"File not found: {media_path}")

    try:
        response = cloudinary.uploader.upload(media_path, resource_type=media_type)
        return response.get("secure_url")
    except Exception as e:
        raise ValueError(f"Error uploading to Cloudinary: {e}")
