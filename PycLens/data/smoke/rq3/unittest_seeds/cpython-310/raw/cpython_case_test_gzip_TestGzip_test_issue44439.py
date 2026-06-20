# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_issue44439

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    q = array.array('Q', [1, 2, 3, 4, 5])
    LENGTH = len(q) * q.itemsize
    with gzip.GzipFile(fileobj=io.BytesIO(), mode='w') as f:
        self.assertEqual(f.write(q), LENGTH)
        self.assertEqual(f.tell(), LENGTH)
