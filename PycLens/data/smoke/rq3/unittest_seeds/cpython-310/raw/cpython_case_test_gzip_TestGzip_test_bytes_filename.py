# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_bytes_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    str_filename = self.filename
    try:
        bytes_filename = str_filename.encode('ascii')
    except UnicodeEncodeError:
        self.skipTest('Temporary file name needs to be ASCII')
    with gzip.GzipFile(bytes_filename, 'wb') as f:
        f.write(data1 * 50)
    with gzip.GzipFile(bytes_filename, 'rb') as f:
        self.assertEqual(f.read(), data1 * 50)
    with gzip.GzipFile(str_filename, 'rb') as f:
        self.assertEqual(f.read(), data1 * 50)
