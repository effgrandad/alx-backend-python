#!/usr/bin/env python3

'''
use of docstring to get the job done
'''

from typing import Sequence, Any, Union

lst_type = Sequence[Any]
return_type = Union[Any, None]


def safe_first_element(lst: lst_type) -> return_type:
    '''
    Get the first element in a sequence safely
    If the there's no elements, return None
    Args:
        lst (list): A list of elements of any type
    Returns:
        if  element != None; Return first element
        else return None
    '''
    if lst:
        return lst[0]
    else:
        return None
