# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_invalid_invocation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, range)
    self.assertRaises(TypeError, range, 1, 2, 3, 4)
    self.assertRaises(ValueError, range, 1, 2, 0)
    a = int(10 * sys.maxsize)
    self.assertRaises(ValueError, range, a, a + 1, int(0))
    self.assertRaises(TypeError, range, 1.0, 1.0, 1.0)
    self.assertRaises(TypeError, range, 1e+100, 1e+101, 1e+101)
    self.assertRaises(TypeError, range, 0, 'spam')
    self.assertRaises(TypeError, range, 0, 42, 'spam')
    self.assertRaises(TypeError, range, 0.0)
    self.assertRaises(TypeError, range, 0, 0.0)
    self.assertRaises(TypeError, range, 0.0, 0)
    self.assertRaises(TypeError, range, 0.0, 0.0)
    self.assertRaises(TypeError, range, 0, 0, 1.0)
    self.assertRaises(TypeError, range, 0, 0.0, 1)
    self.assertRaises(TypeError, range, 0, 0.0, 1.0)
    self.assertRaises(TypeError, range, 0.0, 0, 1)
    self.assertRaises(TypeError, range, 0.0, 0, 1.0)
    self.assertRaises(TypeError, range, 0.0, 0.0, 1)
    self.assertRaises(TypeError, range, 0.0, 0.0, 1.0)
