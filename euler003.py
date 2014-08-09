#! /usr/bin/env python
#
# ProjectEuler.net - problem #003
#
# Summary: The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import sys
from sets import Set
import time
import math

n = 600851475143
queue = [n]
factors = Set([])

def debug(message):
    if debug_enabled:
        print message

# fermat's factorization method.
# see http://de.wikipedia.org/wiki/Faktorisierungsmethode_von_Fermat
def factorize(input):
    x = math.sqrt(input)
    x = math.ceil(x)

    r = x*x - input
    debug("checking if %d is square" % r)
    while not r in squares:
        r = r + 2*x + 1 
        x = x + 1

    y = math.sqrt(r)
    a = x + y
    b = x - y
    
    return a, b

def primesFound(x, y):
    factors.add(x)
    factors.add(y)
    debug("found that both %d and %d are primes" % (x, y))

def output(factors):
    print "The prime factors of %d are:" % n,
    for x in sorted(factors):
        print int(x), 

def main():
    while len(queue) > 0:
        candidate = queue.pop()
        debug("checking %d" % candidate)
        (a, b) = factorize(candidate)
        if a == 1:
            primesFound(candidate, b)
        elif b == 1:
            primesFound(candidate, a)
        else:
            queue.append(a)
            queue.append(b)
            debug("%d can be factored into %d and %d" % (candidate, a, b))

    output(factors)

# generates all square numbers that are smaller than the number we're trying to
# find prime factors for. While this is kinda brute-force-ish it runs
# reasonably fast (< 0.5s on this machine.)
def genSquares():
    
    squares = Set([])
    i = 2
    result = 0
    while result < n:
        result = i * i
        i = i + 1
        squares.add(result)
    
    return squares

if __name__ == "__main__":

    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        debug_enabled = True
    else:
        debug_enabled = False
    
    squares = genSquares()
    main()
