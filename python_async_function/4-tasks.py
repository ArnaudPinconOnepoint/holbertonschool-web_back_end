#!/usr/bin/env python3
"""Documented"""

import asyncio
import importlib
import heapq

tasks = importlib.import_module("3-tasks")
task_wait_random = tasks.task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn wait_random n times with max_delay and return delays in ascending order."""
    delays = []
    # Spawn `wait_random` n times and gather results
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        heapq.heappush(delays, delay)  # Use heapq to keep delays in order

    return [heapq.heappop(delays) for _ in range(n)]  # Pop in ascending order

# if __name__ == "__main__":
#     n = 5
#     max_delay = 6
#     print(asyncio.run(task_wait_n(n, max_delay)))