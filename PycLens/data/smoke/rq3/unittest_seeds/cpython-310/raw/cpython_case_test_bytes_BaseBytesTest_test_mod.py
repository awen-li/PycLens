# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_mod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'hello, %b!')
    orig = b
    b = b % b'world'
    self.assertEqual(b, b'hello, world!')
    self.assertEqual(orig, b'hello, %b!')
    self.assertFalse(b is orig)
    b = self.type2test(b'%s / 100 = %d%%')
    a = b % (b'seventy-nine', 79)
    self.assertEqual(a, b'seventy-nine / 100 = 79%')
    self.assertIs(type(a), self.type2test)
    b = self.type2test(b'hello,\x00%b!')
    b = b % b'world'
    self.assertEqual(b, b'hello,\x00world!')
    self.assertIs(type(b), self.type2test)
