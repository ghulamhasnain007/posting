import requests
from app.config import ACCESS_TOKEN, GRAPH_API_URL, PAGE_ID, PAGE_ACCESS_TOKEN




# Handling Both Image Uploading From Computer and Image URL

def upload_image_to_facebook(image_url: str = None, image_path: str = None, caption: str = None):
    """
    Upload an image to Facebook.
    :param image_url: URL of the image to be uploaded (optional).
    :param image_path: Path to the local image file to be uploaded (optional).
    :param caption: Caption for the image (optional).
    :return: Response from Facebook API.
    """
    # endpoint = f"{GRAPH_API_URL}/me/photos"
    endpoint = f"{GRAPH_API_URL}/{PAGE_ID}/photos"
    payload = {"caption": caption, "access_token": PAGE_ACCESS_TOKEN}

    files = None
    if image_url:
        payload["url"] = image_url
    elif image_path:
        files = {"source": open(image_path, "rb")}

    print(payload)
    response = requests.post(endpoint, data=payload, files=files)
    response_data = response.json()

    if "id" not in response_data:
        raise ValueError(f"Error uploading image: {response_data}")

    return response_data





#Working Correctly

# def upload_image_to_facebook(image_url: str, caption: str = None):
#     """
#     Upload an image to Facebook Page using the Graph API.
#     :param image_url: URL of the image to be uploaded.
#     :param caption: Caption for the image.
#     :return: Response from the Facebook API.
#     """
#     endpoint = f"{GRAPH_API_URL}/{PAGE_ID}/photos"
#     payload = {
#         "url": image_url,
#         "caption": caption,
#         "access_token": PAGE_ACCESS_TOKEN
#     }
#     print(payload)
#     response = requests.post(endpoint, json=payload)
#     response_data = response.json()

#     if response.status_code != 200:
#         print(f"Error: {response_data}")
#         raise ValueError(f"Failed to upload image: {response_data}")

#     return response_data




def upload_video_to_facebook(video_url: str = None, video_path: str = None, description: str = None):
    """
    Upload a video to Facebook.
    :param video_url: URL of the video to be uploaded (optional).
    :param video_path: Path to the local video file to be uploaded (optional).
    :param description: Description for the video (optional).
    :return: Response from Facebook API.
    """
    endpoint = f"{GRAPH_API_URL}/{PAGE_ID}/videos"
    payload = {"description": description, "access_token": PAGE_ACCESS_TOKEN}

    files = None
    if video_url:
        payload["file_url"] = video_url
    elif video_path:
        files = {"source": open(video_path, "rb")}

    response = requests.post(endpoint, data=payload, files=files)
    response_data = response.json()

    if "id" not in response_data:
        raise ValueError(f"Error uploading video: {response_data}")

    return response_data
