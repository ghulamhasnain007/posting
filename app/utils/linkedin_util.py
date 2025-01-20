from fastapi import HTTPException
import requests
from app.config import LINKEDIN_ACCESS_TOKEN
import os

HEADERS = {
    "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0",
    "Content-Type": "application/json",
}

def get_organizations(access_token: str):
    """Fetch organizations associated with the logged-in user"""
    url = "https://api.linkedin.com/v2/organizationalEntityAcls?q=roleAssignee"
    headers = {"Authorization": f"Bearer {access_token}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to fetch organizations")

    return response.json()

def upload_image(image_url: str, author_id: str):
    """Uploads an image to LinkedIn and returns its URN"""
    # org_data = get_organizations(LINKEDIN_ACCESS_TOKEN)
    # organization_id = org_data['elements'][0]['organizationalTarget']  # Fetch the first organization's ID

    upload_url = "https://api.linkedin.com/v2/assets?action=registerUpload"

    payload = {
        "registerUploadRequest": {
            "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],  
            "owner": author_id,  # Using organization ID here
            "serviceRelationships": [
                {
                    "relationshipType": "OWNER",
                    "identifier": "urn:li:userGeneratedContent"
                }
            ]
        }
    }

    response = requests.post(upload_url, headers=HEADERS, json=payload)
    upload_response = response.json()

    if "value" in upload_response and "asset" in upload_response["value"]:
        asset_urn = upload_response["value"]["asset"]  # This is the URN you need
        upload_url = upload_response["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]

        # Upload the actual image
        image_data = requests.get(image_url).content
        image_upload_response = requests.put(upload_url, headers={"Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}"}, data=image_data)

        if image_upload_response.status_code == 201:
            return asset_urn  # Return URN to use in the post
        else:
            return {"error": "Failed to upload image"}
    else:
        return {"error": "Failed to register upload"}




def upload_local_image(file_path: str, author_id: str):
    """Uploads an image from a local file and returns its URN"""
    # org_data = get_organizations(LINKEDIN_ACCESS_TOKEN)
    # organization_id = org_data['elements'][0]['organizationalTarget']  # Fetch the first organization's ID

    upload_url = "https://api.linkedin.com/v2/assets?action=registerUpload"

    payload = {
        "registerUploadRequest": {
            "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],  
            "owner": author_id,  
            "serviceRelationships": [
                {
                    "relationshipType": "OWNER",
                    "identifier": "urn:li:userGeneratedContent"
                }
            ]
        }
    }

    response = requests.post(upload_url, headers=HEADERS, json=payload)
    upload_response = response.json()

    if "value" in upload_response and "asset" in upload_response["value"]:
        asset_urn = upload_response["value"]["asset"]  # This is the URN you need
        upload_url = upload_response["value"]["uploadMechanism"]["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]

        # Open the file and upload it to LinkedIn
        with open(file_path, 'rb') as image_file:
            image_data = image_file.read()

        image_upload_response = requests.put(upload_url, headers={"Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}"}, data=image_data)

        if image_upload_response.status_code == 201:
            return asset_urn  # Return URN to use in the post
        else:
            return {"error": "Failed to upload image"}
    else:
        return {"error": "Failed to register upload"}
