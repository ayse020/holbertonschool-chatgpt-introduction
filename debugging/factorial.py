#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.
    n: integer >= 0
    Returns: n! as integer
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1  # hər iterasiyada n-i azaldırıq
    return result

if len(sys.argv) < 2:
    print("Usage: ./factorial.py <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 0:
        print("Please enter a non-negative integer")
        sys.exit(1)
except ValueError:
    print("Please enter a valid integer")
    sys.exit(1)

f = factorial(n)
print(f"{n}! = {f}")

