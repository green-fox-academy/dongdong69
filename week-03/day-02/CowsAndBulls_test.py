import unittest
from CowsAndBulls import CowsAndBolls

class TestCAB(unittest.TestCase):

    def setUp(self):
        self.game = CowsAndBolls(1234)

    def test_a_guess(self):
        self.assertEqual(self.game.guess(5555), "0 cow, 0 bull")

    def test_c_guess(self):
        self.assertEqual(self.game.guess(4321), "0 cow, 4 bull")
        self.assertEqual(self.game.state, "playing")
        self.assertEqual(self.game.counter, 2)

    def test_b_guess(self):
        self.assertEqual(self.game.guess(1234), "4 cow, 0 bull")
        self.assertEqual(self.game.state, "finished")


if __name__ == '__main__':
    unittest.main()