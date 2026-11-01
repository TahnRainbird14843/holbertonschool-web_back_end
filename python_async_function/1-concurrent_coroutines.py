#!/usr/bin/env python3

"""
this is documented
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """complete and return n random waits"""
    tasks = set()

    for _ in range(n):
        tasks.add(asyncio.create_task(wait_random(max_delay)))

    result = []

    for task in asyncio.as_completed(tasks):
        result.append(await task)

    return (result)
