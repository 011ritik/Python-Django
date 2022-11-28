from django.urls import path, include
from room.consumers import ChatConsumer

websocket_urlpatterns = [
    path("rooms/",ChatConsumer.as_asgi()),
]