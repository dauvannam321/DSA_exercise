# https://vjudge.net/problem/UVA-10341
# eduardo_petry's solution for [UVA-10341] [Problem D]
from math import e, sin, cos, tan
from sys import stdin

def f(x):
    return p * e ** -x + q * sin(x) + r * cos(x) + s * tan(x) + t * x ** 2 + u

def bisection():
    low, high = 0, 1

    while low + 1e-7 < high:
        x = (low + high) / 2
        if f(low) * f(x) <= 0: high = x
        else: low = x

    return (low + high) / 2

for line in stdin:
    p, q, r, s, t, u = map(int, line.split())
    if f(0) * f(1) > 0:
        print("No solution")
    else:
        print("{:.4f}".format(bisection()))

'''
0 0 0 0 -2 1
1 0 0 0 -1 2
1 -1 1 -1 -1 1
'''