# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_dont_memo_immutable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memo = {}
    x = [1, 2, 3, 4]
    y = copy.deepcopy(x, memo)
    self.assertEqual(y, x)
    self.assertEqual(len(memo), 2)
    memo = {}
    x = [(1, 2)]
    y = copy.deepcopy(x, memo)
    self.assertEqual(y, x)
    self.assertEqual(len(memo), 2)
