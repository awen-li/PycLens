# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: PluralFormsTestCase_test_chained_comparison

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = gettext.c2py('n == n == n')
    self.assertEqual(''.join((str(f(x)) for x in range(3))), '010')
    f = gettext.c2py('1 < n == n')
    self.assertEqual(''.join((str(f(x)) for x in range(3))), '100')
    f = gettext.c2py('n == n < 2')
    self.assertEqual(''.join((str(f(x)) for x in range(3))), '010')
    f = gettext.c2py('0 < n < 2')
    self.assertEqual(''.join((str(f(x)) for x in range(3))), '111')
