import unittest
import sys

sys.path.append('C:/Users/pnorov/Desktop/-Python/6-classes')

from task_06_02 import Euro, Dollar, Ruble
e = Euro(5)
class TestCurrency(unittest.TestCase):
    def test_init(self):
        self.assertEqual(e.course, {'$': 1.2, '₽': 60, '€': 1})
        self.assertEqual(e.amount, 5)
        
    def test_str(self):
        self.assertEqual(str(e), '5€')
        
    def test_to(self):
        self.assertIsInstance(e.to(Dollar), Dollar)
        self.assertEqual(e.to(Dollar).amount, Dollar(6.0).amount)
        
    def test_Add(self):
        self.assertIsInstance(e + Dollar(10), Euro)
        self.assertEqual(round((e + Dollar(10)).amount, 2), 13.33)
        
    def test_radd(self):
        self.assertIsInstance(Dollar(10) + e, Dollar)
        self.assertEqual((Dollar(10) + e).amount, 16.0)
        
    def test_sub(self):
        self.assertIsInstance(e - Dollar(10), Euro)
        self.assertEqual(round((e - Dollar(10)).amount, 2), -3.33)
        
    def test_gt(self):
        self.assertFalse(e > Dollar(10))
        
    def test_ge(self):
        self.assertTrue(e >= Dollar(5))
        
    def test_truediv(self):
        self.assertIsInstance(e / 2, Euro)
        self.assertEqual((e / 2).amount, 2.5)
        
    def test_mul(self):
        self.assertIsInstance(e * 2, Euro)
        self.assertEqual((e * 2).amount, 10.0)
        
if __name__ == '__main__':
    unittest.main()