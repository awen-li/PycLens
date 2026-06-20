# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestGzip_test_write_memoryview

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_and_read_back(memoryview(data1 * 50))
    m = memoryview(bytes(range(256)))
    data = m.cast('B', shape=[8, 8, 4])
    self.write_and_read_back(data)
