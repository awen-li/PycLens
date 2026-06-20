# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestOpen_test_newline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    uncompressed = data1.decode('ascii') * 50
    with gzip.open(self.filename, 'wt', encoding='ascii', newline='\n') as f:
        f.write(uncompressed)
    with gzip.open(self.filename, 'rt', encoding='ascii', newline='\r') as f:
        self.assertEqual(f.readlines(), [uncompressed])
