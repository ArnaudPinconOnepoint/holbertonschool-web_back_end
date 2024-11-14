#!/usr/bin/env python3
"""Annote"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Return a list of tuples"""
    return [(i, len(i)) for i in lst]
