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

*** python unittest example
import unittest
from listutil import unique
 
class ListUtilTest(unittest.TestCase):
 
    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']) )
 
if __name__ == '__main__':
    unittest.main()
