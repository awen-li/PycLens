# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = memoryview(bytearray(9))
    r = m.__repr__()
    self.assertTrue(r.startswith('<memory'))
    m.release()
    r = m.__repr__()
    self.assertTrue(r.startswith('<released'))
