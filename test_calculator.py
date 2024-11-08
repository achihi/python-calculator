import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(9, 3), 6)
        self.assertEqual(self.calc.subtract(8, 3), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(7, 2), 14)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)


    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(5, 0)


if __name__ == '__main__':
    unittest.main()
