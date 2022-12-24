#string slicing

#slicing = create a substring by extracting elements from another string
#we can use either indexing[] or slice()
#[start:stop:step]

name = "Ragosh Shrestha"

first_name = name[0:6] #index 0 is inclusive and index 6 is exclusive
last_name = name[7:15]
funky_name = name[::2] #here starting index is 0 and stopping index is 15 by default
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website = "http://www.instagram.com"
website2 = "http://www.facebook.com"
slice = slice(11,-4)


print(website[slice])
print(website2[slice])