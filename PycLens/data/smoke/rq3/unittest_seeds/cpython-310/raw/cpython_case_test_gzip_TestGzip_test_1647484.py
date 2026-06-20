# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_1647484

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for mode in ('wb', 'rb'):
        with gzip.GzipFile(self.filename, mode) as f:
            self.assertTrue(hasattr(f, 'name'))
            self.assertEqual(f.name, self.filename)
