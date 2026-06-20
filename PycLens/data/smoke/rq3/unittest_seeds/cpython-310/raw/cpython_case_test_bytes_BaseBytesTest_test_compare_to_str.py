# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_compare_to_str

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.type2test(b'\x00a\x00b\x00c') == 'abc', False)
    self.assertEqual(self.type2test(b'\x00\x00\x00a\x00\x00\x00b\x00\x00\x00c') == 'abc', False)
    self.assertEqual(self.type2test(b'a\x00b\x00c\x00') == 'abc', False)
    self.assertEqual(self.type2test(b'a\x00\x00\x00b\x00\x00\x00c\x00\x00\x00') == 'abc', False)
    self.assertEqual(self.type2test() == str(), False)
    self.assertEqual(self.type2test() != str(), True)
