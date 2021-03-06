import time

from src.celery import app


@app.task(bind=True, default_retry_delay=10)
def process_event(self, event):
    process_change(event['wait'])
    return event


def process_change(wait_secs):
    start = time.time()
    while time.time() - start < wait_secs:
        time.sleep(0.001)
