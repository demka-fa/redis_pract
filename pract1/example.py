#pip3 indtall redis
import redis

#TODO Поменять
CURRENT_DB = 7
CURRENT_HOST = "127.0.0.1"
CURRENT_PASSWRD = "password"
def main():

    cli = redis.Redis(host=CURRENT_HOST, password=CURRENT_PASSWRD, port=6379, decode_responses=True, db=CURRENT_DB)

    current_key = "fa"
    
    print(cli.get(current_key))
    cli.set(current_key, "value")
    print(cli.get(current_key))

if __name__ == "__main__":
    main()
