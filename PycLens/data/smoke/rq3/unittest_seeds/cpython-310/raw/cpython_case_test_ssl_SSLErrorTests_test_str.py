# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SSLErrorTests_test_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ssl.SSLError(1, 'foo')
    self.assertEqual(str(e), 'foo')
    self.assertEqual(e.errno, 1)
    e = ssl.SSLZeroReturnError(1, 'foo')
    self.assertEqual(str(e), 'foo')
    self.assertEqual(e.errno, 1)
