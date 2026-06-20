# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _(' abc def ghi')
    sublen = len(SUBSTR)
    s = _('').join([SUBSTR, _('-') * size, SUBSTR])
    self.assertEqual(s.index(_(' ')), 0)
    self.assertEqual(s.index(SUBSTR), 0)
    self.assertEqual(s.index(_(' '), sublen), sublen + size)
    self.assertEqual(s.index(SUBSTR, sublen), sublen + size)
    self.assertEqual(s.index(_('i')), SUBSTR.index(_('i')))
    self.assertEqual(s.index(_('i'), sublen), sublen + size + SUBSTR.index(_('i')))
    self.assertEqual(s.index(_('i'), size), sublen + size + SUBSTR.index(_('i')))
    self.assertRaises(ValueError, s.index, _('j'))
