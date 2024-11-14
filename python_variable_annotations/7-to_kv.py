#!/usr/bin/env python3
"""Add tuples"""


from typing import Union


def to_kv(k: str, v: float | int) -> Union[str, float]:
    """tuple"""
    return (k, v * v)
