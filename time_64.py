import time 

print(time.ctime(0)) #converts a time expressed in seconds since epoch to a readable string. epoch = when your computer thinks time began(refrence point)

print(time.time()) #returns current seconds since epoch

print(time.ctime(time.time()))
time_object = time.localtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object) #it is used to display the date and time in proper format
print(local_time)

time.gmtime() #UTC 


time_string = "28 July, 2004"
time_object = time.strptime(time_string,"%d %B, %Y")
print(time_object)
#(year, month, day, hours, minutes, seconds, day of the week, day of the year, dst)



time_tuple = (2004, 7, 28, 4, 51, 54, 0, 0, 0)
time_string = time.asctime(time_tuple) #converts into string based time representation
print(time_string) 

time_string = time.mktime(time_tuple) #converts the given tuple time into seconds since epoch
print(time_string)