import unittest
import sys

sys.path.append('C:/Users/pnorov/Desktop/-Python/6-classes')

from task_06_02 import Euro, Dollar, Ruble
e = Euro(5)
class TestCurrency(unittest.TestCase):
    """
    Класс тестирования абстрактного класса
    """
    def test_init(self):
        """
        Проверка инициализатора
        Return None:
        """
        self.assertEqual(e.course, {'$': 1.2, '₽': 60, '€': 1})
        self.assertEqual(e.amount, 5)
        
    def test_str(self):
        """
        Проверка __str__
        Return None:
        """
        self.assertEqual(str(e), '5€')
        
    def test_to(self):
        """
        Проверка метода to()
        Return None:
        """
        self.assertIsInstance(e.to(Dollar), Dollar)
        self.assertEqual(e.to(Dollar).amount, Dollar(6.0).amount)
        
    def test_Add(self):
        """
        Проверка сложения валют
        Return None:
        """
        self.assertIsInstance(e + Dollar(10), Euro)
        self.assertEqual(round((e + Dollar(10)).amount, 2), 13.33)
        
    def test_radd(self):
        """
        Проверка сложения валют
        Return None:
        """
        self.assertIsInstance(Dollar(10) + e, Dollar)
        self.assertEqual((Dollar(10) + e).amount, 16.0)
        
    def test_sub(self):
        """
        Проверка вычитания валют
        Return None:
        """
        self.assertIsInstance(e - Dollar(10), Euro)
        self.assertEqual(round((e - Dollar(10)).amount, 2), -3.33)
        
    def test_gt(self):
        """
        Проверка на >
        Return None:
        """
        self.assertFalse(e > Dollar(10))
        
    def test_ge(self):
        """
        Проверка на >=
        Return None:
        """
        self.assertTrue(e >= Dollar(5))
        
    def test_truediv(self):
        """
        Проверка на деление
        Return None:
        """
        self.assertIsInstance(e / 2, Euro)
        self.assertEqual((e / 2).amount, 2.5)
        
    def test_mul(self):
        """
        Проверка на умножение
        Return None:
        """
        self.assertIsInstance(e * 2, Euro)
        self.assertEqual((e * 2).amount, 10.0)
        
if __name__ == '__main__':
    unittest.main()