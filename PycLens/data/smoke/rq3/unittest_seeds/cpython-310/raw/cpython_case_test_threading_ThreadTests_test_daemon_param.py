# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_daemon_param

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = threading.Thread()
    self.assertFalse(t.daemon)
    t = threading.Thread(daemon=False)
    self.assertFalse(t.daemon)
    t = threading.Thread(daemon=True)
    self.assertTrue(t.daemon)
