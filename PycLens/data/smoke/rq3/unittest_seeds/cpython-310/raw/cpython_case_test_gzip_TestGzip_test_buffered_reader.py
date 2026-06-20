# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_buffered_reader

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.test_write()
    with gzip.GzipFile(self.filename, 'rb') as f:
        with io.BufferedReader(f) as r:
            lines = [line for line in r]
    self.assertEqual(lines, 50 * data1.splitlines(keepends=True))
