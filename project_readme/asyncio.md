# asyncio - Notes

## What is it?
`asyncio` is a library to write code that is concurrent. \
It allows us to write code that runs on a **single thread**. \
It handles multiple tasks by pausing ones that are "waiting" and switching to others that are "ready"

## Core stuff
asyncio gives us an event loop to work with upon starting it with `asyncio.run(function())`. \
`async def` before a function definition tells python's interpreter this function can be
paused and resumed. \
To actually run an async function it takes not just a function call but something like
`await` or `asyncio.run()`. an async function only returns an Object when you call it, it doesn't run the code inside of it unless you use the keywords i mentioned. 
Whenever you `await` on any function call it will pause the function and asks the event loop
to run another one that was waiting.

