# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bz2.py
# case: BZ2DecompressorTest_test_decompressor_inputbuf_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bzd = BZ2Decompressor()
    out = []
    out.append(bzd.decompress(self.DATA[:200], 5))
    out.append(bzd.decompress(self.DATA[200:300], 5))
    out.append(bzd.decompress(self.DATA[300:]))
    self.assertEqual(b''.join(out), self.TEXT)
