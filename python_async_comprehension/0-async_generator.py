import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
        
""" async def main():
    async for number in async_generator():
        print(number)

asyncio.run(main()) """
