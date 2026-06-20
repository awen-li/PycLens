# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sched.py
# case: TestCase_test_enter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = []
    fun = lambda x: l.append(x)
    scheduler = sched.scheduler(time.time, time.sleep)
    for x in [0.5, 0.4, 0.3, 0.2, 0.1]:
        z = scheduler.enter(x, 1, fun, (x,))
    scheduler.run()
    self.assertEqual(l, [0.1, 0.2, 0.3, 0.4, 0.5])
