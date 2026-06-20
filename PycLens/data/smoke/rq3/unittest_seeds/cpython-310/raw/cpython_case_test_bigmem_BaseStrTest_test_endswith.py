# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_endswith

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _(' abc def ghi')
    s = _('-') * size + SUBSTR
    self.assertTrue(s.endswith(SUBSTR))
    self.assertTrue(s.endswith(s))
    s2 = _('...') + s
    self.assertTrue(s2.endswith(s))
    self.assertFalse(s.endswith(_('a') + SUBSTR))
    self.assertFalse(SUBSTR.endswith(s))
