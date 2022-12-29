from __future__ import absolute_import, unicode_literals
import json
import requests
from .models import Video
from project import settings
from celery import shared_task
from datetime import datetime, timedelta

@shared_task
def call():

    now = datetime.now()

    last_time = now - timedelta(minutes=1)

    apiKeys = settings.YOUTUBE_API_KEYS

    url = "https://youtube.googleapis.com/youtube/v3/search"

    flag = False

    for apiKey in apiKeys:

        try:
            params= {
                'q': 'news',
                'maxResults': 10,
                'key': apiKey,
                'order': 'date',
                'type': 'video',
                'part': 'snippet',
                'publishedAfter': last_time.replace(microsecond=0).isoformat()+'Z',
            }

            r = requests.get(url = url, params = params)
            flag = True

        except:
            continue

        if flag:
            break

    r = requests.get(url = url, params = params)

    json_data = json.loads(r.text)

    for item in reversed(json_data['items']):
        
        title = item['snippet']['title'],
        description = item['snippet']['description'],
        published = item['snippet']['publishedAt'],
        thumbnail = item['snippet']['thumbnails']['default']['url']

        print(title, description, published, thumbnail)

        video = Video(
            title=title[0],
            description=description[0],
            published=published[0],
            thumbnail=thumbnail,
        )

        video.save()
