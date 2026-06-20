# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_startswith

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'hello')
    self.assertFalse(self.type2test().startswith(b'anything'))
    self.assertTrue(b.startswith(b'hello'))
    self.assertTrue(b.startswith(b'hel'))
    self.assertTrue(b.startswith(b'h'))
    self.assertFalse(b.startswith(b'hellow'))
    self.assertFalse(b.startswith(b'ha'))
    with self.assertRaises(TypeError) as cm:
        b.startswith([b'h'])
    exc = str(cm.exception)
    self.assertIn('bytes', exc)
    self.assertIn('tuple', exc)
