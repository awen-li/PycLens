# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSubsets_test_issubset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = self.left
    y = self.right
    for case in ('!=', '==', '<', '<=', '>', '>='):
        expected = case in self.cases
        result = eval('x' + case + 'y', locals())
        self.assertEqual(result, expected)
        if case in TestSubsets.case2method:
            method = getattr(x, TestSubsets.case2method[case])
            result = method(y)
            self.assertEqual(result, expected)
        rcase = TestSubsets.reverse[case]
        result = eval('y' + rcase + 'x', locals())
        self.assertEqual(result, expected)
        if rcase in TestSubsets.case2method:
            method = getattr(y, TestSubsets.case2method[rcase])
            result = method(x)
            self.assertEqual(result, expected)
