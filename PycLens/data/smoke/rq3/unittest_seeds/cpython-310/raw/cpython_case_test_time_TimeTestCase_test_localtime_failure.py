# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_localtime_failure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    invalid_time_t = None
    for time_t in (-1, 2 ** 30, 2 ** 33, 2 ** 60):
        try:
            time.localtime(time_t)
        except OverflowError:
            self.skipTest('need 64-bit time_t')
        except OSError:
            invalid_time_t = time_t
            break
    if invalid_time_t is None:
        self.skipTest('unable to find an invalid time_t value')
    self.assertRaises(OSError, time.localtime, invalid_time_t)
    self.assertRaises(OSError, time.ctime, invalid_time_t)
    self.assertRaises(ValueError, time.localtime, float('nan'))
    self.assertRaises(ValueError, time.ctime, float('nan'))
