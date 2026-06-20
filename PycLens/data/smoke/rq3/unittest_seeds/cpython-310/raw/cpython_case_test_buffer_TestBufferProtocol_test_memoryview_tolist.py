# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_tolist

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array('h', list(range(-6, 6)))
    m = memoryview(a)
    self.assertEqual(m, a)
    self.assertEqual(m.tolist(), a.tolist())
    a = a[2::3]
    m = m[2::3]
    self.assertEqual(m, a)
    self.assertEqual(m.tolist(), a.tolist())
    ex = ndarray(list(range(2 * 3 * 5 * 7 * 11)), shape=[11, 2, 7, 3, 5], format='L')
    m = memoryview(ex)
    self.assertEqual(m.tolist(), ex.tolist())
    ex = ndarray([(2, 5), (7, 11)], shape=[2], format='lh')
    m = memoryview(ex)
    self.assertRaises(NotImplementedError, m.tolist)
    ex = ndarray([b'12345'], shape=[1], format='s')
    m = memoryview(ex)
    self.assertRaises(NotImplementedError, m.tolist)
    ex = ndarray([b'a', b'b', b'c', b'd', b'e', b'f'], shape=[2, 3], format='s')
    m = memoryview(ex)
    self.assertRaises(NotImplementedError, m.tolist)
