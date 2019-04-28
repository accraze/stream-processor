from src.settings import AMQP_URI

from celery import Celery


app = Celery('stream_processor',broker=AMQP_URI,
	backend='rpc://',include=['src.tasks'])