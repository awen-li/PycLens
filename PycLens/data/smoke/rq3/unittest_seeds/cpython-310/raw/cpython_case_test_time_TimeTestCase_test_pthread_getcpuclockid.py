# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_time.py
# case: TimeTestCase_test_pthread_getcpuclockid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    clk_id = time.pthread_getcpuclockid(threading.get_ident())
    self.assertTrue(type(clk_id) is int)
    if platform.system() == 'AIX' and sys.maxsize.bit_length() <= 32:
        self.assertEqual(clk_id, time.CLOCK_THREAD_CPUTIME_ID)
    elif sys.platform.startswith('sunos'):
        self.assertEqual(clk_id, time.CLOCK_THREAD_CPUTIME_ID)
    else:
        self.assertNotEqual(clk_id, time.CLOCK_THREAD_CPUTIME_ID)
    t1 = time.clock_gettime(clk_id)
    t2 = time.clock_gettime(clk_id)
    self.assertLessEqual(t1, t2)
