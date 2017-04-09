# # 1. a,b,c: a + b * ( c / 2 )
#
# a=42
# b=43
# c=4
# v=a+b*c/2
# print (("If 'a' = %d and if 'b' = %d and if 'c' = %d" % (a, b, c)))
# print("Result is ", v)

#
#
#
#
# #2 a,b: (a2 + b2) % 2
#
# a=42
# b=43
# c=(a**2 + b**2)
# v=c%2
# print ("(a2 + b2) % 2")
# print (("If 'a' = %d and if 'b' = %d" % (a, b,)))
# print("c=", c)
# print("v=", v)
#
#
#
# #3 ( a + b ) / 12 * c % 4 + b
# a=42
# b=43
# c=7
# v=( a + b ) / (12*(c%4)) + b
# print("v =", v)
#
#
#
#
#
# #4 (a - b * c ) / ( a + b ) % c
# #a=12
# #b=10
# #c=3
# #e= a + b
# #g= e%c
# #v=(a - b * c ) /g
#
# #print("e=", e)
# #print("g=", g)
# #print("v=", v)
# a=12
# b=10
# c=3
# v=(a - b * c ) /((a + b)%c)
#
# print("v=", v)
#
#
# #5 | a - b | /( a + b)3 - cos( c )
# a=8
# b=10
# c=3
# import math
# v=abs(a - b ) / ( a + b)*3 - math.cos( c )
# e=math.cos(c)
# print(c)
# print("v=", v)



# 6 ( ln( 1 + c ) / -b )4+ | a |

# a=8
# b=10
# c=3
# import math
# v=(math.log(1+c)/-b)*4 + abs(a)
# print(v)

# 7 Преобразовать строку с американским форматом даты в европейский. Например, "05.17.2016" преобразуется в "17.05.2016"

# usa_date = '05.17.2016'
# year = usa_date[-4:]
# month = usa_date[0:2]+"."
# day = usa_date[3:5]+"."
# print(month)
# print(year)
# print(usa_date)
# euro_date = day+month+year
# print(euro_date)



# 8 Написать программу, которая берет две строки и помещает первую строку в середину второй.
# Результат помещается в середину первой. Длину строки можно получить с помощью функции len().

# first_line = 'abcdefg'
# second_line = '01234567'
# hulf_dur_sl = round(len(second_line)/2)
# print(hulf_dur_sl)
# sl_fh = second_line[0:hulf_dur_sl]
# print(sl_fh)
# sl_sh = second_line[hulf_dur_sl:]
# print(sl_sh)
# new_line = sl_fh+first_line+sl_sh
# print(new_line)
# hulf_dur_nl = round(len(first_line)/2)
# fl_fh = first_line[0:hulf_dur_nl]
# print(fl_fh)
# fl_sh = first_line[hulf_dur_nl:]
# required_line = fl_fh+new_line+fl_sh
# print(required_line)

# 9 Написать программу, которая переводит в верхний регистр второе слово
# (слово - последовательность символов между двумя пробелами).
# Например: “abc def ghj” -> “abc DEF ghj”

# frase = 'cvxv fsd fsdf dffd'
# idx1 = frase.find(' ')
# idx2 = frase.find(' ', idx1+1)
# frase_fp = frase[:idx1]
#
# frase_cp = frase[idx1+1:idx2]
#
# frase_lp = frase[idx2+1:]
# frace_cp_new = frase_cp.upper()
# print(frase)
# frace_new = frase_fp+' '+frace_cp_new+' '+frase_lp
# print(frace_new)
#


# 10 Дана строка вида "Leo Tolstoy*1828-08-28*1910-11-20". В этой строке указаны имя писателя и
# через символ * даты рождения и смерти. Даты указаны в формате "YYYY-MM-DD". Требуется написать программу,
# которая по переданной строке определит возраст писателя и вернет его имя и возраст.
# Например, для строки "Leo Tolstoy*1828-08- 28*1910-11-20" функция должна вернуть: "Leo Tolstoy", 82

name_life_period = 'Leo Tolstoy*1828-08-28*1910-11-20'
born_year = int(name_life_period[-21:-17])
print(born_year)
died_year = int(name_life_period[-10:-6])
print(died_year)
life_period = died_year - born_year
print(life_period)
idx1 = name_life_period.find('*')
name = name_life_period[:idx1]
name_ldy = name, life_period
print(name_ldy)

# 9 Написать программу, которая переводит в верхний регистр второе слово
# (слово - последовательность символов между двумя пробелами).
# Например: “abc def ghj” -> “abc DEF ghj”

frase = 'Дуракам закон не писан'
idx1 = frase.find(' ')
idx2 = frase.find(' ', idx1+1)
frase_fp = frase[:idx1]

frase_cp = frase[idx1+1:idx2]

frase_lp = frase[idx2+1:]
frace_cp_new = frase_cp.upper()
print(frase)
frace_new = frase_fp+' '+frace_cp_new+' '+frase_lp
print(frace_new)



# 10 Дана строка вида "Leo Tolstoy*1828-08-28*1910-11-20". В этой строке указаны имя писателя и
# через символ * даты рождения и смерти. Даты указаны в формате "YYYY-MM-DD". Требуется написать программу,
# которая по переданной строке определит возраст писателя и вернет его имя и возраст.
# Например, для строки "Leo Tolstoy*1828-08- 28*1910-11-20" функция должна вернуть: "Leo Tolstoy", 82

# name_life_period = 'Leo Tolstoy*1828-08-28*1910-11-20'
# born_year = int(name_life_period[-21:-17])
# print(born_year)
# died_year = int(name_life_period[-10:-6])
# print(died_year)
# life_period = died_year - born_year
# print(life_period)
# idx1 = name_life_period.find('*')
# name = name_life_period[:idx1]
# name_ldy = name, life_period
# print(name_ldy)
