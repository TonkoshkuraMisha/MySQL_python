from math import *

A = factorial(1_000)
my_string = str(A)
for i in my_string:
    if int(i) != 0:
        my_string = my_string.replace(i, '*')
my_list = my_string.split('*')
print(len(my_list[-1]))
