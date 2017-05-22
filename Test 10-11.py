
# 10. Вывести на экран матрицу, транспонированную заданной (3*8)
#
# a = [[1,2,3],[4,5,6],[3,6,4],[1,2,3],[4,5,6],[3,6,4],[1,2,3],[4,5,6]]
#
# def transpod_matrix(a):
#     b = [[],[],[]]
#
#     for i in range (0, len(a)):
#         for j in range(0, len(a[i])):
#             x = a[i][j]
#             b[j].append(x)
#     return b
# b = transpod_matrix(a)
# print(b)


# # 11. В двумерном массиве отсортировать четные столбцы по возрастанию, а нечетные - по убыванию


a = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
intermediate_table = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
final_table = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

def print_table(table):
    for line in table:
        for elem in line:
            print(elem, end ="\t")
        print()
print_table(a)

for i in range(0, len(a)):
   for j in range (0,len(a[i])):
       x = a[i][j]
       intermediate_table[j][i] = x


i=0
while i < len(intermediate_table):
    intermediate_table[i].sort()
    i = i + 2

i=0
while i < len(intermediate_table):
    intermediate_table[i].sort(reverse=True)
    i = i + 2

for i in range(0, len(intermediate_table)):
   for j in range (0,len(intermediate_table[i])):
       x = intermediate_table[i][j]
       final_table[j][i] = x

print_table(final_table)



