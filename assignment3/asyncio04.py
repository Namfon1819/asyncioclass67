# Starting task
# Starting task
from time import ctime
import asyncio

async def wash(basket):
    print(f'{ctime()} : Washing Machine ({basket}): Put the coin')
    print(f'{ctime()} : Washing Machine ({basket}): Start washing...')
    await asyncio.sleep(5)
    print(f'{ctime()} : Washing Machine ({basket}): Finished washing')
    return f'{ctime()} : {basket} is completed'

async def main():
    # create coroutine
    coro = wash('Basket A')
    print(f"{ctime()} : {coro}")
    print(f"{ctime()} : {type(coro)}")
    #create task
    task = asyncio.create_task(coro)
    print(f"{ctime()} : {task}")
    print(f"{ctime()} : {type(task)}")
    # run the task
    result = await task
    print(f"{ctime()} : {result}")
    
if __name__ == '__main__':
    asyncio.run(main())

#ผลลัพธ์
#Fri Jun 28 11:16:13 2024 : <coroutine object wash at 0x0000020576F9DA80>
#Fri Jun 28 11:16:13 2024 : <class 'coroutine'>
#Fri Jun 28 11:16:13 2024 : <Task pending name='Task-2' coro=<wash() running at c:\analys\asyncioclass67\assignment3\asyncio04.py:6>>
#Fri Jun 28 11:16:13 2024 : <class '_asyncio.Task'>
#Fri Jun 28 11:16:13 2024 : Washing Machine (Basket A): Put the coin
#Fri Jun 28 11:16:13 2024 : Washing Machine (Basket A): Start washing...
#Fri Jun 28 11:16:18 2024 : Washing Machine (Basket A): Finished washing
#Fri Jun 28 11:16:18 2024 : Fri Jun 28 11:16:18 2024 : Basket A is completed