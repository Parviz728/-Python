import numpy as np

class Matrix:
    """
        Класс для реализации действий с матрицами.

        Args:
            *args: Переменное число аргументов.
                Если передан один аргумент, считается, что это двумерный список матрицы.
                Если переданы два аргумента: 1- количество строк, 2 - количество столбцов.

        Attributes:
            matr (np.array): Матрица
    """
    def __init__(self, *args, **kwargs):
        self.matr = []
        if len(args) == 1: # если введен один аргумент       
            self.matr = np.array(args[0])
        else: # если аргкментов несколько
            # надо проверить что введенно ровно два целых числа, иначе косяк
            if len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
                self.matr = np.random.rand(args[0], args[1])
    
          
    @staticmethod
    def __verify_operation(operation: str, matr1, matr2):
        """
        Args:
            operation (str): математическая операция
            matr1 (Matrix): первая матрица
            matr2 (Matrix): вторая матрица

        Raises:
            ArithmeticError: _description_
            ArithmeticError: _description_
            AttributeError: _description_
            TypeError: _description_
        """
        if isinstance(matr1, Matrix) and isinstance(matr2, Matrix):
            if operation == '+' or operation == '-':
                if matr1.matr.shape != matr2.matr.shape:
                    raise ArithmeticError("Обе матрицы должны быть одинакового размера")
            elif operation == '*':
                if matr1.matr.shape[1] != matr2.matr.shape[0]: # количество столбцов первой матрицы должно быть равно количеству строк второй матрицы
                    raise ArithmeticError("Нельзя умножить такие матрицы")
            else:
                raise AttributeError("это не математическая операция")
        else:
            raise TypeError("операнды должны матрицами")
        
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matr])
    
    def __add__(self, other):
        """
        Сложение двух матриц
        Args:
            other (_type_:Matrix): Вторая матрица

        Returns:
            _type_: Matrix
        """
        self.__verify_operation('+', self, other)
        return Matrix(self.matr + other.matr)
    
    def __sub__(self, other):
        """
        Функция вычитания
        Args:
            other (_type_:Matrix): Вторая матрица

        Returns:
            _type_: Matrix
        """
        self.__verify_operation('-', self, other)
        return Matrix(self.matr - other.matr)
    
    def __mul__(self, other):
        """
        Функция умножения
        Args:
            other (_type_:Matrix): Вторая матрица

        Returns:
            _type_: Matrix
            _description: Возвращается матрица произведения
        """
        self.__verify_operation('*', self, other)
        return Matrix(self.matr * other.matr)
    
    def transp(self):
        """
        Returns:
            _type_: Matrix
            _description_: Транспонированная матрица
        """
        return self.matr.transpose()
        
    def __eq__(self, other):
        """

        Args:
            other (_type_:Matrix): Вторая матрица

        Raises:
            TypeError: _description_

        Returns:
            _type_: bool
            _description_: равны ли матрицы
        """
        if not isinstance(other, Matrix):
            raise TypeError("справа должна быть матрица")
        return np.array_equal(self.matr, other.matr)
    
    def is_square(self):
        """

        Returns:
            _type_: bool
            _description_: Квадратная ли матрица
        """
        return self.matr.shape[0] == self.matr.shape[1]
    
    def is_symetric(self):
        """_summary_

        Returns:
            _type_: bool
            _description_: Симметрична ли матрица
        """
        return np.array_equal(self.transp(), self.matr)
    
m = Matrix([[1,2], [3, 4]])
n = Matrix([[1,1], [1, 0]])
print(m + n)
            
            
        
