# nested functions calls = function calls inside other function calls.
#                          innermost function calls are resolved first
#                          return value is used as argument for the next other function
import math


num = float(input("Enter a negative floating number :"))

print(math.sqrt(pow(round(math.sqrt(abs(num))),3)))