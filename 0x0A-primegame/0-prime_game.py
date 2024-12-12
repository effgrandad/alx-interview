#!/usr/bin/python3
"""
module of determining a winner of prime game
"""

def isWinner(x, nums):
    """
    Determine the Winner
    Args:
        x (int): Number
    """
    if not nums or x < 1:
        return
    
    max_num = max(nums)

    # draw a list to mark prime numbers
    is_prime = [True for _ in range(max(max_num + 1, 2))]
    for prime_candidate in range(2, int(pow(max_num, 0.5)) + 1):
        if not is_prime[prime_candidate]:
            continue
        for multiple in range(prime_candidate * prime_candidate,
                              max_num + 1, prime_candidate):
            is_prime[multiple] = False
    is_prime[0] = is_prime[1] = False

    # Count prime numbers up to each number
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
