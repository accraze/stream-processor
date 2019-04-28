from celery import Celery
from src.settings import AMQP_URI

app = Celery('stream_processor', broker=AMQP_URI,
             backend='rpc://', include=['src.tasks'])
