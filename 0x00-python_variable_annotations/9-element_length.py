#!/usr/bin/env python3

'''
annotated function param 
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''function to access length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
