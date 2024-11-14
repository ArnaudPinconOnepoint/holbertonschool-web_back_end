#!/usr/bin/env python3
"""Add tuples"""


from typing import Tuple


def to_kv(k: str, v: float | int) -> Tuple[str, float]:
    """tuple"""
    return (k, v * v)
