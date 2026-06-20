# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_timeit_globals_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global _global_timer
    _global_timer = FakeTimer()
    t = timeit.Timer(stmt='_global_timer.inc()', timer=_global_timer)
    self.assertRaises(NameError, t.timeit, number=3)
    timeit.timeit(stmt='_global_timer.inc()', timer=_global_timer, globals=globals(), number=3)
    local_timer = FakeTimer()
    timeit.timeit(stmt='local_timer.inc()', timer=local_timer, globals=locals(), number=3)
