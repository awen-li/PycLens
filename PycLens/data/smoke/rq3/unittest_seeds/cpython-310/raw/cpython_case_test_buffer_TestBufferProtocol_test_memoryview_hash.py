# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytes(list(range(12)))
    m = memoryview(b)
    self.assertEqual(hash(b), hash(m))
    mc = m.cast('c', shape=[3, 4])
    self.assertEqual(hash(mc), hash(b))
    mx = m[::-2]
    b = bytes(list(range(12))[::-2])
    self.assertEqual(hash(mx), hash(b))
    nd = ndarray(list(range(30)), shape=[3, 2, 5], flags=ND_FORTRAN)
    m = memoryview(nd)
    self.assertEqual(hash(m), hash(nd))
    nd = ndarray(list(range(30)), shape=[3, 2, 5])
    x = nd[::2, :, ::-1]
    m = memoryview(x)
    self.assertEqual(hash(m), hash(x))
    nd = ndarray(list(range(30)), shape=[2, 5, 3], flags=ND_PIL)
    x = nd[::2, :, ::-1]
    m = memoryview(x)
    self.assertEqual(hash(m), hash(x))
    x = ndarray(list(range(12)), shape=[12], format='B')
    a = memoryview(x)
    y = ndarray(list(range(12)), shape=[12], format='b')
    b = memoryview(y)
    self.assertEqual(a, b)
    self.assertEqual(hash(a), hash(b))
    nd = ndarray(list(range(12)), shape=[2, 2, 3], format='L')
    m = memoryview(nd)
    self.assertRaises(ValueError, m.__hash__)
    nd = ndarray(list(range(-6, 6)), shape=[2, 2, 3], format='h')
    m = memoryview(nd)
    self.assertRaises(ValueError, m.__hash__)
    nd = ndarray(list(range(12)), shape=[2, 2, 3], format='= L')
    m = memoryview(nd)
    self.assertRaises(ValueError, m.__hash__)
    nd = ndarray(list(range(-6, 6)), shape=[2, 2, 3], format='< h')
    m = memoryview(nd)
    self.assertRaises(ValueError, m.__hash__)
