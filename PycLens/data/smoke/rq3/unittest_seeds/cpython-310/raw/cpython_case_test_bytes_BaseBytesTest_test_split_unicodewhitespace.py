# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_split_unicodewhitespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for b in (b'a\x1cb', b'a\x1db', b'a\x1eb', b'a\x1fb'):
        b = self.type2test(b)
        self.assertEqual(b.split(), [b])
    b = self.type2test(b'\t\n\x0b\x0c\r\x1c\x1d\x1e\x1f')
    self.assertEqual(b.split(), [b'\x1c\x1d\x1e\x1f'])
