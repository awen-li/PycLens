# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nd = ndarray(list(range(20)), shape=[3], offset=7)
    self.assertEqual(nd.offset, 7)
    self.assertEqual(nd.tolist(), [7, 8, 9])
