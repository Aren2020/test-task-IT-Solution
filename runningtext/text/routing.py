from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/video/text/<int:video_id>/', consumers.VideoConsumer.as_asgi()),
]