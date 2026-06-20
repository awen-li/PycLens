# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_long.py
# case: LongTest_test_shift_bool

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for value in (True, False):
        for shift in (0, 2):
            self.assertEqual(type(value << shift), int)
            self.assertEqual(type(value >> shift), int)
