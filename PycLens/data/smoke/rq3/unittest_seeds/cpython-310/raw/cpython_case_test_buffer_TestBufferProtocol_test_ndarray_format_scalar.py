# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_format_scalar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (fmt, scalar, _) in iter_format(0):
        itemsize = struct.calcsize(fmt)
        nd = ndarray(scalar, shape=(), format=fmt)
        self.verify(nd, obj=None, itemsize=itemsize, fmt=fmt, readonly=True, ndim=0, shape=(), strides=(), lst=scalar)
