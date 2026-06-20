# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestOpen_test_pathlike_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    filename = pathlib.Path(self.filename)
    with gzip.open(filename, 'wb') as f:
        f.write(data1 * 50)
    with gzip.open(filename, 'ab') as f:
        f.write(data1)
    with gzip.open(filename) as f:
        self.assertEqual(f.read(), data1 * 51)
