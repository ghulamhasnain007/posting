from fastapi import APIRouter, Query, File, UploadFile
from app.Linkedin.services import linkedin_callback, linkedin_auth, post_text_to_linkedin, post_media_to_linkedin
from app.utils.linkedin_util import upload_local_media, upload_media
import shutil
from pathlib import Path
from app.config import LINKEDIN_ACCESS_TOKEN
from app.utils.linkedin_util import get_organizations
import requests


router = APIRouter()

@router.get("/callback", tags=["Linkedin"])
def callback(code: str = Query(...)):
    return linkedin_callback(code)


@router.get("/auth", tags=["Linkedin"])
def auth():
    return linkedin_auth()

# @router.post("/post/image", tags=["Linkedin"])
# def post_image(image_url: str = Query(...), text: str = Query(...)):
#     return post_image_to_linkedin(image_url, text)


@router.post("/organization/post/text", tags=["Linkedin"])
def post_text_organization(text: str = Query(...)):
    org_data = get_organizations(LINKEDIN_ACCESS_TOKEN)
    author_id = org_data['elements'][0]['organizationalTarget']  # Fetch the first organization's ID

    if not author_id:
        return {"error": "Failed to get organization ID"}
    
    return post_text_to_linkedin(text, author_id)



@router.post("/profile/post/text", tags=["Linkedin"])
def post_text_profile(text: str = Query(...)):
    org_data = get_organizations(LINKEDIN_ACCESS_TOKEN)
    author_id = org_data['elements'][0]['roleAssignee']  # Fetch the first organization's ID

    if not author_id:
        return {"error": "Failed to get organization ID"}
    
    return post_text_to_linkedin(text, author_id)



# @router.post("/post/organization/image", tags=["Linkedin"])
# def post_image(image_url: str = Query(...), text: str = Query(...)):
    
#     org_data = get_organizations(LINKEDIN_ACCESS_TOKEN)
#     author_id = org_data['elements'][0]['organizationalTarget']  # Fetch the first organization's ID

#     asset_urn = upload_media(image_url, author_id)

#     if "error" in asset_urn:
#         return asset_urn  # Return error message if upload fails
    
#     if not author_id:
#         return {"error": "Failed to get organization ID"}
    
#     return post_image_to_linkedin(asset_urn, text, author_id)



@router.post("/post/profile/media", tags=["Linkedin"])
def post_image(image_url: str = Query(...), text: str = Query(...), media_type: str = Query("image")):

    org_data = get_organizations(LINKEDIN_ACCESS_TOKEN)
    author_id = org_data['elements'][0]['roleAssignee']  # Fetch the first organization's ID
    
    asset_urn = upload_media(image_url, author_id)
    if "error" in asset_urn:
        return asset_urn  # Return error message if upload fails
    

    if not author_id:
        return {"error": "Failed to get organization ID"}
    
    return post_media_to_linkedin(asset_urn, text, author_id, media_type)


@router.post("/post/organization/media", tags=["Linkedin"])
def post_image(image_url: str = Query(...), text: str = Query(...), media_type: str = Query("image")):

    org_data = get_organizations(LINKEDIN_ACCESS_TOKEN)
    author_id = org_data['elements'][0]['organizationalTarget']  # Fetch the first organization's ID
    
    asset_urn = upload_media(image_url, author_id)
    if "error" in asset_urn:
        return asset_urn  # Return error message if upload fails
    

    if not author_id:
        return {"error": "Failed to get organization ID"}
    
    return post_media_to_linkedin(asset_urn, text, author_id, media_type)





# @router.post("/post/profile/local-image", tags=["Linkedin"])
# async def post_local_image(file: UploadFile = File(...), text: str = Query(...)):
#     """Post an image to LinkedIn after uploading from the user's computer."""
#     # Save the file temporarily
#     temp_file_path = Path(f"temp_{file.filename}")
#     with temp_file_path.open("wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     # Upload the image to LinkedIn
#     org_data = get_organizations(LINKEDIN_ACCESS_TOKEN)
#     author_id = org_data['elements'][0]['roleAssignee']  # Fetch the first organization's ID

