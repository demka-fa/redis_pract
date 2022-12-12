#pip3 install redis
import random

import redis

CURRENT_DB = 0
CURRENT_HOST = "127.0.0.1"
CURRENT_PASSWORD = "password"


class NewYearWish:

    def __init__(self, id: int, item: str, accuracy: int = random.randint(0, 100)) -> None:
        self.id = id
        self.item = item
        self.accuracy = accuracy

    def to_storage(self) -> dict:
        return {"id": self.id, "item": self.item, "accuracy": self.accuracy}

    def __str__(self) -> str:
        return f"Моё новогоднее желание: '{self.item}'\nВероятность: {self.accuracy}"


def main():

    cli = redis.Redis(host=CURRENT_HOST, password=CURRENT_PASSWORD, port=6379, decode_responses=True, db=CURRENT_DB)

    if cli.delete("wish") == 1:
        print("Старое новогоднее желание удалено")

    # Пример сохранения структуры класса в Redis
    wish = NewYearWish(1, "To be a millionaire")
    print(wish)

    for key, value in wish.to_storage().items():
        cli.hset("wish", key, value)

    # Пример чтения структуры класса из Redis
    new_wish = NewYearWish(**cli.hgetall("wish"))
    print(new_wish)


if __name__ == "__main__":
    main()
