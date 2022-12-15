import flask
from flask import request, jsonify
import time
app = flask.Flask(__name__)
app.config["DEBUG"] = True
import random
import redis

CURRENT_DB = 0
CURRENT_HOST = "127.0.0.1"
CURRENT_PASSWORD = "password"


def get_item_from_db(value) -> int:
    random_item = random.randint(10,100)
    time.sleep(1)
    return random_item

    
cli = redis.Redis(host=CURRENT_HOST, password=CURRENT_PASSWORD, decode_responses=True, db=CURRENT_DB)

@app.route('/api/item/<item_id>')
def get_item(item_id):

    cache_item = cli.get(item_id)
    if cache_item is not None:
        return {"result" : cache_item}

    item_data = get_item_from_db(item_id)
    cli.set(item_id, item_data)
    return  {"result" : item_data}

app.run(host='127.0.0.1',port=8000, threaded=True)