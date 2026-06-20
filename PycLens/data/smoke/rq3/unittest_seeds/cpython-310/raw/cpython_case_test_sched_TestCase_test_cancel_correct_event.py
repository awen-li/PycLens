# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sched.py
# case: TestCase_test_cancel_correct_event

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    events = []
    scheduler = sched.scheduler()
    scheduler.enterabs(1, 1, events.append, ('a',))
    b = scheduler.enterabs(1, 1, events.append, ('b',))
    scheduler.enterabs(1, 1, events.append, ('c',))
    scheduler.cancel(b)
    scheduler.run()
    self.assertEqual(events, ['a', 'c'])
