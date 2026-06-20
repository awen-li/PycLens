# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_seek_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with gzip.GzipFile(self.filename, 'w') as f:
        for pos in range(0, 256, 16):
            f.seek(pos)
            f.write(b'GZ\n')
