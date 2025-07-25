import unittest
from calculator import add, subtract, multiply

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
    def test_subtract(self):
        self.assertEqual(subtract(5,2),3)
    def test_add(self):
        self.assertEqual(multiply(2,3),6)

if __name__=='__main__':
    unittest.main()