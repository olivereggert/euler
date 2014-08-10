#! /usr/bin/env python
# coding=utf-8
#
# ProjectEuler.net - problem #006
#
# Summary: The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

import sys

def main():
    allsquares = 0
    allsums = 0
    for i in range(1, 101):
        allsquares += i**2
        allsums += i

    allsums = allsums**2

    print "sum of squares: %d" % allsquares
    print "square of sums: %d" % allsums
    print "difference: %d" % (allsums - allsquares)

if __name__ == "__main__":
    main()
