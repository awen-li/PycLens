# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_kqueue.py
# case: TestKQueue_test_close

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    open_file = open(__file__, 'rb')
    self.addCleanup(open_file.close)
    fd = open_file.fileno()
    kqueue = select.kqueue()
    self.assertIsInstance(kqueue.fileno(), int)
    self.assertFalse(kqueue.closed)
    kqueue.close()
    self.assertTrue(kqueue.closed)
    self.assertRaises(ValueError, kqueue.fileno)
    kqueue.close()
    self.assertRaises(ValueError, kqueue.control, None, 4)
