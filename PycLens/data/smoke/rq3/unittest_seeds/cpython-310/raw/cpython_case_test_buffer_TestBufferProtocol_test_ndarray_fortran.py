# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_fortran

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ex = ndarray(items, shape=(3, 4), strides=(1, 3))
    nd = ndarray(ex, getbuf=PyBUF_F_CONTIGUOUS | PyBUF_FORMAT)
    self.assertEqual(nd.tolist(), farray(items, (3, 4)))
