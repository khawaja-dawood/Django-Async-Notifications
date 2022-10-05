from django.urls import path
from .consumer import NotificationConsumer

websocket_url_patterns = [
    path('ws/notification-server/', NotificationConsumer.as_asgi()),
]
