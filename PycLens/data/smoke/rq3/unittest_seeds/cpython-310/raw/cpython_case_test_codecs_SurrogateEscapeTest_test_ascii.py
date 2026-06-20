# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: SurrogateEscapeTest_test_ascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(b'foo\x80bar'.decode('ascii', 'surrogateescape'), 'foo\udc80bar')
    self.assertEqual('foo\udc80bar'.encode('ascii', 'surrogateescape'), b'foo\x80bar')
