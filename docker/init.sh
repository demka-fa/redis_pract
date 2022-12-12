
#!/bin/sh

docker run --name fa_redis \
    -d -p 6379:6379 \
    --env-file ./data/.env\
    -v $(PWD)/data/redis.conf:/opt/bitnami/redis/mounted-etc/redis.conf \
    bitnami/redis:latest