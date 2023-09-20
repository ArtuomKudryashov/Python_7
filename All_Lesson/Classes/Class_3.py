# lst = [10, 'Hello', None, False,25,  True, 26.5, 25]
# print(lst.count(25))
# print(lst.index(True))
# lst2 = [x for  x in lst if isinstance(x, int)]
# print(len(lst2))
# print(lst2)
# print(lst)
# print(lst[0])
# print(lst[-6])
# print(len(lst))
# print(id(lst))
# text = "Bye"
# lst.append(text)
# print(lst)
# print(id(lst))
# lst[-2]=100
# print(lst)
# print(id(lst))
# lst.reverse()
# print(lst)
# print(id(lst))
# lst2 = []
# for i in lst:
#     if isinstance(i, int):
#         lst2.append(i)
# print(lst2)
# print(sum(lst2))

# lst = [1,2,3,4,5,6]
# lst2 = []
# for number in lst:
#     if number % 2 ==0:
#         lst2.append(number*number)
# print(lst2)
#
# lst3 = [num*num for num in lst if num % 2 == 0 ]
# print(lst3)
# my_tuple = 1,2,3
# print(type(my_tuple))
#
# my_tuple2= ("Lemon", "Mango", "aple", "cherry")
# print(type(my_tuple2))
# print(my_tuple2)
#
# lst = list(my_tuple2)
# lst[0]="orange"
# my_tuple2 = tuple(lst)
# print(my_tuple2)
#
# lst1 =list(my_tuple2)
# lst1[2] = "WaterMelon"
# my_tuple2=tuple(lst1)
# print(my_tuple2)
#
# # my_tuple3= ("Lemon",)
# # print(type(my_tuple3))
#
# # my_tuple2[0]=('Test',)
# print(my_tuple)
#
# def  sum_it(*args):
#     return sum(args)
#
# print(sum_it(2,5,8,25))
# print(sum_it(2,5,8,25,2,5,8,25))
# lst = [1,2,3,4,5,6]
# lst.reverse()
# print(lst)
# lst.sort()
# print(lst)
#  # DICTIONARIES
# my_dict ={
#     "name":'Anna',
#     'last_name':'Pavlova',
#     'age':30,
#     'department':'IT'
#
# }
#
# my_dict2= {
#     'name':'Alex',
#     'last_name':'Smith',
#     'age':25,
#     'dep':'Dev'
# }
# print(my_dict2)
# print(my_dict2['name'])
# print(my_dict2['last_name'])
# my_dict2['dep']='IT'
# print(my_dict2.values())
# print(my_dict2.keys())
# print(my_dict2.items())
# print(len(my_dict2))

# def keywords(**kwardgs):
#     return kwardgs
#
# print(keywords(name="Alice", last_name = 'Petrova'))
#
# my_list =[1,2,5,8,10,12,10,12]
# print(my_list)
# my_set =  list(set(my_list))
# print(my_set)

# # # SETS
# print(set([1, 8, 2, 1, 5, 8, 9]))
#
# set1 = {1, 2, 3, 'one', 'ten'}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# set3 = {1, 2, 3}
# print(set1)
# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))
# print(set1)
# set1.remove(1)
# print(set1)
# set1.add(8)
# print(set1)
# #
# fs = frozenset({1, 2, 3})
# print(fs[1])
# print(fs)
# fs.remove(1)
# print(fs)
#
# fs.add(4)
# print(fs)

my_dict = {
    "name": 'Anna',
    'last_name': 'Pavlova',
    'age': 30,
    'department': 'IT'
}

my_dict['salary'] = 5000
print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.pop('salary'))
print(my_dict)
print(my_dict.get('salary', 'Not found'))
