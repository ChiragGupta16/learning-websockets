import asyncio
import websockets

async def hello():
    url = "ws://localhost:9551"
    async with websockets.connect(url) as websocket:
        message = "Hello, Server!"
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received response: {response}")   

if __name__ == "__main__":
    asyncio.run(hello())

