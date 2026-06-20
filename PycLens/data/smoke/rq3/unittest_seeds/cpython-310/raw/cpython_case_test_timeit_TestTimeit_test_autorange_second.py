# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_autorange_second

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (num_loops, time_taken) = self.autorange(seconds_per_increment=1.0)
    self.assertEqual(num_loops, 1)
    self.assertEqual(time_taken, 1.0)
