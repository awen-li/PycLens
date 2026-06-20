# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: PluralFormsTestCase_test_division

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = gettext.c2py('2/n*3')
    self.assertEqual(f(1), 6)
    self.assertEqual(f(2), 3)
    self.assertEqual(f(3), 0)
    self.assertEqual(f(-1), -6)
    self.assertRaises(ZeroDivisionError, f, 0)
