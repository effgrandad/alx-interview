#!/usr/bin/python3
"""
module that determines a winner of prime game
"""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    # Create a list to identify prime numbers
    is_prime = [True for _ in range(max(max_num + 1, 2))]
    for prime_candidate in range(2, int(pow(max_num, 0.5)) + 1):
        if not is_prime[prime_candidate]:
            continue
        for multiple in range(prime_candidate * prime_candidate,
                              max_num + 1, prime_candidate):
            is_prime[multiple] = False
    is_prime[0] = is_prime[1] = False

    # Up to each integer, count the prime numbers.
    prime_counts = [0] * len(is_prime)
    count = 0
    for index, prime_status in enumerate(is_prime):
        if prime_status:
            count += 1
        prime_counts[index] = count

    player1 = 0
    for num in nums:
        player1 += prime_counts[num] % 2 == 1

    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
