import unittest
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Majd.find_missing_number import find_missing_number

class TestFindMissingNumber(unittest.TestCase):
    def test_case1(self):
        n = 5
        numbers = [3, 5, 4, 2]
        self.assertEqual(find_missing_number(n, numbers), 1)

    def test_case2(self):
        n = 3
        numbers = [1, 3]
        self.assertEqual(find_missing_number(n, numbers), 2)

    def test_case3(self):
        n = 7
        numbers = [1, 7, 5, 4, 2, 6]
        self.assertEqual(find_missing_number(n, numbers), 3)

    def test_case4(self):
        n = 10
        numbers = [2, 9, 8, 4, 1, 7, 10, 3, 6]
        self.assertEqual(find_missing_number(n, numbers), 5)

if __name__ == '__main__':
    unittest.main()