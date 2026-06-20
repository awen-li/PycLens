# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_thread_time

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not hasattr(time, 'thread_time'):
        if sys.platform.startswith(('linux', 'win')):
            self.fail('time.thread_time() should be available on %r' % (sys.platform,))
        else:
            self.skipTest('need time.thread_time')
    start = time.thread_time()
    time.sleep(0.1)
    stop = time.thread_time()
    self.assertLess(stop - start, 0.02)
    info = time.get_clock_info('thread_time')
    self.assertTrue(info.monotonic)
    self.assertFalse(info.adjustable)
