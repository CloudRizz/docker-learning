from flask import Flask
import redis
import os

app = Flask(__name__)

# Redis connection details from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

# connect to Redis
r = redis.Redis(
    host=REDIS_HOST, 
    port=REDIS_PORT, 
    decode_responses=True
    )

@app.route('/')
def hello_world():
    return 'Hello from Rizwan Hussain!!!'

@app.route('/count')
def count():
    # Increment the count in Redis
    visits = r.incr('visitor_count')
    return f'visitor count: {visits}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)