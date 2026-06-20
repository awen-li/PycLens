# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_timeit_function_zero_iters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    delta_time = timeit.timeit(self.fake_stmt, self.fake_setup, number=0, timer=FakeTimer())
    self.assertEqual(delta_time, 0)
