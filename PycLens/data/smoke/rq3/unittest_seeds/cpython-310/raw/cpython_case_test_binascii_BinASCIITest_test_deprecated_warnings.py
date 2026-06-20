# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_deprecated_warnings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertWarns(DeprecationWarning):
        self.assertEqual(binascii.b2a_hqx(b'abc'), b'B@*M')
    with self.assertWarns(DeprecationWarning):
        self.assertEqual(binascii.a2b_hqx(b'B@*M'), (b'abc', 0))
    with self.assertWarns(DeprecationWarning):
        self.assertEqual(binascii.rlecode_hqx(b'a' * 10), b'a\x90\n')
    with self.assertWarns(DeprecationWarning):
        self.assertEqual(binascii.rledecode_hqx(b'a\x90\n'), b'a' * 10)
