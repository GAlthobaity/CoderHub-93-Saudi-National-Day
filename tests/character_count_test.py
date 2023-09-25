import unittest
import unittest
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Majd.character_count import character_count

class TestCharacterCount(unittest.TestCase):
    def test_word1(self):
        word = 'aabbbcccc'
        self.assertEqual(character_count(word), 'a2b3c4')

    def test_word2(self):
        word = 'abc'
        self.assertEqual(character_count(word), 'a1b1c1')

    def test_word3(self):
        word = 'Hello'
        self.assertEqual(character_count(word), 'e1h1l2o1')

    def test_word4(self):
        word = 'aabbcc'
        self.assertEqual(character_count(word), 'a2b2c2')

if __name__ == '__main__':
    unittest.main()