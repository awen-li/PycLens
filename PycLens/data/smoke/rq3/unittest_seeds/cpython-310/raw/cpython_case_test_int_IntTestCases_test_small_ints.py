# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntTestCases_test_small_ints

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(int('10'), 10)
    self.assertIs(int('-1'), -1)
    self.assertIs(int(b'10'), 10)
    self.assertIs(int(b'-1'), -1)
