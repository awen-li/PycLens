# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestOpen_test_encoding_error_handler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with gzip.open(self.filename, 'wb') as f:
        f.write(b'foo\xffbar')
    with gzip.open(self.filename, 'rt', encoding='ascii', errors='ignore') as f:
        self.assertEqual(f.read(), 'foobar')
