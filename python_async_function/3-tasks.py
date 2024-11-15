#!/usr/bin/env python3
"""Documented"""

import asyncio
import importlib

basic_async_syntax = importlib.import_module("0-basic_async_syntax")
wait_random = basic_async_syntax.wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return a asyncio.Task object"""
    return asyncio.create_task(wait_random(max_delay))


"""
async def main():
    max_delay = 10
    task = task_wait_random(max_delay)
    delay = await task
    print(f"Task completed with a delay of {delay} seconds")

if __name__ == "__main__":
    asyncio.run(main())
 """
