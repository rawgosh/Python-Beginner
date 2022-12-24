#exception = events detected during execution that interrupt the flow of a program
try:
    numerator = int(input("Enter a number to divide :"))
    denominator = int(input("Enter a divisor :"))
    result = numerator / denominator
except ZeroDivisionError as e: #it excepts the error occuring while dividing by zero
    print("You can't divide by zero!")
    print(e) #to see what is the error
except ValueError as e: #it excepts the value error like strings getting matched with integers and others.
    print("Enter only numbers fool!")
except Exception as e: #it excepts all the exception
    print("Somethings not right")
else: #this block runs only if no exception is found
    print(result)
finally: #runs whether there is exception or not
    print("Cheer Up")
