# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_memoryview_from_buffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for flags in (0, ND_PIL):
        nd = ndarray(list(range(3)), shape=[3], flags=flags)
        m = nd.memoryview_from_buffer()
        self.assertEqual(m, nd)
