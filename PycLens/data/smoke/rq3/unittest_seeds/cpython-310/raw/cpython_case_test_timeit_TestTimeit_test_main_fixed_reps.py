# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_main_fixed_reps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.run_main(seconds_per_increment=60.0, switches=['-r9'])
    self.assertEqual(s, '1 loop, best of 9: 60 sec per loop\n')
