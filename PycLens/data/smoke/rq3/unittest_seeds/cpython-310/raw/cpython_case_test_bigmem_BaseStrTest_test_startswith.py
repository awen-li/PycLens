# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_startswith

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    SUBSTR = _(' abc def ghi')
    s = _('-') * size + SUBSTR
    self.assertTrue(s.startswith(s))
    self.assertTrue(s.startswith(_('-') * size))
    self.assertFalse(s.startswith(SUBSTR))
