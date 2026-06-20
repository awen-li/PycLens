# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_maxlenmisc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dco = zlib.decompressobj()
    self.assertRaises(ValueError, dco.decompress, b'', -1)
    self.assertEqual(b'', dco.unconsumed_tail)
