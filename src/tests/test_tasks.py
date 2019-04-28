import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


from src.tasks import process_event

def test_event():
    event = {'wait': 0.01, 'type': 'edit'}
    res = process_event(event)
    assert event == res