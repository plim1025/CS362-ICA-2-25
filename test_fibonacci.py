import unittest
import pytest
import sys
from fibonacci import factorial, fibonacci

class TestFibbonaci(unittest.TestCase):
    def test_fib1(self):
        self.assertEqual(fibonacci(1), 1)
    def test_fib4(self):
        self.assertEqual(fibonacci(4), 3)
    def test_fibString(self):
        self.assertEqual(fibonacci("sdaf"), None)
    def test_fibNeg(self):
        self.assertEqual(fibonacci(-8), None)
    def test_fac0(self):
        self.assertEqual(factorial(0), 1)
    def test_fac4(self):
        self.assertEqual(factorial(4), 24)
    def test_facString(self):
        self.assertEqual(factorial("asdfda"), None)
    def test_facNeg(self):
        self.assertEqual(factorial(-7), None)


if __name__ == '__main__':
    unittest.main()