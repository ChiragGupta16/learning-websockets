import asyncio
import websockets
 
 
class ChatServer:
    def __init__(self):
        self.connected_clients = {}
        self.client_counter = 0
 
    async def handle_client(self, websocket):
        self.client_counter += 1
        client_name = f"Client {self.client_counter}"
        self.connected_clients[websocket] = client_name
        print(f"{client_name} connected")
 
        try:
            async for message in websocket:
                print(f"Received from {client_name}: {message}")
                await self.broadcast_message(f"{client_name}: {message}", websocket)
 
        except websockets.exceptions.ConnectionClosed:
            print(f"{client_name} disconnected")
 
        finally:
            del self.connected_clients[websocket]
 
    async def broadcast_message(self, message, sender):
        for client, client_name in self.connected_clients.items():
            if client != sender:
                await client.send(message)
                print(f"Message sent to {client_name}")
 
    async def start_server(self):
        server = await websockets.serve(self.handle_client, "localhost", 9551)
        await server.wait_closed()
 
 
if __name__ == "__main__":
    chat_server = ChatServer()
    asyncio.run(chat_server.start_server())