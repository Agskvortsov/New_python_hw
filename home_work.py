# 1. a,b,c: a + b * ( c / 2 )
"""""
a=42
b=43
c=4
v=a+b*c/2
print (("If 'a' = %d and if 'b' = %d and if 'c' = %d" % (a, b, c)))
print("Result is ", v)
"""""



""""
#2 a,b: (a2 + b2) % 2

a=42
b=43
c=(a**2 + b**2)
v=c%2
print ("(a2 + b2) % 2")
print (("If 'a' = %d and if 'b' = %d" % (a, b,)))
print("c=", c)
print("v=", v)
"""""

"""
#3 ( a + b ) / 12 * c % 4 + b
a=42
b=43
c=7
v=( a + b ) / (12*(c%4)) + b
print("v =", v)
"""



"""""
#4 (a - b * c ) / ( a + b ) % c
#a=12
#b=10
#c=3
#e= a + b
#g= e%c
#v=(a - b * c ) /g

#print("e=", e)
#print("g=", g)
#print("v=", v)
a=12
b=10
c=3
v=(a - b * c ) /((a + b)%c)

print("v=", v)
"""

#5 | a - b | /( a + b)3 - cos( c )
a=8
b=10
c=1
e=cos
v=abs(a - b ) / (( a + b) (3)) - ( c ))

print("v=", v)