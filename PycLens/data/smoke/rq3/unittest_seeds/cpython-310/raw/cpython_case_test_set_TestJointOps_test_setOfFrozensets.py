# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_setOfFrozensets

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = map(frozenset, ['abcdef', 'bcd', 'bdcb', 'fed', 'fedccba'])
    s = self.thetype(t)
    self.assertEqual(len(s), 3)
