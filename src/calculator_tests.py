import unittest
from Calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate(
            ['0', '+', '3']), 3, "Should be 3")

    def test_float_inputs(self):
        calculator = Calculator()
        self.assertEqual(calculator.calculate(
            ['0.001', '*', '1000']), 1, "Should be 1")

    def test_substract_from_result(self):
        calculator = Calculator()
        calculator.calculate(['0', '+', '3'])
        self.assertEqual(calculator.calculate(
            ['r', '-', '0']), 3, "Should be 3")

    def test_substract_by_result(self):
        calculator = Calculator()
        calculator.calculate(['0', '+', '3'])
        self.assertEqual(calculator.calculate(
            ['6', '-', 'r']), 3, "Should be 3")

    def test_zero_division(self):
        try:
            calculator = Calculator()
            calculator.calculate(['4', '/', '0'])
        except ZeroDivisionError:
            self.fail("Division by 0 not handled")


if __name__ == '__main__':
    unittest.main()
