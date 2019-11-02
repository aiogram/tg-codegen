import asyncio

import aiohttp

from aiogram.api.methods import GetUpdates

u = GetUpdates(limit=1)
d = u.build_request()
print(u)
print(d)


async def main():
    token = "TOKEN"
    async with aiohttp.ClientSession() as sess:
        async with sess.get(f"https://api.telegram.org/bot{token}/{d.method}") as resp:
            response = await resp.json()
            result = u.build_response(response)
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
