from celery import shared_task
import requests
from api.models import Video
from django.conf import settings

def extract_fields(data):
    """
    Extract the fields needed for Video model form api response
    """
    return {
        "id": data["id"]["videoId"],
        "title": data["snippet"]["title"],
        "description": data["snippet"]["description"],
        "channel": data["snippet"]["channelTitle"],
        "published_at": data["snippet"]["publishTime"],
        "thumbnail": data["snippet"]["thumbnails"]["default"]["url"],
    }

@shared_task(name="fetch_videos_and_store")
def fetch_videos_and_store():
    # Fetch from youtube API
    response = requests.get(
        url="https://youtube.googleapis.com/youtube/v3/search",
        params={
            "part": "snippet",
            "type": "video",
            "maxResults": 10,
            "q": "India cricket",
            "key": settings.GOOGLE_API_KEYS[-1],
            "fields": "items(id(videoId),snippet(publishTime,thumbnails(default(url)),channelTitle,title,description))"
        }
    )

    if response.status_code != 200:
        print("YouTube API response code - {}".format(response.status_code))

        # If google API key quota exceeded, use next available key.
        # We will achieve this by removing the expired key from the keys list
        if response.status_code == 403 or response.status_code == 429:
            settings.GOOGLE_API_KEYS.pop()

        return

    # Update database
    data = response.json()
    video_objects = [Video(**extract_fields(item)) for item in data.get("items",[])]
    Video.objects.bulk_create(video_objects, ignore_conflicts=True)
    print("Successfully inserted")


