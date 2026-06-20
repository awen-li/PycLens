# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_seed_no_mutate_bug_44018

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = bytearray(b'1234')
    self.gen.seed(a)
    self.assertEqual(a, bytearray(b'1234'))
