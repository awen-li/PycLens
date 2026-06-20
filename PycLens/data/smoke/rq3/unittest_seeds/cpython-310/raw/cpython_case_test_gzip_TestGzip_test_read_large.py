# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_read_large

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    compressed = gzip.compress(data1, compresslevel=1)
    f = gzip.GzipFile(fileobj=io.BytesIO(compressed), mode='rb')
    self.assertEqual(f.read(size), data1)
