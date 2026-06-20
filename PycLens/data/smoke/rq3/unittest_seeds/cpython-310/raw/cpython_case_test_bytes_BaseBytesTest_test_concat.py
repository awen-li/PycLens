# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_concat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b1 = self.type2test(b'abc')
    b2 = self.type2test(b'def')
    self.assertEqual(b1 + b2, b'abcdef')
    self.assertEqual(b1 + bytes(b'def'), b'abcdef')
    self.assertEqual(bytes(b'def') + b1, b'defabc')
    self.assertRaises(TypeError, lambda : b1 + 'def')
    self.assertRaises(TypeError, lambda : 'abc' + b2)
