# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bz2.py
# case: BZ2DecompressorTest_test_refleaks_in___init__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gettotalrefcount = support.get_attribute(sys, 'gettotalrefcount')
    bzd = BZ2Decompressor()
    refs_before = gettotalrefcount()
    for i in range(100):
        bzd.__init__()
    self.assertAlmostEqual(gettotalrefcount() - refs_before, 0, delta=10)
