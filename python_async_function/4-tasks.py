#!/usr/bin/env python3

"""
this is documented
"""

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """complete and return n random waits"""
    tasks = set()

    for _ in range(n):
        tasks.add(task_wait_random(max_delay))

    result = []

    for task in asyncio.as_completed(tasks):
        result.append(await task)

    return (result)
