import json
from channels.generic.websocket import AsyncWebsocketConsumer

class VideoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.video_id = self.scope['url_route']['kwargs']['video_id']
        self.video_group_name = f'video_{self.video_id}'

        # Join project group
        await self.channel_layer.group_add(
            self.video_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave project group
        await self.channel_layer.group_discard(
            self.video_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming WebSocket messages if needed
        pass

    # Handler for 'send_video_url' event
    async def send_video_url(self, event):
        video_url = event['video_url']
        
        # Send message to WebSocket
        await self.send(text_data = json.dumps({
            'video_url': video_url
        }))