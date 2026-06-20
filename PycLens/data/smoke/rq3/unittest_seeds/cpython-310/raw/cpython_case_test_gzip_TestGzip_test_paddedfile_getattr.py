# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_paddedfile_getattr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.test_write()
    with gzip.GzipFile(self.filename, 'rb') as f:
        self.assertTrue(hasattr(f.fileobj, 'name'))
        self.assertEqual(f.fileobj.name, self.filename)
