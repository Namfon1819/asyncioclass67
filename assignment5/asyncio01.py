# example of waiting for all tasks to complete
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

# main coroutine
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for all tasks to complete
    done,pending = await asyncio.wait(tasks)
    # report results
    print('All done')
    
# start the asyncio program
asyncio.run(main())

##ผลลัพธ์
#>task 8 done with 0.4270385841894234
#>task 2 done with 0.45008880461646006
#>task 6 done with 0.6615233223100677
#>task 1 done with 0.7528566903967143
#>task 7 done with 0.7607528290536869
#>task 3 done with 0.7858261501549905
#>task 4 done with 0.8075301624896082
#>task 5 done with 0.8579426011842038
#>task 9 done with 0.886705662378863
#>task 0 done with 0.9587687699043862
#All done