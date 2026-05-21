from flask import Flask, request, jsonify, render_template
import redis
import uuid
import os

app = Flask(__name__)

# Redis connection details from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# connect to Redis
r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

### UI HOME PAGE ###
@app.route('/')
def home():
    return render_template('index.html')


### ADD TASK ###
@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task_id = str(uuid.uuid4())

    task = {
        "id": task_id,
        "task": data["task"],
        "done": "false"
    }

    r.hset(f"task:{task_id}", mapping=task)
    r.lpush("tasks", task_id)

    return jsonify(task)


### GET ALL TASKS ###
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    task_ids = r.lrange("tasks", 0, -1)

    tasks = []
    for task_id in task_ids:
        tasks.append(r.hgetall(f"task:{task_id}"))

    return jsonify(tasks)


### DELETE TASK ###
@app.route('/api/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    r.delete(f"task:{task_id}")
    r.lrem("tasks", 0, task_id)

    return jsonify({"status": "deleted"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)