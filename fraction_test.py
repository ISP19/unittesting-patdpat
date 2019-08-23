import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
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

    # TODO Write tests for __init__, __eq__, +, *.
    # Here is an example, but you must add more test cases.
    # The test requires that your __eq__ is correct.
    # def test_add(self):
    #     # 3/4 = 2/3 + 1/12
    #     self.assertEqual(Fraction(3, 4), Fraction(1, 12)+Fraction(2, 3))

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

    def test_eq(self):
        f = Fraction(1, 2)
        g = Fraction(-40, -80)
        h = Fraction(10000, 20001)
        j = Fraction(0, 1)
        k = Fraction(1, 0)
        l = Fraction(-1, 0)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertTrue(j == Fraction(0, 2))
        self.assertTrue(math.isnan(k.value))
        self.assertTrue(math.isnan(l.value))
        # TODO write more tests using other cases.
    #  Consider special values like 0, 1/0, -1/0


if __name__ == '__main__':
    unittest.main()
