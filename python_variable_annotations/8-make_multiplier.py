#!/usr/bin/env python3
"""Add tuples"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a given multiplier."""
    def multiplier_function(n: float) -> float:
        return n * multiplier
    return multiplier_function
