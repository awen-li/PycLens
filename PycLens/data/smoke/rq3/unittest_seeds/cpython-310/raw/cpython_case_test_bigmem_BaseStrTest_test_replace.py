# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_replace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    replacement = _('a')
    s = _(' ') * size
    s = s.replace(_(' '), replacement)
    self.assertEqual(len(s), size)
    self.assertEqual(s.count(replacement), size)
    s = s.replace(replacement, _(' '), size - 4)
    self.assertEqual(len(s), size)
    self.assertEqual(s.count(replacement), 4)
    self.assertEqual(s[-10:], _('      aaaa'))
