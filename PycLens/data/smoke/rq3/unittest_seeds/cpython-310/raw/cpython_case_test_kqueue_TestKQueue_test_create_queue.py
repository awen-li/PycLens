# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_kqueue.py
# case: TestKQueue_test_create_queue

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    kq = select.kqueue()
    self.assertTrue(kq.fileno() > 0, kq.fileno())
    self.assertTrue(not kq.closed)
    kq.close()
    self.assertTrue(kq.closed)
    self.assertRaises(ValueError, kq.fileno)
