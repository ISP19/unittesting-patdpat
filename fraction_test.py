import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_init(self):
        f = Fraction(1, 2)
        j = Fraction(0, 1)
        h = Fraction(10000, 20001)
        l = Fraction(-1)
        # test type of numerator in constructor
        self.assertEqual(1, f.numerator)
        # test type of denominator in constructor
        self.assertEqual(2, f.denominator)
        # test str constructor representation
        self.assertFalse("1/2" == h.__str__())
        # test str constructor representation
        self.assertEqual("0", j.__str__())
        # test str constructor representation
        self.assertEqual("-1", l.__str__())

    def test_str(self):
        """test for str method
        """
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(1, 0)
        self.assertEqual("nan", f.__str__())

    def test_eq(self):
        """test for eq method"""
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)
        j = Fraction(0, 1)
        k = Fraction(1, 0)
        l = Fraction(-1, 0)
        z = Fraction(0, 2)
        # check definable fraction
        self.assertTrue(f == g)
        # same thing
        self.assertTrue(f.__eq__(g))
        # check zero
        self.assertTrue(j == z)
        # same thing
        self.assertTrue(j.__eq__(z))
        # check 0.5 and 0.4999
        self.assertFalse(f == h)
        # same thing
        self.assertFalse(f.__eq__(h))
        # check same value fraction
        self.assertTrue(j == Fraction(0, 2))
        # check division by zero on positive
        self.assertTrue(math.isnan(k.value))
        # check division by zero on negative
        self.assertTrue(math.isnan(l.value))

    def test_mul(self):
        """ test if fraction do correct multiplication
        """
        self.assertEqual(Fraction(3, 8), Fraction(3, 4)*Fraction(1, 2))
        self.assertEqual(Fraction(-3, 8), Fraction(-3, 4)*Fraction(1, 2))
        self.assertEqual(Fraction(-3, 8), Fraction(3, -4)*Fraction(1, 2))
        self.assertEqual(Fraction(3, -8), Fraction(3, -4)*Fraction(1, 2))
        self.assertEqual(Fraction(3, -8), Fraction(-3, 4)*Fraction(1, 2))
        self.assertEqual(Fraction(0, 1), Fraction(-3, 4)*Fraction(0))
        self.assertEqual(Fraction(1, 4), Fraction(-1, 2)*Fraction(-1, 2))

    def test_add(self):
        """test if fraction do correct addition
        """
        self.assertEqual(Fraction(1, 1), Fraction(3, 4)+Fraction(1, 4))
        self.assertEqual(Fraction(3, 4), Fraction(1)+Fraction(-1, 4))
        self.assertEqual(Fraction(-1), Fraction(-1, 4)+Fraction(-3, 4))
        self.assertEqual(Fraction(1, 2), Fraction(1, -4)+Fraction(3, 4))
        self.assertEqual(Fraction(0), Fraction(1, 4)+Fraction(3, -12))


if __name__ == '__main__':
    unittest.main()
