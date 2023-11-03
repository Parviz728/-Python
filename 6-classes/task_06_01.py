from random import randint

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
            self.matr = list(args[0])
        else: # если аргкментов несколько
            # надо проверить что введенно ровно два целых числа, иначе косяк
            if len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
                self.matr = [[randint(1, 10) for i in range(args[1])] for _ in range(args[0])]
        
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
        if not isinstance(other, Matrix):
            raise TypeError("операнд должен быть матрицей")
        else:
            if len(self.matr) == len(other.matr) and len(self.matr[0]) == len(other.matr[0]):
                rows = len(self.matr)
                cols = len(self.matr[0])
                res = [[0] * cols for _ in range(rows)] # создаем пустую матрицу того же размеры что матрицы операнды
                for row in range(rows):
                    for col in range(cols):
                        res[row][col] = self.matr[row][col] + other.matr[row][col]
                return Matrix(res)
            else:
                raise ValueError("матрицы должны быть одинакового размера")
                        
                        
    
    def __sub__(self, other):
        """
        Вычитание двух матриц
        Args:
            other (_type_:Matrix): Вторая матрица

        Returns:
            _type_: Matrix
        """
        if not isinstance(other, Matrix):
            raise TypeError("операнд должен быть матрицей")
        else:
            if len(self.matr) == len(other.matr) and len(self.matr[0]) == len(other.matr[0]):
                rows = len(self.matr)
                cols = len(self.matr[0])
                res = [[0] * cols for _ in range(rows)] # создаем пустую матрицу того же размеры что матрицы операнды
                for row in range(rows):
                    for col in range(cols):
                        res[row][col] = self.matr[row][col] - other.matr[row][col]
                return Matrix(res)
            else:
                raise ValueError("матрицы должны быть одинакового размера")
    
    def transp(self):
        """
        Returns:
            _type_: Matrix
            _description_: Транспонированная матрица
        """
        res = [
                [
                    self.matr[col][row] for col in range(len(self.matr))
                ] for row in range(len(self.matr[0]))
            ]
        return res
    
    def __mul__(self, other):
        """
        Функция умножения
        Args:
            other (_type_:Matrix): Вторая матрица

        Returns:
            _type_: Matrix
            _description: Возвращается матрица произведения
        """
        if not isinstance(other, Matrix):
            raise TypeError("операнд должен быть матрицей")
        else:
            if len(self.matr[0]) == len(other.matr):
                rows = len(self.matr)
                cols = len(other.matr[0])
                res = [[0] * cols for _ in range(rows)]
                for row in range(rows):
                    for col in range(cols):
                        for k in range(cols):
                            res[row][col] += self.matr[row][k] * other.matr[k][col]  
                return Matrix(res)
            else:
                raise ValueError("матрицы не подходят по размеру")
                        
        
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
        for row in range(len(self.matr)):
            for col in range(len(self.matr[0])):
                if self.matr[row][col] != other.matr[row][col]:
                    return False
        return True
    
    def is_square(self):
        """

        Returns:
            _type_: bool
            _description_: Квадратная ли матрица
        """
        return len(self.matrix) == len(self.matrix[0])
    
    def is_symetric(self):
        """_summary_

        Returns:
            _type_: bool
            _description_: Симметрична ли матрица
        """
        if not self.is_square():
            return False
        for row in range(len(self.matr)):
            for col in range(len(self.matr[0])):
                if self.matr[row][col] != self.matr[col][row]:
                    return False
        return True
    
m = Matrix([[1,2], [3, 4]])
n = Matrix([[1,1], [1, 0]])
print(m * n)
            
            
        
