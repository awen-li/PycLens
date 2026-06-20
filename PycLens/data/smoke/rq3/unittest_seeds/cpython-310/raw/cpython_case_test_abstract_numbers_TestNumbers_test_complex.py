# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abstract_numbers.py
# case: TestNumbers_test_complex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(issubclass(complex, Real))
    self.assertTrue(issubclass(complex, Complex))
    (c1, c2) = (complex(3, 2), complex(4, 1))
    self.assertRaises(TypeError, math.trunc, c1)
    self.assertRaises(TypeError, operator.mod, c1, c2)
    self.assertRaises(TypeError, divmod, c1, c2)
    self.assertRaises(TypeError, operator.floordiv, c1, c2)
    self.assertRaises(TypeError, float, c1)
    self.assertRaises(TypeError, int, c1)
