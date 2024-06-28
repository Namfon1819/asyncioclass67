# Thread version of cooking 1 kitchen 1 chefs 1 dishes
import os
from time import time, sleep, ctime
import threading

def cooking(index):
    print(f'{ctime()} Kitchen - {index} : Begin cooking...PID {os.getpid()}')
    cooking_time = time()
    print(f'{ctime()} Kitchen - {index} : Begin cooking...PID')
    sleep(2)
    duration = time() - cooking_time
    basket.use_eggs(index)
    print(f'{ctime()} Kitchen - {index} : Cooked done in {duration:0.2f} seconds!')

class Basket:
    def __init__(self):
        self.eggs = 50
        self._lock = threading.Lock()
    def use_eggs(self, index):
        with self._lock:
            print(f'{ctime()} Kitchen - {index} : Chef - {index} has lock with eggs remaining {self.eggs}')
            self.eggs -= 1
            print(f'{ctime()} Kitchen - {index} : Chef - {index} has release lock with eggs remaining {self.eggs}')

if __name__ == "__main__":
    #Begin of main thread
    print(f'{ctime()} Main          : Start Cooking...')

    start_time = time()

    basket = Basket()

    print(f'{ctime()} Main          : ID of main process: {os.getpid()}')

    #multithread cooking
    chefs = list()
    for index in range(2):
        c = threading.Thread(target=cooking, args=(index,))
        chefs.append(c)
        c.start()

    for index, c in enumerate(chefs):
        c.join()

    print(f'{ctime()} Main          : Basket egg remaining {basket.eggs}')
    duration = time() - start_time
    print(f'{ctime()} Main          : Finished Cooking duration in {duration:0.2f} seconds')

#ผลลัพธ์
#Fri Jun 28 11:01:02 2024 Main          : Start Cooking...
#Fri Jun 28 11:01:02 2024 Main          : ID of main process: 12044
#Fri Jun 28 11:01:02 2024 Kitchen - 0 : Begin cooking...PID 12044
#Fri Jun 28 11:01:02 2024 Kitchen - 0 : Begin cooking...PID
#Fri Jun 28 11:01:02 2024 Kitchen - 1 : Begin cooking...PID 12044
#Fri Jun 28 11:01:02 2024 Kitchen - 1 : Begin cooking...PID
#Fri Jun 28 11:01:04 2024 Kitchen - 0 : Chef - 0 has lock with eggs remaining 50
#Fri Jun 28 11:01:04 2024 Kitchen - 0 : Chef - 0 has release lock with eggs remaining 49
#Fri Jun 28 11:01:04 2024 Kitchen - 0 : Cooked done in 2.00 seconds!
#Fri Jun 28 11:01:04 2024 Kitchen - 1 : Chef - 1 has lock with eggs remaining 49
#Fri Jun 28 11:01:04 2024 Kitchen - 1 : Chef - 1 has release lock with eggs remaining 48
#Fri Jun 28 11:01:04 2024 Kitchen - 1 : Cooked done in 2.00 seconds!
#Fri Jun 28 11:01:04 2024 Main          : Basket egg remaining 48
#Fri Jun 28 11:01:04 2024 Main          : Finished Cooking duration in 2.01 seconds
