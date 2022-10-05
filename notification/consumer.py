from channels.generic.websocket import WebsocketConsumer
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # print(self.scope)
        self.room_group_name = 'notification'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print('recieved')
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'notification_message',
                'message': message
            }
        )

    async def notification_message(self, event):
        print('sending message')
        message = event['message']

        await self.send(text_data=json.dumps({
            'type': 'notification',
            'message': message
        }))


# class NotificationConsumer(WebsocketConsumer):
#
#     def connect(self):
#         self.accept()
#
#         self.send(text_data=json.dumps({
#             'type': 'Connection Established',
#             'message': "You are now connected!"
#         }))
#
#     def receive(self, text_data):
#         data_received = json.loads(text_data)
#         message = data_received['message']
#
#         print(message)
#
#     def disconnect(self, close_code):
#         self.close(close_code)
