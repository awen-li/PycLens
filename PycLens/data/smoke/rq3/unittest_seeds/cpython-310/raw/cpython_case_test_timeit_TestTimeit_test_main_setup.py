# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_main_setup

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.run_main(seconds_per_increment=2.0, switches=['-n35', '-s', 'print("CustomSetup")'])
    self.assertEqual(s, 'CustomSetup\n' * DEFAULT_REPEAT + '35 loops, best of 5: 2 sec per loop\n')
