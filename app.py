from celery import Celery

app = Celery(include=["tasks"])

if __name__ == "__main__":
    app.start()
