from fastapi import FastAPI , WebSocket
import asyncio
from starlette.websockets import WebSocketDisconnect

from redis_config import redis_client
from price_stimulation import poll_prices

app = FastAPI()

@app.get('/check_fastapi')
def check():
    return {"Fastapi is running"}


@app.on_event("startup")
async def fetch_data_yahoo():
    redis_client
    asyncio.create_task(poll_prices())


@app.websocket("/ws/price")
async def websocket_connection(websocket : WebSocket):
    await websocket.accept()

    try:
        while True:
            price = await redis_client.get("RELIANCE.NS")
            if price:
                await websocket.send_json({"RELIANCE.NS": price})
                await asyncio.sleep(2)
    except WebSocketDisconnect as e:
        print("Client disconnected")
