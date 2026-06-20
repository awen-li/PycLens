# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_index_invalid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nd = ndarray([1], shape=[1])
    self.assertRaises(TypeError, nd.__setitem__, 1, 8)
    mv = memoryview(nd)
    self.assertEqual(mv, nd)
    self.assertRaises(TypeError, mv.__setitem__, 1, 8)
    nd = ndarray([1], shape=[1], flags=ND_WRITABLE)
    self.assertRaises(TypeError, nd.__delitem__, 1)
    mv = memoryview(nd)
    self.assertEqual(mv, nd)
    self.assertRaises(TypeError, mv.__delitem__, 1)
    nd = ndarray([1], shape=[1], flags=ND_WRITABLE)
    self.assertRaises(OverflowError, nd.__getitem__, 1 << 64)
    self.assertRaises(OverflowError, nd.__setitem__, 1 << 64, 8)
    mv = memoryview(nd)
    self.assertEqual(mv, nd)
    self.assertRaises(IndexError, mv.__getitem__, 1 << 64)
    self.assertRaises(IndexError, mv.__setitem__, 1 << 64, 8)
    items = [1, 2, 3, 4, 5, 6, 7, 8]
    nd = ndarray(items, shape=[len(items)], format='B', flags=ND_WRITABLE)
    self.assertRaises(struct.error, nd.__setitem__, 2, 300)
    self.assertRaises(ValueError, nd.__setitem__, 1, (100, 200))
    mv = memoryview(nd)
    self.assertEqual(mv, nd)
    self.assertRaises(ValueError, mv.__setitem__, 2, 300)
    self.assertRaises(TypeError, mv.__setitem__, 1, (100, 200))
    items = [(1, 2), (3, 4), (5, 6)]
    nd = ndarray(items, shape=[len(items)], format='LQ', flags=ND_WRITABLE)
    self.assertRaises(ValueError, nd.__setitem__, 2, 300)
    self.assertRaises(struct.error, nd.__setitem__, 1, (b'\x001', 200))
