# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sched.py
# case: TestCase_test_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = []
    fun = lambda x: l.append(x)
    scheduler = sched.scheduler(time.time, time.sleep)
    self.assertTrue(scheduler.empty())
    for x in [0.05, 0.04, 0.03, 0.02, 0.01]:
        z = scheduler.enterabs(x, 1, fun, (x,))
    self.assertFalse(scheduler.empty())
    scheduler.run()
    self.assertTrue(scheduler.empty())
