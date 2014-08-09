#! /usr/bin/env python
#
# ProjectEuler.net - problem #004
#
# Summary: A palindromic number reads the same both ways. The largest
# palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from sets import Set
import math
import time

palindromes = Set([])
def isPalindrome(input):
    return input == input[::-1]

def output(x, before, after):
    print sorted(x)[-1]
    print "this took %.2fs" % (after - before)

# You can generate all numbers whose product we check in this brute force way.
def bruteForce():
    for i in range(1000, 100, -1):
        for j in range(1000, 100, -1):
            temp = i * j
            if(isPalindrome(str(temp))):
                palindromes.add(temp)

    return palindromes

def cantor(i):
    j = math.floor(math.sqrt(0.25 + 2 * i) - 0.5)
    x = j - (i - j*(j+1)/2)
    y = i - j*(j+1)/2

    return (int(x), int(y))

# You can also enumerate all pairs similar to how the cantor enumeration for
# proving that the rational numbers are enumerable works.
def cantorized():
    
    i = 0;
    x = 999;
    y = 999;

    while x >= 100 and y >= 100:
        c = cantor(i)
        x = 999 - c[0]
        y = 999 - c[1]
        temp = x * y
        if isPalindrome(str(temp)):
            return [temp]
        
        i = i + 1

    return []

def main():

    before = time.time()
    result = bruteForce()
    after = time.time()
    output(result, before, after)

    before = time.time()
    result = cantorized()
    after = time.time()
    output(result, before, after)

if __name__ == "__main__":
    main()
