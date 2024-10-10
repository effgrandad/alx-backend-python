#!/usr/bin/env python3

'''
annotated module that return another module
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Creates a multiplier function.
    '''
    return lambda x: x * multiplier
