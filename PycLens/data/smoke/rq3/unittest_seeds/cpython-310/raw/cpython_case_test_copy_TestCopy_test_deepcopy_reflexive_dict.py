# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_reflexive_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = {}
    x['foo'] = x
    y = copy.deepcopy(x)
    for op in order_comparisons:
        self.assertRaises(TypeError, op, y, x)
    for op in equality_comparisons:
        self.assertRaises(RecursionError, op, y, x)
    self.assertIsNot(y, x)
    self.assertIs(y['foo'], y)
    self.assertEqual(len(y), 1)
