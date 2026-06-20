# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_exclusive_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with gzip.GzipFile(self.filename, 'xb') as f:
        f.write(data1 * 50)
    with gzip.GzipFile(self.filename, 'rb') as f:
        self.assertEqual(f.read(), data1 * 50)
    with self.assertRaises(FileExistsError):
        gzip.GzipFile(self.filename, 'xb')
