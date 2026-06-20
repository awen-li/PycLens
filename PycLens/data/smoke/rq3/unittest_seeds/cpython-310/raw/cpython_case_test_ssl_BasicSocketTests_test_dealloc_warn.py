# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_dealloc_warn

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ss = test_wrap_socket(socket.socket(socket.AF_INET))
    r = repr(ss)
    with self.assertWarns(ResourceWarning) as cm:
        ss = None
        support.gc_collect()
    self.assertIn(r, str(cm.warning.args[0]))
