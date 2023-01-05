# Name : M.Saad Bin Shafiq
# Reg No: 200901079
# Batch: BSCS_01_B
#.................Lab Task 4...............

# Question 2: Write a Program for process synchronization using semaphores

import threading

# create a semaphore with a value of 1
semaphore = threading.Semaphore(1)


# a function that will be executed by a thread
def func():
    # acquire the semaphore
    semaphore.acquire()

    # critical section
    print("Thread entered critical section")

    # release the semaphore
    semaphore.release()


# create and start two threads
thread1 = threading.Thread(target=func)
thread2 = threading.Thread(target=func)
thread1.start()
thread2.start()

# wait for the threads to finish
thread1.join()
thread2.join()
