# Name : M. Saad Bin Shafiq
# Reg No: 200901079
# Batch: BSCS-01-B
# .............Lab Task 4..............

# Question 1: Write a program to create two threads, one thread is used to increment the value of shared variable and the other thread is used to decrement the value of shared variable. Show the output with sleep function and without sleep function?
# Part 2: Program with sleep function

import threading
import time
# This is the shared variable
counter = 0

# This is the function that will be executed by the first thread
def increment():
    global counter
    counter += 1
    time.sleep(1)
    print("Incremented value: ", counter)

# This is the function that will be executed by the second thread
def decrement():
    global counter
    counter -= 1
    time.sleep(1)
    print("Decremented value: ", counter)

# Create the threads
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=decrement)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Print the final value of the counter
print("Final value: ",counter)
