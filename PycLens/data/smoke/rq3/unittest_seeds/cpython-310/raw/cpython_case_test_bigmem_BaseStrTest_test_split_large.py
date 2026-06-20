# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_split_large

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    s = _(' a') * size + _(' ')
    l = s.split()
    self.assertEqual(len(l), size)
    self.assertEqual(set(l), set([_('a')]))
    del l
    l = s.split(_('a'))
    self.assertEqual(len(l), size + 1)
    self.assertEqual(set(l), set([_(' ')]))
