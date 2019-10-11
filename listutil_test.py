import unittest
from listutil import unique

# You should test:
#         1.borderline cases, such as a list with 0 or 1 elements
#         2.typical cases, such as a list with a few duplicates or no duplicates
#         3.an impossible case where the method should not work.
#         4.extreme case, such as a very large list


class ListUtilTest(unittest.TestCase):
    """class use to test f(x) unique
    """

    def test_if_it_return_none(self):
        """test f(x) unique on impossible case (f(x) return none)
        """
        self.assertIsNotNone(unique([1]))

    def test_empty_list(self):
        """test f(x) unique on borderline case (0 item)
        """
        self.assertListEqual([], unique([]))

    def test_single_item_list(self):
        """test f(x) unique on borderline case (1 item)
        """
        self.assertListEqual(['hi'], unique(['hi']))

    def test_single_item_list_with_duplication(self):
        """test f(x) unique on typical case (1 item with duplicates)
        and check whether unique do a recursive scan at the same time
        """
        self.assertListEqual(['hi'], unique(['hi', 'hi']))
        self.assertListEqual([1], unique([1, 1]))
        self.assertListEqual([0.5], unique([0.5, 0.5, 0.5]))
        self.assertListEqual([1], unique([1, 1, 1, 1, 1, 1]))
        self.assertListEqual([[1, 2, 3]], unique([[1, 2, 3], [1, 2, 3]]))

    def test_multiple_items_list(self):
        """test f(x) unique on typical case (multiple item with no duplicates)
        """
        self.assertListEqual(['hi', 1,  0.63],
                             unique(['hi', 1, 0.63]))

    def test_multiple_items_list_with_duplication(self):
        """test f(x) unique on typical case (multiple item with duplicates)
        and check whether unique do a recursive scan at the same time
        """
        self.assertListEqual(['hi', 'ho'], unique(['hi', 'hi', 'ho']))
        self.assertListEqual([1, 2], unique([1, 1, 2, 2]))
        self.assertListEqual([0.5, 5], unique([0.5, 0.5, 0.5, 5, 5, 5]))
        self.assertListEqual([1, [1]], unique([1, 1, 1, 1, 1, 1, [1], [1]]))
        self.assertListEqual([[1, 2, 3], 1, 2, 3], unique(
            [[1, 2, 3], [1, 2, 3], 1, 2, 3, 1, 2, 3]))

    def test_huge_amount_of_items_list(self):
        """test f(x) unique on extreme case (very large list)
        """
        self.assertListEqual(self.generate_millions(),
                             unique(self.generate_millions()))

    def generate_millions(self):
        """method use to generate list of ten million items
            In theory python list can hold up to 536,870,912  items
            Ref.https://stackoverflow.com/questions/855191/how-big-can-a-python-list-get
        # """
        # big_boy = []
        # for i in range(10000000):
        #     big_boy.append(i)
        # return big_boy
        pass


if __name__ == '__main__':
    unittest.main()
