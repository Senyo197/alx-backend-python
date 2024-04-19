#!/usr/bin/env python3
"""Augmented the code with the correct duck-typed annotations"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ return first element or None """
    if lst:
        return lst[0]
    else:
        return None
