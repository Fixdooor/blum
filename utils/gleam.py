import aiohttp
from fake_useragent import UserAgent
import asyncio
from urllib.parse import unquote
from pyrogram import Client
from pyrogram.raw.functions.messages import RequestWebView, GetMessagesViews

class gleambot:
    def __init__(self, thread: int, account: str, proxy: [str, None]):
        self.proxy = f"http://{proxy}" if proxy is not None else None
        self.thread = thread

        if proxy:
            proxy = {
                "scheme": "http",
                "hostname": proxy.split(":")[1].split("@")[1],
                "port": int(proxy.split(":")[2]),
                "username": proxy.split(":")[0],
                "password": proxy.split(":")[1].split("@")[0]
            }

        self.client = Client(name=account, api_id=config.API_ID, api_hash=config.API_HASH, workdir=config.WORKDIR, proxy=proxy)

        headers = {'User-Agent': UserAgent(os='android').random}
        self.session = aiohttp.ClientSession(headers=headers, trust_env=True)
        self.refresh_token = ''

    async def logout(self):
        await self.session.close()

    async def claim_daily_reward_gleam(self):
        resp = await self.session.post("https://api.gleam.bot/claim", proxy=self.proxy)
        txt = await resp.text()
        await asyncio.sleep(1)
        return True if txt == 'OK' else txt

        resp2 = await self.session.post("https://api.gleam.bot/start-farming", proxy=self.proxy)
        txt2 = await resp2.text()
        await asyncio.sleep(1)
        return True if txt2 == 'OK' else txt2

