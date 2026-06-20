# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_slice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ex = ndarray(list(range(12)), shape=[12], flags=ND_WRITABLE)
    m = memoryview(ex)
    self.assertRaises(ValueError, m.__getitem__, slice(0, 2, 0))
    self.assertRaises(ValueError, m.__setitem__, slice(0, 2, 0), bytearray([1, 2]))
    self.assertRaises(NotImplementedError, m.__getitem__, ())
    ex = ndarray(list(range(12)), shape=[12], flags=ND_WRITABLE)
    m = memoryview(ex)
    self.assertRaises(NotImplementedError, m.__getitem__, (slice(0, 2, 1), slice(0, 2, 1)))
    self.assertRaises(NotImplementedError, m.__setitem__, (slice(0, 2, 1), slice(0, 2, 1)), bytearray([1, 2]))
    self.assertRaises(TypeError, m.__getitem__, (slice(0, 2, 1), {}))
    self.assertRaises(TypeError, m.__setitem__, (slice(0, 2, 1), {}), bytearray([1, 2]))
    self.assertRaises(TypeError, m.__setitem__, slice(0, 1, 1), [1])
    for flags in (0, ND_PIL):
        ex1 = ndarray(list(range(12)), shape=[12], strides=[-1], offset=11, flags=ND_WRITABLE | flags)
        ex2 = ndarray(list(range(24)), shape=[12], strides=[2], flags=flags)
        m1 = memoryview(ex1)
        m2 = memoryview(ex2)
        ex1[2:5] = ex1[2:5]
        m1[2:5] = m2[2:5]
        self.assertEqual(m1, ex1)
        self.assertEqual(m2, ex2)
        ex1[1:3][::-1] = ex2[0:2][::1]
        m1[1:3][::-1] = m2[0:2][::1]
        self.assertEqual(m1, ex1)
        self.assertEqual(m2, ex2)
        ex1[4:1:-2][::-1] = ex1[1:4:2][::1]
        m1[4:1:-2][::-1] = m1[1:4:2][::1]
        self.assertEqual(m1, ex1)
        self.assertEqual(m2, ex2)
