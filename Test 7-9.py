# 7. Найти сумму десяти первых чисел ряда Фибоначчи.
# #
# def fibonachi_sequence(lim):
#     elem = 1
#     new_elem = 0
#     previos_elem = 1
#     fbc_sequance = [1, 1]
#     while elem < lim:
#         # 1 + 1 = 2
#         # 2 + 1 = 3
#         # 3 + 2 = 5
#         # 5 + 3 = 8
#         # 8 + 5 = 13
#
#         new_elem = elem + previos_elem
#         previos_elem = elem
#         elem = new_elem
#         fbc_sequance.append(new_elem)
#     return fbc_sequance
#
# x = fibonachi_sequence(1000)
# print(x)
#
# sum = 0
# for i in range(0,10):
#     sum = sum + x[i]
#     print(sum)
#
# print(sum)


# 8. В одномерном массиве поменять местами минимальный и максимальный элементы. Остальные оставить на своих местах.


# mas = [7, 4, 10,  12, 9]
# print(mas)
#
# max_elem = max(mas)
# min_elem = min(mas)
#
# idx_max = mas.index(max_elem)
# idx_min = mas.index(min_elem)
#
# del mas[idx_max]
# del mas[idx_min]
#
# mas.insert(idx_max, min_elem)
# mas.insert(idx_min, max_elem)
#
# print(mas)

# 9. Нормировать одномерный массив случайных чисел. Нормирование означает приведение всех значений массива к интервалу
# [-1;1], причем максимальное абсолютное значение элементов после нормирование должно быть равно 1. Например,
# последовательность {-5, 3, 4} после нормирование будет выглядеть {-1, 0.6, 0.8}

import random
lst = []
for i in range (0, 5):
    x = random.randint(-10, 10)
    lst.append(x)

if abs(max(lst)) >= abs(min(lst)):
    max_elem = max(lst)
else:
    max_elem = min(lst)

normilised_lst = []
for i in range(0,len(lst)):
    norm_elem = lst[i] / max_elem
    normilised_lst.append(norm_elem)



print(lst)
print(max_elem)
print(normilised_lst)