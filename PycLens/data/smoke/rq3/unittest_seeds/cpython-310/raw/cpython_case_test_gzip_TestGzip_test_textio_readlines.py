# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_textio_readlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = (data1 * 50).decode('ascii').splitlines(keepends=True)
    self.test_write()
    with gzip.GzipFile(self.filename, 'r') as f:
        with io.TextIOWrapper(f, encoding='ascii') as t:
            self.assertEqual(t.readlines(), lines)
