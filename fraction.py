import math


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """

    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        if type(numerator) is not int:  # prevent string or float in numerator
            raise TypeError("Type of numberator must be int")
        if type(denominator) is not int:  # prevent string or float in denominator
            raise TypeError("Type of denominator must be int")
        if denominator == 0:  # prevent division by zero
            raise ValueError(
                "Division by zero is undefined in ordinary arithmetic.")
        else:
            self.numerator = numerator
            self.denominator = denominator
            self.make_simplest_form()

    def make_simplest_form(self):
        """method to convert any fraction to simplest form
        theory of using gcd to simplest form from https://www.chilimath.com/lessons/introductory-algebra/simplifying-fractions/            
        """
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator/gcd
        self.denominator = self.denominator/gcd

    def make_decimal(self):
        """method to convert fraction to decimal form
        """
        decimal_form = self.numerator/self.denominator
        return decimal_form

    def check_negative(self):
        """method to check the value return true if it's value is negative
        """
        return True if self.make_decimal() < 0 else False:

    def check_negative(self):
        """method to check the value return true if it's value is positive
        """
        return True if self.make_decimal() > 0 else False:

    def check_zero(self):
        """method to check the value return true if it's value is zero
        """
        return True if self.make_decimal() == 0 else False:

    def __str__(self):
        """Return string form of fraction
        """

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        # from given formula a/b + c/d = (ad+bc)/(b*d) these are variables that require
        # to put into formula
        a = int(self.numerator)
        b = int(self.denominator)
        c = int(frac.numerator)
        d = int(frac.denominator)
        result_numerator = a*d+b*c
        result_denominator = b*d
        return Fraction(result_numerator, result_denominator)

    # TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    # Optional have fun and overload other operators such as
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)
    def __mul__(self, frac):
        """Return the  product of multiplication of two fraction as a new fraction.
        """
        # formula for calculate fraction multiplication is a/b * c/d = ac/bd
        # from above formula a/b * c/d = ac/bd these are variables that require
        # to put into formula

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator
