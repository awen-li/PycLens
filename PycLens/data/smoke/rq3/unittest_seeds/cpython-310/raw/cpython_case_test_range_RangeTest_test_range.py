# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_range

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(range(3)), [0, 1, 2])
    self.assertEqual(list(range(1, 5)), [1, 2, 3, 4])
    self.assertEqual(list(range(0)), [])
    self.assertEqual(list(range(-3)), [])
    self.assertEqual(list(range(1, 10, 3)), [1, 4, 7])
    self.assertEqual(list(range(5, -5, -3)), [5, 2, -1, -4])
    a = 10
    b = 100
    c = 50
    self.assertEqual(list(range(a, a + 2)), [a, a + 1])
    self.assertEqual(list(range(a + 2, a, -1)), [a + 2, a + 1])
    self.assertEqual(list(range(a + 4, a, -2)), [a + 4, a + 2])
    seq = list(range(a, b, c))
    self.assertIn(a, seq)
    self.assertNotIn(b, seq)
    self.assertEqual(len(seq), 2)
    seq = list(range(b, a, -c))
    self.assertIn(b, seq)
    self.assertNotIn(a, seq)
    self.assertEqual(len(seq), 2)
    seq = list(range(-a, -b, -c))
    self.assertIn(-a, seq)
    self.assertNotIn(-b, seq)
    self.assertEqual(len(seq), 2)
    self.assertRaises(TypeError, range)
    self.assertRaises(TypeError, range, 1, 2, 3, 4)
    self.assertRaises(ValueError, range, 1, 2, 0)
    self.assertRaises(TypeError, range, 0.0, 2, 1)
    self.assertRaises(TypeError, range, 1, 2.0, 1)
    self.assertRaises(TypeError, range, 1, 2, 1.0)
    self.assertRaises(TypeError, range, 1e+100, 1e+101, 1e+101)
    self.assertRaises(TypeError, range, 0, 'spam')
    self.assertRaises(TypeError, range, 0, 42, 'spam')
    self.assertEqual(len(range(0, sys.maxsize, sys.maxsize - 1)), 2)
    r = range(-sys.maxsize, sys.maxsize, 2)
    self.assertEqual(len(r), sys.maxsize)
