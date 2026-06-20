# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_memoryview_compare_not_equal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for byteorder in ['=', '<', '>', '!']:
        x = ndarray([2 ** 63] * 120, shape=[3, 5, 2, 2, 2], format=byteorder + 'Q')
        y = ndarray([2 ** 63] * 120, shape=[3, 5, 2, 2, 2], format=byteorder + 'Q', flags=ND_WRITABLE | ND_FORTRAN)
        y[2][3][1][1][1] = 1
        a = memoryview(x)
        b = memoryview(y)
        self.assertEqual(a, x)
        self.assertEqual(b, y)
        self.assertNotEqual(a, b)
        self.assertNotEqual(a, y)
        self.assertNotEqual(b, x)
        x = ndarray([(2 ** 63, 2 ** 31, 2 ** 15)] * 120, shape=[3, 5, 2, 2, 2], format=byteorder + 'QLH')
        y = ndarray([(2 ** 63, 2 ** 31, 2 ** 15)] * 120, shape=[3, 5, 2, 2, 2], format=byteorder + 'QLH', flags=ND_WRITABLE | ND_FORTRAN)
        y[2][3][1][1][1] = (1, 1, 1)
        a = memoryview(x)
        b = memoryview(y)
        self.assertEqual(a, x)
        self.assertEqual(b, y)
        self.assertNotEqual(a, b)
        self.assertNotEqual(a, y)
        self.assertNotEqual(b, x)
