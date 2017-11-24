# 1. (a + b * c)2                                     2. a - 4 * b / c                                   3. (a * b + 4) / (c - 1)

# # 1
# a = 3
# b = 5
# c = 7
#
# x1 = (a + b*c)**2
# print('x(1) = ', x1)
#
#
# # 2
#
# a = 3
# b = 5
# c = 7
#
# x2 = a - b*4/c
# print("x(2) = ", x2)
#
#
# # 3
#
# a = 3
# b = 5
# c = 7
#
# x3 = (a*b+4) / (c - 1)
# print("x(3) = ", x3)

#
# 4. Найти произведение нечетных цифр пятизначного целого числа, введенного пользователем с клавиатуры

4

number = input("Pleae enter five digit-number")

multiplic = 1
for i in range (0, int(len(number))):
    x = int(number[i])
    if (x+1)%2 == 0:
        multiplic = multiplic * x



print(multiplic)



# # 5. Создать программу, выводящую на экран ближайшее к 10 из двух чисел, введенных пользователем. Например, среди
# # чисел 8,5 и 11,45 ближайшее к десяти 11,45.
#
#
# number_a = input("Please enter first number")
# number_b = input("Please enter second number")
#
# k1 = abs(10 - float(number_a))
# k2 = abs(10 - float(number_b))
# print(k1, k2)
# if k1 > k2:
#     print(number_b)
# if k1 < k2:
#     print(number_a)







# 6. Создать массив из 10 элементов и проинициализировать его простыми числами в случайном порядке


# mass = []
#
# def prime_numbers(b):
#     prime_numer_list = []
#
#     for i in range(1, b+1):
#         for l in range(2, i):
#
#             if i%l==0:
#                 break
#
#         else:
#             prime_numer_list.append(i)
#     return prime_numer_list
#
# prime_numbers_list = prime_numbers(10000)
#
# import random
# for i in range(0, 9):
#     x = random.randint(0, len(prime_numbers_list))
#     elem = prime_numbers_list[x]
#     mass.append(elem)
#
# print(mass)

