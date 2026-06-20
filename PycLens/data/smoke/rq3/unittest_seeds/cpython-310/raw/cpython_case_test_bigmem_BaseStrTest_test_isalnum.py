# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_isalnum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _('123456')
    s = _('a') * size + SUBSTR
    self.assertTrue(s.isalnum())
    s += _('.')
    self.assertFalse(s.isalnum())
