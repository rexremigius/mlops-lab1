import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator

class TestCalculator(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(calculator.sqrt(4), 2)
        self.assertEqual(calculator.sqrt(0), 0)

    def test_degree_to_radian(self):
        self.assertAlmostEqual(calculator.degree_to_radian(180), 3.14159, places=5)
        self.assertEqual(calculator.degree_to_radian(0), 0)

    def test_radian_to_degree(self):
        self.assertAlmostEqual(calculator.radian_to_degree(3.14159), 180, places=5)
        self.assertEqual(calculator.radian_to_degree(0), 0)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 0), 1)
        self.assertEqual(calculator.power(10, 2), 100)

if __name__ == '__main__':
    unittest.main()