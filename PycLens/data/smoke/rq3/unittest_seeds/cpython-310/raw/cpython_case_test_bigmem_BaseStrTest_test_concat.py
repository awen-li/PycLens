# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_concat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    s = _('.') * size
    self.assertEqual(len(s), size)
    s = s + s
    self.assertEqual(len(s), size * 2)
    self.assertEqual(s.count(_('.')), size * 2)
