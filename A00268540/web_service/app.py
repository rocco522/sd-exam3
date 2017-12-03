from flask import Flask, render_template, request, make_response, g
from redis import Redis
import os
import socket
import random
import json

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
host = socket.gethostname()

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen %s times. My Host name is %s\n\n' % (count ,host)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)