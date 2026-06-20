# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sched.py
# case: TestCase_test_args_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    seq = []

    def fun(*a, **b):
        seq.append((a, b))
    now = time.time()
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enterabs(now, 1, fun)
    scheduler.enterabs(now, 1, fun, argument=(1, 2))
    scheduler.enterabs(now, 1, fun, argument=('a', 'b'))
    scheduler.enterabs(now, 1, fun, argument=(1, 2), kwargs={'foo': 3})
    scheduler.run()
    self.assertCountEqual(seq, [((), {}), ((1, 2), {}), (('a', 'b'), {}), ((1, 2), {'foo': 3})])
