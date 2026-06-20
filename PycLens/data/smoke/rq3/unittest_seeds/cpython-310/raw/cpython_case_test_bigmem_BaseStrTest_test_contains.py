# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_contains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _('0123456789')
    edge = _('-') * (size // 2)
    s = _('').join([edge, SUBSTR, edge])
    del edge
    self.assertTrue(SUBSTR in s)
    self.assertFalse(SUBSTR * 2 in s)
    self.assertTrue(_('-') in s)
    self.assertFalse(_('a') in s)
    s += _('a')
    self.assertTrue(_('a') in s)
