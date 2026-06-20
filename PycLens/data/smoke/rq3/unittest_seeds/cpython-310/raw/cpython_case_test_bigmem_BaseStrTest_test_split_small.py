# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_split_small

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    chunksize = int(size ** 0.5 + 2)
    SUBSTR = _('a') + _(' ') * chunksize
    s = SUBSTR * chunksize
    l = s.split()
    self.assertEqual(len(l), chunksize)
    expected = _('a')
    for item in l:
        self.assertEqual(item, expected)
    del l
    l = s.split(_('a'))
    self.assertEqual(len(l), chunksize + 1)
    expected = _(' ') * chunksize
    for item in filter(None, l):
        self.assertEqual(item, expected)
