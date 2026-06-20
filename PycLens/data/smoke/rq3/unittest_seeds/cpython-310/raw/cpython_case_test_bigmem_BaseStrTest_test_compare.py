# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    s1 = _('-') * size
    s2 = _('-') * size
    self.assertTrue(s1 == s2)
    del s2
    s2 = s1 + _('a')
    self.assertFalse(s1 == s2)
    del s2
    s2 = _('.') * size
    self.assertFalse(s1 == s2)
