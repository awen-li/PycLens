# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: OverflowTestCase_test_sequence_repeat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(OverflowError, lambda : 'a' * self.pos)
    self.assertRaises(OverflowError, lambda : 'a' * self.neg)
