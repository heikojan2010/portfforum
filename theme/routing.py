# chat/routing.py
from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path('ws/public/', consumers.PublicChat.as_asgi()),
]
