# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_fileobj_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gzip.GzipFile(self.filename, 'wb').close()
    with open(self.filename, 'r+b') as f:
        with gzip.GzipFile(fileobj=f, mode='r') as g:
            self.assertEqual(g.mode, gzip.READ)
        with gzip.GzipFile(fileobj=f, mode='w') as g:
            self.assertEqual(g.mode, gzip.WRITE)
        with gzip.GzipFile(fileobj=f, mode='a') as g:
            self.assertEqual(g.mode, gzip.WRITE)
        with gzip.GzipFile(fileobj=f, mode='x') as g:
            self.assertEqual(g.mode, gzip.WRITE)
        with self.assertRaises(ValueError):
            gzip.GzipFile(fileobj=f, mode='z')
    for mode in ('rb', 'r+b'):
        with open(self.filename, mode) as f:
            with gzip.GzipFile(fileobj=f) as g:
                self.assertEqual(g.mode, gzip.READ)
    for mode in ('wb', 'ab', 'xb'):
        if 'x' in mode:
            os_helper.unlink(self.filename)
        with open(self.filename, mode) as f:
            with self.assertWarns(FutureWarning):
                g = gzip.GzipFile(fileobj=f)
            with g:
                self.assertEqual(g.mode, gzip.WRITE)
