#!/usr/bin/env python3

"""
this is document
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension.py').async_comprehension


async def measure_runtime() -> float:
    tasks = set()

    for _ in range(4):
        tasks.add(asyncio.create_task(async_comprehension()))

    start = time.time()
    asyncio.gather(*tasks)
    end = time.time()

    return (end - start)
