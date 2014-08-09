#! /usr/bin/env python
#
# ProjectEuler.net - problem #005
#
# Summary: 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?

import sys

# x is divisable by 20 -> x is divisable by 2, 4, 5, 10
# x is divisable by 19 ->
# x is divisable by 18 -> x is divisable by 2, 3, 6, 9
# x is divisable by 17 ->
# x is divisable by 16 -> x is divisable by 2, 4, 8
# x is divisable by 15 -> x is divisable by 3, 5
# x is divisable by 14 -> x is divisable by 2, 7
# x is divisable by 13 -> 
# x is divisable by 12 -> x is divisable by 2, 6
# x is divisable by 11 ->
# 10 through 2 are already covered, no point checking for 1

def check(n):
    #print "checking %d" % n
    for i in range(11, 21):
        if not n % i == 0:
            return False

    return True

def main():
    
    result = 20
    while(True):
        if check(result):
            print result
            return

        result = result + 20

if __name__ == "__main__":
    main()
