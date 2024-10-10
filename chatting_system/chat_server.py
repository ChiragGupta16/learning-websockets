import asyncio
import websockets

# Keep track of all connected clients
connected_clients = set()

async def chat_server(websocket, path):
    # Add the new client to the set of connected clients
    connected_clients.add(websocket)
    print(f"A client connected: {websocket.remote_address}")

    try:
        # Listen for incoming messages from the client
        async for message in websocket:
            print(f"Received message: {message}")

            # Broadcast the message to all connected clients
            for client in connected_clients:
                if client != websocket:  # Don't send the message to the sender
                    await client.send(f"Broadcast: {message}")

    except websockets.ConnectionClosed:
        print(f"Client disconnected: {websocket.remote_address}")
    finally:
        # Remove the client from the set when they disconnect
        connected_clients.remove(websocket)

# Start the WebSocket server
async def main():
    async with websockets.serve(chat_server, "localhost", 9551):
        print("Server started on ws://localhost:9551")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())