#     if not author_id:
#         return {"error": "Failed to get organization ID"}

#     asset_urn = upload_local_image(str(temp_file_path), author_id)  # Pass the temporary file path to upload_image
#     if "error" in asset_urn:
#         return asset_urn  # Return error message if upload fails
    

#     # Post the image to LinkedIn
#     response = post_image_to_linkedin(asset_urn, text, author_id)

#     # Delete the temporary file after upload
#     temp_file_path.unlink()

#     return response




# @router.post("/post/organization/local-image", tags=["Linkedin"])
# async def post_local_image(file: UploadFile = File(...), text: str = Query(...)):
#     """Post an image to LinkedIn after uploading from the user's computer."""
#     # Save the file temporarily
#     temp_file_path = Path(f"temp_{file.filename}")
#     with temp_file_path.open("wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     org_data = get_organizations(LINKEDIN_ACCESS_TOKEN)
#     author_id = org_data['elements'][0]['organizationalTarget']  # Fetch the first organization's ID

#     if not author_id:
#         return {"error": "Failed to get organization ID"}
    
#     # Upload the image to LinkedIn
#     asset_urn = upload_local_image(str(temp_file_path), author_id)  # Pass the temporary file path to upload_image
#     if "error" in asset_urn:
#         return asset_urn  # Return error message if upload fails
    

#     # Post the image to LinkedIn
#     response = post_image_to_linkedin(asset_urn, text, author_id)

#     # Delete the temporary file after upload
#     temp_file_path.unlink()

#     return response


@router.post("/post/profile/local-media", tags=["Linkedin"])
async def post_local_media(file: UploadFile = File(...), text: str = Query(...), media_type: str = Query("image")):
    """Post an image or video to LinkedIn after uploading from the user's computer."""
    # Save the file temporarily
    temp_file_path = Path(f"temp_{file.filename}")
    with temp_file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Get LinkedIn organization ID
    org_data = get_organizations(LINKEDIN_ACCESS_TOKEN)
    author_id = org_data['elements'][0]['roleAssignee'] 

    if not author_id:
        return {"error": "Failed to get organization ID"}

    # Upload media (image or video)
    asset_urn = upload_local_media(str(temp_file_path), author_id, media_type.lower())
    if "error" in asset_urn:
        return asset_urn  # Return error message if upload fails

    # Post to LinkedIn
    response = post_media_to_linkedin(asset_urn, text, author_id, media_type.lower())

    # Delete the temporary file
    temp_file_path.unlink()

    return response


@router.post("/post/organization/local-media", tags=["Linkedin"])
async def post_local_media(file: UploadFile = File(...), text: str = Query(...), media_type: str = Query("image")):
    """Post an image or video to LinkedIn after uploading from the user's computer."""
    # Save the file temporarily
    temp_file_path = Path(f"temp_{file.filename}")
    with temp_file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Get LinkedIn organization ID
    org_data = get_organizations(LINKEDIN_ACCESS_TOKEN)
    author_id = org_data['elements'][0]['organizationalTarget'] 

    if not author_id:
        return {"error": "Failed to get organization ID"}

    # Upload media (image or video)
    asset_urn = upload_local_media(str(temp_file_path), author_id, media_type.lower())
    if "error" in asset_urn:
        return asset_urn  # Return error message if upload fails

    # Post to LinkedIn
    response = post_media_to_linkedin(asset_urn, text, author_id, media_type.lower())

    # Delete the temporary file
    temp_file_path.unlink()

    return response










@router.get('/requset')
def requetsInfo():
    response = requests.get("https://api64.ipify.org?format=json")
    print(response.json())  # This should show your VPN IP


