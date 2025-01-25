"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""


def is_prime(a: int) -> bool:
    return not (a < 2 or any(a % x == 0 for x in range(2, int(a**0.5) + 1)))


def solution(nmax: int) -> int:
    idx = 0
    n = 1
    primes = []
    while idx < nmax:
        if is_prime(n):
            primes.append(n)
            idx += 1
        n += 1
    return n - 1


if __name__ == "__main__":
    print(solution(10001))
