# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_check_released

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array('d', [1.1, 2.2, 3.3])
    m = memoryview(a)
    m.release()
    self.assertRaises(ValueError, memoryview, m)
    self.assertRaises(ValueError, m.cast, 'c')
    self.assertRaises(ValueError, ndarray, m)
    self.assertRaises(ValueError, m.tolist)
    self.assertRaises(ValueError, m.tobytes)
    self.assertRaises(ValueError, eval, '1.0 in m', locals())
    self.assertRaises(ValueError, m.__getitem__, 0)
    self.assertRaises(ValueError, m.__setitem__, 0, 1)
    for attr in ('obj', 'nbytes', 'readonly', 'itemsize', 'format', 'ndim', 'shape', 'strides', 'suboffsets', 'c_contiguous', 'f_contiguous', 'contiguous'):
        self.assertRaises(ValueError, m.__getattribute__, attr)
    b = array.array('d', [1.1, 2.2, 3.3])
    m1 = memoryview(a)
    m2 = memoryview(b)
    self.assertEqual(m1, m2)
    m1.release()
    self.assertNotEqual(m1, m2)
    self.assertNotEqual(m1, a)
    self.assertEqual(m1, m1)
