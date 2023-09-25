import unittest
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Amal.sum_numbers import sum_numbers

class TestSumNumbers(unittest.TestCase):
    def test_even_numbers(self):
        self.assertEqual(sum_numbers(5, 'زوجي'), 6)
        self.assertEqual(sum_numbers(10, 'زوجي'), 30)
    
    def test_odd_numbers(self):
        self.assertEqual(sum_numbers(15, 'فردي'), 64)
        self.assertEqual(sum_numbers(7, 'فردي'), 16)

if __name__ == '__main__':
    unittest.main()