#nested loop = The 'inner loop' will finish all of it's iterations before finishing one iteration of the 'outer loop'

rows = int(input("Enter the no. of rows :"))
columns = int(input("Enter the no. of columns :"))
symbol = input("Enter the symbol :")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #this prevents from moving the cursor to the another line.
    print()