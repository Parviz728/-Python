import unittest
import sys
sys.path.insert(0, 'C:/Users/pnorov/Desktop/-Python/6-classes')

from task_06_01 import m, n, Matrix

class MatrixTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(m + n, Matrix([[2, 3], [4, 4]]))
        
    def test_sub(self):
        self.assertEqual(m - n, Matrix([[0, 1], [2, 4]]))
        
    def test_mul(self):
        self.assertEqual(m * n, Matrix([[3, 1], [7, 3]]))
        
    def test_eq(self):
        self.assertEqual(m == n, False)
        
    def test_is_square(self):
        self.assertEqual(m.is_square(), True)
        
    def test_is_symetric(self):
        self.assertEqual(m.is_symetric(), False)
        

        
        