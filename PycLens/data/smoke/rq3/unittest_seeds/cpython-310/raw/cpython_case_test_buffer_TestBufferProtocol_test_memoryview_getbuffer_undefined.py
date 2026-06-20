# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_getbuffer_undefined

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nd = ndarray([1, 2, 3], [3], flags=ND_GETBUF_FAIL | ND_GETBUF_UNDEFINED)
    self.assertRaises(BufferError, memoryview, nd)
