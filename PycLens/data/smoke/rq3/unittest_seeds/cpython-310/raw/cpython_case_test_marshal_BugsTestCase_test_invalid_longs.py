# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: BugsTestCase_test_invalid_longs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    invalid_string = b'l\x02\x00\x00\x00\x00\x00\x00\x00'
    self.assertRaises(ValueError, marshal.loads, invalid_string)
