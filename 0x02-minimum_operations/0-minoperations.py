#!/usr/bin/python3

'''
Module for the interview question in the third round
The bare minimum of actions
'''


def minOperations(n: int) -> int:
    '''
     Determine the minimum opeartions to run
    Args:
        n (int):
    Returns:
        Returns an int
    '''
    if n <= 1:
        return 0
    num, div, numOfOperations = n, 2, 0

    while num > 1:
        if num % div == 0:
            num = num / div
            numOfOperations = numOfOperations + div
        else:
            div += 1
    return numOfOperations
