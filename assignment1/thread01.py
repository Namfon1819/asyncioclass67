# running a function in another thread
from time import sleep, ctime
from threading import Thread

#a custom function that blocks for a moment
def task():
    #blocks for a moment
    sleep(1)
    #displays a message
    #ctime = package
    print(f'{ctime()} this is from another thread')

#create a thread
thread = Thread(target=task)
#run the thread
thread.start()
#wait for the thread to finish
print(f'{ctime()} Wait for the thread to finish')
thread.join()

#ผลลัพธ์ที่ได้คือบรรทัดที่ 17 จะเห็นค่าก่อน
#Fri Jun 21 10:05:32 2024 Wait for the thread to finish
#Fri Jun 21 10:05:33 2024 this is from another thread