#!/usr/bin/env python3
"""Documented"""

import asyncio
import importlib
import time

basic_async_syntax = importlib.import_module("1-async_comprehension")
async_comprehension = basic_async_syntax.async_comprehension


# The async_comprehension coroutine
async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel and measure total runtime."""
    start_time = time.perf_counter()

    # Run async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    return end_time - start_time
