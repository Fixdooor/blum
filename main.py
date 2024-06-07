from utils.core import create_sessions
from utils.telegram import Accounts
from utils.starter import start, stats
import asyncio
from itertools import zip_longest
from utils.core import get_all_lines
import os


async def main():
    action = int(input("Выберите действие:\n1. Начать\n2. Добавить аккаунты\n\n> "))

    if not os.path.exists('sessions'): os.mkdir('sessions')
    if not os.path.exists('statistics'): os.mkdir('statistics')

    if action == 2:
        await create_sessions()

    if action == 1:
        action = int(input("Что автоматизируем?:\n1. Blum\n2. Gleam\n3. Все сразу нахуй\n> "))
        if action == 1:
            accounts = await Accounts().get_accounts()
            proxys = get_all_lines("data/proxy.txt")

            tasks = []
            for thread, (account, proxy) in enumerate(zip_longest(accounts, proxys)):
                if not account: break
                tasks.append(asyncio.create_task(start(account=account, thread=thread, proxy=proxy)))

            await asyncio.gather(*tasks)
        if action == 2:
            accounts = await Accounts().get_accounts()
            proxys = get_all_lines("data/proxy.txt")
            tasks = []
            print("Пока такого нету :(")
        if action == 3:
            print("Пока такого нету :(")




if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
