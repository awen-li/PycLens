# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_source_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(_imp.source_hash(42, b'hi'), b'\xc6\xe7Z\r\x03:}\xab')
    self.assertEqual(_imp.source_hash(43, b'hi'), b'\x85\x9765\xf8\x9a\x8b9')
