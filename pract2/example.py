#pip3 indtall redis
import random

import redis

#TODO Поменять
CURRENT_DB = 7
CURRENT_HOST = "127.0.0.1"
CURRENT_PASSWRD = "password"


class NewYearWish:
    def __init__(self, item: str, accuracy: int = random.randint(0, 100)) -> None:
        self.item = item
        self.accuracy = accuracy

    def to_dict(self) -> dict:
        return {"item": self.item, "accuracy": self.accuracy}

    def __str__(self) -> str:
        return f"Моё новогоднее желание: '{self.item}'\nВероятность\n:{self.accuracy}"

def main():

    cli = redis.Redis(host=CURRENT_HOST, password=CURRENT_PASSWRD, port=6379, decode_responses=True, db=CURRENT_DB)

    # Пример сохранения структуры класса в Redis
    wish = NewYearWish("car")
    cli.set("wish", wish.to_dict())

    # Пример чтения структуры класса из Redis
    new_wish = NewYearWish(**cli.get("wish"))
    print(new_wish)


if __name__ == "__main__":
    main()
