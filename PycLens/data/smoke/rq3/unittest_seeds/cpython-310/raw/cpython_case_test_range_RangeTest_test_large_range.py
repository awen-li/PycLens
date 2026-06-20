# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_large_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _range_len(x):
        try:
            length = len(x)
        except OverflowError:
            step = x[1] - x[0]
            length = 1 + (x[-1] - x[0]) // step
        return length
    a = -sys.maxsize
    b = sys.maxsize
    expected_len = b - a
    x = range(a, b)
    self.assertIn(a, x)
    self.assertNotIn(b, x)
    self.assertRaises(OverflowError, len, x)
    self.assertTrue(x)
    self.assertEqual(_range_len(x), expected_len)
    self.assertEqual(x[0], a)
    idx = sys.maxsize + 1
    self.assertEqual(x[idx], a + idx)
    self.assertEqual(x[idx:idx + 1][0], a + idx)
    with self.assertRaises(IndexError):
        x[-expected_len - 1]
    with self.assertRaises(IndexError):
        x[expected_len]
    a = 0
    b = 2 * sys.maxsize
    expected_len = b - a
    x = range(a, b)
    self.assertIn(a, x)
    self.assertNotIn(b, x)
    self.assertRaises(OverflowError, len, x)
    self.assertTrue(x)
    self.assertEqual(_range_len(x), expected_len)
    self.assertEqual(x[0], a)
    idx = sys.maxsize + 1
    self.assertEqual(x[idx], a + idx)
    self.assertEqual(x[idx:idx + 1][0], a + idx)
    with self.assertRaises(IndexError):
        x[-expected_len - 1]
    with self.assertRaises(IndexError):
        x[expected_len]
    a = 0
    b = sys.maxsize ** 10
    c = 2 * sys.maxsize
    expected_len = 1 + (b - a) // c
    x = range(a, b, c)
    self.assertIn(a, x)
    self.assertNotIn(b, x)
    self.assertRaises(OverflowError, len, x)
    self.assertTrue(x)
    self.assertEqual(_range_len(x), expected_len)
    self.assertEqual(x[0], a)
    idx = sys.maxsize + 1
    self.assertEqual(x[idx], a + idx * c)
    self.assertEqual(x[idx:idx + 1][0], a + idx * c)
    with self.assertRaises(IndexError):
        x[-expected_len - 1]
    with self.assertRaises(IndexError):
        x[expected_len]
    a = sys.maxsize ** 10
    b = 0
    c = -2 * sys.maxsize
    expected_len = 1 + (b - a) // c
    x = range(a, b, c)
    self.assertIn(a, x)
    self.assertNotIn(b, x)
    self.assertRaises(OverflowError, len, x)
    self.assertTrue(x)
    self.assertEqual(_range_len(x), expected_len)
    self.assertEqual(x[0], a)
    idx = sys.maxsize + 1
    self.assertEqual(x[idx], a + idx * c)
    self.assertEqual(x[idx:idx + 1][0], a + idx * c)
    with self.assertRaises(IndexError):
        x[-expected_len - 1]
    with self.assertRaises(IndexError):
        x[expected_len]
