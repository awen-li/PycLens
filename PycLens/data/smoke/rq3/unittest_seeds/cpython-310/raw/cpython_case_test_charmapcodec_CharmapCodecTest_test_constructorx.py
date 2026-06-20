# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_charmapcodec.py
# case: CharmapCodecTest_test_constructorx

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(str(b'abc', codecname), 'abc')
    self.assertEqual(str(b'xdef', codecname), 'abcdef')
    self.assertEqual(str(b'defx', codecname), 'defabc')
    self.assertEqual(str(b'dxf', codecname), 'dabcf')
    self.assertEqual(str(b'dxfx', codecname), 'dabcfabc')
