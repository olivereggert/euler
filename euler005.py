#! /usr/bin/env python
#
# ProjectEuler.net - problem #005
#
# Summary: 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?

import sys
import math

class BruteForce:

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

    @staticmethod
    def solve(max):
        result = max
        while True:
            if BruteForce.check(result):
                print result
                break

            result += 20

    @staticmethod
    def check(n):
        for i in range(11, 21):
            if not n % i == 0:
                return False

        return True

class Primes:

    def __init__(self, max):
        self.max = max
        self.squares = []
        self.gen_squares(max)

        self.result = dict()

    def gen_squares(self, input):
        print "Generating square numbers smaller than %d" % input
        i = 2
        while True:
            temp = i * i
            if temp > input:
                return

            self.squares.append(temp)
            i += 1

    def factorize(self, input):

        # can't compute prime factors of non-positive numbers
        if input <= 0:
            raise ArithmeticError("Supplied arguments must be greater than 0")

        # the first two numbers are prime themselves
        if input <= 2:
            return [input]

        # a number that is divisable by two has two as one prime factor
        # and uses the function recursively
        if input % 2 == 0:
            temp = [2]
            for f in self.factorize(input/2):
                temp.append(f)
            return temp

        # when factorize is called recursively some factors might
        # already be known
        # ex. factorize(6) will result in calling factorize(3)
        if input in self.result:
            return self.result[input]

        # use fermat's method to generate factors
        x = math.sqrt(input)
        x = math.ceil(x)

        r = x*x - input
        # has been added to deal with numbers that are product
        # of two primes (eg 9)
        if r == 0:
            return [int(x), int(x)]

        while not r in self.squares:
            # has been added to stop checking once the resulting
            # prime factor would exceed the number we're checking
            # if no factors have been found than the number itself
            # is prime
            if r > input**2:
                return [input]

            r = r + 2*x + 1
            x += 1

        y = math.sqrt(r)
        a = int(x + y)
        b = int(x - y)

        if a == 1:
            return [b]
        elif b == 1:
            return [a]
        else:
            return [a, b]

    def solve(self):
        for i in range(1, max + 1):
            self.result[i] = self.factorize(i)

        print "Found all the prime factors"
        for i in range(1, max + 1):
            print "%2d: %s" % (i, self.result[i])

        # iterate over all numbers from 1 .. max
        for i in range(2, max + 1):
            # check each factor
            for factor in self.result[i]:
                # iterate over all entries greater than the current entry
                for j in range(i + 1, max + 1):
                    # if it has this factor, remove it
                    if factor in self.result[j]:
                        self.result[j].remove(factor)

        print "I've thrown away those that occur multiple times:"
        total = 1
        for i in range(1, max + 1):
            print self.result[i]


if __name__ == "__main__":
    max = 20
    if "-bruteforce" in sys.argv:
        BruteForce.solve(max)
    elif "-primes" in sys.argv:
        primes = Primes(max)
        primes.solve()
    elif "-debug" in sys.argv:
        primes = Primes(max)
        print primes.factorize(10)
    else:
        print "use either -bruteforce or -primes"
