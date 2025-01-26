"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def is_pythogorean_triplet(a: int, b: int, c: int) -> bool:
    return a**2 + b**2 == c**2


def solution() -> int:
    for c in range(999, 1, -1):
        for b in range(1000 - c, 1, -1):
            for a in range(1000 - b - c, 1, -1):
                if is_pythogorean_triplet(a=a, b=b, c=c):
                    if a + b + c == 1000:
                        product = a * b * c
                        break
    return product


if __name__ == "__main__":
    print(solution())
