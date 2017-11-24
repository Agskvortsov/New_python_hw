# 11 Написать функцию, которая будет переводить градусы в радианы.
# Используя эту функцию вывести на экран значения косинусов углов в 60, 45 и 40 градусов.

# def degrees2radians(degrees):
#     radians = math.pi * degrees /180
#     return radians
#
# import math
#


# angle1_radians = degrees2radians(60)
# angle2_radians = degrees2radians(45)
# angle3_radians = degrees2radians(40)
#
# cosin_angle1 = math.cos(angle1_radians)
# cosin_angle2 = math.cos(angle2_radians)
# cosin_angle3 = math.cos(angle3_radians)
#
# print("Cos (", angle1_radians, ") =", cosin_angle1 )
# print("Cos (", angle2_radians, ") =", cosin_angle2 )
# print("Cos (", angle3_radians, ") =", cosin_angle3 )


# 12 Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа,
# введенного пользователем в консоли, без использования операторов цикла.

# threedigit_number = input("Please enter three-digit number")
# symbol_1 = int(threedigit_number[0])
# symbol_2 = int(threedigit_number[1])
# symbol_3 = int(threedigit_number[2])
# sum_of_digits = symbol_1 + symbol_2 + symbol_3
#
# print(sum_of_digits)
#
# first_digit = input("Please enter first digit")



#  13 Пользователь вводит длины катетов прямоугольного треугольника.
# Написать функцию, которая вычислит и выведет на экран площадь треугольника и его периметр.
#
catet1 = int(input(" Please enter catet 1"))
catet2 = int(input("Please enter catet 2"))

import math

def triangle_main_ops(catet1, catet2):
    square_of_triangle = (catet1 * catet2) / 2
    gipotenusa = math.sqrt (catet1**2 + catet2**2)
    perimetr = catet1 + catet2 + math.sqrt(catet1**2 + catet2**2)
    return square_of_triangle, gipotenusa, perimetr

square_of_triangle = triangle_main_ops(catet1, catet2)

print(square_of_triangle)



