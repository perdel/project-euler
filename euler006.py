"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


def sum_of_squares(n: int) -> int:
    return sum([i**2 for i in range(1, n + 1)])


def solution(n: int) -> int:
    sum_sq = sum_of_squares(n)
    sq_sum = sum(range(1, n + 1)) ** 2
    return sq_sum - sum_sq


if __name__ == "__main__":
    print(solution(100))
