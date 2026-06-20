# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_cast

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bytespec = (('B', lambda ex: list(ex.tobytes())), ('b', lambda ex: [x - 256 if x > 127 else x for x in list(ex.tobytes())]), ('c', lambda ex: [bytes(chr(x), 'latin-1') for x in list(ex.tobytes())]))

    def iter_roundtrip(ex, m, items, fmt):
        srcsize = struct.calcsize(fmt)
        for (bytefmt, to_bytelist) in bytespec:
            m2 = m.cast(bytefmt)
            lst = to_bytelist(ex)
            self.verify(m2, obj=ex, itemsize=1, fmt=bytefmt, readonly=False, ndim=1, shape=[31 * srcsize], strides=(1,), lst=lst, cast=True)
            m3 = m2.cast(fmt)
            self.assertEqual(m3, ex)
            lst = ex.tolist()
            self.verify(m3, obj=ex, itemsize=srcsize, fmt=fmt, readonly=False, ndim=1, shape=[31], strides=(srcsize,), lst=lst, cast=True)
    srcsize = struct.calcsize('I')
    ex = ndarray(9, shape=[], format='I')
    (destitems, destshape) = cast_items(ex, 'B', 1)
    m = memoryview(ex)
    m2 = m.cast('B')
    self.verify(m2, obj=ex, itemsize=1, fmt='B', readonly=True, ndim=1, shape=destshape, strides=(1,), lst=destitems, cast=True)
    destsize = struct.calcsize('I')
    ex = ndarray([9] * destsize, shape=[destsize], format='B')
    (destitems, destshape) = cast_items(ex, 'I', destsize, shape=[])
    m = memoryview(ex)
    m2 = m.cast('I', shape=[])
    self.verify(m2, obj=ex, itemsize=destsize, fmt='I', readonly=True, ndim=0, shape=(), strides=(), lst=destitems, cast=True)
    for (fmt, items, _) in iter_format(31, 'array'):
        ex = array.array(fmt, items)
        m = memoryview(ex)
        iter_roundtrip(ex, m, items, fmt)
    for (fmt, items, _) in iter_format(31, 'memoryview'):
        ex = ndarray(items, shape=[31], format=fmt, flags=ND_WRITABLE)
        m = memoryview(ex)
        iter_roundtrip(ex, m, items, fmt)
