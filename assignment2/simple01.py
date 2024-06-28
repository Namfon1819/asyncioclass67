# Synchronous cooking
# 1 kitchen 1 chefs 1 dish

from time import sleep, ctime, time

# Cooking synchronous
def cooking(index):
    print(f'{ctime()} Kitchen-{index} : Begin cooking...')
    sleep(2)
    print(f'{ctime()} Kitchen-{index} : Cooking done!' )

if __name__=="__main__":
    # Begin of main thread
    print(f'{ctime()} Main         : Start Cooking. ') 
    start_time = time()
    # Cooking
    cooking(0)

    duration = time() - start_time
    print(f"{ctime()} Main      : Finished Cooking duration in {duration:0.2f} seconds")

#ผลลัพธ์
#Fri Jun 28 10:41:47 2024 Main         : Start Cooking. 
#Fri Jun 28 10:41:47 2024 Kitchen-0 : Begin cooking...
#Fri Jun 28 10:41:49 2024 Kitchen-0 : Cooking done!
#Fri Jun 28 10:41:49 2024 Main      : Finished Cooking duration in 2.00 seconds