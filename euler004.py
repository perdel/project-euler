"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from typing import List, Tuple


def boundaries(digit_length: int = 3) -> Tuple:
    left, right = 9 * 10 ** (digit_length - 1), 10**digit_length
    return left, right


def pallindrom(digit_length: int = 3) -> List[int]:
    left, right = boundaries(digit_length)
    pal = [int(str(i) + str(i)[::-1]) for i in range(left, right)]
    return pal


def find_largest(pallindroms: List[int], digit_length: int = 3):
    left, right = boundaries(digit_length)
    for p in pallindroms:
        for j in range(left, int(0.5 * (left + right) + 1)):
            if p % j == 0 and p / j < right:
                return (j, int(p / j))


if __name__ == "__main__":
    P = pallindrom(3)
    val1, val2 = find_largest(P, 3)
    print(val1 * val2)
