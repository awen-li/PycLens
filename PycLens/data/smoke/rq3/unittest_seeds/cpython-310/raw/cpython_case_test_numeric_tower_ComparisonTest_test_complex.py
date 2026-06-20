# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_numeric_tower.py
# case: ComparisonTest_test_complex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    z = 1.0 + 0j
    w = -3.14 + 2.7j
    for v in (1, 1.0, F(1), D(1), complex(1)):
        self.assertEqual(z, v)
        self.assertEqual(v, z)
    for v in (2, 2.0, F(2), D(2), complex(2)):
        self.assertNotEqual(z, v)
        self.assertNotEqual(v, z)
        self.assertNotEqual(w, v)
        self.assertNotEqual(v, w)
    for v in (1, 1.0, F(1), D(1), complex(1), 2, 2.0, F(2), D(2), complex(2), w):
        for op in (operator.le, operator.lt, operator.ge, operator.gt):
            self.assertRaises(TypeError, op, z, v)
            self.assertRaises(TypeError, op, v, z)
