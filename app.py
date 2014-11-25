from flask import Flask
from redis import Redis
import os
app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    backend_id =  os.environ['AJ_BACKEND']
    return 'Hello World! I have been opened %s times. \nBackend ID: %s' % (redis.get('hits'), backend_id)

@app.route('/health')
def health():
    return 'works'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
