#!/usr/bin/env python3
"""Documented"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Return a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

""" if __name__ == "__main__":
    print(asyncio.run(wait_random(4)))
 """
