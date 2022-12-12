import os
import redis
import time

CURRENT_DB = 0
CURRENT_HOST = "127.0.0.1"
CURRENT_PASSWORD = "password"


def ttl_example(r: redis.Redis) -> None:
    """
    Данная функция показывает, как можно устанавливать определенное время жизни ключей (time to live)
    """
    # Создаем ключ '444' со значением 'это не ЕНОТ! и время жизни 8 секунд'
    r.setex('444', 8, "это не ЕНОТ!")
    r.setex('333', 4, "bytrjn")
    r.psetex('555', 3000, "fdctrgd")

    print(r.keys())
    print("-"*40)
    print(f"{r.pttl('555')} - время в милисекундах для ключа 555")
    print(f"{r.ttl('444')} - время в секундах для ключа 444")
    print(f"{r.ttl('333')} - время в секундах для ключа 333\n")
    print("-"*40)

def ttl_remove(r:redis.Redis) -> None:
    """Функция для снятия ограничения времени действия ключа"""
    time.sleep(2)
    r.persist("444") # команда для снятия ограничения
    print(f"{r.pttl('555')} - время в милисекундах для ключа 555")
    print(f"Время жизни для ключа 444 теперь не ограничено", end=": ")
    print(r.ttl("444")) # -1 означает, что ключ не может истечь по времени
    print(f"{r.pttl('333')} - время в милисекундах для ключа 333\n")
    print("-"*40)

def main():

    r = redis.Redis(host=CURRENT_HOST, password=CURRENT_PASSWORD, decode_responses=True, db=CURRENT_DB)

    ttl_example(r)
    ttl_remove(r)
    time.sleep(5) # для того чтобы истек срок действия ключей
    print(f"Ключи которые остались:{r.keys()}")



if __name__ == "__main__":
    main()
