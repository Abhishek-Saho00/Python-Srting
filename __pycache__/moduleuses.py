 # first way to import function .

import Module
print(Module.sum(2,10))
print(Module.sum(5,10))

# second way to import function .


from Module import sum
print(sum(10,20))

# third way to import 
import Module as m
print(m.sum(21,21))

# in-built module function 
import math

print(math.ceil(10.2))
print(math.fabs(-19))

print(math.factorial(4))
print(math.floor(2.3))
 # out put is 2
x = [1,2,4,6,6]
print(math.fsum(x))
# sum the list value .only int value work . tuple aslo work sa same 

# math.sqrt(x)square root function return a 2=4,81=9.

# Random Module............
 