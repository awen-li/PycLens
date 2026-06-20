# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_read_truncated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = data1 * 50
    truncated = gzip.compress(data)[:-8]
    with gzip.GzipFile(fileobj=io.BytesIO(truncated)) as f:
        self.assertRaises(EOFError, f.read)
    with gzip.GzipFile(fileobj=io.BytesIO(truncated)) as f:
        self.assertEqual(f.read(len(data)), data)
        self.assertRaises(EOFError, f.read, 1)
    for i in range(2, 10):
        with gzip.GzipFile(fileobj=io.BytesIO(truncated[:i])) as f:
            self.assertRaises(EOFError, f.read, 1)
