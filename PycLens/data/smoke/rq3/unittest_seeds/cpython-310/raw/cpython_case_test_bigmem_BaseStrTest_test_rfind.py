# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_rfind

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _(' abc def ghi')
    sublen = len(SUBSTR)
    s = _('').join([SUBSTR, _('-') * size, SUBSTR])
    self.assertEqual(s.rfind(_(' ')), sublen + size + SUBSTR.rfind(_(' ')))
    self.assertEqual(s.rfind(SUBSTR), sublen + size)
    self.assertEqual(s.rfind(_(' '), 0, size), SUBSTR.rfind(_(' ')))
    self.assertEqual(s.rfind(SUBSTR, 0, sublen + size), 0)
    self.assertEqual(s.rfind(_('i')), sublen + size + SUBSTR.rfind(_('i')))
    self.assertEqual(s.rfind(_('i'), 0, sublen), SUBSTR.rfind(_('i')))
    self.assertEqual(s.rfind(_('i'), 0, sublen + size), SUBSTR.rfind(_('i')))
    self.assertEqual(s.rfind(_('j')), -1)
