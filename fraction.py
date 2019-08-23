import math
from fractions import Fraction as FT


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
        # Prevent string, float or any type that is not float
        if isinstance(numerator, (int)) is False:
            raise TypeError(
                "Numerator must be whole number")
        if isinstance(denominator, (int)) is False:
            raise TypeError(
                "Denominator must be whole number")
        if denominator == 0:
            self.value = math.nan
            self.numerator = int(numerator)
            self.denominator = int(denominator)
        else:
            self.numerator = int(numerator)
            self.denominator = int(denominator)
            self.value = self.numerator/self.denominator

    def __str__(self):
        if self.denominator == 0:
            return f"{math.nan}"
        else:
            if self.value == 0:
                return "0"
            else:
                numerator, denominator = self.make_simplest_form()
                if self.check_negative():
                    if self.check_whole(denominator):
                        return f"-{abs(numerator)}"
                    else:
                        return f"-{abs(numerator)}/{abs(denominator)}"
                else:
                    if self.check_whole(denominator):
                        return f"{numerator}"
                    else:
                        return f"{numerator}/{denominator}"

    def make_simplest_form(self):
        """transform fraction into it's simplest form
        """
        if self.value == math.nan:  # python not allow division by zero
            pass
        else:  # convert fraction to it's simplest from through gcd
            gcd = math.gcd(self.numerator, self.denominator)
            numerator = int(self.numerator/gcd)
            denominator = int(self.denominator/gcd)
            return numerator, denominator

    def check_negative(self):
        """metohd to check is the fraction is whole number or not
        """

        if self.value < 0:
            return True
        elif self.value > 0:
            return False

    def check_whole(self, denominator):
        """metohd to check is the fraction is whole number or not
        """
        if denominator == 1:
            return True
        elif denominator == -1:
            return True
        else:
            return False

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        # call fraction library in order to convert decimal to fraction
        result = FT(self.value+frac.value)
        return Fraction(result.numerator, result.denominator)

    def __mul__(self, frac):
        """Return the product of two fractions as a new fraction.
           Use the standard formula  a/b * c/d = ac/bd
        """
        # call fraction library in order to convert decimal to fraction
        result = FT(self.value*frac.value)
        return Fraction(result.numerator, result.denominator)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        if self.value == frac.value:
            return True
        else:
            return False
