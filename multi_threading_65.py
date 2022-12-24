# thread =  a flow of execution, like a separate order of instructions. each thread takes a turn running to achieve concurrency. GIL = Global Interpreter Lock allows only one thread to jold the control of the Python interpreter.

# cpu bound = program/task spends most of its time waiting for internal events(CPU intensive), use multiprocessing

# io bound = program/task spends most of its time waiting for external events  (user input, web scraping), use multithreading


import threading
import time
start = time.perf_counter() #without initializing the performance counter method big number is displayed


def study():
    time.sleep(4)
    print("You studied well")
def sleep():
    time.sleep(5)
    print("How was your sleep")
def eat():
    time.sleep(3)
    print("Always eat healthy")

x = threading.Thread(target=study, args=())
x.start()

y = threading.Thread(target=sleep, args=())
y.start()

z = threading.Thread(target=eat, args=())
z.start()
# it helps to use different function simultaneously.

x.join() #thread syncronization, main thread waits for thread x before moving on
y.join()
z.join()
"""study()
sleep()
eat()"""

print(threading.active_count()) #counts how many threads are running currently
print(threading.enumerate()) #list of all the threads that are running
print(time.perf_counter() - start)

