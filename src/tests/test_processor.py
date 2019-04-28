from src.processor import Processor
from unittest.mock import Mock, patch
from collections import deque
import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


@patch('src.tasks.process_event.delay')
def test_process_events(process_event_task_mock):
    events = [{'wait': 0.01, 'type': 'edit'} for x in range(5)]
    p = Processor()
    assert p.async_results == deque()
    p._process_events(events)
    assert len(p.async_results) == 5
    process_event_task_mock.assert_called_with(events[0])


def test_next_result_ready():
    a = Mock()
    a.ready.return_value = False
    p = Processor()
    p.async_results = deque([a])
    res = p._next_result_ready()
    assert res is False
    a.ready.return_value = True
    p.async_results = deque([a])
    res = p._next_result_ready()
    assert res is True


@patch('src.processor.Processor._process_events')
@patch('src.processor.Processor._write_outfile')
def test_processor_process(process_events_mock, write_outfile_mock):
    events = [{'wait': 0.01, 'type': 'edit'} for x in range(5)]
    p = Processor()
    p.process(events=events)
    process_events_mock.assert_called_once()
    write_outfile_mock.assert_called_once()


def test_processor_init():
    p = Processor()
    assert p.async_results is not None
    assert isinstance(p.async_results, deque)
