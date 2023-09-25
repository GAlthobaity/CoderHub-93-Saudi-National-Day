import unittest
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Namaa.largest_result import expression

class TestExpression(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(expression(1, 2, 3), 9)

    def test_case2(self):
        self.assertEqual(expression(1, 3, 2), 8)

    def test_case3(self):
        self.assertEqual(expression(3, 4, 2), 24)

    def test_case4(self):
        self.assertEqual(expression(5, 2, 1), 15)

if __name__ == '__main__':
    unittest.main()