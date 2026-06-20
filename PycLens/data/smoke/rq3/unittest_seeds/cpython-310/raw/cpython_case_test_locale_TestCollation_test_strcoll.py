# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: TestCollation_test_strcoll

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertLess(locale.strcoll('a', 'b'), 0)
    self.assertEqual(locale.strcoll('a', 'a'), 0)
    self.assertGreater(locale.strcoll('b', 'a'), 0)
    self.assertRaises(ValueError, locale.strcoll, 'a\x00', 'a')
    self.assertRaises(ValueError, locale.strcoll, 'a', 'a\x00')
