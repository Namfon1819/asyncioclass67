# running a function in another thread
from time import sleep, ctime
from threading import Thread

# a custom function that blocks for a moment
def task():
    # block for a moment
    sleep(1)
    # display a message
    print(f'{ctime()} This is from another thread')

# create a thread
thread = Thread(target=task)
# run the thread
thread.start()
# wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()

#ผลลัพธ์
#Fri Jun 28 10:30:01 2024 Waiting for the thread...
#Fri Jun 28 10:30:02 2024 This is from another thread

