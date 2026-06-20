# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_rsplit_unicodewhitespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'\t\n\x0b\x0c\r\x1c\x1d\x1e\x1f')
    self.assertEqual(b.rsplit(), [b'\x1c\x1d\x1e\x1f'])
