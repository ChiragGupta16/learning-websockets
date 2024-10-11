import asyncio
import websockets
import os
 
 
async def get_user_input():
    return await asyncio.to_thread(input, "Enter your message: ")
 
 
async def send_messages(websocket):
    while True:
        message = await get_user_input()
        await websocket.send(message)
 
 
async def receive_messages(websocket):
    while True:
        try:
            async for response in websocket:
 
                os.system("clear")  # use cls rather than clear for shitdows
 
                print(f"Received message from server: {response}")
                print("Enter your message: ", end="", flush=True)
 
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed by server.")
            break
 
 
async def chat_client():
    uri = "ws://localhost:9551"
    async with websockets.connect(uri) as websocket:
        await asyncio.gather(send_messages(websocket), receive_messages(websocket))
 
 
if __name__ == "__main__":
    asyncio.run(chat_client())