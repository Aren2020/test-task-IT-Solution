from celery import shared_task
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Video
from .utils import VideoCreator
import logging

@shared_task
def create_video_task(video_id):
    try:
        video = Video.objects.get(id = video_id)
        if not video.video:
            video_creator = VideoCreator(video)
            video_url = video_creator.create_video()
            video.video = video_url
            video.save()
        video_url = video.video.url

        channel_layer = get_channel_layer()

        # Use async_to_sync to make the async call in a sync context (like Celery)
        async_to_sync(channel_layer.group_send)(
            f'video_{video_id}',
            {
                'type': 'send_video_url',  # This should match the handler in your consumer
                'video_url': video_url,
                'width': video.width,
                'height': video.height
            }
        )
    except Exception as e:
        channel_layer = get_channel_layer()
        
        # Use async_to_sync to make the async call in a sync context (like Celery)
        async_to_sync(channel_layer.group_send)(
            f'video_{video_id}',
            {
                'type': 'send_video_url',  # This should match the handler in your consumer
                'video_url': None,
            }
        )
        logging.error(f"An error occurred: {e}")