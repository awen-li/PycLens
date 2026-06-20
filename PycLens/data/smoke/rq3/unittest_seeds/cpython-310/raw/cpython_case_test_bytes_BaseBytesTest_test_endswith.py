# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_endswith

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.type2test(b'hello')
    self.assertFalse(bytearray().endswith(b'anything'))
    self.assertTrue(b.endswith(b'hello'))
    self.assertTrue(b.endswith(b'llo'))
    self.assertTrue(b.endswith(b'o'))
    self.assertFalse(b.endswith(b'whello'))
    self.assertFalse(b.endswith(b'no'))
    with self.assertRaises(TypeError) as cm:
        b.endswith([b'o'])
    exc = str(cm.exception)
    self.assertIn('bytes', exc)
    self.assertIn('tuple', exc)
