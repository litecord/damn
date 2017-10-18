import asyncpg

from sanic import Sanic
from sanic import response

app = Sanic()


def to_json(record):
    base = {}
    for field in record:
        base[field] = record[field]
    return base


class DamnState:
    def __init__(self, app, **kwargs):
        self.app = app
        self.loop = app.loop
        self.loop.ensure_future(self.init_async(**kwargs))

    async def init_async(self, **kwargs):
        self.conn = await asyncpg.connect(**kwargs)

    @app.route('/')
    async def index(self, req):
        return response.text('hello')

    @app.route('/raw_query_user')
    async def h_rawquery_user(self, req):
        pass

    @app.route('/query_user')
    async def h_queryuser(self, req):
        payload = req.json
        user_id = payload['id']
        limit = payload.get('limit')
        stmt = await self.conn.prepare(
            f'''SELECT * FROM users WHERE user_id={user_id} LIMIT '''
            f'''{"LIMIT {limit}" if payload["limit"]}'''
        )

        rows = await stmt.fetchrows()
        res = []
        for record in rows:
            res.append(to_json(record))

        return response.json(res)

    @app.route('/query_channel')
    async def h_querychan(self, req):
        pass

    @app.route('/query_guild')
    async def h_queryguild(self, req):
        pass

    @app.route('/query_message')
    async def h_querymessage(self, req):
        pass

    @app.route('/put')
    async def h_put(self, req):
        pass

    def run(self, **kwargs):
        app.run(**kwargs)


if __name__ == "__main__":
    damn = DamnState(app)
    damn.run(host="0.0.0.0", port=8691)
