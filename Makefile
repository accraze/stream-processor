export AMQP_USERNAME=rabbitmq
export AMQP_PASSWORD=1234
export AMQP_URI=amqp://$(AMQP_USERNAME):$(AMQP_PASSWORD)@rabbitmq:5672/%2f

start:
	docker-compose up --build --scale worker=5

reset:
	docker-compose down

test:
	docker exec -it stream-processor_worker_1 sh -c "python -m pytest --disable-pytest-warnings"

process:
	docker exec -it stream-processor_worker_1 sh -c "python -u -m src.processor; exit $?"