# usuarios/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['user'].id
        self.destinatario_id = self.scope['url_route']['kwargs']['user_id']
        self.room_name = f"chat_{min(self.user_id, self.destinatario_id)}_{max(self.user_id, self.destinatario_id)}"
        self.room_group_name = f"chat_{self.room_name}"

        # Únete al grupo de WebSocket para la sala de chat
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Abandona el grupo de WebSocket al desconectar
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Recibe el mensaje de WebSocket y envíalo al grupo
        text_data_json = json.loads(text_data)
        mensaje = text_data_json['mensaje']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'mensaje': mensaje,
                'remitente': self.user_id
            }
        )

    async def chat_message(self, event):
        # Envía el mensaje de vuelta a WebSocket
        mensaje = event['mensaje']
        remitente = event['remitente']

        await self.send(text_data=json.dumps({
            'mensaje': mensaje,
            'remitente': remitente
        }))
