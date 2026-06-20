# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_issue_7385

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = ndarray([1, 2, 3], shape=[3], flags=ND_GETBUF_FAIL)
    self.assertRaises(BufferError, memoryview, x)
