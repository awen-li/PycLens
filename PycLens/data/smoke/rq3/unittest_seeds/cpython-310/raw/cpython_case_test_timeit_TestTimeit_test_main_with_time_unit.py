# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_timeit.py
# case: TestTimeit_test_main_with_time_unit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    unit_sec = self.run_main(seconds_per_increment=0.003, switches=['-u', 'sec'])
    self.assertEqual(unit_sec, '100 loops, best of 5: 0.003 sec per loop\n')
    unit_msec = self.run_main(seconds_per_increment=0.003, switches=['-u', 'msec'])
    self.assertEqual(unit_msec, '100 loops, best of 5: 3 msec per loop\n')
    unit_usec = self.run_main(seconds_per_increment=0.003, switches=['-u', 'usec'])
    self.assertEqual(unit_usec, '100 loops, best of 5: 3e+03 usec per loop\n')
    with captured_stderr() as error_stringio:
        invalid = self.run_main(seconds_per_increment=0.003, switches=['-u', 'parsec'])
    self.assertEqual(error_stringio.getvalue(), 'Unrecognized unit. Please select nsec, usec, msec, or sec.\n')
