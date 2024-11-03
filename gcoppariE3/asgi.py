"""
ASGI config for gcoppariE3 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.generic.websocket import AsyncWebsocketConsumer
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gcoppariE3.settings')

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from usuarios.routing import websocket_urlpatterns



application = get_asgi_application()

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import usuarios.routing  # Importa las rutas WebSocket

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tu_proyecto.settings')



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = f'chat_{self.scope["user"].id}'
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        mensaje = data['mensaje']
        usuario = self.scope['user']

        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'mensaje': mensaje,
                'usuario': usuario.username
            }
        )

    async def chat_message(self, event):
        mensaje = event['mensaje']
        usuario = event['usuario']

        await self.send(text_data=json.dumps({
            'mensaje': mensaje,
            'usuario': usuario
        }))
        
        
        
        import os






application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
