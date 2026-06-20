# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strtod.py
# case: StrtodTests_test_oversized_digit_strings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = '1.' + '1' * maxsize
    with self.assertRaises(ValueError):
        float(s)
    del s
    s = '0.' + '0' * maxsize + '1'
    with self.assertRaises(ValueError):
        float(s)
    del s
