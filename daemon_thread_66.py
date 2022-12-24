#daemon thread =  a thread that runs in the background, not important for program to run your program will not wait for daemon threads to complete before exiting, non-daemon threads cannot normally be killed, stays alive until task is complete. 
# eg. background tasks, waiting for input, long running process


import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ",count,"seconds")

x = threading.Thread(target=timer, args=(), daemon=True) #converting the thread into daemon
x.start()

#x.setDaemon(True) #cant set for running thread
print(x.isDaemon()) #checking if the thread is daemon or not
answer = input("Do you want to exit?")


