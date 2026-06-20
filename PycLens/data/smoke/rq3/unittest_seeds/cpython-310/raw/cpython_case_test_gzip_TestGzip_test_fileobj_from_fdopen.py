# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_fileobj_from_fdopen

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fd = os.open(self.filename, os.O_WRONLY | os.O_CREAT)
    with os.fdopen(fd, 'wb') as f:
        with gzip.GzipFile(fileobj=f, mode='w') as g:
            pass
