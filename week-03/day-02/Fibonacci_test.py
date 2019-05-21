import unittest
from Fibonacci import fibonacci

class TestFibonacciFunction(unittest.TestCase):
    
    def test_index_0(self):
        self.assertEqual(fibonacci(0), 0)
        
    def test_index_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_index_positive_int(self):
        self.assertEqual(fibonacci(9), 34)

if __name__ == '__main__':
    unittest.main()