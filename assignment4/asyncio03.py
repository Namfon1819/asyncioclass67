# example of gather for many coroutines in a list
import asyncio

# coroutine used for a task
async def task_coro(value):
    # report a message
    print(f'>task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)
    
# coroutine used for the entry point
async def main():
    # report a message
    print('main starting')
    # create many coroutines
    coros = [task_coro(i) for i in range(10)]
    # run the tasks
    await asyncio.gather(*coros)
    # report a message
    print('main done')
    
# start the asyncio program
asyncio. run(main())

##ผลลัพธ์
#main starting
#>task 0 executing
#>task 1 executing
#>task 2 executing
#>task 3 executing
#>task 4 executing
#>task 5 executing
#>task 6 executing
#>task 7 executing
#>task 8 executing
#>task 9 executing
#main done