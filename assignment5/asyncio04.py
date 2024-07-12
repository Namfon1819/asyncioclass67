# example of waiting for all tasks to be completed with a timeout
from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 10
    value = random()* 10
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'>task {arg} done with {value}')

# main coroutine
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for all tasks to complete
    done, pending = await asyncio.wait(tasks, timeout=5)
    # report results
    print(f'Done, {len(done)} tasks completed in time')

# start the asyncio program
asyncio. run(main())

##ผลลัพธ์
#>task 5 done with 1.3223095134290352
#>task 8 done with 2.426086634260013
#>task 3 done with 4.861360704169354
#Done, 3 tasks completed in time