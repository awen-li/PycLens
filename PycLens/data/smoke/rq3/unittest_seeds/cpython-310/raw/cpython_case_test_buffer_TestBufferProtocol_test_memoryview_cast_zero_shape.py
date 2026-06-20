# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_cast_zero_shape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    items = [1, 2, 3]
    for shape in ([0, 3, 3], [3, 0, 3], [0, 3, 3]):
        ex = ndarray(items, shape=shape)
        self.assertTrue(ex.c_contiguous)
        msrc = memoryview(ex)
        self.assertRaises(TypeError, msrc.cast, 'c')
    for (fmt, _, _) in iter_format(1, 'memoryview'):
        msrc = memoryview(b'')
        m = msrc.cast(fmt)
        self.assertEqual(m.tobytes(), b'')
        self.assertEqual(m.tolist(), [])
