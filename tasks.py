from app import app


@app.task(bind=True)
def hello_world(self) -> None:
    return "hello world"
