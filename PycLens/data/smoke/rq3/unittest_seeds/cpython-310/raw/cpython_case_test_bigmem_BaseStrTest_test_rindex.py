# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_rindex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _(' abc def ghi')
    sublen = len(SUBSTR)
    s = _('').join([SUBSTR, _('-') * size, SUBSTR])
    self.assertEqual(s.rindex(_(' ')), sublen + size + SUBSTR.rindex(_(' ')))
    self.assertEqual(s.rindex(SUBSTR), sublen + size)
    self.assertEqual(s.rindex(_(' '), 0, sublen + size - 1), SUBSTR.rindex(_(' ')))
    self.assertEqual(s.rindex(SUBSTR, 0, sublen + size), 0)
    self.assertEqual(s.rindex(_('i')), sublen + size + SUBSTR.rindex(_('i')))
    self.assertEqual(s.rindex(_('i'), 0, sublen), SUBSTR.rindex(_('i')))
    self.assertEqual(s.rindex(_('i'), 0, sublen + size), SUBSTR.rindex(_('i')))
    self.assertRaises(ValueError, s.rindex, _('j'))
