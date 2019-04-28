# stream-processor
A simple, scalable stream processor powered via Celery.

## Setup

### Running via Docker

First, build all containers and start all workers.
```
make start
```

In another terminal, you can run the following command to process the sampled
events:

```
make process
```


### Running locally

```
virtualenv -p python 3 env
source env/bin/activate
```

Next install dependencies:

```
pip install pipenv
pipenv install
```

Start a celery worker:

```
celery -A src worker --loglevel=info
```

In another terminal, run the processor script:

```
python -m src.processor
```


### Tests

You can run the tests inside a worker container via Docker as follows:
```
make test
```

Or you can do it locally as follows:
```
python -m pytest
```
