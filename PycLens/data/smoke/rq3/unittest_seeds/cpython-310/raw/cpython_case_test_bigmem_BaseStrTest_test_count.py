# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _(' abc def ghi')
    s = _('.') * size + SUBSTR
    self.assertEqual(s.count(_('.')), size)
    s += _('.')
    self.assertEqual(s.count(_('.')), size + 1)
    self.assertEqual(s.count(_(' ')), 3)
    self.assertEqual(s.count(_('i')), 1)
    self.assertEqual(s.count(_('j')), 0)
