# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zlib.py
# case: CompressObjectTestCase_test_badcompresscopy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = zlib.compressobj()
    c.compress(HAMLET_SCENE)
    c.flush()
    self.assertRaises(ValueError, c.copy)
    self.assertRaises(ValueError, copy.copy, c)
    self.assertRaises(ValueError, copy.deepcopy, c)
