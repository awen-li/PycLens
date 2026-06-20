# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_find

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _(' abc def ghi')
    sublen = len(SUBSTR)
    s = _('').join([SUBSTR, _('-') * size, SUBSTR])
    self.assertEqual(s.find(_(' ')), 0)
    self.assertEqual(s.find(SUBSTR), 0)
    self.assertEqual(s.find(_(' '), sublen), sublen + size)
    self.assertEqual(s.find(SUBSTR, len(SUBSTR)), sublen + size)
    self.assertEqual(s.find(_('i')), SUBSTR.find(_('i')))
    self.assertEqual(s.find(_('i'), sublen), sublen + size + SUBSTR.find(_('i')))
    self.assertEqual(s.find(_('i'), size), sublen + size + SUBSTR.find(_('i')))
    self.assertEqual(s.find(_('j')), -1)
