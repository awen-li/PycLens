# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressDecompressFunctionTestCase_test_bad_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, lzma.compress)
    self.assertRaises(TypeError, lzma.compress, [])
    self.assertRaises(TypeError, lzma.compress, b'', format='xz')
    self.assertRaises(TypeError, lzma.compress, b'', check='none')
    self.assertRaises(TypeError, lzma.compress, b'', preset='blah')
    self.assertRaises(TypeError, lzma.compress, b'', filters=1024)
    with self.assertRaises(ValueError):
        lzma.compress(b'', preset=3, filters=[{'id': lzma.FILTER_LZMA2}])
    self.assertRaises(TypeError, lzma.decompress)
    self.assertRaises(TypeError, lzma.decompress, [])
    self.assertRaises(TypeError, lzma.decompress, b'', format='lzma')
    self.assertRaises(TypeError, lzma.decompress, b'', memlimit=7300000000.0)
    with self.assertRaises(TypeError):
        lzma.decompress(b'', format=lzma.FORMAT_RAW, filters={})
    with self.assertRaises(ValueError):
        lzma.decompress(b'', format=lzma.FORMAT_RAW, memlimit=16777216)
    with self.assertRaises(ValueError):
        lzma.decompress(b'', filters=FILTERS_RAW_1)
    with self.assertRaises(ValueError):
        lzma.decompress(b'', format=lzma.FORMAT_XZ, filters=FILTERS_RAW_1)
    with self.assertRaises(ValueError):
        lzma.decompress(b'', format=lzma.FORMAT_ALONE, filters=FILTERS_RAW_1)
