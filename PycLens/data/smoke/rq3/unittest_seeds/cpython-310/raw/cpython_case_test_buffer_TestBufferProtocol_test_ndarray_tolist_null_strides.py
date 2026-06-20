# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_tolist_null_strides

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ex = ndarray(list(range(20)), shape=[2, 2, 5])
    nd = ndarray(ex, getbuf=PyBUF_ND | PyBUF_FORMAT)
    self.assertEqual(nd.tolist(), ex.tolist())
    m = memoryview(ex)
    self.assertEqual(m.tolist(), ex.tolist())
