
# In Python, if you are working with Coroutines and Tasks in Asynchronous programming, then determine the output of the following code:
import asyncio

async def myAsyncFunc():
    print('Welcome to Asynchronous programing')
    try:
        await asyncio.sleep(-1)
    except asyncio. CancelledError:
        print('Hello Python')
    raise
    finally:
        print('Hello world')

async def main():
    task = asyncio.create_task(myAsyncFunc()) 
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio. CancelledError:
        print("Hi HackerEarth")
asyncio.run(main())
# Output
# 1.
# 2.
# 3.
# 4.
# Welcome to Asynchronous programming
# Hello world
# Hi HackerEarth

# Welcome to Asynchronous programming
# Hello world

# Welcome to Asynchronous programming
# Hello Python
# Hello world

# Welcome to Asynchronous programming
# Hello Python
# Hi HackerEarth
