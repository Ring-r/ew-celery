# ew-celery
experiments with celery

[Celery - Distributed Task Queue — Celery 5.4.0 documentation](https://docs.celeryq.dev/).

## create enviroment
```shell
python3 -m venv .venv
source ./.venv/bin/activate
pip install celery
```

## run dependencies
```shell
docker compose up
```

## run worker
```shell
celery -A app worker --loglevel=INFO
```

## create task
```shell
celery -A app call tasks.hello_world
```

## todo
- [ ] use different backends and brokers.
- [ ] fix docker files and add notes about celery + docker.
...
