# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: PluralFormsTestCase_test_invalid_syntax

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    invalid_expressions = ['x>1', '(n>1', 'n>1)', '42**42**42', '0xa', '1.0', '1e2', 'n>0x1', '+n', '-n', 'n()', 'n(1)', '1+', 'nn', 'n n']
    for expr in invalid_expressions:
        with self.assertRaises(ValueError):
            gettext.c2py(expr)
