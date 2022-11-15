import unittest

from src import add


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add.addition(1, 5), 6)
