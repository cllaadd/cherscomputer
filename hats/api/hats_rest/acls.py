import requests
import json
import os

# PEXELS_API_KEY = os.environ["PEXELS_API_KEY"]

# def get_photo(color, style):
#     headers = {"Authorization": PEXELS_API_KEY}
#     params = {
#         "per_page": 1,
#         "query": f"{color} {style}",
#     }
#     url= "https://api.pexels.com/v1/search"
#     response=requests.get(url, params=params, headers=headers)
#     content= json.loads(response.content)
#     try:
#         return {"picture_url": content["photos"][0]["src"]["original"]}
#     except (KeyError, IndexError):
#         return {"picture_url": None}
