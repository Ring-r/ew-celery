from app import app
import time


@app.task(bind=True)
def hello_world(self) -> None:
    return "hello world"


@app.task(bind=True)
def sleep(self, seconds: float) -> None:
    time.sleep(seconds)
