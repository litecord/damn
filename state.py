import asyncio
import asyncpg


class DamnState:
    def __init__(self, app, **kwargs):
        self.app = app
        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self.init_async(**kwargs))

    async def init_async(self, **kwargs):
        self.conn = await asyncpg.connect(**kwargs)

    def run(self, **kwargs):
        self.app.run(**kwargs)
