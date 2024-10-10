#!/usr/bin/env python3

'''
Obtain a dictionary value securely with a key
Return the default value if the key is missing.
'''

from typing import TypeVar, Union, Mapping, Any

T = TypeVar('T')
dict_type = Mapping
key_type = Any
def_type = Union[T, None]
ret_type = Union[Any, T]


def safely_get_value(
    dct: dict_type,
    key: key_type,
    default: def_type = None
        ) -> ret_type:
    '''
    Function for securely obtaining a dictionary value from a key
    Args:
        dct (dict): the dictionary to lookup a value
        key (string): the key we want to lookup
        default (Any): the default value to return if no key
    Returns:
        Returns dict[key] if key in dict.keys()
        else; returns default
    '''
    if key in dct:
        return dct[key]
    else:
        return default
