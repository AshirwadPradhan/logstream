import websockets
import asyncio
import datetime
import random

async def show_time(websocket: websockets.WebSocketServerProtocol):
    while True:
        message = datetime.datetime.utcnow().isoformat()
        await websocket.send(message)
        await asyncio.sleep(random.random()*2 + 1)


async def main():
    async with websockets.serve(show_time, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())