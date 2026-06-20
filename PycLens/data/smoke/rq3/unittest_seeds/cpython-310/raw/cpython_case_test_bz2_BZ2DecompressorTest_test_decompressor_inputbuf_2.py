# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bz2.py
# case: BZ2DecompressorTest_test_decompressor_inputbuf_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bzd = BZ2Decompressor()
    out = []
    self.assertEqual(bzd.decompress(self.DATA[:200], max_length=0), b'')
    out.append(bzd.decompress(b''))
    out.append(bzd.decompress(self.DATA[200:280], 2))
    out.append(bzd.decompress(self.DATA[280:300], 2))
    out.append(bzd.decompress(self.DATA[300:]))
    self.assertEqual(b''.join(out), self.TEXT)
