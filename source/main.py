from flask import Flask, request
import redis


app = Flask(__name__)
# We may use redis hostname because web and redis located in the same network
cache = redis.Redis("redis", port=6379, decode_responses=True)


@app.route("/")
def home():
    return "DocuSketch Flask Application"


@app.route("/", methods=["POST"])
def create_item():
    if request.method == "POST":
        # You can send more than 1 value, and they will be added to cache
        keys = request.json.keys()
        for key in keys:
            value = request.json.get(key)
            if value is not None:
                cache.set(key, value)
            else:
                return {"status": 404}
    return {"status": 200}


@app.route("/<item_key>", methods=["GET"])
def get_item(item_key):
    value = cache.get(item_key)
    if value is not None:
        return cache.get(item_key)
    else:
        return {"status": 404}


@app.route("/<item_key>", methods=["PUT"])
def update_item(item_key):
    if request.method == "PUT":
        new_value = request.json.get(item_key)
        old_value = cache.get(item_key)
        if new_value is not None and old_value is not None:
            cache.set(item_key, new_value)
        else:
            return {"status": 404}
    return {"status": 200}



