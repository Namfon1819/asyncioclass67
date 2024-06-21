# extending the Thread class and return values
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
        #stores return values
        self.value = 99

#create a thread
thread = CustomThread()
#run the thread
thread.start()
#wait for the thread to finish
print(f'{ctime()} Wait for the thread to finish')
thread.join()
#get the value returned from run
value = thread.value
print(f'{ctime()} Got: {value}')