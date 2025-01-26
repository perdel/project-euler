"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def is_prime(a: int) -> bool:
    return not (a < 2 or any(a % x == 0 for x in range(2, int(a**0.5) + 1)))


def solution(nmax: int) -> int:
    primes = [i for i in range(nmax + 1) if is_prime(a=i)]
    return sum(primes)


if __name__ == "__main__":
    print(solution(nmax=2_000_000))
