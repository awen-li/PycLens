# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bz2.py
# case: BZ2DecompressorTest_test_failure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bzd = BZ2Decompressor()
    self.assertRaises(Exception, bzd.decompress, self.BAD_DATA * 30)
    self.assertRaises(Exception, bzd.decompress, self.BAD_DATA * 30)
