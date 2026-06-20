# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: TestCollation_test_strxfrm

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertLess(locale.strxfrm('a'), locale.strxfrm('b'))
    self.assertRaises(ValueError, locale.strxfrm, 'a\x00')
