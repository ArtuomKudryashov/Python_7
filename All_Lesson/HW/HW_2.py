# print("<<<<<<<<<<<<<<<<<<<<<Task1>>>>>>>>>>>>>>>>>>>>>>>>")
# health = -5
# if health > 0:
#     print(True)
# else:
#     print(False)
#
# print("<<<<<<<<<<<<<<<<<<<<<Task2>>>>>>>>>>>>>>>>>>>>>>>>")
#
# if health % 2 !=1:
#     print("Четное")
# else:
#     print("Нечетное")
# print("<<<<<<<<<<<<<<<<<<<<<Task3>>>>>>>>>>>>>>>>>>>>>>>>")
#
# currentYear = 1800
# if (currentYear % 4 == 0 and currentYear % 100 != 0) or (currentYear % 400 == 0):
#     print("Current year is Leap year")
# else:
#     print("Current year is not Leap year")

print("<<<<<<<<<<<<<<<<<<<<<Task4>>>>>>>>>>>>>>>>>>>>>>>>")
texts = input("Please, Type your  text  " )
numberOfRepeats = int(input("Please, Type numbersOfRepeats "))

separator = input("Please, Type your  separator  " )

print("<<<<<<<<<<<<<<<<<<<<<Task4a>>>>>>>>>>>>>>>>>>>>>>>>")
print((texts + ' ') * numberOfRepeats)
print("<<<<<<<<<<<<<<<<<<<<<Task4b>>>>>>>>>>>>>>>>>>>>>>>>")
result = (texts + separator) * (numberOfRepeats - 1) + texts
print(result)
print("<<<<<<<<<<<<<<<<<<<<<Task4c>>>>>>>>>>>>>>>>>>>>>>>>")
result = (texts + separator+'\n') * (numberOfRepeats - 1) + texts
print(result)
print("<<<<<<<<<<<<<<<<<<<<<Task4d>>>>>>>>>>>>>>>>>>>>>>>>")
result = (texts + separator + "  ") * (numberOfRepeats - 1) + texts
print(result)

# print("<<<<<<<<<<<<<<<<<<<<<Task4>>>>>>>>>>>>>>>>>>>>>>>>")
# first_number = int(input("Введите первое число: "));
# second_number = int(input("Введите первое число: "));
# arithmetical_sign = input("Введите арифметический знак: ");
# if arithmetical_sign == "+":
#     result = first_number + second_number
# elif arithmetical_sign == "-":
#     result = first_number - second_number
# elif arithmetical_sign == "*":
#     result = first_number * second_number
# elif arithmetical_sign == "/":
#     result = first_number / second_number
# else:
#     print("Неверный арифметический знак")
#     exit()
#
# print(f"Результат: {result}")
# print(f'{first_number} {arithmetical_sign} {second_number} = {result}')
#
