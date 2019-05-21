import unittest
from Sum import sum

class TestClassSum(unittest.TestCase):

    def setUp(self):
        self.test_list = [1,2,3,4,5]

    def test_empyt(self):
        self.assertEqual(sum([]), 0)
    
    def test_multiple_elements(self):
        self.assertEqual(sum([1,2,3,4,5]), 15)

    def test_none(self):
        self.assertEqual(sum(), 0)

    def test_one_element(self):
        self.assertEqual(sum([1]), 2)

if __name__ == '__main__':
    unittest.main()
    