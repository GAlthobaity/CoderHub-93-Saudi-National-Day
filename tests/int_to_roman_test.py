import unittest
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Namaa.int_to_roman import int_to_roman

class TestIntToRoman(unittest.TestCase):
    def test_num1(self):
        self.assertEqual(int_to_roman(1), 'I')

    def test_num2(self):
        self.assertEqual(int_to_roman(2), 'II')

    def test_num3(self):
        self.assertEqual(int_to_roman(6), 'VI')

    def test_num4(self):
        self.assertEqual(int_to_roman(23), 'XXIII')

if __name__ == '__main__':
    unittest.main()