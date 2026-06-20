# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_index_scalar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nd = ndarray(1, shape=(), flags=ND_WRITABLE)
    mv = memoryview(nd)
    self.assertEqual(mv, nd)
    x = nd[()]
    self.assertEqual(x, 1)
    x = nd[...]
    self.assertEqual(x.tolist(), nd.tolist())
    x = mv[()]
    self.assertEqual(x, 1)
    x = mv[...]
    self.assertEqual(x.tolist(), nd.tolist())
    self.assertRaises(TypeError, nd.__getitem__, 0)
    self.assertRaises(TypeError, mv.__getitem__, 0)
    self.assertRaises(TypeError, nd.__setitem__, 0, 8)
    self.assertRaises(TypeError, mv.__setitem__, 0, 8)
    self.assertEqual(nd.tolist(), 1)
    self.assertEqual(mv.tolist(), 1)
    nd[()] = 9
    self.assertEqual(nd.tolist(), 9)
    mv[()] = 9
    self.assertEqual(mv.tolist(), 9)
    nd[...] = 5
    self.assertEqual(nd.tolist(), 5)
    mv[...] = 5
    self.assertEqual(mv.tolist(), 5)
