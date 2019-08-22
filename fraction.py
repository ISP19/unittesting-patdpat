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
        if isinstance(numerator, (int, float)) is False:
            raise TypeError(
                "Numerator must be whole or floating point numbers ")
        if isinstance(denominator, (int, float)) is False:
            raise TypeError(
                "Denominator must be whole or floating point numbers ")
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator},{self.denominator}"

    def make_simplest_form(self):
        """transform fraction into it's simplest form
        """
        pass

    # TODO Write the __add__ method, and remove this TODO comment.

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        pass

    # TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    # Optional have fun and overload other operators such as
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator


# a = 1.1
# b = 0
# c = Fraction(a, b)
# print(c)
if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
