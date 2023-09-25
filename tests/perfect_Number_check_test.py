import unittest
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Amal.perfect_Number_check import perfect_Number_check

class TestPerfectNumberCheck(unittest.TestCase):
    def test_perfect_numbers(self):
        self.assertTrue(perfect_Number_check(6))
        self.assertTrue(perfect_Number_check(28))
    
    def test_non_perfect_numbers(self):
        self.assertFalse(perfect_Number_check(12))
        self.assertFalse(perfect_Number_check(14))

if __name__ == '__main__':
    unittest.main()