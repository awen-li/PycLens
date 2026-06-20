# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_repr_daemon

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = threading.Thread()
    self.assertNotIn('daemon', repr(t))
    t.daemon = True
    self.assertIn('daemon', repr(t))
