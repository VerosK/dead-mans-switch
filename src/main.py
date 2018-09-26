#!/usr/bin/env python3

from redis import StrictRedis
import json

from flask import Flask, make_response, request

application = Flask(__name__)

@application.route("/")
def alive():
    return "Yes, I'm alive."

@application.route("/alive/<key>/")
def set_alive(key):
    ttl = 300
    redis_store = StrictRedis(host='localhost', port=6379, db=0)
    redis_store.set(name=key, value="1", ex=ttl)
    redis_store.set(name='{}:address'.format(key),
                    value=request.remote_addr,
                    ex=ttl)
    redis_store.set(name='{}:headers'.format(key),
                    value=json.dumps(dict(request.headers)),
                    ex=ttl)

    response = make_response('OK')
    response.headers['Cache-Control'] = 'no-cache'
    return response

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8230)
