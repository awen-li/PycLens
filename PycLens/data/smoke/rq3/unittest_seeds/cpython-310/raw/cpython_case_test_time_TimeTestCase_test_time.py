# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_time

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    time.time()
    info = time.get_clock_info('time')
    self.assertFalse(info.monotonic)
    self.assertTrue(info.adjustable)
