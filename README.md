# ew-celery
experiments with celery

[Celery - Distributed Task Queue — Celery 5.4.0 documentation](https://docs.celeryq.dev/).

## run
```shell
docker compose up
```

## create task
```shell
celery -A app call tasks.hello_world
```

## todo
- [ ] use different backends and brokers.
- [ ] fix docker files and add notes about celery + docker.
...
