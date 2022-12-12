# pip3 install redis
import random

import redis

CURRENT_DB = 0
CURRENT_HOST = "127.0.0.1"
CURRENT_PASSWORD = "password"


def main():
    cli = redis.Redis(host=CURRENT_HOST, password=CURRENT_PASSWORD, port=6379, decode_responses=True, db=CURRENT_DB)

    # Пример сохранения int
    cli.set("example_int", 1)
    print(cli.get("example_int"))

    # Пример сохранения float
    cli.set("example_float", 1.1)
    print(cli.get("example_float"))

    # Пример сохранения str
    cli.set("example_str", "str")
    print(cli.get("example_str"))

    # Пример сохранения bytes
    cli.set("example_bytes", b"bytes_example")
    print(cli.get("example_bytes"))

    # Пример получения всех данных + их удаление
    for key in cli.keys("example_*"):
        print(f"Key -> {key}, value -> {cli.get(key)} ")
        cli.delete(key)

    # Убедимся в том, что
    print(len(cli.keys("example_*")))

    # Пример обновления данных
    cli.set("example_int", 41)
    print(cli.get("example_int"))
    cli.set("example_int", 42)
    print(cli.get("example_int"))
    cli.incr("example_int")
    print(cli.get("example_int"))


if __name__ == "__main__":
    main()
