# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_complex.py
# case: ComplexTest_test_underscores

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for lit in VALID_UNDERSCORE_LITERALS:
        if not any((ch in lit for ch in 'xXoObB')):
            self.assertEqual(complex(lit), eval(lit))
            self.assertEqual(complex(lit), complex(lit.replace('_', '')))
    for lit in INVALID_UNDERSCORE_LITERALS:
        if lit in ('0_7', '09_99'):
            continue
        if not any((ch in lit for ch in 'xXoObB')):
            self.assertRaises(ValueError, complex, lit)
