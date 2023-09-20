# print("<<<<<<<<<<<<<<<<<<<<<Task1>>>>>>>>>>>>>>>>>>>>>>>>")
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2][0])
# print(my_list[2][1])
# print(my_list[2][2])
# print(my_list[0])
# print(my_list[1])
# print(my_list[3])
# print(my_list[2])
# print("<<<<<<<<<<<<<<<<<<<<<Task2>>>>>>>>>>>>>>>>>>>>>>>>")
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# lst2 = [x for x in list_1 if isinstance(x, int)]
# # print(sum(lst2))
# print(lst2)
# print(*lst2)

# sum_of_num = 0
# for item in list_1:
#     if isinstance(item,int):
#         sum_of_num += item
# print("Сумма всех чисел:", sum_of_num)
#
# for item in list_1:
#     if isinstance(item,str) and  'a' in item:
#         print(item)
#
#
# for digit in list_1:
#     if isinstance( digit, int):
#         print( digit, end = " ")
#         # print()
#
# print()

# print("<<<<<<<<<<<<<<<<<<<<<Task3>>>>>>>>>>>>>>>>>>>>>>>>")
# my_list = ['cat', 'dog', 'horse', 'cow']
# my_tuple = tuple(my_list)
# print(my_tuple)
# print("<<<<<<<<<<<<<<<<<<<<<Task4>>>>>>>>>>>>>>>>>>>>>>>>")
# Ввод информации о первой семье
# family_1 = input("Введите членов первой семьи, разделяя их запятыми: ").split(',')

# Ввод информации о второй семье
# family_2 = input("Введите членов второй семьи, разделяя их запятыми: ").split(',')
# print(family_1)
# print(family_2)
#
# # Определение количества членов в каждой семье
# count_family_1 = len(family_1)
# count_family_2 = len(family_2)
# #
# # Сравнение количества членов семей и вывод результата
# if count_family_1 > count_family_2:
#     print("Семья 1 больше")
# elif count_family_2 > count_family_1:
#     print("Семья 2 больше")
# else:
#     print("Equal")
# #
# print("<<<<<<<<<<<<<<<<<<<<<Task5>>>>>>>>>>>>>>>>>>>>>>>>")
# film = {
#     "title": "Фокус",
#     "director": "Гленн Фикарра, Джон Рекуа",
#     "year": 2015,
#     "budget": 50000000,
#     "main_actor": "Уилл Смит",
#     "slogan": "Never Drop the Con."
# }
# print(film.keys())
# print(film.values())
# print(film.items())
# print("<<<<<<<<<<<<<<<<<<<<<Task6>>>>>>>>>>>>>>>>>>>>>>>>")
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))
#
# print("<<<<<<<<<<<<<<<<<<<<<Task7>>>>>>>>>>>>>>>>>>>>>>>>")
# my_list = [1, 2, 3, 4, 5, 3, 2, 1]
# my_set = list(set(my_list))
# print(my_set)
#
print("<<<<<<<<<<<<<<<<<<<<<Task8>>>>>>>>>>>>>>>>>>>>>>>>")
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set2.issuperset(set1))
# print(set1.issuperset(set2))
print(set2.intersection(set1))
print(set2.difference(set1))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))