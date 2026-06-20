# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_isdigit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _('123456')
    s = _('9') * size + SUBSTR
    self.assertTrue(s.isdigit())
    s += _('z')
    self.assertFalse(s.isdigit())
