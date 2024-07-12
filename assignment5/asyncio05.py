import asyncio
from random import random

async def task_menu(arg):
    value = 1 + random()
    print(f"Microwave ({arg}): Cooking {value} seconds...")
    await asyncio.sleep(value)
    print(f"Microwave ({arg}): Finished cooking")
    return f'--{arg} is complete in {value} '

async def main():
    tasks = [
        asyncio.create_task(task_menu("Rice")),
        asyncio.create_task(task_menu("Noodle")),
        asyncio.create_task(task_menu("Curry"))
    ]

    # wait for the first task to fail, or all tasks to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # รายงานจำนวนงานที่เสร็จและรายงานว่าอะไรที่เสร็จแล้วเสร็จตอนไหน และรายงานว่าไม่เสร็จกี่อัน
    print(f"Completed task: {len(done)} task.")
     # get the result of the first completed task
    first_completed_task = done.pop()
    print(first_completed_task.result())
    print(f"Uncompleted tasks: {len(pending)} tasks.")

asyncio.run(main())
