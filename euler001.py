"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solution(n: int) -> int:
    fsum = []
    for i in range(1, n):
        if i % 3 == 0:
            fsum.append(i)
        elif i % 5 == 0:
            fsum.append(i)
    return sum(fsum)


if __name__ == "__main__":
    print(solution(1000))
