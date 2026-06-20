# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_join

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    s = _('A') * size
    x = s.join([_('aaaaa'), _('bbbbb')])
    self.assertEqual(x.count(_('a')), 5)
    self.assertEqual(x.count(_('b')), 5)
    self.assertTrue(x.startswith(_('aaaaaA')))
    self.assertTrue(x.endswith(_('Abbbbb')))
