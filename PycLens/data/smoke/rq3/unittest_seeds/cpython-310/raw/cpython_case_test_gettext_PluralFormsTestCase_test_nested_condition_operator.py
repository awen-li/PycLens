# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: PluralFormsTestCase_test_nested_condition_operator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(gettext.c2py('n?1?2:3:4')(0), 4)
    self.assertEqual(gettext.c2py('n?1?2:3:4')(1), 2)
    self.assertEqual(gettext.c2py('n?1:3?4:5')(0), 4)
    self.assertEqual(gettext.c2py('n?1:3?4:5')(1), 1)
