# 17 Написать функцию решения квадратного уравнения.



# def quad_equation(a, b, c):
#     import math
#     d = b**2 - 4*a*c
#
#     print("D =",d)
#     if d > 0:
#         x1 = (-b + math.sqrt(d)) / (2*a)
#         x2 = (-b - math.sqrt(d)) /(2*a)
#         return x1, x2
#     elif d == 0:
#         x1 = -b / (2*a)
#         x2 = x1
#         return x1, x2
#     else:
#         print('Net deistvitelnih corney')
#
#
#
# v = quad_equation(2, 1, -1)
# print(v)


# 18 Каждому символу в таблице символов Unicode соответствует число. Написать функцию, которая расчитывает сумму чисел,
# которые соответствуют символам, стоящим между двумя заданными включительно. Например, в функцию передаются
# символы ‘x’ и ‘z’. Значит надо вычислить сумму кодов символов ‘x’,’y’,’z’.



# def unicod_symbol_number_sum(a, b):
#     alfavit = ("abcdefghijklmnopqrstuwxyz")
#     idx1 = alfavit.find(a)
#     idx2 = alfavit.find(b)
#     print(idx1)
#     print(idx2)
#
#     sum = 0
#
#     while idx1 < idx2:
#         v = alfavit[idx1]
#         n = ord(v)
#         idx1 = idx1+1
#         sum = sum + n
#     return sum
#
# sum = unicod_symbol_number_sum("k", "z")
# print(sum)


# 19 Вывести сумму всех чисел, которые являются степенью 3ки и принадлежат диапазону чисел от 0 до 1000000.
# Т.е. sum = 3^0 + 3^1 + 3^2 + ...

# sum = 0
# v = 0
# i = 0
# while v < 1000000:
#     i = i + 1
#     v = 3**(i)
#     if v < 1000000:
#         sum = sum + v
#     print(v, i, sum)



# 20 Вывести все числа от 0 до 1000, которые содержат в себе цифры 1 и 7. Т.е. числа: 17, 71, 107, 117, 127, 137, …

def print_figures(parametr1, parametr2, range_limit):

    sum = 0
    for i in range (1, range_limit +1):
        d = int(i)
        if (str(parametr1) in str(d)) or (str(parametr2) in str(d)):
            sum = sum + d
            print(d)
    return sum
v = print_figures(1, 7, 17)
print("sum =", v)