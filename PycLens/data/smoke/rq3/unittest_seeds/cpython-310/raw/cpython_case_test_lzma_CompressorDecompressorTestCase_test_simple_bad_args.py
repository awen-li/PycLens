# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: CompressorDecompressorTestCase_test_simple_bad_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, LZMACompressor, [])
    self.assertRaises(TypeError, LZMACompressor, format=3.45)
    self.assertRaises(TypeError, LZMACompressor, check='')
    self.assertRaises(TypeError, LZMACompressor, preset='asdf')
    self.assertRaises(TypeError, LZMACompressor, filters=3)
    self.assertRaises(ValueError, LZMACompressor, format=lzma.FORMAT_AUTO)
    with self.assertRaises(ValueError):
        LZMACompressor(preset=7, filters=[{'id': lzma.FILTER_LZMA2}])
    self.assertRaises(TypeError, LZMADecompressor, ())
    self.assertRaises(TypeError, LZMADecompressor, memlimit=b'qw')
    with self.assertRaises(TypeError):
        LZMADecompressor(lzma.FORMAT_RAW, filters='zzz')
    with self.assertRaises(ValueError):
        LZMADecompressor(lzma.FORMAT_RAW, memlimit=16777216)
    self.assertRaises(ValueError, LZMADecompressor, filters=FILTERS_RAW_1)
    with self.assertRaises(ValueError):
        LZMADecompressor(format=lzma.FORMAT_XZ, filters=FILTERS_RAW_1)
    with self.assertRaises(ValueError):
        LZMADecompressor(format=lzma.FORMAT_ALONE, filters=FILTERS_RAW_1)
    lzc = LZMACompressor()
    self.assertRaises(TypeError, lzc.compress)
    self.assertRaises(TypeError, lzc.compress, b'foo', b'bar')
    self.assertRaises(TypeError, lzc.flush, b'blah')
    empty = lzc.flush()
    self.assertRaises(ValueError, lzc.compress, b'quux')
    self.assertRaises(ValueError, lzc.flush)
    lzd = LZMADecompressor()
    self.assertRaises(TypeError, lzd.decompress)
    self.assertRaises(TypeError, lzd.decompress, b'foo', b'bar')
    lzd.decompress(empty)
    self.assertRaises(EOFError, lzd.decompress, b'quux')
