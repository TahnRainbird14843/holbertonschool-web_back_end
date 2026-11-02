#!/usr/bin/env python3

"""
this is documented
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    result = []
    generator = await async_generator
    for i in generator:
        result.append(i)
    return result
