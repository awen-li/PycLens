# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_zero_padded_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with gzip.GzipFile(self.filename, 'wb') as f:
        f.write(data1 * 50)
    with open(self.filename, 'ab') as f:
        f.write(b'\x00' * 50)
    with gzip.GzipFile(self.filename, 'rb') as f:
        d = f.read()
        self.assertEqual(d, data1 * 50, 'Incorrect data in file')
