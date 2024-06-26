# extending the Thread class
#เป็นเรื่องของ class
from time import sleep, ctime
from threading import Thread

#custom thread class
class CustomThread(Thread):
    #override the run function
    def run(self):
        #blocks for a moment
        sleep(1)
        #displays a message
        print(f'{ctime()} this is from another thread')

#create a thread
thread = CustomThread()
#run the thread
thread.start()
#wait for the thread to finish
print(f'{ctime()} Wait for the thread to finish')
thread.join()

#ผลลัพธ์
#Fri Jun 28 10:28:50 2024 Wait for the thread to finish
#Fri Jun 28 10:28:51 2024 this is from another thread