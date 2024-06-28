# Synchronous cooking
# 2 kitchen 2 chefs 2 dishes

from time import sleep, ctime, time

# Cooking synchronous
def cooking(index):
    print(f'{ctime()} Kitchen-{index} : Begin cooking...')
    sleep(2)
    print(f'{ctime()} Kitchen-{index}: Cooking done!')


if __name__=="__main__":
    # Begin of main thread
    print(f' {ctime()} Main       : Start Cooking.')
    start_time = time()

    # Cooking for each dish
    for index in range(2):
        cooking(index)

    duration = time() - start_time
    print(f"{ctime()} Main        : Finished Cooking duration in {duration:0.2f} seconds")


#ผลลัพธ์
#Fri Jun 28 10:48:31 2024 Main       : Start Cooking.
#Fri Jun 28 10:48:31 2024 Kitchen-0 : Begin cooking...
#Fri Jun 28 10:48:33 2024 Kitchen-0: Cooking done!
#Fri Jun 28 10:48:33 2024 Kitchen-1 : Begin cooking...
#Fri Jun 28 10:48:35 2024 Kitchen-1: Cooking done!
#Fri Jun 28 10:48:35 2024 Main        : Finished Cooking duration in 4.00 seconds