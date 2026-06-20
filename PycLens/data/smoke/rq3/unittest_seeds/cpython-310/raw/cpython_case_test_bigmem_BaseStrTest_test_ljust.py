# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_ljust

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _(' abc def ghi')
    s = SUBSTR.ljust(size)
    self.assertTrue(s.startswith(SUBSTR + _('  ')))
    self.assertEqual(len(s), size)
    self.assertEqual(s.strip(), SUBSTR.strip())
