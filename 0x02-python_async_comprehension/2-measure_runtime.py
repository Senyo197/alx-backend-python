#!/usr/bin/env python3

""" Measure Routine """

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that executes async_comprehension four times in parallel using
    asyncio.gather.
    """
    time_started = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - time_started
