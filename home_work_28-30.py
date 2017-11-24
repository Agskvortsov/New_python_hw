# 28 Создайте 2 списка из 5 случайных целых чисел из отрезка [0;5] каждый, выведите списки на экран в двух отдельных строках.
# Посчитайте среднее арифметическое элементов каждого списка и сообщите, для какого из списков это значение оказалось
# больше (либо сообщите, что их средние арифметические равны).


# def random_lst_create(lim_low, lim_up, lst_duration):
#     import random
#     i = 1
#     random_lst = []
#     while i < lst_duration + 1:
#         x = random.randint(lim_low, lim_up)
#         random_lst.append(x)
#         i = i + 1
#     return random_lst
#
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
#
# lst1 = random_lst_create(0, 5, 5)
# lst2 = random_lst_create(0, 5, 5)
#
# average_lst1 = average_of_list(lst1)
# average_lst2 = average_of_list(lst2)
#
#
# print(lst1)
# print(lst2)
#
# print(average_lst1)
# print(average_lst2)
#
# if average_lst1 > average_lst2:
#     print("Average of first list is bigger then average of second list")
# if average_lst1 < average_lst2:
#     print("Average of first list one less then average of second list")
# if average_lst1 == average_lst2:
#     print("Averages of first and second lists are equal")



# # 29 Создайте список из 11 случайных целых чисел из отрезка [-1;1], выведите список на экран в строку. Определите какой
# # элемент встречается в списке чаще всего и выведите об этом сообщение на экран. Если два каких-то элемента встречаются
# # одинаковое количество раз, то не выводить ничего.
#
# def random_lst_create(lim_low, lim_up, lst_duration):
#     import random
#     i = 1
#     random_lst = []
#     while i < lst_duration + 1:
#         x = random.randint(lim_low, lim_up)
#         random_lst.append(x)
#         i = i + 1
#     return random_lst
#
# lst = random_lst_create(-1, 1, 11)
# print(lst)
#
# def count_digit_in_list(lst, lim_low, lim_up):
#     lst_of_elem = [x for x in range(lim_low, lim_up)]
#     lst_of_qtty_of_each_digit = []
#     for i in range(lim_low, lim_up + 1):
#         x = lst.count(i)
#         print('I=',i , "X=", x)
#         lst_of_qtty_of_each_digit.append(x)
#     print("Not sorted", lst_of_qtty_of_each_digit)
#     return lst_of_qtty_of_each_digit
#
# def compare_lst_elem(x):
#     lst = x
#     print("lst compare", lst)
#     lst_sort = x.sort
#     print(lst_sort)
#     max_elem = x[int(len(x))]
#     print("max_elem", max_elem)
#     if x[int(len(x))-1] == x [int(len(x))]:
#         pass
#     else:
#         index_of_max_elem = x.index(max_elem)
#         print(index_of_max_elem)
#
#
#
# # def compare_list_elem(comp_lst):
# #     comp_lst = []
# #     if comp_lst[1] == comp_lst[2] or comp_lst[0] == comp_lst[1] or
#
#
# x = count_digit_in_list(lst, -1, 1)
# print("x=", x)
#
# index_of_max_elem = compare_lst_elem(x)
# print(index_of_max_elem)
#
# #
# # x = [2, 4, 1, 2]
# # v = x.index(4)
# # print(x[v])
# # print(v)



# 30 Создать программу, которая запрашивает у пользователя произвольную строку символов. Далее программа ее шифрует и
# выводит на экран в зашифрованном виде. Шифрование происходит путем замены каждого символа символом, который находится
# на 5 позиций правее в предопределенной таблице шифрования. Таблица шифрования задается программистом в виде
# одномерного списка символов. Если при выборе символа для шифровки таблица шифрования заканчивается, то циклически
# переходить к ее началу.
# 	Например: Таблица шифрования (а,б,в,г,д,о,1,2,3,4,5,6,-,0)
# 	Исходная строка, которую ввел пользователь: год-2016
# 	Зашифрованная строка, которую выдала программа: 354г-д6в
# 	Примечание: т.н. таблица шифрования может быть представлена как строка или список.



list_of_symbols = "0123456789abcdefghigklmnopqrstuvwxyz"

str = list(input("Please input the string"))
print(type(str))
print(str)


def crypt_of_str(str):
    str_crypted = []
    i = 0
    for i in range (0,int(len(str))):
        x = str[i]
        position_of_crypt_symbol = list_of_symbols.index(x)

        if position_of_crypt_symbol+5 > int(len(list_of_symbols)):
            indx = position_of_crypt_symbol+5 - int(len(list_of_symbols))
            v = list_of_symbols[indx-1]
            str_crypted.append(v)

        else:
            v = list_of_symbols[list_of_symbols.index(x)+5]
            str_crypted.append(v)

        i = i + 1
    return str_crypted
    print(str_crypted)

f = crypt_of_str(str)
print(f)