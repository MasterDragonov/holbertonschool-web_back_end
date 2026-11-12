#!/usr/bin/env python3
import random
import asyncio

async def wait_random() -> float:
    max_delay = 10
    await asyncio.sleep(random(0, max_delay))