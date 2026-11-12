#!/usr/bin/env python3
"""Module for a coroutine that takes an integer arg"""
import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_value"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay