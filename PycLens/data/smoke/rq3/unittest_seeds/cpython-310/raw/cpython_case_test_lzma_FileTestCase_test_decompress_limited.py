# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_lzma.py
# case: FileTestCase_test_decompress_limited

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bomb = lzma.compress(b'\x00' * int(2000000.0), preset=6)
    self.assertLess(len(bomb), _compression.BUFFER_SIZE)
    decomp = LZMAFile(BytesIO(bomb))
    self.assertEqual(decomp.read(1), b'\x00')
    max_decomp = 1 + DEFAULT_BUFFER_SIZE
    self.assertLessEqual(decomp._buffer.raw.tell(), max_decomp, 'Excessive amount of data was decompressed')
