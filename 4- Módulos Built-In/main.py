#Programa Principal

import math_operations #importanto módulo
from math_operations import multiply, divide #importando somente funções específicas do módulo

import string_utils

print(math_operations.sum(5,3)) #usando função do módulo
print(math_operations.subtract(5,3))

print(multiply(5,3))
print(divide(5,3))

print(string_utils.capitalize("hello"))
print(string_utils.reverse_string("python"))
print(string_utils.count("apple"))