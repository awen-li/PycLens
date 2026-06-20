# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_format_shape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nitems = randrange(1, 10)
    for (fmt, items, _) in iter_format(nitems):
        itemsize = struct.calcsize(fmt)
        for flags in (0, ND_PIL):
            nd = ndarray(items, shape=[nitems], format=fmt, flags=flags)
            self.verify(nd, obj=None, itemsize=itemsize, fmt=fmt, readonly=True, ndim=1, shape=(nitems,), strides=(itemsize,), lst=items)
