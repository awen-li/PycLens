# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_strip_bytearray

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.type2test(b'abc').strip(memoryview(b'ac')), b'b')
    self.assertEqual(self.type2test(b'abc').lstrip(memoryview(b'ac')), b'bc')
    self.assertEqual(self.type2test(b'abc').rstrip(memoryview(b'ac')), b'ab')
