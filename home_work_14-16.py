# 14 Написать функцию, которая будет проверять четность некоторого числа.

#
# def pairity_check (number):
#     result = number%2
#     if result == 0:
#         print("Number is even")
#     if result != 0:
#         print("Number is not even")
#     return result
#
# x = pairity_check(16)



# 15 Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости.
    # Каждая окружность задается координатами центра и радиусом.

import math
def round_crossing_check(first_circle_coord_x, first_circle_coord_y, first_circle_radius, second_circle_coord_x,
                         second_circle_coord_y, second_circle_radius):

    if (first_circle_coord_x - second_circle_coord_x) == 0 or (first_circle_coord_y - second_circle_coord_y) == 0:
        if (first_circle_radius + second_circle_radius) >= (abs(first_circle_coord_x - second_circle_coord_x) +
                                                                abs(first_circle_coord_y - second_circle_coord_y)):
            print("Circles are crossing")
        if (first_circle_radius + second_circle_radius) < (abs(first_circle_coord_x - second_circle_coord_x) +
                                                               abs(first_circle_coord_y - second_circle_coord_y)):
            print("Circles are not crossing")

    if (first_circle_coord_x - second_circle_coord_x) != 0 and (first_circle_coord_y - second_circle_coord_y) != 0:
        distance_between_centrs = math.sqrt((abs(first_circle_coord_x - second_circle_coord_x)) ** 2 + (
                                    abs(first_circle_coord_y - second_circle_coord_y)) ** 2)
        if distance_between_centrs <= ( first_circle_radius + second_circle_radius ):
            print("Circles are crossing")
        if distance_between_centrs > ( first_circle_radius + second_circle_radius ):
            print("Circles are not crossing")


x = round_crossing_check(1, 1, 1 , 3, 1, 1)


# 16 Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути.
# Через 4 км пути первый поезд может свернуть на запасной путь. При заданных скоростях узнать столкнутся ли поезда.

# Изначально сделал без  while true, все работало если скорость второго поезда не была равна нулю.

#
# while True:
#     v1 = float(input("Please enter speed of first train"))
#     v2 = float(input("Please enter speed of second speed"))
#
#     if v2 == 0:
#         print("Keep going whith current speed")
#         break
#
#     if (v1/v2) > (4/6):
#         print("Keep going whith current speed")
#     if (v1/v2) <= (4/6):
#         print("STOP! Train crash expected")

