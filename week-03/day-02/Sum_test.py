import unittest
from Sum import sum

class TestClassSum(unittest.TestCase):

    def setUp(self):
        self.test_list = [1,2,3,4,5]

    def test_sum(self):
        self.assertEqual(sum([1,2,3,4,5]), 15)

if __name__ == '__main__':
    unittest.main()
    