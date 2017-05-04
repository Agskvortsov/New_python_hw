# 21 Вывести на экран все простые числа от 1 до 100
#
# def prime_numbers(b):
#
#     for i in range(1, b+1):
#         for l in range(2, i):
#             # if i == 1:
#             #     print("PC= 1")
#             if i%l==0:
#                 break
#
#         else:
#              print('PC=', i)
#
#
# k = prime_numbers(19)


# 22 Создать функцию, выводящую на экран случайно сгенерированное 12 ти-значное натуральное число и возвращающую его наибольшую цифру.
#
# def maximum_digit_random_generated():
#     import random
#     random_figure = str(random.randint(100000000000, 999999999999))
#     x = int(random_figure[0])
#     for i in range(1, len(random_figure)):
#         if int(random_figure[i]) > x:
#             x = int(random_figure[i])
#
#     return random_figure, x
#
# x = maximum_digit_random_generated()
# print(x)



# 23 Вычислить факториал некоторого числа, используя рекурсию.

# def factorial(x):
#     if x == 0:
#         return 1
#     else:
#         return x * factorial(x - 1)
#
# print(factorial(4))
#

# 24 Случайным образом программа выбирает целое число от 1 до 10 и предлагает пользователю его угадать. Пользователь вводит
# число,а программа проверяет его и, если пользователь не угадал, то говорит больше или меньше. После чего опять просит
# угадать. И так пока пользователь не угадает выбранное число.

import random

d = random.randint(1,10)
print(d)

x = int(input("Пожалуйста угадайте число"))

while True:

    if x == d:
        print("Вы угадали")
        break

    if x > d:

        x = int(input("Не угадали! Выберите число меньше"))
    if x < d :
        x = int(input ("Не угадали! Выберите число больше"))
