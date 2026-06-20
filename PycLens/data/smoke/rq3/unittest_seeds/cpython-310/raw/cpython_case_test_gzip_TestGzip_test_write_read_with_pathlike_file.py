# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_write_read_with_pathlike_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = pathlib.Path(self.filename)
    with gzip.GzipFile(filename, 'w') as f:
        f.write(data1 * 50)
    self.assertIsInstance(f.name, str)
    with gzip.GzipFile(filename, 'a') as f:
        f.write(data1)
    with gzip.GzipFile(filename) as f:
        d = f.read()
    self.assertEqual(d, data1 * 51)
    self.assertIsInstance(f.name, str)
