#!/usr/bin/env python3
"""Added type annotations to the function"""
from typing import Any, Union, Mapping, Optional, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """returns map key value"""
    if key in dct:
        return dct[key]
    else:
        return default
