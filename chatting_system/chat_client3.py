import asyncio
import websockets

async def chat_client():
    url = "ws://localhost:9551"
    async with websockets.connect(url) as websocket:
        print("Connected to server")

        async def receive_messages():
            async for message in websocket:
                print(f"Server : {message}")

        receive_task = asyncio.create_task(receive_messages())

        while True:
            message = input("You :")
            await websocket.send(message)

if __name__ == "__main__":
    asyncio.run(chat_client())