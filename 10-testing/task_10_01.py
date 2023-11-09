import unittest
import sys
sys.path.append('C:/Users/pnorov/Desktop/-Python/6-classes')

from task_06_01 import m, n, Matrix

class MatrixTest(unittest.TestCase):
    """
    класс тестирования матриц
    """
    def test_add(self):
        """
        Сложение матриц
        Return: None
        """
        self.assertEqual(m + n, Matrix([[2, 3], [4, 4]]))
        
    def test_sub(self):
        """
        Вычитание матриц
        Return: None
        """
        self.assertEqual(m - n, Matrix([[0, 1], [2, 4]]))
        
    def test_mul(self):
        """
        Произведение матриц
        Return: None
        """
        self.assertEqual(m * n, Matrix([[3, 1], [7, 3]]))
        
    def test_eq(self):
        """
        Равенство матриц
        Return: None
        """
        self.assertFalse(m == n)
        
    def test_is_square(self):
        """
        Проверка матрицы на квадратичность
        Return: None
        """
        self.assertTrue(m.is_square())
        
    def test_is_symetric(self):
        """
        Проверка матрицы на симметричность
        Return: None
        """
        self.assertFalse(m.is_symetric())
        
if __name__ == '__main__':
    unittest.main()
        
        