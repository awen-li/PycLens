# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_prepend_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with gzip.open(self.filename, 'wb') as f:
        f.write(data1)
    with gzip.open(self.filename, 'rb') as f:
        f._buffer.raw._fp.prepend()
