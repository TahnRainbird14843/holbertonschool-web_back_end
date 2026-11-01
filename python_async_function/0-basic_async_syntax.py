#!/usr/bin/env python3

"""
this is documented
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait a random amount then return the wait"""
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return (wait)
