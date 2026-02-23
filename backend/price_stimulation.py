import asyncio
import yfinance as yf

from redis_config import redis_client

ticker = yf.Ticker("RELIANCE.NS")

def get_price():
    return ticker.info["regularMarketPrice"]


async def poll_prices():
    while True:
        try:
            price_polled = await asyncio.to_thread(get_price)
            await redis_client.set("RELIANCE.NS" , price_polled)
            price = await redis_client.get("RELIANCE.NS")
            print(price)

        except Exception as e:
            print(f"some error occured {e}")

        await asyncio.sleep(2)