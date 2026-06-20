# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_from_static_exporter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fmt = 'B'
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    self.assertRaises(TypeError, staticarray, 1, 2, 3)
    x = staticarray()
    y = memoryview(x)
    self.verify(y, obj=x, itemsize=1, fmt=fmt, readonly=True, ndim=1, shape=[12], strides=[1], lst=lst)
    for i in range(12):
        self.assertEqual(y[i], i)
    del x
    del y
    x = staticarray()
    y = memoryview(x)
    del y
    del x
    x = staticarray()
    y = ndarray(x, getbuf=PyBUF_FULL_RO)
    z = ndarray(y, getbuf=PyBUF_FULL_RO)
    m = memoryview(z)
    self.assertIs(y.obj, x)
    self.assertIs(m.obj, z)
    self.verify(m, obj=z, itemsize=1, fmt=fmt, readonly=True, ndim=1, shape=[12], strides=[1], lst=lst)
    del x, y, z, m
    x = staticarray()
    y = ndarray(x, getbuf=PyBUF_FULL_RO, flags=ND_REDIRECT)
    z = ndarray(y, getbuf=PyBUF_FULL_RO, flags=ND_REDIRECT)
    m = memoryview(z)
    self.assertIs(y.obj, x)
    self.assertIs(z.obj, x)
    self.assertIs(m.obj, x)
    self.verify(m, obj=x, itemsize=1, fmt=fmt, readonly=True, ndim=1, shape=[12], strides=[1], lst=lst)
    del x, y, z, m
    x = staticarray(legacy_mode=True)
    y = memoryview(x)
    self.verify(y, obj=None, itemsize=1, fmt=fmt, readonly=True, ndim=1, shape=[12], strides=[1], lst=lst)
    for i in range(12):
        self.assertEqual(y[i], i)
    del x
    del y
    x = staticarray(legacy_mode=True)
    y = memoryview(x)
    del y
    del x
    x = staticarray(legacy_mode=True)
    y = ndarray(x, getbuf=PyBUF_FULL_RO)
    z = ndarray(y, getbuf=PyBUF_FULL_RO)
    m = memoryview(z)
    self.assertIs(y.obj, None)
    self.assertIs(m.obj, z)
    self.verify(m, obj=z, itemsize=1, fmt=fmt, readonly=True, ndim=1, shape=[12], strides=[1], lst=lst)
    del x, y, z, m
    x = staticarray(legacy_mode=True)
    y = ndarray(x, getbuf=PyBUF_FULL_RO, flags=ND_REDIRECT)
    z = ndarray(y, getbuf=PyBUF_FULL_RO, flags=ND_REDIRECT)
    m = memoryview(z)
    self.assertIs(y.obj, None)
    self.assertIs(z.obj, y)
    self.assertIs(m.obj, y)
    self.verify(m, obj=y, itemsize=1, fmt=fmt, readonly=True, ndim=1, shape=[12], strides=[1], lst=lst)
    del x, y, z, m
