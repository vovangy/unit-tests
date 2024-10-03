import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    
    def test_add_float(self):
        self.assertEqual(self.calculator.addition(1.2, 2.1), 3.3)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
    
    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.multiplication(1, 0), 0)

    def test_multiplication_float(self):
        self.assertEqual(self.calculator.multiplication(2.4, 3), 2.4 * 3)

def addition_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculator('test_add'))
    suite.addTest(TestCalculator('test_add_float'))
    return suite

def multiplication_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCalculator('test_multiplication'))
    suite.addTest(TestCalculator('test_multiplication_zero'))
    suite.addTest(TestCalculator('test_multiplication_float'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()

    print("Running addition tests:")
    runner.run(addition_suite())

    print("\nRunning multiplication tests:")
    runner.run(multiplication_suite())