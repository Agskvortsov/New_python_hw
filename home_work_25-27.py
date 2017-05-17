# 25 Написать функцию для поиска среднее арифметическое всех элементов списка.

# def average_of_list (list):
#     list_element_qtty = int(len(list))
#     # print(list_element_qtty)
#     sum = 0
#     for i in range(0, list_element_qtty):
#         sum = sum + list[i]
#         # print(sum)
#
#     average = sum / list_element_qtty
#     return average
#
# list = [2, 5, 3, 12, 1, 18]
# x = average_of_list(list)
# print(x)


# 26 Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел списка. Т.е.
# От суммы четных чисел вычесть сумму нечетных чисел в списке.

# def  diff_even_uneven (list):
#     even_sum = 0
#     uneven_sum = 0
#     for i in range (0, int(len(list))):
#         if list[i] == 0:
#             pass
#         if list[i]%2 == 0:
#             even_sum = even_sum + list[i]
#         if list[i]%2 != 0:
#             uneven_sum = uneven_sum + list[i]
#     difference = even_sum - uneven_sum
#     return difference
#
# list = [2, 5, 13, 12, 19, 0, 18]
# x = diff_even_uneven(list)
# print(x)


# 27 Создайте список на 50 элементов из всех нечётных чисел от 1 до 99, выведите его на экран в строку,
# а затем этот же список выведите на экран тоже в строку, но в случайном порядке (например, 99 11 43 19 … 7 91 3 1).


import random

lst = [x for x in range(1,100) if x%2!=0]
print("uneven list =", lst)

random_lst = []

i = int(len(lst))

while i > 0:
    x = random.randint(0, i-1)
    random_lst.append(lst[x])

    lst.pop(x)
    i = i - 1

print("Random lst", random_lst)


