# from fastapi import FastAPI, HTTPException
# import requests

# app = FastAPI()

# # Replace these with your actual credentials
# ACCESS_TOKEN = "EAAJFhdnkB7UBO6q5jKNUIlyZBiHAWpoE8SzkVZCyNugQYFOBpjgqlfSVfkVXcUC5V4ky0ufk36RmZCMfnK4kYzEx2dcccZAyFML0UK3DMdVgO2FSt7yOJzpguA0nPW4GZC1Q4XFH5qLSoju4mZCn4UxVifDRrOZCfb4ZBABkUSuwYWt7nWezIQlZBbC6DUVWUGSGqu0e5Dsl4TAv6Rxa1ZCQZDZD"
# INSTAGRAM_BUSINESS_ACCOUNT_ID = "17841471530163817"
# GRAPH_API_URL = "https://graph.facebook.com/v21.0"

# @app.post("/post-to-instagram")
# async def post_to_instagram(image_url: str, caption: str):
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


# Run the app
# Use `uvicorn` to start the server: uvicorn <filename>:app --reload




import uvicorn
# from app.core.database import init_db


if __name__ == "__main__":
    # init_db()  # Initialize the database tables
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
