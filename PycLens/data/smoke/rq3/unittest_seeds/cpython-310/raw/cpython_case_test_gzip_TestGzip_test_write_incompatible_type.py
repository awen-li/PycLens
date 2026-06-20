# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_write_incompatible_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with gzip.GzipFile(self.filename, 'wb') as f:
        with self.assertRaises(TypeError):
            f.write('')
        with self.assertRaises(TypeError):
            f.write([])
        f.write(data1)
    with gzip.GzipFile(self.filename, 'rb') as f:
        self.assertEqual(f.read(), data1)
