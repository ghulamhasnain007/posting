import requests
from app.config import ACCESS_TOKEN, GRAPH_API_URL, PAGE_ID, PAGE_ACCESS_TOKEN
from fastapi import HTTPException



def upload_online_image_to_facebook(image_url: str, caption: str = None):
    """
    Upload an image to Facebook.
    
    :param image_url: URL of the image to be uploaded.
    :param caption: Caption for the image (optional).
    :return: Response from Facebook API.
    """
    if not image_url:
        raise ValueError("Image URL is required")

    endpoint = f"{GRAPH_API_URL}/{PAGE_ID}/photos"
    payload = {
        "url": image_url,
        "caption": caption,
        "access_token": PAGE_ACCESS_TOKEN
    }

    try:
        response = requests.post(endpoint, data=payload, timeout=60)
        response_data = response.json()

        if "id" not in response_data:
            raise ValueError(f"Error uploading image: {response_data}")

        return response_data  # Return the successful response data

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Request failed: {e}")
    


def upload_local_image_to_facebook(image_path: str = None, caption: str = None):
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

    files = {"source": open(image_path, "rb")}

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



def upload_local_video_to_facebook(video_path: str, description: str = None):
    try:
        """
        Upload a video to Facebook.
        :param video_url: URL of the video to be uploaded (optional).
        :param video_path: Path to the local video file to be uploaded (optional).
        :param description: Description for the video (optional).
        :return: Response from Facebook API.
        """
        endpoint = f"{GRAPH_API_URL}/{PAGE_ID}/videos"
        payload = {"description": description, "access_token": PAGE_ACCESS_TOKEN}

        # files = None
        # if video_url:
        #     payload["file_url"] = video_url
        # elif video_path:
        files = {"source": open(video_path, "rb")}

        response = requests.post(endpoint, data=payload, files=files)
        response_data = response.json()

        if "id" not in response_data:
            raise ValueError(f"Error uploading video: {response_data}")

        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error while uploading local video: {str(e)}")
    
    

def upload_online_video_to_facebook(video_url: str, description: str = None):

    try:
        """
        Upload a video to Facebook.
        :param video_url: URL of the video to be uploaded (optional).
        :param video_path: Path to the local video file to be uploaded (optional).
        :param description: Description for the video (optional).
        :return: Response from Facebook API.
        """
        endpoint = f"{GRAPH_API_URL}/{PAGE_ID}/videos"
        payload = {
            "url": video_url,
            "description": description,
            "access_token": PAGE_ACCESS_TOKEN
        }

        response = requests.post(endpoint, data=payload)
        response_data = response.json()

        if "id" not in response_data:
            raise ValueError(f"Error uploading video: {response_data}")

        return response_data
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error Uploading video: {str(e)}")

