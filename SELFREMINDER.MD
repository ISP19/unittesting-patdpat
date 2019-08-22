Problem 1. listutil

The starter code for listutil.py describes the unique function.

    Write the code for unique. See below for examples.
    In README.md write a table of test cases to thoroughly test the code. You should test:
        1.borderline cases, such as a list with 0 or 1 elements
        2.typical cases, such as a list with a few duplicates or no duplicates
        3.an impossible case where the method should not work.
        4.extreme case, such as a very large list
    Write the tests using Python unittest. The test file should be listutil_test.py. Each test case is a separate method.
    Run the tests until your code passes them all.

Announcement
Please allow Fraction(0,0) as valid fraction.
Allow Fraction(n, 0) where n is any integer, including 0.
Don't throw exception. This enables your Fraction class
to handle "extended numbers". If you want to practice
throwing and test for exception, then throw exception
in constructor if the parameters are not "int".

\*\*\* python unittest example
https://docs.python.org/2/library/unittest.html

import unittest
from listutil import unique

class ListUtilTest(unittest.TestCase):

    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']) )

    #put each test case in seperate method

if **name** == '**main**':
unittest.main()

111111111111111111111111111111111111111111111111111111111111111111111111111111

Problem 2. Fraction and FractionTest
The Fraction class and operator overloading will be discussed in class.

Write a Fraction class that performs exact arithmetic using fractions. Here are some examples:

Python lets you define operators like +, -, _, /, and unary minus (-f) methods for your own classes, called operator overloading. You can also overload relational operators like a==b, a<b, a>=b. You do this by defining special methods in your class:
Operator Syntax Method invoked
f + g **add**(f,g)
f - g **sub**(f,g)
f _ g **mul**(f,g)
-f **neg**(f)
f == g **eq**(f,g)

When you write f+g, python invokes **add**(self,g) where self=f. Each of these methods returns a new Fraction, except **eq** which returns boolean. For example:

class Fraction:

    def __add__(self, frac):
        """Add two fractions and return the sum as a new Fraction"""
        numerator =        # compute numerator of self + frac
        denominator =      # compute denominator of self + frac
        return Fraction(numerator, denominator)

    Write these methods in the Fraction class:

Method Name Meaning
**init**(num,denom=1) Constructor sets fraction numerator and denominator in proper form. Default value of denominator is 1.
**add**(self,frac) add fractions self and frac
**mul**(self,frac) multiply fractions self and frac
**str**(self) return fraction as a string, such as "3/4" or "2" (if denominator=1)
**eq**(self,frac) test if two fractions have same value, self == frac

    The constructor should always store a Fraction in proper form. This means:
        numerator and denominator have no common factors
        denominator is always positive or zero.
        Fraction(3,0) has numerator=1 and denominator=0.
        Hint: Python has a function math.gcd() you can use to remove the greatest common denominator. math.gcd(a,b) is always positive unless a and b are both 0.
    __str__ should return fraction as a string, such as “2/3” or “4” (if fraction has denominator 1 then return as integer).
    __eq__ is true if fractions have the same value.
        Example: Fraction(3,4) == Fraction(-9,-12) should be True.
        If constructor always stores fractions in proper form, then this method is easy.
    Write unittests for all methods, including the constructor.

Example Test Cases in README.md

You should design your own test cases. Can you think of anything not should here?
Tests for unique
Test case Expected Result
empty list empty list
one item list with 1 item
one item many times list with 1 item
2 items, many times, many orders list with each item only once
argument not a list throws exception
