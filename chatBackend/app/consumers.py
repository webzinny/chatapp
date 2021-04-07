import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room = self.scope['url_route']['kwargs']['room_name']
        self.group = 'chat_%s' % self.room

        # Join room group
        await self.channel_layer.group_add(
            self.group,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['msg']

        # Send message to room group
        await self.channel_layer.group_send(
            self.group,
            {
                'type': 'chat_message',
                'msg': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['msg']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'msg': message
        }))
