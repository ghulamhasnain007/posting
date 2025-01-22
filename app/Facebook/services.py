import requests
from app.config import ACCESS_TOKEN, GRAPH_API_URL, PAGE_ID, PAGE_ACCESS_TOKEN
from fastapi import HTTPException


def upload_online_media_to_facebook(media_url: str, caption: str, media_type: str):
    """ Upload an image or video from a URL to Facebook. """
    if not media_url:
        raise HTTPException(status_code=400, detail="Media URL is required")

    endpoint = f"{GRAPH_API_URL}/{PAGE_ID}/{media_type}"
    payload = {
        "access_token": PAGE_ACCESS_TOKEN
    }

    # Ensure correct parameter names for each type
    if media_type == "photos":
        payload["url"] = media_url  # Correct key for images
        payload["caption"] = caption
    elif media_type == "videos":
        payload["file_url"] = media_url  # Correct key for videos
        payload["description"] = caption
    else:
        raise HTTPException(status_code=400, detail="Invalid media type")

    try:
        response = requests.post(endpoint, data=payload, timeout=60)
        response_data = response.json()

        if "id" not in response_data:
            raise HTTPException(status_code=500, detail=f"Error uploading media: {response_data}")

        return response_data

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error uploading {media_type}: {str(e)}")


# def upload_online_image_to_facebook(media_url: str, caption: str, media_type):
#     """
#     Upload an image to Facebook.
    
#     :param image_url: URL of the image to be uploaded.
#     :param caption: Caption for the image (optional).
#     :return: Response from Facebook API.
#     """
#     if not media_url:
#         raise ValueError("Media URL is required")

#     endpoint = f"{GRAPH_API_URL}/{PAGE_ID}/{media_type}"
#     payload = {
#         "url": media_url,
#         "access_token": PAGE_ACCESS_TOKEN
#     }

#     if media_type == "photos":
#         payload["caption"] = caption

#     if media_type == "videos":
#         payload["description"] = caption


#     try:
#         response = requests.post(endpoint, data=payload, timeout=60)
#         response_data = response.json()

#         if "id" not in response_data:
#             raise ValueError(f"Error uploading media: {response_data}")

#         return response_data  # Return the successful response data

#     except requests.exceptions.RequestException as e:
#         raise RuntimeError(f"Request failed: {e}")
    


def upload_local_media(media_path, caption: str, media_type):
    """
    Upload an image to Facebook.
    :param image_url: URL of the image to be uploaded (optional).
    :param image_path: Path to the local image file to be uploaded (optional).
    :param caption: Caption for the image (optional).
    :return: Response from Facebook API.
    """
    # endpoint = f"{GRAPH_API_URL}/me/photos"
    endpoint = f"{GRAPH_API_URL}/{PAGE_ID}/{media_type}"
    payload = {
        "access_token": PAGE_ACCESS_TOKEN
    }

    if media_type == "photos":
        payload["caption"] = caption

    if media_type == "videos":
        payload["description"] = caption


    files = {"source": open(media_path, "rb")}

    print(payload)
    try:
        response = requests.post(endpoint, data=payload, files=files)
        response_data = response.json()

        if "id" not in response_data:
            raise ValueError(f"Error uploading image: {response_data}")

        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while uploading local image {str(e)}" )




# def upload_video_to_facebook(video_url: str = None, video_path: str = None, description: str = None):
#     """
#     Upload a video to Facebook.
#     :param video_url: URL of the video to be uploaded (optional).
#     :param video_path: Path to the local video file to be uploaded (optional).
#     :param description: Description for the video (optional).
#     :return: Response from Facebook API.
#     """
#     endpoint = f"{GRAPH_API_URL}/{PAGE_ID}/videos"
#     payload = {"description": description, "access_token": PAGE_ACCESS_TOKEN}

#     files = None
#     if video_url:
#         payload["file_url"] = video_url
#     elif video_path:
#         files = {"source": open(video_path, "rb")}

#     response = requests.post(endpoint, data=payload, files=files)
#     response_data = response.json()

#     if "id" not in response_data:
#         raise ValueError(f"Error uploading video: {response_data}")

#     return response_data



# def upload_local_video_to_facebook(video_path: str, description: str = None):
#     try:
#         """
#         Upload a video to Facebook.
#         :param video_url: URL of the video to be uploaded (optional).
#         :param video_path: Path to the local video file to be uploaded (optional).
#         :param description: Description for the video (optional).
#         :return: Response from Facebook API.
#         """
#         endpoint = f"{GRAPH_API_URL}/{PAGE_ID}/videos"
#         payload = {"description": description, "access_token": PAGE_ACCESS_TOKEN}

#         # files = None
#         # if video_url:
#         #     payload["file_url"] = video_url
#         # elif video_path:
#         files = {"source": open(video_path, "rb")}

#         response = requests.post(endpoint, data=payload, files=files)
#         response_data = response.json()

#         if "id" not in response_data:
#             raise ValueError(f"Error uploading video: {response_data}")

#         return response_data
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error while uploading local video: {str(e)}")
    
    

# def upload_online_video_to_facebook(video_url: str, description: str = None):

#     try:
#         """
#         Upload a video to Facebook.
#         :param video_url: URL of the video to be uploaded (optional).
#         :param video_path: Path to the local video file to be uploaded (optional).
#         :param description: Description for the video (optional).
#         :return: Response from Facebook API.
#         """
#         endpoint = f"{GRAPH_API_URL}/{PAGE_ID}/videos"
#         payload = {
#             "url": video_url,
#             "description": description,
#             "access_token": PAGE_ACCESS_TOKEN
#         }

#         response = requests.post(endpoint, data=payload)
#         response_data = response.json()

#         if "id" not in response_data:
#             raise ValueError(f"Error uploading video: {response_data}")

#         return response_data
    
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error Uploading video: {str(e)}")

