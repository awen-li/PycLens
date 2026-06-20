# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_decompress_limited

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bomb = gzip.compress(b'\x00' * int(2000000.0), compresslevel=9)
    self.assertLess(len(bomb), io.DEFAULT_BUFFER_SIZE)
    bomb = io.BytesIO(bomb)
    decomp = gzip.GzipFile(fileobj=bomb)
    self.assertEqual(decomp.read(1), b'\x00')
    max_decomp = 1 + io.DEFAULT_BUFFER_SIZE
    self.assertLessEqual(decomp._buffer.raw.tell(), max_decomp, 'Excessive amount of data was decompressed')
