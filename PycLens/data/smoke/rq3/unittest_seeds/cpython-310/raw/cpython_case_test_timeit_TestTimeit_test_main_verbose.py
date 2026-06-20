# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_main_verbose

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.run_main(switches=['-v'])
    self.assertEqual(s, dedent('                1 loop -> 1 secs\n\n                raw times: 1 sec, 1 sec, 1 sec, 1 sec, 1 sec\n\n                1 loop, best of 5: 1 sec per loop\n            '))
