# min_item = min(20, 15, 77, 100)
# print(min_item)
#
#
# def person(age, first_name, last_name):
#     return f'Hello, my name is {first_name}{last_name}.I am {age} years old'
#
#
# print(person(" Anna ", " Smith ", 25))
#
# print(person(first_name=" Anna ", last_name=" Smith ", age=25))
#
# print(person(first_name= " Bob ", last_name=" Smith ", age=25))
#
# print("<<<<<<<<<<<<<<<<<<<<<<<<<<<1>>>>>>>>>>>>>>>>>>>>>>>>>")
#
# # print(person(25, first_name= " Bob "))
#
# print("<<<<<<<<<<<<<<<<<<<<<<<<<<<2>>>>>>>>>>>>>>>>>>>>>>>>>")
#
# # print(person(25))
# # print("<<<<<<<<<<<<<<<<<<<<<<<<<<<3>>>>>>>>>>>>>>>>>>>>>>>>>")
# # # print(person(26))
#
# def pattern (length, char1="",char_2="*"):
#     return (char1+char_2)*length + char1
#
#
#
# print(pattern(char1='/',length=9))

# def decorator_function(func):
#     def wrapper(*args):
#         print("Wrapper function")
#         print(f'Calling function: {func. __name__}')
#         print (f'With arguments:{args}')
#         print('Wrapped function in process')
#         print((func(*args)))
#         print('Exiting wripper')
#     return wrapper
#
# @decorator_function
# def hello (item):
#     return f'{item} is wrapped '
#
# hello('candy')
#
# x = 15
# y = 25
#
# def sum_it(x, y):
#     print(f'local{locals()}')
#     return x +y
#
# print(f'Inside the function: {sum_it(10,18)}')
# print(f'Outside the function:{x+y}')
# print(f'Globals:{globals()}')

# name = "Alice"
# def outer_function():
#
#     def inner_function():
#         name = "Alex"
#         return  name
#     return  inner_function
#
# closure = outer_function()
# result = closure()
#
# print(result)
#
#
# name = "Alice"
# def outer_function():
#     name = 'Albert'
#
#     def inner_function():
#
#         return  name
#     return  inner_function
#
# closure = outer_function()
# result = closure()
#
# print(result)
#
#
# name = "Alice"
# def outer_function():
#
#
#     def inner_function():
#
#         return  name
#     return  inner_function
#
# closure = outer_function()
# result = closure()
#
# print(result)


# result = lambda n: n*n;
# print(result(6))

# list_1 = ['Hi', 'ananas', 2 , None, 75, 'pizza', 36, 100]
# def filter_and_sum(lst):
#     new_l = []
#     for x in lst:
#         if isinstance(x, int):
#             new_l.append(x)
#     print(new_l)
#     return sum(new_l)
# print(filter_and_sum(list_1))
#
# new_l = sum(filter(lambda x: isinstance(x, int),list_1))
# print(new_l)
# print(list(filter(lambda x: isinstance(x, int),list_1)))
# filtered= list(filter(lambda x: isinstance(x, str),list_1))
# print(list(filter(lambda i: 'a' in i, filtered)))
#
# print(list(filter(lambda x: isinstance(x,str)and 'a' in x, list_1)))
#
#
# from functools import reduce
#
# result  = reduce ( lambda x, y :  x*y, [1, 5 , 8, 11, 13])
# print(result)
#
# result  = reduce ( lambda x, y :  x + y, [1, 5 , 8, 11, 13])
# print(result)
# result  = reduce ( lambda x, y :  x**y, [1, 5 , 8, 11, 13])
# print(result)
#
# result  = reduce ( lambda x, y :  x**y, [2, 5 , 8, 11, 13])
# print(result)

# print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Map>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#
# result = map (lambda  x: x**2, [2, 5 , 8, 11, 13] )
#
# print(result)
#
# result = list( map (lambda  x: x**2, [2, 5 , 8, 11, 13] ))
#
# print(result)

# print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Module>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#
# from math import prod
#
# l = [1,2,5,7]
#
# print(prod(l))
#
# import  math
#
# l = [1,2,5,7]
#
# print(math.prod(l))
#
# import  math as m
#
# l = [1,2,5,7]
#
# print(m.prod(l))
#
# import  math as m
# from math  import  *
# l = [1,2,5,7]
#
# print(prod(l))
from Class_4_myModule import *
result = sum_it (7, 8 )
result1= sum_it(15, 20)
#
# print(result)
import  Class_4_myModule as mm
result = mm.sum_it (7, 8 )
#
# print(result)
# from Class_4_myModule import *
#
# def tests():
#     assert  sum_it(5,8)==13, f'wrong number, actual  result  is {sum_it(5,8)}'
#     assert sum_it(10, 15) == 23, f'wrong number, actual  result  is {sum_it(10, 15)}'
#
# tests()
import datetime

birth_year  = 1984
current_date = datetime.date.today()
print(current_date)

current_age = current_date.year - birth_year
print(current_age)


