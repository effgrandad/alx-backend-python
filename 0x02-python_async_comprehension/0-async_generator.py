#!/usr/bin/env python3

'''
A module featuring an async generator that
creates arbitrary numbers ranging from 1 to 10.
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generates a sequence of 10 numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
