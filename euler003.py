"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from math import floor, sqrt
from typing import List


def fac(n: int) -> List[int]:
    """Based on Rosetta code prime decomposition"""

    def step(x):
        return 1 + (x << 2) - ((x >> 1) << 1)

    maxq = floor(sqrt(n))
    d = 1
    q = 2 if n % 2 == 0 else 3
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return [q] + fac(n // q) if q <= maxq else [n]


def solution(n: int) -> int:
    return max(fac(n))


if __name__ == "__main__":
    print(solution(600851475143))
