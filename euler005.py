"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

if __name__ == "__main__":
    """
    Idea: Multiply all prime numbers between 1 and 20 
    to the highest power that is less than or equal to 20
    """
    print(2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)
