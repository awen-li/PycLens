# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_pop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(len(self.s)):
        elem = self.s.pop()
        self.assertNotIn(elem, self.s)
    self.assertRaises(KeyError, self.s.pop)
