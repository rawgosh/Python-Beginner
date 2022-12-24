#reduce() = used to apply a function to an iterable and reduce it to a single cumulative value, it performs function on first two elements and repeats process until 1 value remains.

#reduce(function,iterable)

import functools #to use reduce function

letters = ["P","Y","T","H","O","N"]
word = functools.reduce(lambda x, y : x + y,letters) #It concatenates the strings present in the list and creates a single word.
print(word)

factorial = [9,8,7,6,5,4,3,2,1]
fact = functools.reduce(lambda x,y : (x*y), factorial)#starts to multiply each number of the list from the beginning till the end number.
print(fact)