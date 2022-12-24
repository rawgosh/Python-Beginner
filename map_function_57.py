#map() = it applies a function to each item in an iterable (list, tuple,...)
#map(function,iterable)



#converting the price of the items into nepali 
store = [("Shirt",20.00),("Pant",35.00),("Shoes",99.99),("Hoodie",75.55)]

to_nepali = lambda money:(money[0],int(money[1]*127.62))

store_nepali = list(map(to_nepali,store))
for price in store_nepali:
    print(price)