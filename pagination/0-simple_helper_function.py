#!/usr/bin/env python3
"""Pagination"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """Return a tuple containing the start and end indexes for a page."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
