import math
from collections import namedtuple
from functools import reduce
from   my_calc import *

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    SquareInfo = namedtuple('SquareInfo', ['perimeter', 'area', 'diagonal'])
    return SquareInfo(perimeter, area, diagonal)

# Пример использования функции:
side_length = 5
result = square(side_length)
print("Периметр:", result.perimeter)
print("Площадь:", result.area)
print("Диагональ:", result.diagonal)
print(square(10))


print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Task#2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

def print_named_arguments(**kwargs):
    for key, value in kwargs.items():
        # print(f"{key}: {value}")
        # print(f'{key}')
        # print(f'{value}')
        print(*kwargs.keys())
        print(*kwargs.values())
        # print(*kwargs.items())

# Пример использования функции:
print_named_arguments(name="John", last_name="Smith", age=35, position="web developer")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Task#3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

my_list = [20, -3, 15, 2, -1, -21]
new_l = sum(x for x in my_list if x > 0)
print(new_l)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Task#3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
result  = reduce ( lambda x, y :  x*y, [20, -3, 15, 2, -1, -21])
print(result)

my_list =  [20, -3, 15, 2, -1, -21]
result2 = reduce(lambda x, y: x * y, filter(lambda x: x > 0, my_list))
print(result2)
print(result2)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Task#4>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

import time

# Декоратор для измерения времени выполнения функции
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} выполнена за {execution_time:.2f} секунд")
        return result
    return wrapper

# Применяем декоратор к функции
@timing_decorator
def some_function():
    result = 0
    for i in range(1, 1000001):
        result += i
    return result

# Вызываем декорированную функцию
result = some_function()
print(f"Сумма чисел от 1 до 1,000,000 равна {result}")

def my_decorator(func):
    def wrapper():
        print("До выполнения функции")
        func()
        print("После выполнения функции")
    return wrapper

# Используем декоратор с помощью символа @
@my_decorator
def say_hello():
    print("Привет, мир!")

# Вызываем функцию, к которой применен декоратор
say_hello()

print("<<<<<<<<<<<<<<<<<<<<<<Example>>>>>>>>>>>>>>>>>>>>>>>>>")
# Декоратор для логирования вызовов функции и результатов
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызывается функция {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Результат функции {func.__name__}: {result}")
        return result
    return wrapper

# Применяем декоратор к функции
@logging_decorator
def add(a, b):
    return a + b

@logging_decorator
def multiply(x, y):
    return x * y

# Вызываем функции
result1 = add(3, 5)
result2 = multiply(2, 4)
print("<<<<<<<<<<<<<<<<<<<<<<Task # 6>>>>>>>>>>>>>>>>>>>>>>>>>")

# from my_calc import *
import my_calc

sum = add(5,8)
sub = subtract(10, 89)
mult = multiply(5, 20)
dived = divide(8,2)

# print(f"Сложение: 5 + 8 = {sum}")
# print(f"Вычитание: 10 - 4 = {sub}")
# print(f"Умножение: 6 * 7 = {mult}")
# print(f"Деление: 8 / 2 = {dived}")

sum_result = my_calc.add(5, 8)
sub_result = my_calc.subtract(10, 89)
mult_result = my_calc.multiply(5, 20)
div_result = my_calc.divide(8, 2)

print(f"Сложение: 5 + 8 = {sum_result}")
print(f"Вычитание: 10 - 89 = {sub_result}")
print(f"Умножение: 5 * 20 = {mult_result}")
print(f"Деление: 8 / 2 = {div_result}")




