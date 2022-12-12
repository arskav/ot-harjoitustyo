import unittest
from services.calculator import calculator

class TestUtitities(unittest.TestCase):

    def test_calculator(self):

        self.assertEqual(calculator("(2+3)*3 - 10 / 2"), 10)
        self.assertEqual(calculator(""), None)
        self.assertEqual(calculator("(2+3)**3 - 10 / 2"), None)
        self.assertEqual(calculator("2++3)*3 - 10 / 2"), None)
        self.assertEqual(calculator("x + 2"), None)

