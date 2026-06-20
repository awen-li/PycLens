# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_slice_zero_shape

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x = ndarray(items, shape=[12], format='L', flags=ND_WRITABLE)
    y = ndarray(items, shape=[12], format='L')
    x[4:4] = y[9:9]
    self.assertEqual(x.tolist(), items)
    ml = memoryview(x)
    mr = memoryview(y)
    self.assertEqual(ml, x)
    self.assertEqual(ml, y)
    ml[4:4] = mr[9:9]
    self.assertEqual(ml.tolist(), items)
    x = ndarray(items, shape=[3, 4], format='L', flags=ND_WRITABLE)
    y = ndarray(items, shape=[4, 3], format='L')
    x[1:2, 2:2] = y[1:2, 3:3]
    self.assertEqual(x.tolist(), carray(items, [3, 4]))
