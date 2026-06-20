# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ex = ndarray(12.5, shape=[], format='d')
    m = memoryview(ex)
    self.assertEqual(m[()], 12.5)
    self.assertEqual(m[...], m)
    self.assertEqual(m[...], ex)
    self.assertRaises(TypeError, m.__getitem__, 0)
    ex = ndarray((1, 2, 3), shape=[], format='iii')
    m = memoryview(ex)
    self.assertRaises(NotImplementedError, m.__getitem__, ())
    ex = ndarray(list(range(7)), shape=[7], flags=ND_WRITABLE)
    m = memoryview(ex)
    self.assertRaises(IndexError, m.__getitem__, 2 ** 64)
    self.assertRaises(TypeError, m.__getitem__, 2.0)
    self.assertRaises(TypeError, m.__getitem__, 0.0)
    self.assertRaises(IndexError, m.__getitem__, -8)
    self.assertRaises(IndexError, m.__getitem__, 8)
    ex = ndarray(list(range(12)), shape=[3, 4], flags=ND_WRITABLE)
    m = memoryview(ex)
    self.assertEqual(m[0, 0], 0)
    self.assertEqual(m[2, 0], 8)
    self.assertEqual(m[2, 3], 11)
    self.assertEqual(m[-1, -1], 11)
    self.assertEqual(m[-3, -4], 0)
    for index in (3, -4):
        with self.assert_out_of_bounds_error(dim=1):
            m[index, 0]
    for index in (4, -5):
        with self.assert_out_of_bounds_error(dim=2):
            m[0, index]
    self.assertRaises(IndexError, m.__getitem__, (2 ** 64, 0))
    self.assertRaises(IndexError, m.__getitem__, (0, 2 ** 64))
    self.assertRaises(TypeError, m.__getitem__, (0, 0, 0))
    self.assertRaises(TypeError, m.__getitem__, (0.0, 0.0))
    self.assertRaises(NotImplementedError, m.__getitem__, ())
    self.assertRaises(NotImplementedError, m.__getitem__, 0)
