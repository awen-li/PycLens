# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compare.py
# case: ComparisonTest_test_issue_1393

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = lambda : None
    self.assertEqual(x, ALWAYS_EQ)
    self.assertEqual(ALWAYS_EQ, x)
    y = object()
    self.assertEqual(y, ALWAYS_EQ)
    self.assertEqual(ALWAYS_EQ, y)
