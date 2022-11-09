import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import random
import asgiref.sync
from channels.auth import login, logout
from asgiref.sync import async_to_sync

class PublicChat(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']
        #self.scope["session"]["seed"] = random.randint(1, 1000)
        self.room_group_name = 'pubchat'
        #self.user = self.scope["user"]

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name, 
            #self.user
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name, 
            #self.user
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        username = text_data_json["username"]

        message = text_data_json['message']
        #async_to_sync(login)(self.scope, user)
        #self.scope["session"].save()
       

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                "username": username,
                'message': message
            }
        )
       


    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        username = event["username"]
      
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'username': username,
            'message': message
        }))
        """
        Called when someone has messaged our chat.
      
        # Send a message down to the client
        self.send(
        {3
            "type": 'chat_message',
            "username": event["username"],
            "message": event["message"],
        },
    )
        
          """
