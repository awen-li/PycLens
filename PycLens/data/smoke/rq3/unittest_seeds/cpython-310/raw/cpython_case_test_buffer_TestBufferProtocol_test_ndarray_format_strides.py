# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_format_strides

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nitems = randrange(1, 30)
    for (fmt, items, _) in iter_format(nitems):
        itemsize = struct.calcsize(fmt)
        for step in range(-5, 5):
            if step == 0:
                continue
            shape = [len(items[::step])]
            strides = [step * itemsize]
            offset = itemsize * (nitems - 1) if step < 0 else 0
            for flags in (0, ND_PIL):
                nd = ndarray(items, shape=shape, strides=strides, format=fmt, offset=offset, flags=flags)
                self.verify(nd, obj=None, itemsize=itemsize, fmt=fmt, readonly=True, ndim=1, shape=shape, strides=strides, lst=items[::step])
