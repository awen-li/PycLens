# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compare.py
# case: ComparisonTest_test_comparisons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for a in self.candidates:
        for b in self.candidates:
            if a in self.set1 and b in self.set1 or a is b:
                self.assertEqual(a, b)
            else:
                self.assertNotEqual(a, b)
