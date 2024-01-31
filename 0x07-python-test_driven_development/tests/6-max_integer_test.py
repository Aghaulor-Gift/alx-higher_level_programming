#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -5, -8, -3]), -3)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 5, -8, 3]), 5)

    def test_duplicate_max_values(self):
        self.assertEqual(max_integer([1, 3, 5, 5, 2, 4]), 5)

    def test_single_value(self):
        self.assertEqual(max_integer([10]), 10)

    def test_all_equal_values(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

if __name__ == '__main__':
    unittest.main()
