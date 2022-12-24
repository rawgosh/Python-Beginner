#multiprocessing = act of running tasks in parallel on different cpu cores, bypasses GIL used for threading

#  multiprocessing -> better for cpu bound tasks (heavy cpu usage)
#  multithreading -> better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time
start = time.perf_counter()

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    print(cpu_count()) #displays how many process can be run at a time.

    a = Process(target=counter, args=(100000000,))
    b = Process(target=counter, args=(100000000,))
    c = Process(target=counter, args=(100000000,))
    d = Process(target=counter, args=(100000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print("finished in:",time.perf_counter() - start,"seconds")

if __name__ == "__main__":
    main()