#!/usr/bin/env python3

'''
annotate function
With Union types
'''


from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Sum a list of mixed values (int and floats)
    '''
    return float(sum(mxd_lst))
