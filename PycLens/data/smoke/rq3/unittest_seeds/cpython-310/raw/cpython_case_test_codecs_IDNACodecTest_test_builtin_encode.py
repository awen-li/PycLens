# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: IDNACodecTest_test_builtin_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('python.org'.encode('idna'), b'python.org')
    self.assertEqual('python.org.'.encode('idna'), b'python.org.')
    self.assertEqual('pythön.org'.encode('idna'), b'xn--pythn-mua.org')
    self.assertEqual('pythön.org.'.encode('idna'), b'xn--pythn-mua.org.')
