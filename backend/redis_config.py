import redis.asyncio as redis

global redis_client

redis_client = redis.Redis(host="localhost" , port= 6379 , decode_responses=True)