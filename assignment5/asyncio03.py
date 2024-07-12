# example of waiting for the first task to fail
from random import random
import asyncio

# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'>task {arg} done with {value}')
    # conditionally fail
    if value < 0.5:
        raise Exception(f'Something bad happened in {arg}')

# main coroutine
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for the first task to fail, or all tasks to complete
    done,pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    # report result
    print('Done')
    # get the first task to fail
    first = done.pop()
    print(first)
    
# start the asyncio program
asyncio.run(main())

##ผลลัพธ์
#>task 2 done with 0.1688667983149037
#>task 9 done with 0.17493062325197217
#Done
#<Task finished name='Task-4' coro=<task_coro() done, defined at c:\analys\asyncioclass67\assignment5\asyncio03.py:6> exception=Exception('Something bad happened in 2')>