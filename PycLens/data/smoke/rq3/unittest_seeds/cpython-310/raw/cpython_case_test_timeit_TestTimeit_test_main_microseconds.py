# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_main_microseconds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.run_main(seconds_per_increment=2.5e-06, switches=['-n100'])
    self.assertEqual(s, '100 loops, best of 5: 2.5 usec per loop\n')
