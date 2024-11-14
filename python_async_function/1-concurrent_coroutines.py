#!/usr/bin/env python3

import asyncio
import importlib
import heapq

basic_async_syntax = importlib.import_module("0-basic_async_syntax")
wait_random = basic_async_syntax.wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn wait_random n times with max_delay and return delays in ascending order."""
    delays = []
    # Spawn `wait_random` n times and gather results
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        print(delay)
        heapq.heappush(delays, delay)  # Use heapq to keep delays in order

    return [heapq.heappop(delays) for _ in range(n)]  # Pop in ascending order

""" # For testing
if __name__ == "__main__":
    n = 5
    max_delay = 10
    print(asyncio.run(wait_n(n, max_delay)))
 """