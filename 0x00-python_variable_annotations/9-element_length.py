#!/usr/bin/env python3

'''
annotated function param 
'''

from typing import Iterable, List, Sequence, Tuple

lst_type = Iterable[Sequence]
return_type = List[Tuple[Sequence, int]]


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    function to access length of a list of sequences
    Args:
        lst (list): A list of elements
    Returns:
        Returns a list
    '''
    return [(i, len(i)) for i in lst]
