# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with gzip.GzipFile(self.filename, 'wb') as f:
        f.write(data1 * 50)
        f.flush()
        f.fileno()
        if hasattr(os, 'fsync'):
            os.fsync(f.fileno())
        f.close()
    f.close()
