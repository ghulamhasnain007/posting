from fastapi import HTTPException
import requests
from app.config import LINKEDIN_ID, LINKEDIN_SECRET, REDIRECT_URI, LINKEDIN_ACCESS_TOKEN
from app.utils.linkedin_util import HEADERS

TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"




def linkedin_auth():
    """Redirect users to LinkedIn OAuth authorization page"""
    auth_url = (
        f"https://www.linkedin.com/oauth/v2/authorization"
        f"?response_type=code&client_id={LINKEDIN_ID}"
        f"&redirect_uri={REDIRECT_URI}&scope=w_member_social"
    )
    return {"auth_url": auth_url}



def linkedin_callback(code: str):
    """Exchange authorization code for an access token"""
    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": LINKEDIN_ID,
        "client_secret": LINKEDIN_SECRET,
    }
    
    response = requests.post(token_url, data=payload)
    token_data = response.json()

    if "access_token" not in token_data:
        raise HTTPException(status_code=400, detail="Failed to obtain access token")

    return {"access_token": token_data["access_token"], "expires_in": token_data["expires_in"]}


# @app.post("/linkedin/post")
def post_text_to_linkedin(text: str, author_id: str):
    """Post text content to LinkedIn"""
    headers = {"Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}", "Content-Type": "application/json"}

    # user_info = requests.get("https://api.linkedin.com/v2/me", headers=headers).json()
    # author = f"urn:li:person:{user_info.get('id')}"
    # org_data = get_organizations(LINKEDIN_ACCESS_TOKEN)
    # organization_id = org_data['elements'][0]['organizationalTarget']  # Fetch the first organization's ID

    post_url = "https://api.linkedin.com/v2/ugcPosts"
    payload = {
        # "author": organization_id,
        "author": author_id,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": "NONE",
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }

    response = requests.post(post_url, headers=headers, json=payload)
    return response.json()





def post_image_to_linkedin(image_urn: str, text: str, author_id: str):
    """Post an image to LinkedIn"""
    headers = {"Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}", "Content-Type": "application/json"}

    # org_data = get_organizations(LINKEDIN_ACCESS_TOKEN)
    # organization_id = org_data['elements'][0]['organizationalTarget']  # Fetch the first organization's ID
    
    post_url = "https://api.linkedin.com/v2/ugcPosts"
    payload = {
        "author": author_id,  # Use the organization ID as author
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": "IMAGE",
                "media": [{"status": "READY", "media": image_urn}],  # Use the asset URN here
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }

    response = requests.post(post_url, headers=headers, json=payload)
    return response.json()



def post_media_to_linkedin(media_urn: str, text: str, author_id: str, media_type: str):
    """Post an image or video to LinkedIn."""
    headers = {"Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}", "Content-Type": "application/json"}

    post_url = "https://api.linkedin.com/v2/ugcPosts"

    media_category = "IMAGE" if media_type == "image" else "VIDEO"

    payload = {
        "author": author_id,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": media_category,
                "media": [{"status": "READY", "media": media_urn}],  
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
    }

    response = requests.post(post_url, headers=headers, json=payload)
    return response.json()
