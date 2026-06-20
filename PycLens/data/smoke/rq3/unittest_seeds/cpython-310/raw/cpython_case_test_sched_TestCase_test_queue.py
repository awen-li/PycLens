# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sched.py
# case: TestCase_test_queue

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = []
    fun = lambda x: l.append(x)
    scheduler = sched.scheduler(time.time, time.sleep)
    now = time.time()
    e5 = scheduler.enterabs(now + 0.05, 1, fun)
    e1 = scheduler.enterabs(now + 0.01, 1, fun)
    e2 = scheduler.enterabs(now + 0.02, 1, fun)
    e4 = scheduler.enterabs(now + 0.04, 1, fun)
    e3 = scheduler.enterabs(now + 0.03, 1, fun)
    self.assertEqual(scheduler.queue, [e1, e2, e3, e4, e5])
