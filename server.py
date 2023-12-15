import websockets
import asyncio
import datetime
import random

connections = set()

async def register(websocket: websockets.WebSocketServerProtocol):
    connections.add(websocket)
    try:
        await websocket.wait_closed()
        print("Connection closed")
    finally:
        connections.remove(websocket)

async def show_time():
    while True:
        message = datetime.datetime.utcnow().isoformat()
        websockets.broadcast(connections, message)
        await asyncio.sleep(random.random()*2 + 1)


async def main():
    async with websockets.serve(register, "localhost", 8765):
        await show_time()

if __name__ == "__main__":
    asyncio.run(main())