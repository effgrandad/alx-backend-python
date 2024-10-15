#!/usr/bin/env python3

'''
A module that can also produce random numbers
'''

from typing import List
async_generator = __import__('0-async_generator').async_generator


return_type = List[float]


async def async_comprehension() -> return_type:
    '''
    Returns some 10 random numbers based on the
    other function defined in the previous module
    '''
    return [num async for num in async_generator()]
