# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_baddecompresscopy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = zlib.compress(HAMLET_SCENE)
    d = zlib.decompressobj()
    d.decompress(data)
    d.flush()
    self.assertRaises(ValueError, d.copy)
    self.assertRaises(ValueError, copy.copy, d)
    self.assertRaises(ValueError, copy.deepcopy, d)
