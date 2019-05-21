from Sharpie import Sharpie
import unittest

class TestClassSharpie(unittest.TestCase):

    def setUp(self):
        self.s1 = Sharpie("red", 100)
        self.s2 = Sharpie("blue", 1000, 500)

    def test_init(self):
        self.assertEqual(self.s1.color, "red")
        self.assertEqual(self.s2.width, 1000)
        self.assertEqual(self.s1.ink_amount, 100)

    def test_use(self):
        self.s1.use()
        self.assertEqual(self.s1.ink_amount, 99)

if __name__ == '__main__':
    unittest.main()