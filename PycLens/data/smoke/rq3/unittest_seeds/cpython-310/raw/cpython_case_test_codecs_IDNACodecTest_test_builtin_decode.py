# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: IDNACodecTest_test_builtin_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(str(b'python.org', 'idna'), 'python.org')
    self.assertEqual(str(b'python.org.', 'idna'), 'python.org.')
    self.assertEqual(str(b'xn--pythn-mua.org', 'idna'), 'pythön.org')
    self.assertEqual(str(b'xn--pythn-mua.org.', 'idna'), 'pythön.org.')
