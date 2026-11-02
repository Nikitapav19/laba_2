import numpy as np
import sympy as sym
from scipy.differentiate import derivative
from scipy.optimize import minimize


class SciPyPractice:
    def __init__(self, student_num=18):
        self.x0 = 2
        self.a = 1
        self.b = 6

    def f(self, x):
        return np.log(np.sqrt(x))

    def derivative(self):  # 1
        print("Задание 1")

        d1 = derivative(self.f, self.x0).df  # df для вывода числа
        d2 = derivative(lambda x: derivative(self.f, x).df, self.x0).df

        print(f"Первая производная: {d1}")
        print(f"Вторая производная: {d2}")

    def sympy_derivative(self):  # 2
        print("\nЗадание 2")

        x = sym.Symbol('x')
        y = sym.log(sym.sqrt(x))
        dy = sym.diff(y, x)

        print(f"Исходная функция: {y}")
        print(f"Символьная производная: {dy}")

    def integral(self):
        print("\nЗадание 3")

        n = 5000  # Кол-во прямоуов
        h = (self.b - self.a) / n  # Ширина прямоуга

        x_points = np.linspace(self.a + h / 2, self.b - h / 2, n)  # linspace создает n точек от а+пол шага до b-пол шага
        y_values = self.f(x_points)

        integral_value = h * np.sum(y_values)  # площадь
        print(f"Приближенное значение интеграла: {integral_value}")

    def sympy_integral(self):
        print("\nЗадание 4")

        x = sym.Symbol('x')
        y = sym.log(sym.sqrt(x))

        integ = sym.integrate(y, x)

        print(f"Исходная функция: y = {y}")
        print(f"Неопределенный интеграл: {integ} + C")

    def optimization(self):
        print('\nЗадание 5')

        def func(var):
            x1, x2 = var
            return (x1 - 3)**2 + (x2 - 1)**2

        cons = (  # ineq - нер-во, fun - функция сама наша
            {'type': 'ineq', 'fun': lambda y: -2*y[0] + y[1] - 2},  # -2x1 + x2 >= 2
            {'type': 'ineq', 'fun': lambda y:  3*y[1] - 10}         # 3x2 >= 10
        )

        bounds = ((0, None), (0, None))  # неотриц-ть
        x_start = [1.0, 4.0]

        result = minimize(func, x_start, method='SLSQP', bounds=bounds, constraints=cons)

        if result.success:
            print(f"Оптимальное решение: x1 = {result.x[0]:}, x2 = {result.x[1]:}")
            print(f"Оптимальное значение функции: {result.fun:}")
        else:
            print("Оптимизация не удалась:", result.message)


if __name__ == "__main__":
    lab = SciPyPractice()
    lab.derivative()
    lab.sympy_derivative()
    lab.integral()
    lab.sympy_integral()
    lab.optimization()