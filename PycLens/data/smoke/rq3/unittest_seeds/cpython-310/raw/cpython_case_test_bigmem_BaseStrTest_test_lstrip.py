# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_lstrip

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _('abc def ghi')
    s = SUBSTR.rjust(size)
    self.assertEqual(len(s), size)
    self.assertEqual(s.lstrip(), SUBSTR.lstrip())
    del s
    s = SUBSTR.ljust(size)
    self.assertEqual(len(s), size)
    if isinstance(s, (str, bytes)):
        stripped = s.lstrip()
        self.assertTrue(stripped is s)
