# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hmac.py
# case: CopyTestCase_test_realcopy_hmac

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h1 = hmac.HMAC.__new__(hmac.HMAC)
    h1._init_hmac(b'key', b'msg', digestmod='sha256')
    h2 = h1.copy()
    self.assertTrue(id(h1._hmac) != id(h2._hmac))
