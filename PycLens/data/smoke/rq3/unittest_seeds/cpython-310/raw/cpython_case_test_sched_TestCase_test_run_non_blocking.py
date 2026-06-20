# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sched.py
# case: TestCase_test_run_non_blocking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l = []
    fun = lambda x: l.append(x)
    scheduler = sched.scheduler(time.time, time.sleep)
    for x in [10, 9, 8, 7, 6]:
        scheduler.enter(x, 1, fun, (x,))
    scheduler.run(blocking=False)
    self.assertEqual(l, [])
