# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_with_open

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with gzip.GzipFile(self.filename, 'wb') as f:
        f.write(b'xxx')
    f = gzip.GzipFile(self.filename, 'rb')
    f.close()
    try:
        with f:
            pass
    except ValueError:
        pass
    else:
        self.fail("__enter__ on a closed file didn't raise an exception")
    try:
        with gzip.GzipFile(self.filename, 'wb') as f:
            1 / 0
    except ZeroDivisionError:
        pass
    else:
        self.fail("1/0 didn't raise an exception")
