"""
Task:
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i^2.
"""


def square_number(n):
    for i in range(n):
        print(i ** 2)


num = int(input())
square_number(num)
