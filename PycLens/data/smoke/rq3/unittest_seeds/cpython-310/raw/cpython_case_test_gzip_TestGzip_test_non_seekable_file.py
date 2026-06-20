# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_non_seekable_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    uncompressed = data1 * 50
    buf = UnseekableIO()
    with gzip.GzipFile(fileobj=buf, mode='wb') as f:
        f.write(uncompressed)
    compressed = buf.getvalue()
    buf = UnseekableIO(compressed)
    with gzip.GzipFile(fileobj=buf, mode='rb') as f:
        self.assertEqual(f.read(), uncompressed)
