import unittest
from Apple import Apple

class TestAppleClass(unittest.TestCase):

    def setUp(self):
        self.apple = Apple()

    def test_get_apple(self):
        self.assertEqual(self.apple.getApple(), "apple")

if __name__ == '__main__':
    unittest.main()