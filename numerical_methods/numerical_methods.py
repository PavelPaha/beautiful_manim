import math
from prettytable import PrettyTable

class NumericalMethodsTester:

    f = lambda self, x: math.sin(x) + 0.1 - 1.4 * x ** 2
    epsilon = 0.5 * 10 ** (-4)
    root = 0.7456928328435

    def devf(self, x, delta=1e-5):
        return (self.f(x + delta) - self.f(x)) / delta

    # Метод Ньютона
    def newton_method(self, x):
        table = PrettyTable(['n', 'x_n', '|x_n - root|', 'f(x_n)'])
        print("Метод Ньютона")
        iterations = 0
        while abs(x - self.root) >= self.epsilon:
            table.add_row([iterations, x, abs(x - self.root), self.f(x)])
            x = x - self.f(x) / self.devf(x)
            iterations += 1
        table.add_row([iterations, x, abs(x - self.root), self.f(x)])
        print(table)
        print(f'Потрачено итераций - {iterations}, приближение корня равно {x}')

    def modified_newton_method(self, x):
        print("Модифицированный метод Ньютона")
        table = PrettyTable(['n', 'x_n', '|x_n - root|', 'f(x_n)'])
        x_0 = x
        iterations = 0
        while abs(x - self.root) >= self.epsilon:
            table.add_row([iterations, x, abs(x - self.root), self.f(x)])
            x = x - self.f(x) / self.devf(x_0)
            iterations += 1
        table.add_row([iterations, x, abs(x - self.root), self.f(x)])
        print(table)
        print(f'Потрачено итераций - {iterations}, приближение корня равно {x}')

    def binary_search(self, a, b, depth, table):
        c = (a + b) / 2
        table.add_row([depth, a, b, c, abs(a - b), self.f(c)])
        if abs(a - b) < self.epsilon:
            return
        if self.f(c) * self.f(a) < 0:
            self.binary_search(a, c, depth + 1, table)
        else:
            self.binary_search(c, b, depth + 1, table)

    def half_division_method(self, a, b):
        print("Метод половинного деления")
        table = PrettyTable(['n', 'a', 'b', 'c', '|a-b|', 'f(c)'])
        self.binary_search(a, b, 0, table)
        print(table)

    def run_test(self):
        print(self.f(10000))
        self.newton_method(1)
        print()
        self.modified_newton_method(1)
        self.half_division_method(0, 10000)


test = NumericalMethodsTester()
test.run_test()
