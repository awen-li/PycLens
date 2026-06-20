# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntTestCases_test_underscores

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for lit in VALID_UNDERSCORE_LITERALS:
        if any((ch in lit for ch in '.eEjJ')):
            continue
        self.assertEqual(int(lit, 0), eval(lit))
        self.assertEqual(int(lit, 0), int(lit.replace('_', ''), 0))
    for lit in INVALID_UNDERSCORE_LITERALS:
        if any((ch in lit for ch in '.eEjJ')):
            continue
        self.assertRaises(ValueError, int, lit, 0)
    self.assertEqual(int('1_00', 3), 9)
    self.assertEqual(int('0_100'), 100)
    self.assertEqual(int(b'1_00'), 100)
    self.assertRaises(ValueError, int, '_100')
    self.assertRaises(ValueError, int, '+_100')
    self.assertRaises(ValueError, int, '1__00')
    self.assertRaises(ValueError, int, '100_')
