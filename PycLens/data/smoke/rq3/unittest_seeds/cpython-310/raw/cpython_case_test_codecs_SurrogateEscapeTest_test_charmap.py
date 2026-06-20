# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: SurrogateEscapeTest_test_charmap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(b'foo\xa5bar'.decode('iso-8859-3', 'surrogateescape'), 'foo\udca5bar')
    self.assertEqual('foo\udca5bar'.encode('iso-8859-3', 'surrogateescape'), b'foo\xa5bar')
