#!/usr/bin/env python3
"""Documented"""

import importlib
from typing import List

basic_async_syntax = importlib.import_module("0-async_generator")
async_generator = basic_async_syntax.async_generator

# The async_comprehension coroutine
async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using an async comprehension."""
    return [number async for number in async_generator()]
