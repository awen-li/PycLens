# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_zfill

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _('-568324723598234')
    s = SUBSTR.zfill(size)
    self.assertTrue(s.endswith(_('0') + SUBSTR[1:]))
    self.assertTrue(s.startswith(_('-0')))
    self.assertEqual(len(s), size)
    self.assertEqual(s.count(_('0')), size - len(SUBSTR))
