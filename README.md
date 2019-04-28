# stream-processor
A simple, scalable stream processor powered via Celery and RabbitMQ.
This was developed using Python 3.7.2 and is not compatible with Python 2.7

## Setup

### Running via Docker

First, build and start all containers. 
**Note:** this will start 5 workers. You can scale the number of workers in the Makefile script.
```
make start
```

In another terminal, once all containers have started, you can run the following command to process the sampled events:

```
make process
```

You can monitor the workers in real-time using the `flower` container hosted at:
http://localhost:8888/

Also, the worker container has been released to Dockerhub:
https://hub.docker.com/r/accraze/stream-processor

### Running locally
First make sure you have [RabbitMQ](https://www.rabbitmq.com/) installed and running on your local machine.
Now create a virtualenv:
```
virtualenv -p python3 env
source env/bin/activate
```

Next install dependencies and set env variables:

```
pip install pipenv
pipenv install

export PROCESSOR_EVENT_FILE="sampled_rc.json"
export PROCESSOR_RESULTS_OUTFILE="results.json"
```

Start celery workers (**Note:** this will start 5 workers):

```
celery multi start 5 -A src worker --loglevel=info
```

Run the processor script:

```
python -m src.processor
```

Stop workers:
```
celery multi stop 5
```


## Tests

You can run the tests inside a worker container via Docker as follows:
```
make test
```

Or you can do it locally as follows:
```
python -m pytest
```
