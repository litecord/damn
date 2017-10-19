import logging

from sanic import Sanic
from sanic import response

from state import DamnState

logging.basicConfig(level=logging.DEBUG)
app = Sanic()
state = DamnState(app)


def to_json(record):
    base = {}
    for field in record:
        base[field] = record[field]
    return base


@app.route('/')
async def index(req):
    return response.text('hello')


@app.route('/raw_query_user')
async def h_rawquery_user(req):
    pass


@app.route('/query_user')
async def h_queryuser(req):
    payload = req.json
    user_id = payload['id']
    limit = payload.get('limit')

    basequery = f'SELECT * FROM users WHERE user_id={user_id}'
    if limit:
        basequery = f'{basequery} LIMIT {limit}'

    stmt = await state.conn.prepare(basequery)
    rows = await stmt.fetchrows()
    res = []
    for record in rows:
        res.append(to_json(record))

    return response.json(res)


@app.route('/query_channel')
async def h_querychan(req):
    pass


@app.route('/query_guild')
async def h_queryguild(req):
    pass


@app.route('/query_message')
async def h_querymessage(req):
    pass


@app.route('/put')
async def h_put(req):
    pass


if __name__ == "__main__":
    damn = DamnState(app)
    damn.run(host="0.0.0.0", port=8691)
