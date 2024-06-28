# check the type of a coroutine
import asyncio
# define a coroutine
async def custom_coro():
    # await another coroutine
    await asyncio.sleep(1)
    
#create the coroutine
coro = custom_coro()
# check the type of the coroutine
print(type(coro))

#ผลลัพธ์
#<class 'coroutine'>
#sys:1: RuntimeWarning: coroutine 'custom_coro' was never awaited