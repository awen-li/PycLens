# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestOpen_test_bad_params

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        gzip.open(123.456)
    with self.assertRaises(ValueError):
        gzip.open(self.filename, 'wbt')
    with self.assertRaises(ValueError):
        gzip.open(self.filename, 'xbt')
    with self.assertRaises(ValueError):
        gzip.open(self.filename, 'rb', encoding='utf-8')
    with self.assertRaises(ValueError):
        gzip.open(self.filename, 'rb', errors='ignore')
    with self.assertRaises(ValueError):
        gzip.open(self.filename, 'rb', newline='\n')
