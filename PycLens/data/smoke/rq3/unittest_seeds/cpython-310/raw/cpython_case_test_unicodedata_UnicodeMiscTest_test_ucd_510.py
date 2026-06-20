# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeMiscTest_test_ucd_510

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import unicodedata
    self.assertTrue(unicodedata.mirrored('༺'))
    self.assertTrue(not unicodedata.ucd_3_2_0.mirrored('༺'))
    self.assertTrue('a'.upper() == 'A')
    self.assertTrue('ᵹ'.upper() == 'Ᵹ')
    self.assertTrue('.'.upper() == '.')
