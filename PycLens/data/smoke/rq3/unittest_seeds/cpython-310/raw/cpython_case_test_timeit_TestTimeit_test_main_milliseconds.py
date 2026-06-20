# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_main_milliseconds

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.run_main(seconds_per_increment=0.0055)
    self.assertEqual(s, '50 loops, best of 5: 5.5 msec per loop\n')
