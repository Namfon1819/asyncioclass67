# example of waiting for the first task to complete
from random import random
import asyncio

# coroutine to execute in a new |task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'>task {arg} done with {value}')

# main coroutine
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # report result
    print ( 'Done')
    # get the first task to complete
    first = done.pop()
    print(first)

# start the asyncio program
asyncio.run(main())

##ผลลัพธ์
#>task 1 done with 0.022523360413796878
#>task 3 done with 0.02602417074129515
#>task 2 done with 0.03335267590991098
#>task 4 done with 0.04524360076776324
#Done
#<Task finished name='Task-6' coro=<task_coro() done, defined at c:\analys\asyncioclass67\assignment5\asyncio02.py:6> result=None>