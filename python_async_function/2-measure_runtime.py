#!/usr/bin/env python3
"""Documented"""

import asyncio
import importlib
import time

concurrent_coroutines = importlib.import_module("1-concurrent_coroutines")
wait_n = concurrent_coroutines.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay) and return total_time / n."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    
    total_time = end_time - start_time
    return total_time / n

""" if __name__ == "__main__":
    n = 5
    max_delay = 10
    print(measure_time(n, max_delay)) """
