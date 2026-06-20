# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_cast_zero_strides

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ex = ndarray([1, 2, 3], shape=[3], strides=[0])
    self.assertFalse(ex.c_contiguous)
    msrc = memoryview(ex)
    self.assertRaises(TypeError, msrc.cast, 'c')
