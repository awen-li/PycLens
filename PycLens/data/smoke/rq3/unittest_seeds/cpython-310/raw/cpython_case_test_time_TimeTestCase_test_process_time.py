# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_process_time

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    start = time.process_time()
    time.sleep(0.1)
    stop = time.process_time()
    self.assertLess(stop - start, 0.02)
    info = time.get_clock_info('process_time')
    self.assertTrue(info.monotonic)
    self.assertFalse(info.adjustable)
