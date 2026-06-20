# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: SurrogateEscapeTest_test_utf8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(b'foo\x80bar'.decode('utf-8', 'surrogateescape'), 'foo\udc80bar')
    self.assertEqual('foo\udc80bar'.encode('utf-8', 'surrogateescape'), b'foo\x80bar')
    self.assertEqual(b'\xed\xb0\x80'.decode('utf-8', 'surrogateescape'), '\udced\udcb0\udc80')
    self.assertEqual('\udced\udcb0\udc80'.encode('utf-8', 'surrogateescape'), b'\xed\xb0\x80')
