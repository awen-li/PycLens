# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF16BETest_test_nonbmp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('\U00010203'.encode(self.encoding), b'\xd8\x00\xde\x03')
    self.assertEqual(b'\xd8\x00\xde\x03'.decode(self.encoding), '\U00010203')
