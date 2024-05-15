#!/usr/bin/python3
"""defining a prime numbers game"""


def isWinner(x, nums):
    """determines the winner of the prime numbers game"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def play_game(n):
    """Play ia single game of prime number removal."""
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    maria_turn = True
    while prime_set:
        if maria_turn:
            for p in primes:
                if p in prime_set:
                    prime_set -= {i for i in prime_set if i % p == 0}
                    break
                else:
                    for p in primes:
                        if p in prime_set:
                            prime_set -= {i for i in prime_set if i % p == 0}
                            break
                maria_turn = not maria_turn
            return "Maria" if maria_turn else "Ben"
    maria_wins = sum(1 for n in nums if play_game(n) == "Maria")
    return "Maria" if maria_wins > x / 2 else "Ben" if maria_wins < x / 2 else None
