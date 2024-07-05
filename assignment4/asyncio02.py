# example of starting many tasks and getting access to all tasks
import asyncio

# coroutine for a task
async def task_coroutine(value):
    # report a message
    print(f'task {value} is running')
    # block for a moment
    await asyncio.sleep(1)

# define a main coroutine
async def main():
    # report a message
    print('main coroutine started')
    # start many tasks
    started_tasks = [asyncio.create_task(task_coroutine(i)) for i in range(10)]
    # allow some of the tasks time to start
    await asyncio.sleep(0.1)
    # get all tasks
    tasks = asyncio.all_tasks()
    # report all tasks
    for task in tasks:
        print(f'> {task.get_name()},{task.get_coro()}')
    # wait for all tasks to complete
    for task in started_tasks:
        await task

# start the asyncio program
asyncio.run(main())

##ผลลัพธ์
#main coroutine started
#task 0 is running
#task 1 is running
#task 2 is running
#task 3 is running
#task 4 is running
#task 5 is running
#task 6 is running
#task 7 is running
#task 8 is running
#task 9 is running
#> Task-8,<coroutine object task_coroutine at 0x000001E0CFA9E5E0>
#> Task-10,<coroutine object task_coroutine at 0x000001E0CFA9E7A0>
#> Task-11,<coroutine object task_coroutine at 0x000001E0CFA9E880>
#> Task-1,<coroutine object main at 0x000001E0CFA05840>
#> Task-4,<coroutine object task_coroutine at 0x000001E0CFA9E260>
#> Task-6,<coroutine object task_coroutine at 0x000001E0CFA9E420>
#> Task-9,<coroutine object task_coroutine at 0x000001E0CFA9E6C0>
#> Task-5,<coroutine object task_coroutine at 0x000001E0CFA9E340>
#> Task-3,<coroutine object task_coroutine at 0x000001E0CFA9DE00>
#> Task-2,<coroutine object task_coroutine at 0x000001E0CFA9E0A0>
#> Task-7,<coroutine object task_coroutine at 0x000001E0CFA9E500>