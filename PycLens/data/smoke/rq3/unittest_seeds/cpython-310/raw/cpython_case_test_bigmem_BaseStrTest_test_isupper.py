# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bigmem.py
# case: BaseStrTest_test_isupper

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _ = self.from_latin1
    chars = _(''.join((chr(c) for c in range(255) if not chr(c).islower())))
    repeats = size // len(chars) + 2
    s = chars * repeats
    self.assertTrue(s.isupper())
    s += _('a')
    self.assertFalse(s.isupper())
