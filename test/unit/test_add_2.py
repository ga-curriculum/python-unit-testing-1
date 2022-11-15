import unittest
from src import add_2


class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(add_2.add(2, 5), 10)


if __name__ == '__main__':
    unittest.main()
