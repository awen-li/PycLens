# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_refleaks_in_decompressor___init__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gettotalrefcount = support.get_attribute(sys, 'gettotalrefcount')
    lzd = LZMADecompressor()
    refs_before = gettotalrefcount()
    for i in range(100):
        lzd.__init__()
    self.assertAlmostEqual(gettotalrefcount() - refs_before, 0, delta=10)
