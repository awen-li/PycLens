# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_charmapcodec.py
# case: CharmapCodecTest_test_encodex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('abc'.encode(codecname), b'abc')
    self.assertEqual('xdef'.encode(codecname), b'abcdef')
    self.assertEqual('defx'.encode(codecname), b'defabc')
    self.assertEqual('dxf'.encode(codecname), b'dabcf')
    self.assertEqual('dxfx'.encode(codecname), b'dabcfabc')
