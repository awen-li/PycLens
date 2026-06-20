# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_index_null_strides

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ex = ndarray(list(range(2 * 4)), shape=[2, 4], flags=ND_WRITABLE)
    nd = ndarray(ex, getbuf=PyBUF_CONTIG)
    self.assertRaises(BufferError, nd.__getitem__, 1)
    self.assertRaises(BufferError, nd.__getitem__, slice(3, 5, 1))
