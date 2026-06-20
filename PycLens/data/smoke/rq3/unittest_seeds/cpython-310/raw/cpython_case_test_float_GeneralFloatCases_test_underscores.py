# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_float.py
# case: GeneralFloatCases_test_underscores

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for lit in VALID_UNDERSCORE_LITERALS:
        if not any((ch in lit for ch in 'jJxXoObB')):
            self.assertEqual(float(lit), eval(lit))
            self.assertEqual(float(lit), float(lit.replace('_', '')))
    for lit in INVALID_UNDERSCORE_LITERALS:
        if lit in ('0_7', '09_99'):
            continue
        if not any((ch in lit for ch in 'jJxXoObB')):
            self.assertRaises(ValueError, float, lit)
    self.assertRaises(ValueError, float, '_NaN')
    self.assertRaises(ValueError, float, 'Na_N')
    self.assertRaises(ValueError, float, 'IN_F')
    self.assertRaises(ValueError, float, '-_INF')
    self.assertRaises(ValueError, float, '-INF_')
    self.assertRaises(ValueError, float, b'0_.\xff9')
