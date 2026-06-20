# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gettext.py
# case: PluralFormsTestCase_test_plural_number

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = gettext.c2py('n != 1')
    self.assertEqual(f(1), 0)
    self.assertEqual(f(2), 1)
    with self.assertWarns(DeprecationWarning):
        self.assertEqual(f(1.0), 0)
    with self.assertWarns(DeprecationWarning):
        self.assertEqual(f(2.0), 1)
    with self.assertWarns(DeprecationWarning):
        self.assertEqual(f(1.1), 1)
    self.assertRaises(TypeError, f, '2')
    self.assertRaises(TypeError, f, b'2')
    self.assertRaises(TypeError, f, [])
    self.assertRaises(TypeError, f, object())
