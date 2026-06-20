# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_memo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = []
    x = [x, x]
    y = copy.deepcopy(x)
    self.assertEqual(y, x)
    self.assertIsNot(y, x)
    self.assertIsNot(y[0], x[0])
    self.assertIs(y[0], y[1])
