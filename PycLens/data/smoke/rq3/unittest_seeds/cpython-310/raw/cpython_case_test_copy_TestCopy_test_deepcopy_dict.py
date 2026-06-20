# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_deepcopy_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = {'foo': [1, 2], 'bar': 3}
    y = copy.deepcopy(x)
    self.assertEqual(y, x)
    self.assertIsNot(x, y)
    self.assertIsNot(x['foo'], y['foo'])
