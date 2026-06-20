# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bz2.py
# case: BZ2DecompressorTest_test_decompressor_inputbuf_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bzd = BZ2Decompressor()
    out = []
    self.assertEqual(bzd.decompress(self.DATA[:100], max_length=0), b'')
    out.append(bzd.decompress(b'', 2))
    out.append(bzd.decompress(self.DATA[100:105], 15))
    out.append(bzd.decompress(self.DATA[105:]))
    self.assertEqual(b''.join(out), self.TEXT)
