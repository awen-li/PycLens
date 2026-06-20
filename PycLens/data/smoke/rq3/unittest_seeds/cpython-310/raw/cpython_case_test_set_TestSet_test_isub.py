# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_isub

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.s -= set(self.otherword)
    for c in self.word + self.otherword:
        if c in self.word and c not in self.otherword:
            self.assertIn(c, self.s)
        else:
            self.assertNotIn(c, self.s)
