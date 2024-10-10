import asyncio
import websockets

async def chat_client():
    url = "ws://localhost:9551"
    async with websockets.connect(url) as websocket:
        print("Connected to server")

        # Coroutine for receiving messages from the server
        async def receive_messages():
            try:
                response = await websocket.recv()
                print(f"Server : {response}")
            except websockets.ConnectionClosed:
                print("Connection closed by server.")

        # Create a task to receive messages asynchronously
        receive_task = asyncio.create_task(receive_messages())

        while True:
            try:
                message = input("You: ")
                if message:
                    await websocket.send(message)
            except websockets.ConnectionClosed:
                print("Connection closed by server.")
                break

if __name__ == "__main__":
    asyncio.run(chat_client())