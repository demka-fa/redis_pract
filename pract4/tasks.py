from datetime import datetime, timedelta
#Запускать через rq worker --url redis://:secrets@example.com:1234/9 --with-scheduler с терминалки
import time

def print_task(seconds):
    print("Starting task")
    for num in range(seconds):
        print(num, ". Hello World!")
        time.sleep(1)
    print("Task completed")

def print_numbers(seconds):
    print("Starting num task")
    for num in range(seconds):
        print(num)
        time.sleep(1)
    print("Task to print_numbers completed")