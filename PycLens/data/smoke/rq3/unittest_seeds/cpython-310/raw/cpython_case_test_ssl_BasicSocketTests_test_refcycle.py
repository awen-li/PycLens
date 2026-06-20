# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_refcycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = socket.socket(socket.AF_INET)
    ss = test_wrap_socket(s)
    wr = weakref.ref(ss)
    with warnings_helper.check_warnings(('', ResourceWarning)):
        del ss
    self.assertEqual(wr(), None)
