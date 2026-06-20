# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_expandtabs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    s = _('-') * size
    tabsize = 8
    self.assertTrue(s.expandtabs() == s)
    del s
    (slen, remainder) = divmod(size, tabsize)
    s = _('       \t') * slen
    s = s.expandtabs(tabsize)
    self.assertEqual(len(s), size - remainder)
    self.assertEqual(len(s.strip(_(' '))), 0)
