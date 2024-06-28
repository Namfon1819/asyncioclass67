# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
import multiprocessing
import os
from time import sleep, ctime, time

def cooking(index):
    cooking_time = time()
    print(f'{ctime()} Kitchen - {index} : Begin cooking...PID {os.getpid()}')
    sleep(2)
    duration = time() - cooking_time
    print(f'{ctime()} Kitchen - {index} : Cooked done in {duration:0.2f} seconds')

def kitchen(index):
    cooking(index)

if __name__ == "__main__":
    #Begin of main thread
    print(f'{ctime()} Main          : Start Cooking...PID {os.getpid()}')
    start_time = time()

    # Multi kitchens with each chef
    kitchens = list()
    for index in range(2):
        p = multiprocessing.Process(target=kitchen, args=(index,))
        kitchens.append(p)
        #starting process
        p.start()


#ผลลัพธ์ 
#Fri Jun 28 10:31:16 2024 Main          : Start Cooking...PID 9760
#Fri Jun 28 10:31:17 2024 Kitchen - 0 : Begin cooking...PID 8688
#Fri Jun 28 10:31:17 2024 Kitchen - 1 : Begin cooking...PID 14020
#Fri Jun 28 10:31:19 2024 Kitchen - 0 : Cooked done in 2.00 seconds
#Fri Jun 28 10:31:19 2024 Kitchen - 1 : Cooked done in 2.01 seconds