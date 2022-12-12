# pip install rq
from datetime import timedelta

import redis
from rq import Queue

import tasks



CURRENT_DB = 0
CURRENT_HOST = "127.0.0.1"
CURRENT_PASSWORD = "password"

cli = redis.Redis(host=CURRENT_HOST, password=CURRENT_PASSWORD, decode_responses=True, db=CURRENT_DB)
queue = Queue(connection=cli)

def queue_tasks():
    queue.enqueue(tasks.print_task, 5)
    queue.enqueue_in(timedelta(seconds=10), tasks.print_numbers, 5)

def main():
    queue_tasks()

if __name__ == "__main__":
    main()