import websockets
import asyncio

async def echo(websocket,path):

    print("Client connected")

    try:
        async for message in websocket:
            print(f"Message received : {message}")
            await websocket.send("HI")
            print("Reply sent")

    except websockets.ConnectionClosed as e:
        print("Client disconnected")


async def main():
    server = await websockets.serve(echo,"localhost",9551)
    print("server started on ws://localhost:9551")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
