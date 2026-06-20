# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_multidim

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for ndim in range(5):
        shape_t = [randrange(2, 10) for _ in range(ndim)]
        nitems = prod(shape_t)
        for shape in permutations(shape_t):
            (fmt, items, _) = randitems(nitems)
            itemsize = struct.calcsize(fmt)
            for flags in (0, ND_PIL):
                if ndim == 0 and flags == ND_PIL:
                    continue
                nd = ndarray(items, shape=shape, format=fmt, flags=flags)
                strides = strides_from_shape(ndim, shape, itemsize, 'C')
                lst = carray(items, shape)
                self.verify(nd, obj=None, itemsize=itemsize, fmt=fmt, readonly=True, ndim=ndim, shape=shape, strides=strides, lst=lst)
                if is_memoryview_format(fmt):
                    ex = ndarray(items, shape=shape, format=fmt)
                    nd = ndarray(ex, getbuf=PyBUF_CONTIG_RO | PyBUF_FORMAT)
                    self.assertTrue(nd.strides == ())
                    mv = nd.memoryview_from_buffer()
                    self.verify(mv, obj=None, itemsize=itemsize, fmt=fmt, readonly=True, ndim=ndim, shape=shape, strides=strides, lst=lst)
                nd = ndarray(items, shape=shape, format=fmt, flags=flags | ND_FORTRAN)
                strides = strides_from_shape(ndim, shape, itemsize, 'F')
                lst = farray(items, shape)
                self.verify(nd, obj=None, itemsize=itemsize, fmt=fmt, readonly=True, ndim=ndim, shape=shape, strides=strides, lst=lst)
