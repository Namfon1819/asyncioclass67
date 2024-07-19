import time

class Coffee:
    pass
class Egg:
    pass
class Bacon:
    pass
class Toast:
    pass
class Juice:
    pass

def PourCoffee():
    print(f"{time.ctime()} - Begin pour coffee...")
    time.sleep(2)
    print(f"{time.ctime()} - Finish pour coffee...")
    return Coffee()

def ApplyButter():
    print(f"{time.ctime()} - Begin apply butter...")
    time.sleep(1)
    print(f"{time.ctime()} - Finish apply butter...")

def FryEggs(eggs):
    print(f"{time.ctime()} - Begin fry eggs...")
    print(f"{time.ctime()} - Heat pan to fry eggs")
    time.sleep(1)
    for egg in range(eggs):
        print(f"{time.ctime()} - Frying", egg+1,"eggs")
        time.sleep(1)
    print(f"{time.ctime()} - Finish fry eggs...")
    print(f"{time.ctime()} - >>>>>>>>>> Fry eggs are ready...")

def FryBacon():
    print(f"{time.ctime()} - Begin fry bacon...")
    time.sleep(2)
    print(f"{time.ctime()} - Finish fry bacon...")
    print(f"{time.ctime()} - - >>>>>>>> Fry bacon is ready...")
    return Bacon()

def ToastBread(slices):
    for slice in range(slices):
        print(f"{time.ctime()} - Toasting bread", slice + 1)
        time.sleep(1)
        print(f"{time.ctime()} - Bread", slice + 1, "toasted")
        ApplyButter()
        print (f"{time.ctime()} - Toast", slice + 1, "ready")
    print(f"{time.ctime()} - >>>>>>>> Toast are ready\n")
    return Toast()

def PourJuice():
    print(f"{time.ctime()} - Begin pour joice...")
    time.sleep(1)
    print(f"{time.ctime()} - Finish pour joice...")
    return Juice()

def main():
    PourCoffee()
    print(f"{time.ctime()} - >>>>>>>> Coffee is ready\n")
    FryEggs(2)
    FryBacon()
    ToastBread(2)
    print(f"\n{time.ctime()} - >>>>>>>> Nealy to finished...")
    PourJuice()

if __name__ == "__main__":
    start_cooking = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_cooking
    print(f"{time.ctime()} - Breakfast cooked in ", elapsed, "seconds.")

##ผลลัพธ์
#Fri Jul 19 09:43:03 2024 - Begin pour coffee...
#Fri Jul 19 09:43:05 2024 - Finish pour coffee...
#Fri Jul 19 09:43:06 2024 - >>>>>>>> Coffee is ready

#Fri Jul 19 09:43:06 2024 - Begin fry eggs...
#Fri Jul 19 09:43:06 2024 - Heat pan to fry eggs
#Fri Jul 19 09:43:07 2024 - Frying 1 eggs
#Fri Jul 19 09:43:08 2024 - Frying 2 eggs
#Fri Jul 19 09:43:09 2024 - Finish fry eggs...
#Fri Jul 19 09:43:09 2024 - >>>>>>>>>> Fry eggs are ready...
#Fri Jul 19 09:43:09 2024 - Begin fry bacon...
#Fri Jul 19 09:43:11 2024 - Finish fry bacon...
#Fri Jul 19 09:43:11 2024 - - >>>>>>>> Fry bacon is ready...
#Fri Jul 19 09:43:11 2024 - Toasting bread 1
#Fri Jul 19 09:43:12 2024 - Bread 1 toasted
#Fri Jul 19 09:43:12 2024 - Begin apply butter...
#Fri Jul 19 09:43:13 2024 - Finish apply butter...
#Fri Jul 19 09:43:13 2024 - Toast 1 ready
#Fri Jul 19 09:43:13 2024 - Toasting bread 2
#Fri Jul 19 09:43:14 2024 - Bread 2 toasted
#Fri Jul 19 09:43:14 2024 - Begin apply butter...
#Fri Jul 19 09:43:15 2024 - Finish apply butter...
#Fri Jul 19 09:43:15 2024 - Toast 2 ready
#Fri Jul 19 09:43:15 2024 - >>>>>>>> Toast are ready


#Fri Jul 19 09:43:15 2024 - >>>>>>>> Nealy to finished...
#Fri Jul 19 09:43:15 2024 - Begin pour joice...
#Fri Jul 19 09:43:16 2024 - Finish pour joice...
#Fri Jul 19 09:43:16 2024 - Breakfast cooked in  12.022275399998762 seconds.