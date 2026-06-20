# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_isspace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    whitespace = _(' \x0c\n\r\t\x0b')
    repeats = size // len(whitespace) + 2
    s = whitespace * repeats
    self.assertTrue(s.isspace())
    s += _('j')
    self.assertFalse(s.isspace())
