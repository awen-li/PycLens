# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_readline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.test_write()
    with gzip.GzipFile(self.filename, 'rb') as f:
        line_length = 0
        while 1:
            L = f.readline(line_length)
            if not L and line_length != 0:
                break
            self.assertTrue(len(L) <= line_length)
            line_length = (line_length + 1) % 50
