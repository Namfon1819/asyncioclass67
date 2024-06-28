# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
# 2 process

import multiprocessing
from multiprocessing import Value
import os
from time import sleep, ctime, time

class Basket:
    def __init__(self, eggs):
        self.eggs = Value("i", eggs)
    def use_eggs(self, index):
        print(f'{ctime()} Kitchen - {index} : Chef - {index} has lock with eggs remaining {self.eggs.value}')
        self.eggs.value -= 1
        print(f'{ctime()} Kitchen - {index} : Chef - {index} has release lock with eggs remaining {self.eggs.value}')

def cooking(index, basket):
    cooking_time = time()
    print(f'{ctime()} Kitchen - {index} : Begin cooking...PID {os.getpid()}')
    sleep(2)
    duration = time() - cooking_time
    with basket.eggs.get_lock():
        basket.eggs.value = basket.eggs.value - 1
    print(f'{ctime()} Kitchen - {index} : Cooked done in {duration:0.2f} seconds')

def kitchen(index, basket):
    cooking(index, basket)

if __name__ == "__main__":
    #Begin of main thread
    print(f'{ctime()} Main          : Begin Cooking...PID {os.getpid()}')
    start_time = time()

    basket = Basket(50)

    print(f'{ctime()} Main          : ID of main process {os.getpid()}')
    # Multi kitchens with each chef
    kitchens = []
    for index in range(2):
        p = multiprocessing.Process(target=kitchen, args=(index, basket))
        kitchens.append(p)
        #starting process
        p.start()

    for p in kitchens:
    #wait until process are finished
        p.join()

    print(f'{ctime()} Main          : Basket egg remaining {basket.eggs.value}')
    duration = time() - start_time
    print(f'{ctime()} Main          : Finished Cooking duration in {duration:0.2f} seconds')

#ผลลัพธ์
#Fri Jun 28 10:50:43 2024 Main          : Begin Cooking...PID 12836
#Fri Jun 28 10:50:43 2024 Main          : ID of main process 12836
#Fri Jun 28 10:50:43 2024 Kitchen - 0 : Begin cooking...PID 15292
#Fri Jun 28 10:50:43 2024 Kitchen - 1 : Begin cooking...PID 5308
#Fri Jun 28 10:50:45 2024 Kitchen - 0 : Cooked done in 2.00 seconds
#Fri Jun 28 10:50:45 2024 Kitchen - 1 : Cooked done in 2.00 seconds
#Fri Jun 28 10:50:46 2024 Main          : Basket egg remaining 48
#Fri Jun 28 10:50:46 2024 Main          : Finished Cooking duration in 2.86 seconds