# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_bad_gzip_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(self.filename, 'wb') as file:
        file.write(data1 * 50)
    with gzip.GzipFile(self.filename, 'r') as file:
        self.assertRaises(gzip.BadGzipFile, file.readlines)
