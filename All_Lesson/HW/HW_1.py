# a = "Hello";
# b = " World";
# print(a+b);
# print(f'{a}+{b}');
#
# user_name = input("Введите ваше имя: ")
# print(f"Hello {user_name}!");
#
# print("Task #4");
#
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

def square(n, m ,s,v):
    # print(n*m +"\n",n+s*v+n+"\n",n+s*v+n+"\n",n*m )
    print(n * m+"\n"+n+s*v+n+"\n" +n+s*v+n+"\n"+n * m )

print(square("7",4," ",2));

n = "*";
m = 5;
s= " ";
v = 3;
print(n * m + "\n" + n + s * v + n + "\n" + n + s * v + n + "\n" + n * m)
quantity =5;
item = "books";
print(str(quantity) + " "+ item);
print(item + str(quantity));
number = input("Введите четырёхзначное число: ")

try:
    num = int(number)
    if 1000 <= num <= 9999:
        thousands = num // 1000
        hundreds = (num // 100) % 10
        tens = (num // 10) % 10
        units = num % 10

        print(f"Тысячи - {thousands}")
        print(f"Сотни - {hundreds}")
        print(f"Десятки - {tens}")
        print(f"Единицы - {units}")
    else:
        print("Неверный ввод. Пожалуйста, введите четырёхзначное число.")
except ValueError:
    print("Неверный ввод. Пожалуйста, введите числовое значение.")


n=8;
k="b";
print(k*n)