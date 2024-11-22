#!/usr/bin/env python3
"""Module containing the async_generator coroutine."""

import asyncio
import random
from typing import Generator, NoneType


async def async_generator() -> Generator[float, NoneType, NoneType]: # type: ignore
    """Yield 10 random floats between 0 and 10 asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
