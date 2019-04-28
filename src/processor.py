import json
import time
import filecmp
from collections import deque

from src.settings import PROCESSOR_EVENT_FILE, PROCESSOR_RESULTS_OUTFILE
from src.tasks import process_event


class Processor:

    def __init__(self):
        self.async_results = deque()

    def process(self, events=None):
        """Process a stream of events."""
        if not events:
            events = self._load_event_samples(PROCESSOR_EVENT_FILE)
        self._process_events(events)
        self._write_outfile()

    def _load_event_samples(self, event_file):
        """Load sampled event stream for testing."""
        samples = []
        with open(event_file, 'r') as f:
            for line in f:
                samples.append(json.loads(line))
        return samples

    def _process_events(self, events):
        """Send edit events to celery queue and store results in list."""
        for event in events:
            # save AsyncResult obj to list
            self.async_results.append(process_event.delay(event))

    def _write_outfile(self):
        """Write results to a json file."""
        with open(PROCESSOR_RESULTS_OUTFILE, 'w') as outfile:
            while self.async_results:
                if self._next_result_ready():
                    result = self.async_results.popleft()
                    outfile.write(json.dumps(result.get())+'\n')

    def _next_result_ready(self):
        return self.async_results[0].ready()


if __name__ == '__main__':
    print('Processing sampled events...')
    start_time = time.time()
    Processor().process()
    end_time = time.time()
    print('Total runtime: {}'.format(end_time - start_time))
    valid = filecmp.cmp(PROCESSOR_EVENT_FILE, PROCESSOR_RESULTS_OUTFILE)
    if not valid:
        raise Exception("Files do not match.")
