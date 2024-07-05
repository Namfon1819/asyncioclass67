# example of getting the current task from the main coroutine
import asyncio

# define a main coroutine
async def main():
    # report a message
    print('main coroutine started')
    # get the current task
    task = asyncio.current_task()
    # report its details
    print(task)

# start the asyncio program
asyncio.run(main())

##ผลลัพธ์
#main coroutine started
#<Task pending name='Task-1' coro=<main() running at c:\analys\asyncioclass67\assignment4\asyncio01.py:11> cb=[_run_until_complete_cb() at C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\asyncio\base_events.py:181]> 