#!/usr/bin/env python3
"""
Basic async syntax
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that
    waits for a random delay between 0 and max_delay (included and float value)
    seconds and eventually returns it.
    """
    random_wait_time = random.random() * max_delay
    await asyncio.sleep(random_wait_time)
    return random_wait_time
