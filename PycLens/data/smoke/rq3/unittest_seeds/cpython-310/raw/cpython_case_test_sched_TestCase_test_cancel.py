# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sched.py
# case: TestCase_test_cancel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = []
    fun = lambda x: l.append(x)
    scheduler = sched.scheduler(time.time, time.sleep)
    now = time.time()
    event1 = scheduler.enterabs(now + 0.01, 1, fun, (0.01,))
    event2 = scheduler.enterabs(now + 0.02, 1, fun, (0.02,))
    event3 = scheduler.enterabs(now + 0.03, 1, fun, (0.03,))
    event4 = scheduler.enterabs(now + 0.04, 1, fun, (0.04,))
    event5 = scheduler.enterabs(now + 0.05, 1, fun, (0.05,))
    scheduler.cancel(event1)
    scheduler.cancel(event5)
    scheduler.run()
    self.assertEqual(l, [0.02, 0.03, 0.04])
