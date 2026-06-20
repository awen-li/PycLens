# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntTestCases_test_int_base_limits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(int('0', 5), 0)
    with self.assertRaises(ValueError):
        int('0', 1)
    with self.assertRaises(ValueError):
        int('0', 37)
    with self.assertRaises(ValueError):
        int('0', -909)
    with self.assertRaises(ValueError):
        int('0', base=0 - 2 ** 234)
    with self.assertRaises(ValueError):
        int('0', base=2 ** 234)
    for base in range(2, 37):
        self.assertEqual(int('0', base=base), 0)
