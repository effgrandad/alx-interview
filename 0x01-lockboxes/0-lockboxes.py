#!/usr/bin/python3

"""
The answer to the interview question about lockboxes
is provided in this module
"""

from typing import List


def canUnlockAll(boxes: List[List]) -> bool:
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing box and keys
    Returns:
        bool: True if all the boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list):
        raise TypeError('Boxes should be a list')

    key_list = [0]
    for key in key_list:
        for h in boxes[key]:
            if h not in key_list and h < len(boxes):
                key_list.append(h)
    for x in range(len(boxes)):
        if x not in key_list:
            return False
    return True
