import unittest
from Anagram import anagram, word_to_dic

class TestFunctionAnagram(unittest.TestCase):

    def setUp(self):
        self.testing_word1 = "cinema"
        self.testing_word2 = "iceman"
        self.word = "acanian"
        self.word_to_dic = {'c':1, 'i':1, 'n':2, 'a':3}
        self.result = True

    def test_anagram(self):
        self.assertEqual(anagram(self.testing_word1, self.testing_word2), self.result)

    def test_word_to_dic(self):
        self.assertEqual(word_to_dic(self.word), self.word_to_dic)

if __name__ == '__main__':
    unittest.main()