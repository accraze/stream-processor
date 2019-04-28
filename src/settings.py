import os


AMQP_URI = os.environ.get("AMQP_URI")


PROCESSOR_EVENT_FILE = os.environ.get("PROCESSOR_EVENT_FILE", 
	"/stream-processor/sampled_rc.json")

PROCESSOR_RESULTS_OUTFILE = os.environ.get("PROCESSOR_RESULTS_OUTFILE", 
	"/stream-processor/results.json")